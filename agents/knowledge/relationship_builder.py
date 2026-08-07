import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

KNOWN_RELATIONSHIPS = [
    (
        "Windows on the World",
        "located_in",
        "North Tower"
    ),
    (
        "North Tower",
        "part_of",
        "World Trade Center"
    ),
    (
        "South Tower",
        "part_of",
        "World Trade Center"
    ),
    (
        "Observation Deck",
        "located_in",
        "South Tower"
    ),
    (
        "Austin J Tobin Plaza",
        "part_of",
        "World Trade Center"
    )
]

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()


def get_entity_id(entity_name):

    cur.execute(
        """
        SELECT id
        FROM entities
        WHERE name = %s
        """,
        (entity_name,)
    )

    row = cur.fetchone()

    if row:
        return row[0]

    return None


for source_name, relationship_type, target_name in KNOWN_RELATIONSHIPS:

    source_id = get_entity_id(source_name)
    target_id = get_entity_id(target_name)

    if not source_id:

        cur.execute(
            """
            INSERT INTO entities
            (
                name,
                entity_type
            )
            VALUES
            (%s, %s)
            ON CONFLICT (name)
            DO NOTHING
            """,
            (
                source_name,
                "unknown"
            )
        )

        conn.commit()

        source_id = get_entity_id(source_name)

    if not target_id:

        cur.execute(
            """
            INSERT INTO entities
            (
                name,
                entity_type
            )
            VALUES
            (%s, %s)
            ON CONFLICT (name)
            DO NOTHING
            """,
            (
                target_name,
                "unknown"
            )
        )

        conn.commit()

        target_id = get_entity_id(target_name)

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
        """,
        (
            source_id,
            relationship_type,
            target_id,
            90
        )
    )

    print(
        f"Created relationship: "
        f"{source_name} "
        f"--{relationship_type}--> "
        f"{target_name}"
    )

conn.commit()

cur.close()
conn.close()

print()
print("Relationship Build Complete")