import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

search_term = input(
    "Enter entity name: "
)

cur.execute(
    """
    SELECT
        id,
        name
    FROM entities
    WHERE LOWER(name)
    LIKE LOWER(%s)
    """,
    (
        f"%{search_term}%",
    )
)

entity = cur.fetchone()

if not entity:

    print("Entity not found")

    cur.close()
    conn.close()
    exit()

entity_id = entity[0]
entity_name = entity[1]

print()
print("=" * 50)
print(f"ENTITY: {entity_name}")
print("=" * 50)

#
# Facts
#
print()
print("FACTS")
print("-" * 50)

cur.execute(
    """
    SELECT
        fact_text,
        confidence,
        verification_status
    FROM facts
    WHERE entity_id = %s
    """,
    (entity_id,)
)

facts = cur.fetchall()

if facts:

    for fact in facts:

        print(f"Fact         : {fact[0]}")
        print(f"Confidence   : {fact[1]}")
        print(f"Verification : {fact[2]}")
        print()

else:

    print("No facts found")

#
# Outgoing Relationships
#
print()
print("RELATIONSHIPS")
print("-" * 50)

cur.execute(
    """
    SELECT
        r.relationship_type,
        e.name
    FROM relationships r
    JOIN entities e
        ON r.target_entity_id = e.id
    WHERE r.source_entity_id = %s
    """,
    (entity_id,)
)

relationships = cur.fetchall()

if relationships:

    for rel in relationships:

        print(
            f"{rel[0]} -> {rel[1]}"
        )

else:

    print("No relationships found")

#
# Incoming Relationships
#
print()
print("CONNECTED FROM")
print("-" * 50)

cur.execute(
    """
    SELECT
        r.relationship_type,
        e.name
    FROM relationships r
    JOIN entities e
        ON r.source_entity_id = e.id
    WHERE r.target_entity_id = %s
    """,
    (entity_id,)
)

incoming = cur.fetchall()

if incoming:

    for rel in incoming:

        print(
            f"{e.name if False else rel[1]} "
            f"--{rel[0]}--> "
            f"{entity_name}"
        )

else:

    print("No incoming relationships")

cur.close()
conn.close()