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


def search_relationships(search_term):

    conn = get_connection()
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
            e1.name ASC
        """,
        (
            f"%{search_term}%",
            f"%{search_term}%"
        )
    )

    rows = cur.fetchall()

    print()
    print("=" * 60)
    print("RELATIONSHIP SEARCH")
    print("=" * 60)
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

        print("-" * 60)
        print(f"Source        : {source}")
        print(f"Relationship  : {relationship_type}")
        print(f"Target        : {target}")
        print(f"Confidence    : {confidence}")
        print(f"Evidence Count: {evidence_count}")
        print(f"Source Method : {source_method}")
        print("-" * 60)
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