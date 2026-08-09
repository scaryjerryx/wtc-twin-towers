"""M19 — AI-Powered Metadata Processing.

Read one pending metadata_queue row, download the asset from R2,
send it to OpenRouter for AI analysis, and store results in ai_analysis.

Provider selection via METADATA_PROVIDER environment variable:
    METADATA_PROVIDER=mock        → uses mock_analyze logic (no API calls)
    METADATA_PROVIDER=openrouter  → uses OpenRouter AI (default)

Usage:
    python -m agents.metadata.ai_analyze
"""

from __future__ import annotations

import json
import os
import tempfile
from datetime import datetime, timezone

from dotenv import load_dotenv

load_dotenv(".secrets/cline-db.env")

from agents.discovery.database import get_db_connection
from agents.metadata.r2_download import download_file


def _run_mock_analysis(cur, asset_id: int, queue_id: int) -> None:
    """Insert mock analysis data (no API calls)."""
    cur.execute(
        """
        INSERT INTO ai_analysis
            (asset_id, tower, floor, area, estimated_year,
             confidence_score, analysis_json)
        VALUES
            (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            asset_id,
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            50,
            json.dumps(
                {
                    "agent": "mock",
                    "model": "mock",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
            ),
        ),
    )
    cur.execute(
        "UPDATE metadata_queue SET status = 'completed' WHERE id = %s",
        (queue_id,),
    )
    cur.execute(
        "UPDATE assets SET metadata_status = 'completed' WHERE id = %s",
        (asset_id,),
    )
    # Mock analysis never has high-enough confidence to override classification.
    print("  Classification skipped (mock provider)")


def _run_openrouter_analysis(
    cur,
    asset_id: int,
    queue_id: int,
    r2_key: str,
) -> None:
    """Download from R2, send to OpenRouter AI, store results, classify."""
    from agents.metadata.ai_client import analyze_with_ai  # noqa: PLC0415

    ext = os.path.splitext(r2_key or "asset.bin")[1] or ".bin"
    fd, local_file = tempfile.mkstemp(suffix=ext, prefix=f"ai_asset_{asset_id}_")
    os.close(fd)

    try:
        download_file(r2_key, local_file)

        analysis = analyze_with_ai(local_file)

        now_iso = datetime.now(timezone.utc).isoformat()

        cur.execute(
            """
            INSERT INTO ai_analysis
                (asset_id, tower, floor, area, estimated_year,
                 confidence_score, image_description, tags,
                 analysis_version, analysis_json,
                 asset_type_detected, asset_type_confidence)
            VALUES
                (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """,
            (
                asset_id,
                analysis["tower"],
                analysis["floor"],
                analysis["area"],
                analysis["estimated_year"],
                analysis["confidence_score"],
                analysis["description"],
                analysis["tags"],
                "ai-v1",
                json.dumps(
                    {
                        "agent": "openrouter",
                        "model": analysis["model"],
                        "timestamp": now_iso,
                    }
                ),
                analysis["asset_type"],
                analysis["asset_type_confidence"],
            ),
        )

        cur.execute(
            "UPDATE metadata_queue SET status = 'completed' WHERE id = %s",
            (queue_id,),
        )
        cur.execute(
            "UPDATE assets SET metadata_status = 'completed' WHERE id = %s",
            (asset_id,),
        )

        # ---- M20 Classification: refine asset_type from AI results ----------
        classification = analysis.get("asset_type")
        classification_confidence = analysis.get("asset_type_confidence", 0)
        if (
            classification
            and classification_confidence > 60
            and classification != "unknown"
        ):
            cur.execute(
                "UPDATE assets SET asset_type = %s WHERE id = %s",
                (classification, asset_id),
            )
            print(f"  Classified as: {classification} (confidence: {classification_confidence})")
        else:
            print(f"  Classify skipped (confidence: {classification_confidence}, type: {classification})")

        print(f"  Provider : openrouter")
        print(f"  Model    : {analysis['model']}")
        print(f"  Type     : {analysis['asset_type']}")
        print(f"  Desc     : {analysis['description'][:80]}")

    finally:
        if os.path.exists(local_file):
            os.unlink(local_file)


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT id, asset_id
            FROM metadata_queue
            WHERE status = 'pending'
            LIMIT 1
            """
        )

        item = cur.fetchone()

        if item is None:
            print("No pending metadata items")
            return

        queue_id = item[0]
        asset_id = item[1]

        cur.execute(
            """
            SELECT id, r2_key, title, content_type
            FROM assets
            WHERE id = %s
            """,
            (asset_id,),
        )
        asset = cur.fetchone()
        if asset is None:
            print(f"Asset {asset_id} not found")
            return

        r2_key = asset[1]

        print()
        print("=" * 60)
        print("METADATA PROCESSING")
        print("=" * 60)
        print()
        print(f"  Queue ID : {queue_id}")
        print(f"  Asset ID : {asset_id}")

        provider = os.getenv("METADATA_PROVIDER", "openrouter").strip().lower()

        if provider == "mock":
            print(f"  Provider : mock")
            _run_mock_analysis(cur, asset_id, queue_id)
        elif provider == "openrouter":
            _run_openrouter_analysis(cur, asset_id, queue_id, r2_key)
        else:
            print(f"Unknown METADATA_PROVIDER '{provider}' — using openrouter")
            _run_openrouter_analysis(cur, asset_id, queue_id, r2_key)

        conn.commit()
        print(f"\n  Asset {asset_id}: metadata complete")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()