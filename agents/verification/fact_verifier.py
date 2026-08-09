from agents.discovery.database import get_db_connection


def calculate_status(independent_source_count):
    """Return verification status based on independent source count."""

    if independent_source_count >= 3:
        return "verified"

    if independent_source_count == 2:
        return "well_supported"

    if independent_source_count == 1:
        return "supported"

    return "claim"


def calculate_confidence(independent_source_count):
    """Return confidence score based on independent source count."""

    if independent_source_count >= 3:
        return 95

    if independent_source_count == 2:
        return 85

    if independent_source_count == 1:
        return 70

    return 50


def verify_facts():
    """Verify facts based on independent source count.

    Independent sources are counted using a composite key:
      'asset:{asset_id}' when asset_id is available (acquisition assets)
      'file:{source_file}' when asset_id is NULL (local PDFs, legacy)

    Multiple pages from the same document count as one independent source.
    Multiple facts from one asset count as one independent source per fact.
    """

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            f.id,
            f.fact_text,
            COUNT(
                DISTINCT
                CASE
                    WHEN fs.asset_id IS NOT NULL
                        THEN 'asset:' || fs.asset_id::text
                    ELSE 'file:' || fs.source_file
                END
            ) AS independent_sources
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
        independent_sources = row[2]

        status = calculate_status(
            independent_sources
        )

        confidence = calculate_confidence(
            independent_sources
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