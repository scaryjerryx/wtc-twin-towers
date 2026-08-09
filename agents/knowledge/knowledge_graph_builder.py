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
        source_file = (
            f"acquisition_asset_{asset_id}"
            if asset_id
            else f"ai_analysis_{analysis_id}"
        )

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

                cur.execute(
                    """
                    SELECT id
                    FROM facts
                    WHERE fact_text = %s
                    """,
                    (
                        fact,
                    ),
                )

                fact_row = cur.fetchone()

                if fact_row is None:
                    continue

                fact_id = fact_row[0]

                cur.execute(
                    """
                    INSERT INTO fact_sources
                    (
                        fact_id,
                        source_file,
                        source_page,
                        confidence,
                        asset_id
                    )
                    VALUES
                    (
                        %s,
                        %s,
                        NULL,
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
                        50,
                        asset_id,
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