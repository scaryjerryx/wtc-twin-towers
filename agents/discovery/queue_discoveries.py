"""M10 – Discovery Queue.

Read approved discoveries from the canonical discoveries table and queue
them into discovery_queue for the downloader, linking via discovery_id.

Usage:
    python -m agents.discovery.queue_discoveries

Idempotency:
    - LEFT JOIN on discovery_id ensures already-queued discoveries are excluded
    - ON CONFLICT (target_url) DO NOTHING prevents duplicate queue rows
    - No boolean flag to go stale — queue membership derived from JOIN
    - Crash-safe: re-run re-queues only discoveries still missing queue rows
"""

import sys

from agents.discovery.database import get_db_connection


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # ---- 1. Find approved discoveries not yet queued ------------------------
        cur.execute(
            """
            SELECT d.id, d.source_name, d.target, d.discovered_url
            FROM discoveries d
            LEFT JOIN discovery_queue dq ON d.id = dq.discovery_id
            WHERE dq.id IS NULL
              AND d.status = 'approved'
            ORDER BY d.id
            """
        )
        discoveries = cur.fetchall()

        if not discoveries:
            print("No unqueued approved discoveries found.")
            return

        queued = 0
        already_present = 0

        for discovery in discoveries:
            discovery_id, source_name, target, discovered_url = discovery

            cur.execute(
                """
                INSERT INTO discovery_queue
                    (source_name, title, target_url, discovery_id, status)
                VALUES
                    (%s, %s, %s, %s, 'pending')
                ON CONFLICT (target_url) DO NOTHING
                RETURNING id
                """,
                (source_name, target, discovered_url, discovery_id),
            )

            if cur.fetchone() is not None:
                queued += 1
                print(
                    f"Queued: [{discovery_id}] {target} → {discovered_url[:80]}"
                )
            else:
                already_present += 1
                print(
                    f"Already present: [{discovery_id}] {target} → {discovered_url[:80]}"
                )

        conn.commit()

        # ---- 2. Summary ----------------------------------------------------------
        print()
        print("Queue creation complete.")
        print(f"  Queued           : {queued}")
        print(f"  Already present  : {already_present}")
        print(f"  Total eligible   : {len(discoveries)}")
        print(f"  discovery_queue  : discovery_id FK populated")
        print(f"  discovered_urls  : untouched")
        print(f"  search_candidates: untouched")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()