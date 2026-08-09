"""M13 — Downloader.

Read a pending discovery_queue row with discovery_id populated, download
the file, compute SHA-256 hash, detect content type, deduplicate by hash,
upload to R2, register asset, register asset_sources provenance, and hand
off to metadata_queue for processing.

Usage:
    python -m agents.downloader.main
"""

from __future__ import annotations

import hashlib
import os
import sys
import tempfile
from datetime import datetime, timezone
from urllib.parse import urlparse

import requests

from agents.discovery.database import get_db_connection
from agents.downloader.r2 import upload_file
from agents.downloader.register_asset import register_asset_source


# ---- Mapping from MIME Content-Type to file extension and asset_type ----
MIME_TO_EXT: dict[str, tuple[str, str]] = {
    "image/jpeg": (".jpg", "photo"),
    "image/jpg": (".jpg", "photo"),
    "image/png": (".png", "photo"),
    "image/gif": (".gif", "photo"),
    "image/webp": (".webp", "photo"),
    "image/tiff": (".tif", "photo"),
    "application/pdf": (".pdf", "document"),
    "video/mp4": (".mp4", "video"),
    "video/webm": (".webm", "video"),
    "audio/mpeg": (".mp3", "audio"),
    "audio/ogg": (".ogg", "audio"),
    "text/html": (".html", "unknown"),
}


def _get_extension_and_type(content_type: str | None) -> tuple[str, str]:
    """Map Content-Type header to file extension and asset_type."""
    if content_type is None:
        return (".bin", "unknown")
    clean = content_type.split(";")[0].strip().lower()
    return MIME_TO_EXT.get(clean, (".bin", "unknown"))


def _safe_filename(url: str) -> str:
    """Extract a safe filename from a URL path."""
    path = urlparse(url).path
    name = os.path.basename(path) or "download"
    # remove query-string fragments that may have leaked in
    name = name.split("?")[0]
    # strip non-alphanumeric except . - _
    safe = "".join(c for c in name if c.isalnum() or c in "._-")
    return safe or "download"


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # ---- 1. Claim one pending queue row ---------------------------------
        cur.execute(
            """
            SELECT dq.id, dq.title, dq.target_url, dq.discovery_id, dq.source_name
            FROM discovery_queue dq
            WHERE dq.status = 'pending'
              AND dq.discovery_id IS NOT NULL
            ORDER BY dq.id
            LIMIT 1
            """
        )
        row = cur.fetchone()

        if row is None:
            print("No pending queue items with discovery_id found.")
            return

        queue_id, title, target_url, discovery_id, source_name = row

        # Claim the row
        cur.execute(
            "UPDATE discovery_queue SET status = 'in_progress' WHERE id = %s",
            (queue_id,),
        )

        print(f"Processing queue {queue_id}: {title}")
        print(f"  URL: {target_url[:100]}")

        # ---- 2. HTTP download with validation --------------------------------
        print("  Downloading...")
        headers = {
            "User-Agent": "WTC-Evidence-Engine/1.0 (research project; contact@example.com)"
        }
        response = requests.get(target_url, timeout=30, stream=True, headers=headers)

        if response.status_code != 200:
            raise RuntimeError(
                f"HTTP {response.status_code} for {target_url[:100]}"
            )

        content = response.content
        content_type_header: str | None = response.headers.get("Content-Type")

        ext, asset_type = _get_extension_and_type(content_type_header)
        local_filename = f"{queue_id}_{_safe_filename(target_url)}{ext}"
        local_path = os.path.join("storage", "raw", local_filename)

        print(f"  Content-Type: {content_type_header or 'unknown'}")
        print(f"  Size: {len(content)} bytes")

        # ---- 3. Compute SHA-256 hash -----------------------------------------
        file_hash = hashlib.sha256(content).hexdigest()
        print(f"  SHA-256: {file_hash}")

        # ---- 4. File-hash deduplication --------------------------------------
        cur.execute("SELECT id FROM assets WHERE file_hash = %s", (file_hash,))
        existing_asset = cur.fetchone()
        is_duplicate = existing_asset is not None
        asset_id = existing_asset[0] if is_duplicate else None

        # ---- 5. Resolve source_id --------------------------------------------
        cur.execute("SELECT id FROM sources WHERE name = %s", (source_name,))
        source_row = cur.fetchone()
        source_id = source_row[0] if source_row else None

        # ---- 6. R2 upload (only if new asset) --------------------------------
        r2_key: str | None = None
        if not is_duplicate:
            os.makedirs("storage/raw", exist_ok=True)
            with open(local_path, "wb") as f:
                f.write(content)

            r2_key = f"downloads/{queue_id}_{_safe_filename(target_url)}{ext}"
            upload_file(local_path, r2_key)
            print(f"  R2: {r2_key}")

        # ---- 7. Asset registration (only if new asset) -----------------------
        if not is_duplicate:
            cur.execute(
                """
                INSERT INTO assets
                    (source_id, title, asset_type, source_url, local_path,
                     r2_key, file_hash, content_type,
                     download_status, metadata_status)
                VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, 'downloaded', 'pending')
                RETURNING id
                """,
                (
                    source_id,
                    title,
                    asset_type,
                    target_url,
                    local_path,
                    r2_key,
                    file_hash,
                    content_type_header,
                ),
            )
            asset_id = cur.fetchone()[0]
            print(f"  Asset registered: id={asset_id} (new)")
        else:
            print(f"  Asset reused: id={asset_id} (hash match)")

        # ---- 8. Asset sources provenance -------------------------------------
        final_url = response.url if response.url != target_url else target_url
        retrieved_at = datetime.now(timezone.utc)
        cur.execute(
            """
            INSERT INTO asset_sources
                (asset_id, source_id, original_url, normalised_url,
                 final_effective_url, retrieved_at)
            VALUES
                (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (asset_id, COALESCE(source_id, -1), original_url)
            DO NOTHING
            RETURNING id
            """,
            (asset_id, source_id, target_url, target_url, final_url, retrieved_at),
        )
        as_row = cur.fetchone()
        if as_row:
            print(f"  asset_sources: id={as_row[0]} (new)")
        else:
            print("  asset_sources: already registered")

        # ---- 9. Metadata handoff (only if new asset) -------------------------
        if not is_duplicate:
            cur.execute(
                "INSERT INTO metadata_queue (asset_id, status) VALUES (%s, 'pending')",
                (asset_id,),
            )
            print(f"  metadata_queue: asset_id={asset_id} (new)")
        else:
            print("  metadata_queue: skipped (asset already has metadata)")

        # ---- 10. Queue completion --------------------------------------------
        cur.execute(
            "UPDATE discovery_queue SET status = 'completed' WHERE id = %s",
            (queue_id,),
        )

        conn.commit()
        print(f"  Queue {queue_id}: completed")

    except Exception as exc:
        conn.rollback()
        if "queue_id" in locals():
            try:
                cur.execute(
                    """
                    UPDATE discovery_queue
                    SET status = 'failed_permanent', last_error = %s
                    WHERE id = %s
                    """,
                    (str(exc)[:500], queue_id),
                )
                conn.commit()
            except Exception:
                pass
        print(f"ERROR: {exc}", file=sys.stderr)
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()