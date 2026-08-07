import os
import re

import psycopg2
from dotenv import load_dotenv


load_dotenv()


DEFAULT_ALIASES = [
    ("WTC", "World Trade Center"),
    ("WTC COMPLEX", "World Trade Center"),
    ("WORLD TRADE CENTER", "World Trade Center"),
    ("THE WORLD TRADE CENTER", "World Trade Center"),

    ("WTC 1", "North Tower"),
    ("WTC1", "North Tower"),
    ("WORLD TRADE CENTER 1", "North Tower"),
    ("NORTH TOWER", "North Tower"),
    ("TOWER 1", "North Tower"),

    ("WTC 2", "South Tower"),
    ("WTC2", "South Tower"),
    ("WORLD TRADE CENTER 2", "South Tower"),
    ("SOUTH TOWER", "South Tower"),
    ("TOWER 2", "South Tower"),

    ("WTC PLAZA", "Austin J Tobin Plaza"),
    ("AUSTIN J TOBIN PLAZA", "Austin J Tobin Plaza"),
    ("AUSTIN J. TOBIN PLAZA", "Austin J Tobin Plaza"),

    ("DRAWING BOOK 1", "Drawing Book 1"),
    ("EXTERIOR WALL TO EL. 363", "Exterior Wall To EL. 363"),
    ("EXTERIOR WALL TO EL.363", "Exterior Wall To EL. 363"),
    ("EXTERIOR WALL TO El. 363", "Exterior Wall To EL. 363"),
]


def normalize_key(value):

    value = value.strip()

    value = re.sub(
        r"\s+",
        " ",
        value
    )

    return value.upper()


def get_connection():

    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


def ensure_alias_table(cur):

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS entity_aliases
        (
            id SERIAL PRIMARY KEY,
            alias_text TEXT NOT NULL,
            alias_key TEXT UNIQUE NOT NULL,
            canonical_name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT NOW()
        )
        """
    )


def seed_aliases(cur):

    for alias_text, canonical_name in DEFAULT_ALIASES:

        alias_key = normalize_key(
            alias_text
        )

        cur.execute(
            """
            INSERT INTO entity_aliases
            (
                alias_text,
                alias_key,
                canonical_name
            )
            VALUES
            (
                %s,
                %s,
                %s
            )
            ON CONFLICT (alias_key)
            DO UPDATE SET
                canonical_name = EXCLUDED.canonical_name
            """,
            (
                alias_text,
                alias_key,
                canonical_name
            )
        )


def resolve_entity_name(cur, name):

    alias_key = normalize_key(
        name
    )

    cur.execute(
        """
        SELECT canonical_name
        FROM entity_aliases
        WHERE alias_key = %s
        """,
        (
            alias_key,
        )
    )

    row = cur.fetchone()

    if row:
        return row[0]

    return name.strip()


def get_or_create_entity(
    cur,
    name,
    entity_type="unknown"
):

    canonical_name = resolve_entity_name(
        cur,
        name
    )

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
            canonical_name,
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
            canonical_name,
        )
    )

    row = cur.fetchone()

    if not row:
        raise RuntimeError(
            f"Could not create or find entity: {canonical_name}"
        )

    return row[0], canonical_name


def merge_relationships_for_alias(
    cur,
    alias_entity_id,
    canonical_entity_id
):

    cur.execute(
        """
        SELECT
            id,
            source_entity_id,
            relationship_type,
            target_entity_id,
            confidence,
            evidence_count,
            source_method
        FROM relationships
        WHERE
            source_entity_id = %s
            OR target_entity_id = %s
        """,
        (
            alias_entity_id,
            alias_entity_id
        )
    )

    relationships = cur.fetchall()

    for relationship in relationships:

        relationship_id = relationship[0]
        source_entity_id = relationship[1]
        relationship_type = relationship[2]
        target_entity_id = relationship[3]
        confidence = relationship[4] or 50
        evidence_count = relationship[5] or 1
        source_method = relationship[6]

        new_source_id = source_entity_id
        new_target_id = target_entity_id

        if source_entity_id == alias_entity_id:
            new_source_id = canonical_entity_id

        if target_entity_id == alias_entity_id:
            new_target_id = canonical_entity_id

        if new_source_id != new_target_id:

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
                    confidence = GREATEST(
                        relationships.confidence,
                        EXCLUDED.confidence
                    ),
                    evidence_count = GREATEST(
                        relationships.evidence_count,
                        EXCLUDED.evidence_count
                    ),
                    source_method = COALESCE(
                        relationships.source_method,
                        EXCLUDED.source_method
                    )
                """,
                (
                    new_source_id,
                    relationship_type,
                    new_target_id,
                    confidence,
                    evidence_count,
                    source_method
                )
            )

        cur.execute(
            """
            DELETE FROM relationships
            WHERE id = %s
            """,
            (
                relationship_id,
            )
        )


def reconcile_entities(cur):

    cur.execute(
        """
        SELECT
            id,
            name,
            entity_type
        FROM entities
        ORDER BY id
        """
    )

    entities = cur.fetchall()

    merged_count = 0

    for entity_id, name, entity_type in entities:

        canonical_name = resolve_entity_name(
            cur,
            name
        )

        if canonical_name == name:
            continue

        canonical_id, _ = get_or_create_entity(
            cur,
            canonical_name,
            entity_type or "unknown"
        )

        cur.execute(
            """
            UPDATE facts
            SET entity_id = %s
            WHERE entity_id = %s
            """,
            (
                canonical_id,
                entity_id
            )
        )

        merge_relationships_for_alias(
            cur,
            entity_id,
            canonical_id
        )

        cur.execute(
            """
            DELETE FROM entities
            WHERE id = %s
            """,
            (
                entity_id,
            )
        )

        merged_count += 1

        print(
            f"Merged entity '{name}' into '{canonical_name}'"
        )

    return merged_count


def main():

    conn = get_connection()
    cur = conn.cursor()

    ensure_alias_table(
        cur
    )

    seed_aliases(
        cur
    )

    merged_count = reconcile_entities(
        cur
    )

    conn.commit()

    print()
    print("=" * 60)
    print("ENTITY RESOLUTION COMPLETE")
    print("=" * 60)
    print()
    print(
        f"Aliases Seeded: {len(DEFAULT_ALIASES)}"
    )
    print(
        f"Entities Merged: {merged_count}"
    )
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    main()
