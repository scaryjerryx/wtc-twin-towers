from collections import Counter

from agents.discovery.database import get_db_connection


def get_or_create_entity(cur, name, entity_type="fact"):
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
            entity_type
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

    if not row:
        raise RuntimeError(
            f"Could not find or create entity: {name}"
        )

    return row[0]


def calculate_confidence(evidence_count):
    return min(
        50 + (evidence_count * 5),
        100
    )


def upsert_relationship(
    cur,
    source_name,
    relationship_type,
    target_name,
    evidence_count,
    source_method
):
    source_id = get_or_create_entity(
        cur,
        source_name
    )

    target_id = get_or_create_entity(
        cur,
        target_name
    )

    confidence = calculate_confidence(
        evidence_count
    )

    cur.execute(
        """
        INSERT INTO relationships
        (
            source_entity_id,
            relationship_type,
            target_entity_id,
            confidence,
            evidence_count,
            source_method
        )
        VALUES
        (
            %s,
            %s,
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
        DO UPDATE SET
            confidence = EXCLUDED.confidence,
            evidence_count = EXCLUDED.evidence_count,
            source_method = EXCLUDED.source_method
        """,
        (
            source_id,
            relationship_type,
            target_id,
            confidence,
            evidence_count,
            source_method
        )
    )


def should_skip_fact(fact):
    if fact.startswith("Referenced year"):
        return True

    return False


def load_page_facts(cur):
    cur.execute(
        """
        SELECT
            fs.source_file,
            fs.source_page,
            f.fact_text
        FROM fact_sources fs
        JOIN facts f
            ON fs.fact_id = f.id
        WHERE fs.source_page IS NOT NULL
        ORDER BY
            fs.source_file,
            fs.source_page,
            f.fact_text
        """
    )

    rows = cur.fetchall()

    page_facts = {}

    for source_file, source_page, fact_text in rows:
        key = (
            source_file,
            source_page
        )

        if key not in page_facts:
            page_facts[key] = []

        page_facts[key].append(
            fact_text
        )

    return page_facts


def mine_relationships(page_facts):
    relationship_counter = Counter()

    for page_key, facts in page_facts.items():
        clean_facts = [
            fact
            for fact in facts
            if not should_skip_fact(fact)
        ]

        drawing_books = [
            fact
            for fact in clean_facts
            if fact.startswith("Drawing Book")
        ]

        exterior_walls = [
            fact
            for fact in clean_facts
            if fact.startswith("Exterior Wall")
        ]

        for drawing_book in drawing_books:
            for fact in clean_facts:
                if fact == drawing_book:
                    continue

                relationship_counter[
                    (
                        fact,
                        "appears_in",
                        drawing_book
                    )
                ] += 1

        for exterior_wall in exterior_walls:
            for fact in clean_facts:
                if fact == exterior_wall:
                    continue

                relationship_counter[
                    (
                        fact,
                        "associated_with",
                        exterior_wall
                    )
                ] += 1

    return relationship_counter


def build_relationships():
    conn = get_db_connection()
    cur = conn.cursor()

    page_facts = load_page_facts(
        cur
    )

    relationship_counter = mine_relationships(
        page_facts
    )

    for relationship, evidence_count in relationship_counter.items():
        source_name = relationship[0]
        relationship_type = relationship[1]
        target_name = relationship[2]

        upsert_relationship(
            cur,
            source_name,
            relationship_type,
            target_name,
            evidence_count,
            "page_cooccurrence"
        )

    conn.commit()

    print()
    print("=" * 60)
    print("FACT RELATIONSHIP BUILD COMPLETE")
    print("=" * 60)
    print()
    print(f"Pages Processed: {len(page_facts)}")
    print(f"Relationships Found: {len(relationship_counter)}")
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":
    build_relationships()