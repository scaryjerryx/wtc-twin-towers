from agents.discovery.database import get_db_connection


def get_count(cur, sql):
    cur.execute(sql)
    return cur.fetchone()[0]


def print_line():
    print("-" * 80)


def print_header(title):
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)
    print()


def report_counts(cur):
    print_header("DATABASE COUNTS")

    checks = [
        ("Entities", "SELECT COUNT(*) FROM entities"),
        ("Facts", "SELECT COUNT(*) FROM facts"),
        ("Fact Sources", "SELECT COUNT(*) FROM fact_sources"),
        ("Citations", "SELECT COUNT(*) FROM citations"),
        ("Relationships", "SELECT COUNT(*) FROM relationships"),
        ("Entity Aliases", "SELECT COUNT(*) FROM entity_aliases")
    ]

    for label, sql in checks:
        try:
            print(f"{label:<35} {get_count(cur, sql)}")
        except Exception:
            print(f"{label:<35} unavailable")


def report_verification(cur):
    print_header("FACT VERIFICATION")

    cur.execute(
        "SELECT verification_status, COUNT(*) FROM facts GROUP BY verification_status ORDER BY verification_status"
    )

    rows = cur.fetchall()

    if not rows:
        print("No verification data available.")
        return

    for status, count in rows:
        print(f"{status:<35} {count}")


def report_relationships(cur):
    print_header("RELATIONSHIP TYPES")

    cur.execute(
        "SELECT relationship_type, COUNT(*) FROM relationships GROUP BY relationship_type ORDER BY relationship_type"
    )

    rows = cur.fetchall()

    if not rows:
        print("No relationships found.")
        return

    for rel_type, count in rows:
        print(f"{rel_type:<35} {count}")


def report_assets(cur):
    print_header("ASSETS")

    cur.execute(
        "SELECT download_status, COUNT(*) FROM assets GROUP BY download_status ORDER BY download_status"
    )

    rows = cur.fetchall()

    if not rows:
        print("No assets found.")
        return

    for status, count in rows:
        print(f"{status:<35} {count}")


def run_health_report():

    conn = get_db_connection()
    cur = conn.cursor()

    report_counts(cur)
    report_verification(cur)
    report_relationships(cur)
    report_assets(cur)

    print()
    print("=" * 80)
    print("HEALTH REPORT COMPLETE")
    print("=" * 80)
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    run_health_report()