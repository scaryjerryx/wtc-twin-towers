"""Interactive fact search engine."""

from agents.discovery.database import get_db_connection


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    search_term = input("Enter search term: ")

    cur.execute(
        """
        SELECT
            e.name,
            f.fact_text,
            f.confidence,
            f.verification_status
        FROM facts f
        JOIN entities e
            ON f.entity_id = e.id
        WHERE
            LOWER(e.name)
            LIKE LOWER(%s)
        """,
        (f"%{search_term}%",),
    )

    rows = cur.fetchall()

    print()

    if not rows:

        print("No results found.")

    else:

        for row in rows:

            print("-------------------------")
            print(f"Entity      : {row[0]}")
            print(f"Fact        : {row[1]}")
            print(f"Confidence  : {row[2]}")
            print(f"Verification: {row[3]}")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()