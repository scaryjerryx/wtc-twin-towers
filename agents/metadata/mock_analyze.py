"""M15 — Metadata Processing (Mock Analysis).

Read one pending metadata_queue row, insert mock ai_analysis data,
and update the queue and asset statuses to completed.

Usage:
    python -m agents.metadata.mock_analyze
"""

from agents.discovery.database import get_db_connection


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

        if item:
            queue_id = item[0]
            asset_id = item[1]

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
                    '{"agent":"mock"}',
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

            print(f"Processed Asset {asset_id}")

        else:
            print("No pending metadata items")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()