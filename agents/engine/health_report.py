import os
import psycopg2

from dotenv import load_dotenv


load_dotenv()


def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


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
        print("No facts found.")
        return

    for status, total in rows:
        print(f"{status or 'unknown':<35} {total}")


def report_quality(cur):
    print_header("DATA QUALITY")

    facts_without_sources = get_count(
        cur,
        "SELECT COUNT(*) FROM facts f LEFT JOIN fact_sources fs ON f.id = fs.fact_id WHERE fs.id IS NULL"
    )

    relationships_without_method = get_count(
        cur,
        "SELECT COUNT(*) FROM relationships WHERE source_method IS NULL"
    )

    print(f"{'Facts without sources':<35} {facts_without_sources}")
    print(f"{'Relationships without method':<35} {relationships_without_method}")


def report_sources(cur):
    print_header("TOP SOURCE FILES")

    cur.execute(
        "SELECT source_file, COUNT(*) FROM fact_sources GROUP BY source_file ORDER BY COUNT(*) DESC LIMIT 10"
    )

    rows = cur.fetchall()

    if not rows:
        print("No source files found.")
        return

    for source_file, total in rows:
        print(f"{source_file:<35} {total}")


def report_relationships(cur):
    print_header("TOP RELATIONSHIPS")

    cur.execute(
        "SELECT e1.name, r.relationship_type, e2.name, r.confidence, r.evidence_count, r.source_method FROM relationships r JOIN entities e1 ON r.source_entity_id = e1.id JOIN entities e2 ON r.target_entity_id = e2.id ORDER BY r.confidence DESC, r.evidence_count DESC LIMIT 10"
    )

    rows = cur.fetchall()

    if not rows:
        print("No relationships found.")
        return

    for row in rows:
        print_line()
        print(f"Source        : {row[0]}")
        print(f"Relationship  : {row[1]}")
        print(f"Target        : {row[2]}")
        print(f"Confidence    : {row[3]}")
        print(f"Evidence Count: {row[4]}")
        print(f"Source Method : {row[5]}")
        print_line()


def build_health_report():
    conn = get_connection()
    cur = conn.cursor()

    print_header("WTC KNOWLEDGE ENGINE HEALTH REPORT")

    report_counts(cur)
    report_verification(cur)
    report_quality(cur)
    report_sources(cur)
    report_relationships(cur)

    print_header("HEALTH REPORT COMPLETE")

    cur.close()
    conn.close()


if __name__ == "__main__":
    build_health_report()
