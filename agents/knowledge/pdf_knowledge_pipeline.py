from agents.processors.pdf_text_extractor import (
    extract_text
)

from agents.knowledge.knowledge_extractor import (
    extract_entities,
    extract_facts
)

from agents.knowledge.fact_cleaner import (
    clean_facts
)

from dotenv import load_dotenv

import os
import psycopg2


load_dotenv()


def store_entities(cur, entities):

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
                "document"
            )
        )


def store_facts(cur, facts):

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
                75
            )
        )


def process_pdf(pdf_path):

    print()
    print("Extracting text...")
    print()

    text = extract_text(pdf_path)

    print()
    print("Extracting entities...")
    print()

    entities = extract_entities(text)

    print()
    print("Extracting facts...")
    print()

    facts = clean_facts(
        extract_facts(text)
    )

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    store_entities(
        cur,
        entities
    )

    store_facts(
        cur,
        facts
    )

    conn.commit()

    print()
    print("=" * 60)
    print("PDF KNOWLEDGE INGESTED")
    print("=" * 60)

    print()

    print("Entities:")

    for entity in entities:
        print(f" - {entity}")

    print()

    print("Facts:")

    for fact in facts:
        print(f" - {fact}")

    print()

    print(
        f"Entity Count: {len(entities)}"
    )

    print(
        f"Fact Count: {len(facts)}"
    )

    cur.close()
    conn.close()


if __name__ == "__main__":

    pdf_path = input(
        "PDF Path: "
    )

    process_pdf(pdf_path)