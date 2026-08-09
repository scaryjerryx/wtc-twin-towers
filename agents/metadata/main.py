"""Diagnostic metadata-queue inspector — not the processor."""

from agents.discovery.database import get_db_connection


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

    if queue_item:

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

        if asset:

            print(f"Queue ID: {queue_id}")
            print(f"Asset ID: {asset[0]}")
            print(f"Title: {asset[1]}")
            print(f"R2 Key: {asset[2]}")
            print(f"Source URL: {asset[3]}")

    else:

        print("No pending metadata items")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()