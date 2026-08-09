"""Vision Analysis — reads metadata_queue, downloads from R2, analyses image, writes ai_analysis."""

from agents.discovery.database import get_db_connection
from agents.metadata.r2_download import download_file
from agents.metadata.vision_client import analyze_image


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, asset_id
        FROM metadata_queue
        WHERE status = 'pending'
        LIMIT 1
        """
    )

    queue_item = cur.fetchone()

    if not queue_item:

        print("No pending metadata items")

        cur.close()
        conn.close()
        return

    queue_id = queue_item[0]
    asset_id = queue_item[1]

    cur.execute(
        """
        SELECT
            id,
            title,
            r2_key,
            source_url
        FROM assets
        WHERE id = %s
        """,
        (asset_id,),
    )

    asset = cur.fetchone()

    if not asset:

        print("Asset not found")

        cur.close()
        conn.close()
        return

    r2_key = asset[2]

    local_file = f"tmp/asset_{asset_id}.jpg"

    download_file(r2_key, local_file)

    analysis = analyze_image(local_file)

    asset_type = analysis["asset_type"]
    asset_type_confidence = analysis["asset_type_confidence"]

    description = analysis["description"]
    tags = analysis["tags"]
    confidence_score = analysis["confidence"]

    cur.execute(
        """
        INSERT INTO ai_analysis
        (
            asset_id,
            tower,
            floor,
            area,
            estimated_year,
            confidence_score,
            image_description,
            tags,
            analysis_version,
            analysis_json,
            asset_type_detected,
            asset_type_confidence
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
        """,
        (
            asset_id,
            "Unknown",
            "Unknown",
            "Unknown",
            "Unknown",
            confidence_score,
            description,
            tags,
            "v2",
            '{"agent":"vision_analyze"}',
            asset_type,
            asset_type_confidence,
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

    conn.commit()

    print()
    print("Analysis Complete")
    print("-----------------")
    print(f"Queue ID              : {queue_id}")
    print(f"Asset ID              : {asset_id}")
    print(f"Title                 : {asset[1]}")
    print(f"Local File            : {local_file}")
    print(f"Asset Type            : {asset_type}")
    print(f"Type Confidence       : {asset_type_confidence}")
    print(f"Description           : {description}")
    print(f"Tags                  : {tags}")
    print(f"Analysis Confidence   : {confidence_score}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()