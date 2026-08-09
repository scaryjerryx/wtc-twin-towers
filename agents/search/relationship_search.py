from agents.discovery.database import get_db_connection


def get_fact_details(cur, fact_text):

    cur.execute(
        """
        SELECT
            id,
            confidence,
            verification_status
        FROM facts
        WHERE fact_text = %s
        """,
        (
            fact_text,
        )
    )

    fact = cur.fetchone()

    if not fact:

        return {
            "fact_id": None,
            "confidence": None,
            "verification_status": None,
            "sources": []
        }

    fact_id = fact[0]
    confidence = fact[1]
    verification_status = fact[2]

    cur.execute(
        """
        SELECT
            source_file,
            source_page,
            confidence
        FROM fact_sources
        WHERE fact_id = %s
        ORDER BY
            source_file,
            source_page
        """,
        (
            fact_id,
        )
    )

    sources = cur.fetchall()

    return {
        "fact_id": fact_id,
        "confidence": confidence,
        "verification_status": verification_status,
        "sources": sources
    }


def print_fact_details(label, details):

    print(f"{label} Fact ID        : {details['fact_id']}")
    print(f"{label} Confidence     : {details['confidence']}")
    print(f"{label} Verification   : {details['verification_status']}")

    sources = details["sources"]

    if not sources:

        print(f"{label} Sources        : None")
        return

    print(f"{label} Sources:")

    for source in sources:

        source_file = source[0]
        source_page = source[1]
        source_confidence = source[2]

        print(
            f"  - {source_file} | "
            f"page {source_page} | "
            f"confidence {source_confidence}"
        )


def search_relationships(search_term):

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            e1.name AS source,
            r.relationship_type,
            e2.name AS target,
            r.confidence,
            r.evidence_count,
            r.source_method
        FROM relationships r
        JOIN entities e1
            ON r.source_entity_id = e1.id
        JOIN entities e2
            ON r.target_entity_id = e2.id
        WHERE
            LOWER(e1.name) LIKE LOWER(%s)
            OR LOWER(e2.name) LIKE LOWER(%s)
        ORDER BY
            r.confidence DESC,
            r.evidence_count DESC,
            e1.name ASC,
            e2.name ASC
        """,
        (
            f"%{search_term}%",
            f"%{search_term}%"
        )
    )

    rows = cur.fetchall()

    print()
    print("=" * 80)
    print("RELATIONSHIP SEARCH V2")
    print("=" * 80)
    print()
    print(f"Search Term: {search_term}")
    print()

    if not rows:

        print("No relationships found.")
        print()

        cur.close()
        conn.close()

        return

    for row in rows:

        source = row[0]
        relationship_type = row[1]
        target = row[2]
        confidence = row[3]
        evidence_count = row[4]
        source_method = row[5]

        source_details = get_fact_details(
            cur,
            source
        )

        target_details = get_fact_details(
            cur,
            target
        )

        print("=" * 80)
        print(f"Source              : {source}")
        print(f"Relationship        : {relationship_type}")
        print(f"Target              : {target}")
        print(f"Relation Confidence : {confidence}")
        print(f"Evidence Count      : {evidence_count}")
        print(f"Source Method       : {source_method}")
        print("-" * 80)

        print_fact_details(
            "Source",
            source_details
        )

        print("-" * 80)

        print_fact_details(
            "Target",
            target_details
        )

        print("=" * 80)
        print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    search_term = input(
        "Search relationship term: "
    )

    search_relationships(
        search_term
    )