import os

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

from agents.discovery.database import get_db_connection


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


def get_fact_id(cur, fact):

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
        ON CONFLICT (fact_text)
        DO NOTHING
        """,
        (
            fact,
            75
        )
    )

    cur.execute(
        """
        SELECT id
        FROM facts
        WHERE fact_text = %s
        """,
        (
            fact,
        )
    )

    row = cur.fetchone()

    return row[0]


def store_fact_source(
    cur,
    fact_id,
    source_file,
    source_page
):

    cur.execute(
        """
        INSERT INTO fact_sources
        (
            fact_id,
            source_file,
            source_page,
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
            fact_id,
            source_file,
            source_page
        )
        DO NOTHING
        """,
        (
            fact_id,
            source_file,
            source_page,
            75
        )
    )


def process_pdf(pdf_path, source_file=None):

    if source_file is None:
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

    conn = get_db_connection()
    cur = conn.cursor()

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        print(
            f"Processing page {page_number}"
        )

        entities = extract_entities(
            text
        )

        facts = clean_facts(
            extract_facts(text)
        )

        for entity in entities:
            all_entities.add(entity)

        for fact in facts:

            all_facts.add(fact)

            fact_id = get_fact_id(
                cur,
                fact
            )

            store_fact_source(
                cur,
                fact_id,
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