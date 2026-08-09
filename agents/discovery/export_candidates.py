"""Export search_candidates rows for human review.

Usage:
    python -m agents.discovery.export_candidates
    python -m agents.discovery.export_candidates --type evidence_candidate
    python -m agents.discovery.export_candidates --type search_request
"""

import argparse

from agents.discovery.database import get_db_connection


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export search_candidates for review."
    )
    parser.add_argument(
        "--type",
        dest="record_type",
        choices=["evidence_candidate", "search_request"],
        default=None,
        help="Filter by record_type (default: all rows)",
    )
    args = parser.parse_args()

    conn = get_db_connection()
    cur = conn.cursor()

    if args.record_type:
        cur.execute(
            """
            SELECT id, source_name, target, search_url, record_type, status
            FROM search_candidates
            WHERE record_type = %s
            ORDER BY id
            """,
            (args.record_type,),
        )
    else:
        cur.execute(
            """
            SELECT id, source_name, target, search_url, record_type, status
            FROM search_candidates
            ORDER BY id
            """
        )

    rows = cur.fetchall()

    if not rows:
        print("No candidates found.")
        cur.close()
        conn.close()
        return

    print(f"{'ID':<6} {'Source':<25} {'Target':<30} {'Type':<20} {'Status':<12} URL")
    print("-" * 140)

    for row in rows:
        candidate_id, source_name, target, search_url, record_type, status = row
        print(
            f"{candidate_id:<6} "
            f"{source_name[:24]:<25} "
            f"{target[:29]:<30} "
            f"{record_type or 'N/A':<20} "
            f"{status or 'N/A':<12} "
            f"{search_url}"
        )

    print()
    print(f"Total: {len(rows)} rows")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()