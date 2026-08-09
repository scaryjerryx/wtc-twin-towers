from agents.discovery.database import get_db_connection
from agents.knowledge.entity_resolver import get_entity_id
from agents.knowledge.knowledge_extractor import extract_entities, extract_facts


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            id,
            asset_id,
            image_description
        FROM ai_analysis
        WHERE knowledge_processed = FALSE
        """
    )

    rows = cur.fetchall()

    for row in rows:

        analysis_id = row[0]
        asset_id = row[1]
        description = row[2]

        if description is None:

            print(
                f"Skipping analysis {analysis_id} "
                f"(no description)"
            )

            cur.execute(
                """
                UPDATE ai_analysis
                SET knowledge_processed = TRUE
                WHERE id = %s
                """,
                (analysis_id,),
            )

            continue

        entities = extract_entities(description)
        facts = extract_facts(description)

        print()
        print(f"Processing Analysis: {analysis_id}")
        print(f"Asset ID: {asset_id}")

        print("Entities:")
        print(entities)

        print("Facts:")
        print(facts)

        #
        # Store entities
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
                    "unknown",
                ),
            )

        conn.commit()

        #
        # Link facts to entities
        #
        for entity in entities:

            entity_id = get_entity_id(entity)

            if entity_id is None:
                continue

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
                        %s,
                        %s,
                        %s
                    )
                    """,
                    (
                        entity_id,
                        fact,
                        50,
                    ),
                )

                print(
                    f"Linked fact '{fact}' "
                    f"to entity '{entity}'"
                )

        cur.execute(
            """
            UPDATE ai_analysis
            SET knowledge_processed = TRUE
            WHERE id = %s
            """,
            (analysis_id,),
        )

    conn.commit()

    cur.close()
    conn.close()

    print()
    print("Knowledge Graph Build Complete")


if __name__ == "__main__":
    main()