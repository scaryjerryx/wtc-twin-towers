"""M9 – Human Review & Manual Promotion.

Promote approved evidence_candidate rows from search_candidates into the
canonical discoveries table.

Usage:
    python -m agents.discovery.manual_promote --ids 121,122,125

Idempotency:
    - Query filters to record_type='evidence_candidate' AND status='pending'
    - Application-level SELECT-before-INSERT on discoveries.discovered_url
    - Already-promoted candidates are reported and skipped
    - Running with the same IDs twice is safe
"""

import argparse
import sys

from agents.discovery.database import get_db_connection


def parse_ids(ids_arg: str) -> list[int]:
    """Parse a comma-separated list of candidate IDs."""
    ids: list[int] = []
    for part in ids_arg.split(","):
        part = part.strip()
        if not part:
            continue
        try:
            ids.append(int(part))
        except ValueError:
            print(f"ERROR: Invalid candidate ID: {part!r}", file=sys.stderr)
            sys.exit(1)
    return ids


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Promote approved evidence candidates into discoveries."
    )
    parser.add_argument(
        "--ids",
        required=True,
        help="Comma-separated list of search_candidates IDs to promote",
    )
    args = parser.parse_args()

    candidate_ids = parse_ids(args.ids)

    if not candidate_ids:
        print("No candidate IDs provided.")
        return

    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # ---- 1. Fetch eligible candidates ------------------------------------
        # Only rows that are evidence_candidates and still pending.
        cur.execute(
            """
            SELECT id, source_name, target, search_url
            FROM search_candidates
            WHERE record_type = 'evidence_candidate'
              AND status = 'pending'
              AND id = ANY(%s)
            ORDER BY id
            """,
            (candidate_ids,),
        )
        candidates = cur.fetchall()

        if not candidates:
            print("No eligible candidates found.")
            print(
                "Candidates must have record_type='evidence_candidate' "
                "and status='pending'."
            )
            # Report which requested IDs were not found
            found_ids = set()
            not_found = [cid for cid in candidate_ids if cid not in found_ids]
            # We'll check below after we know what was found
            return

        found_ids = {row[0] for row in candidates}
        not_found = [cid for cid in candidate_ids if cid not in found_ids]

        promoted = 0
        already_present = 0
        skipped = 0

        for candidate in candidates:
            candidate_id, source_name, target, search_url = candidate

            # ---- 2. Application-level idempotency check ----------------------
            cur.execute(
                "SELECT id FROM discoveries WHERE discovered_url = %s",
                (search_url,),
            )
            if cur.fetchone() is not None:
                print(f"Already promoted: {search_url}")
                already_present += 1
                # Still mark the candidate as promoted so it isn't re-selected.
                cur.execute(
                    "UPDATE search_candidates SET status = 'promoted' WHERE id = %s",
                    (candidate_id,),
                )
                continue

            # ---- 3. Insert into discoveries ----------------------------------
            cur.execute(
                """
                INSERT INTO discoveries
                (source_name, target, discovered_url, status)
                VALUES (%s, %s, %s, 'approved')
                """,
                (source_name, target, search_url),
            )

            # ---- 4. Update candidate status ----------------------------------
            cur.execute(
                "UPDATE search_candidates SET status = 'promoted' WHERE id = %s",
                (candidate_id,),
            )

            promoted += 1
            print(f"Promoted: [{candidate_id}] {target} → {search_url}")

        conn.commit()

        # ---- 5. Summary ------------------------------------------------------
        print()
        print("Promotion complete.")
        print(f"  Promoted         : {promoted}")
        print(f"  Already present  : {already_present}")
        print(f"  Not found/skipped: {len(not_found)}")
        if not_found:
            print(f"  Missing IDs      : {not_found}")
        print(f"  discoveries      : canonical table updated")
        print(f"  discovery_queue  : untouched")
        print(f"  discovered_urls  : untouched")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()