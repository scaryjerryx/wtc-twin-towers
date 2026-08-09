"""M12 – Asset Source Registration.

Register one retrieval event per asset-source-URL combination into
asset_sources, providing retrieval-event provenance for every downloaded
asset.

Usage:
    python -m agents.downloader.register_asset

Idempotency:
    - Unique constraint on (asset_id, COALESCE(source_id, -1), original_url)
    - ON CONFLICT DO NOTHING prevents duplicate registration
    - Repeated calls with the same parameters are safe no-ops
    - A genuinely new retrieval (different URL) creates a new row
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from agents.discovery.database import get_db_connection


def register_asset_source(
    asset_id: int,
    source_id: Optional[int],
    original_url: str,
    normalised_url: Optional[str] = None,
    final_effective_url: Optional[str] = None,
    retrieved_at: Optional[datetime] = None,
) -> Optional[int]:
    """Insert one asset_sources row for a retrieval event.

    Returns the new asset_sources.id, or None if the row already existed
    (idempotent via unique constraint).

    Args:
        asset_id: The assets.id this retrieval produced.
        source_id: The sources.id this URL was discovered from (nullable).
        original_url: The URL as originally discovered.
        normalised_url: Normalised form of the URL (optional).
        final_effective_url: The final URL after redirects (optional).
        retrieved_at: When the retrieval occurred (defaults to now()).
    """
    conn = get_db_connection()
    cur = conn.cursor()

    try:
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
            (
                asset_id,
                source_id,
                original_url,
                normalised_url,
                final_effective_url,
                retrieved_at if retrieved_at is not None else datetime.now(timezone.utc),
            ),
        )

        row = cur.fetchone()
        conn.commit()

        if row is not None:
            new_id: int = row[0]
            print(
                f"Registered asset_sources id={new_id}: "
                f"asset={asset_id} source={source_id} "
                f"url={original_url[:80]}"
            )
            return new_id
        else:
            print(
                f"Already registered: asset={asset_id} source={source_id} "
                f"url={original_url[:80]}"
            )
            return None

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


def main() -> None:
    """Quick smoke-test: register a retrieval event for an existing asset."""
    import sys

    # Default test: asset 1 (Test Image 4), source 4 (Wikimedia Commons)
    asset_id = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    source_id = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    test_url = sys.argv[3] if len(sys.argv) > 3 else (
        "https://commons.wikimedia.org/wiki/File:WTC_Plaza_Test.jpg"
    )

    result = register_asset_source(
        asset_id=asset_id,
        source_id=source_id,
        original_url=test_url,
        normalised_url=test_url,
        final_effective_url=test_url,
    )

    if result is not None:
        print(f"Registration successful: asset_sources.id={result}")
    else:
        print("Registration skipped (already exists).")


if __name__ == "__main__":
    main()