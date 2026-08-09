"""Export discoveries rows for review.

Reads from the canonical discoveries table.

Usage:
    python -m agents.discovery.export_discoveries
"""

from agents.discovery.database import get_db_connection


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, source_name, target, discovered_url, status, created_at
        FROM discoveries
        ORDER BY id
        """
    )

    rows = cur.fetchall()

    if not rows:
        print("No discoveries found.")
        cur.close()
        conn.close()
        return

    print(f"{'ID':<6} {'Source':<25} {'Target':<30} {'Status':<12} {'Created':<20} URL")
    print("-" * 140)

    for row in rows:
        discovery_id, source_name, target, discovered_url, status, created_at = row
        created_str = str(created_at)[:19] if created_at else "N/A"
        print(
            f"{discovery_id:<6} "
            f"{source_name[:24] if source_name else 'N/A':<25} "
            f"{target[:29] if target else 'N/A':<30} "
            f"{status or 'N/A':<12} "
            f"{created_str:<20} "
            f"{discovered_url}"
        )

    print()
    print(f"Total: {len(rows)} rows")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()