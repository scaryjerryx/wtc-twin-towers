from agents.discovery.database import get_db_connection


def calculate_status(source_count):

    if source_count >= 3:
        return "verified"

    if source_count == 2:
        return "well_supported"

    if source_count == 1:
        return "supported"

    return "claim"


def calculate_confidence(source_count):

    if source_count >= 3:
        return 95

    if source_count == 2:
        return 85

    if source_count == 1:
        return 70

    return 50


def verify_facts():

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            f.id,
            f.fact_text,
            COUNT(fs.id) AS source_count
        FROM facts f
        LEFT JOIN fact_sources fs
            ON f.id = fs.fact_id
        GROUP BY
            f.id,
            f.fact_text
        ORDER BY
            f.id
        """
    )

    rows = cur.fetchall()

    updated_count = 0

    for row in rows:

        fact_id = row[0]
        fact_text = row[1]
        source_count = row[2]

        status = calculate_status(
            source_count
        )

        confidence = calculate_confidence(
            source_count
        )

        cur.execute(
            """
            UPDATE facts
            SET
                verification_status = %s,
                confidence = %s
            WHERE id = %s
            """,
            (
                status,
                confidence,
                fact_id
            )
        )

        updated_count += 1

    conn.commit()

    print()
    print("=" * 60)
    print("FACT VERIFICATION COMPLETE")
    print("=" * 60)
    print()
    print(f"Facts Verified: {updated_count}")
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    verify_facts()