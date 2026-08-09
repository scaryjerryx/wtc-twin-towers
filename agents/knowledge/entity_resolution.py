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


def seed_aliases(cur):

    inserted = 0

    for alias, canonical in DEFAULT_ALIASES:

        cur.execute(
            """
            INSERT INTO entity_aliases
            (
                alias_text,
                alias_key,
                canonical_name
            )
            VALUES
            (%s, %s, %s)
            ON CONFLICT (alias_key)
            DO NOTHING
            """,
            (
                alias,
                normalize_key(alias),
                canonical
            )
        )

        inserted += cur.rowcount

    return inserted


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


def ensure_canonical_entities(cur):

    canonical_names = set()

    for _, canonical in DEFAULT_ALIASES:
        canonical_names.add(canonical)

    for name in sorted(canonical_names):

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
                name,
                "canonical"
            )
        )


def resolve_name(cur, alias_text):

    cur.execute(
        """
        SELECT canonical_name
        FROM entity_aliases
        WHERE alias_key = %s
        """,
        (
            normalize_key(alias_text),
        )
    )

    row = cur.fetchone()

    if row:
        return row[0]

    return alias_text


def rebuild_relationships(cur):

    cur.execute(
        """
        SELECT
            id,
            source_entity,
            target_entity
        FROM relationships
        """
    )

    relationships = cur.fetchall()

    reassigned = 0

    for rel_id, source, target in relationships:

        resolved_source = resolve_name(
            cur,
            source
        )
        resolved_target = resolve_name(
            cur,
            target
        )

        if resolved_source != source or resolved_target != target:

            cur.execute(
                """
                UPDATE relationships
                SET
                    source_entity = %s,
                    target_entity = %s
                WHERE id = %s
                """,
                (
                    resolved_source,
                    resolved_target,
                    rel_id
                )
            )

            reassigned += 1

    return reassigned


def run_entity_resolution():

    from agents.discovery.database import get_db_connection

    conn = get_db_connection()
    cur = conn.cursor()

    try:

        ensure_alias_table(cur)
        conn.commit()

        ensure_canonical_entities(cur)
        conn.commit()

        inserted = seed_aliases(cur)
        conn.commit()

        reassigned = rebuild_relationships(cur)
        conn.commit()

        print()
        print("=" * 60)
        print("ENTITY RESOLUTION V2 COMPLETE")
        print("=" * 60)
        print()
        print(f"Canonical entities ensured")
        print(f"Aliases seeded: {inserted}")
        print(f"Relationships reassigned: {reassigned}")
        print()

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":

    run_entity_resolution()