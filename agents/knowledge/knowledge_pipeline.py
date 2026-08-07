import os
import psycopg2

from dotenv import load_dotenv
from knowledge_extractor import (
    extract_entities,
    extract_facts
)

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
    SELECT
        id,
        asset_id,
        image_description
    FROM ai_analysis
    WHERE image_description IS NOT NULL
""")

rows = cur.fetchall()

for row in rows:

    analysis_id = row[0]
    asset_id = row[1]
    description = row[2]

    entities = extract_entities(description)
    facts = extract_facts(description)

    print()
    print(f"Analysis: {analysis_id}")

    print("Entities:")
    print(entities)

    print("Facts:")
    print(facts)

    #
    # Store Entities
    #
    for entity in entities:

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
                entity,
                "unknown"
            )
        )

    #
    # Store Facts
    #
    for fact in facts:

        cur.execute(
            """
            INSERT INTO facts
            (
                entity_id,
                fact_text,
                confidence
            )
            VALUES
            (
                NULL,
                %s,
                %s
            )
            """,
            (
                fact,
                50
            )
        )

conn.commit()

print()
print("Knowledge Pipeline Complete")

cur.close()
conn.close()