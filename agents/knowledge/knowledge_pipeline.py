from agents.processors.pdf_text_extractor import (
    extract_pages
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


def store_fact(
    cur,
    fact,
    source_file,
    source_page
):

    cur.execute(
        """
        INSERT INTO facts
        (
            entity_id,
            fact_text,
            confidence,
            source_file,
            source_page
        )
        VALUES
        (
            NULL,
            %s,
            %s,
            %s,
            %s
        )
        ON CONFLICT (fact_text)
        DO NOTHING
        """,
        (
            fact,
            75,
            source_file,
            source_page
        )
    )


def process_pdf(pdf_path):

    source_file = os.path.basename(
        pdf_path
    )

    print()
    print("Extracting pages...")
    print()

    pages = extract_pages(
        pdf_path
    )

    all_entities = set()
    all_facts = set()

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        entities = extract_entities(
            text
        )

        facts = clean_facts(
            extract_facts(text)
        )

        print(
            f"Processing page {page_number}"
        )

        for entity in entities:
            all_entities.add(entity)

        for fact in facts:

            all_facts.add(fact)

            store_fact(
                cur,
                fact,
                source_file,
                page_number
            )

    store_entities(
        cur,
        sorted(all_entities)
    )

    conn.commit()

    print()
    print("=" * 60)
    print("PDF KNOWLEDGE INGESTED")
    print("=" * 60)

    print()

    print(
        f"Source File: {source_file}"
    )

    print()

    print("Entities:")

    for entity in sorted(all_entities):
        print(f" - {entity}")

    print()

    print("Facts:")

    for fact in sorted(all_facts):
        print(f" - {fact}")

    print()

    print(
        f"Entity Count: {len(all_entities)}"
    )

    print(
        f"Fact Count: {len(all_facts)}"
    )

    cur.close()
    conn.close()


if __name__ == "__main__":

    pdf_path = input(
        "PDF Path: "
    )

    process_pdf(
        pdf_path
    )