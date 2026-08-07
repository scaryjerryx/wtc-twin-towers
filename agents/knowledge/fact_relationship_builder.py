import os
import psycopg2

from dotenv import load_dotenv


load_dotenv()


def get_or_create_entity(cur, name):

    cur.execute(
        """
        INSERT INTO entities
        (
            name,
            entity_type
        )
        VALUES
        (
            %s,
            %s
        )
        ON CONFLICT (name)
        DO NOTHING
        """,
        (
            name,
            "fact"
        )
    )

    cur.execute(
        """
        SELECT id
        FROM entities
        WHERE name = %s
        """,
        (
            name,
        )
    )

    row = cur.fetchone()

    return row[0]


def create_relationship(
    cur,
    source_name,
    relationship_type,
    target_name
):

    source_id = get_or_create_entity(
        cur,
        source_name
    )

    target_id = get_or_create_entity(
        cur,
        target_name
    )

    cur.execute(
        """
        INSERT INTO relationships
        (
            source_entity_id,
            relationship_type,
            target_entity_id,
            confidence
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT
        (
            source_entity_id,
            relationship_type,
            target_entity_id
        )
        DO NOTHING
        """,
        (
            source_id,
            relationship_type,
            target_id,
            75
        )
    )


def build_relationships():

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            fs.source_page,
            f.fact_text
        FROM fact_sources fs
        JOIN facts f
            ON fs.fact_id = f.id
        ORDER BY
            fs.source_page,
            f.fact_text
        """
    )

    rows = cur.fetchall()

    page_facts = {}

    for page, fact in rows:

        page_facts.setdefault(
            page,
            []
        ).append(fact)

    relationships_created = 0

    for page, facts in page_facts.items():

        drawing_books = [
            f
            for f in facts
            if f.startswith(
                "Drawing Book"
            )
        ]

        for drawing_book in drawing_books:

            for fact in facts:

                if fact == drawing_book:
                    continue

                create_relationship(
                    cur,
                    fact,
                    "appears_in",
                    drawing_book
                )

                relationships_created += 1

        exterior_walls = [
            f
            for f in facts
            if f.startswith(
                "Exterior Wall"
            )
        ]

        for wall in exterior_walls:

            for fact in facts:

                if fact == wall:
                    continue

                create_relationship(
                    cur,
                    fact,
                    "associated_with",
                    wall
                )

                relationships_created += 1

    conn.commit()

    print()
    print("=" * 60)
    print("FACT RELATIONSHIP BUILD COMPLETE")
    print("=" * 60)

    print()

    print(
        f"Pages Processed: "
        f"{len(page_facts)}"
    )

    print(
        f"Relationships Created: "
        f"{relationships_created}"
    )

    cur.close()
    conn.close()


if __name__ == "__main__":

    build_relationships()