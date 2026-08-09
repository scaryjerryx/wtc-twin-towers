"""M17 — Acquisition Asset Knowledge Processor.

Query assets from the acquisition pipeline that are ready for knowledge
extraction (downloaded, metadata-complete, PDF content type), download
them from R2, and process them through the PDF knowledge pipeline.

Usage:
    from agents.ingestion.process_acquisition_assets import (
        process_acquisition_assets
    )
"""

from __future__ import annotations

import os
import tempfile

from agents.discovery.database import get_db_connection
from agents.knowledge.pdf_knowledge_pipeline import process_pdf
from agents.metadata.r2_download import download_file


def process_acquisition_assets() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    # Count total acquisition assets for reporting
    cur.execute(
        "SELECT COUNT(*) FROM assets WHERE source_id IS NOT NULL"
    )
    total_acquisition = cur.fetchone()[0]

    # Select PDF assets ready for knowledge processing
    cur.execute(
        """
        SELECT id, r2_key, title, source_url, content_type
        FROM assets
        WHERE download_status = 'downloaded'
          AND metadata_status = 'completed'
          AND content_type ILIKE '%pdf%'
          AND r2_key IS NOT NULL
        ORDER BY id
        """
    )

    pdf_assets = cur.fetchall()

    print()
    print("=" * 60)
    print("ACQUISITION ASSET PROCESSING")
    print("=" * 60)
    print()
    print(f"Total acquisition assets: {total_acquisition}")
    print(f"PDF assets eligible: {len(pdf_assets)}")
    print()

    if not pdf_assets:
        print("No eligible PDF assets found.")
        print(
            "(Assets with content_type not containing 'pdf', "
            "incomplete downloads, or pending metadata are skipped.)"
        )
        print()

        cur.close()
        conn.close()
        return

    processed_count = 0
    skipped_count = 0

    for asset in pdf_assets:
        asset_id = asset[0]
        r2_key = asset[1]
        title = asset[2]
        source_url = asset[3]
        content_type = asset[4]

        # Build a provenance source_file identifier from the asset record
        source_file = f"acquisition_asset_{asset_id}"

        print()
        print("-" * 60)
        print(f"Asset ID      : {asset_id}")
        print(f"Title         : {title or '(none)'}")
        print(f"R2 Key        : {r2_key}")
        print(f"Content-Type  : {content_type}")
        print(f"Source File   : {source_file}")
        print("-" * 60)

        # Download the asset from R2 to a temporary file
        ext = ".pdf"
        fd, tmp_path = tempfile.mkstemp(suffix=ext, prefix=f"asset_{asset_id}_")
        os.close(fd)

        try:
            download_file(r2_key, tmp_path)
        except Exception as exc:
            print(f"R2 download failed: {exc}")
            print("Skipped.")
            skipped_count += 1
            os.unlink(tmp_path)
            continue

        # Process through the PDF knowledge pipeline with explicit provenance
        try:
            process_pdf(tmp_path, source_file=source_file)
            processed_count += 1
        except Exception as exc:
            print(f"Knowledge extraction failed: {exc}")
            print("Skipped.")
            skipped_count += 1
        finally:
            # Clean up the temporary file
            if os.path.exists(tmp_path):
                os.unlink(tmp_path)

    cur.close()
    conn.close()

    print()
    print("=" * 60)
    print("ACQUISITION ASSET PROCESSING COMPLETE")
    print("=" * 60)
    print()
    print(f"Processed : {processed_count}")
    print(f"Skipped   : {skipped_count}")
    print()