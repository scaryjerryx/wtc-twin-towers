import re

from agents.discovery.database import get_db_connection


def extract_year_from_fact(fact_text):
    """Extract a 4-digit year from a 'Referenced year' fact.

    Returns the year as an integer, or None if not a year fact.
    """

    if not fact_text.startswith(
        "Referenced year"
    ):
        return None

    match = re.search(
        r"\b(19\d{2}|20\d{2})\b",
        fact_text
    )

    if not match:
        return None

    year = int(
        match.group(1)
    )

    if 1800 <= year <= 2100:
        return year

    return None


def resolve_entity_for_fact(cur, fact_id):
    """Look up the entity_id linked to this fact."""

    cur.execute(
        "SELECT entity_id FROM facts WHERE id = %s",
        (fact_id,),
    )

    row = cur.fetchone()

    if row and row[0]:
        return row[0]

    return None


def resolve_asset_for_fact(cur, fact_id):
    """Look up the asset_id from fact_sources for this fact."""

    cur.execute(
        """
        SELECT asset_id
        FROM fact_sources
        WHERE fact_id = %s
          AND asset_id IS NOT NULL
        ORDER BY id
        LIMIT 1
        """,
        (fact_id,),
    )

    row = cur.fetchone()

    if row and row[0]:
        return row[0]

    return None


def build_timeline():
    """Build persistent timeline events from facts.

    Reads facts with 'Referenced year' pattern, extracts the year,
    resolves entity and asset provenance, and inserts into the
    timeline_events table idempotently.

    The timeline_events table must already exist (created by migration
    database/migrations/005_create_timeline_events.sql).
    """

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT
            f.id,
            f.fact_text,
            f.confidence,
            f.verification_status
        FROM facts f
        WHERE f.fact_text LIKE 'Referenced year%%'
        ORDER BY f.id
        """
    )

    rows = cur.fetchall()

    created_count = 0

    for row in rows:

        fact_id = row[0]
        fact_text = row[1]
        fact_confidence = row[2]
        verification_status = row[3]

        year = extract_year_from_fact(
            fact_text
        )

        if year is None:
            continue

        entity_id = resolve_entity_for_fact(
            cur,
            fact_id,
        )

        asset_id = resolve_asset_for_fact(
            cur,
            fact_id,
        )

        # Determine confidence from verification status
        confidence = fact_confidence

        cur.execute(
            """
            INSERT INTO timeline_events
            (
                event_year,
                event_type,
                description,
                date_text,
                fact_id,
                entity_id,
                asset_id,
                confidence
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
            ON CONFLICT
            (
                fact_id,
                event_year,
                event_type
            )
            DO NOTHING
            """,
            (
                year,
                "reference",
                fact_text,
                str(year),
                fact_id,
                entity_id,
                asset_id,
                confidence,
            ),
        )

        if cur.rowcount > 0:
            created_count += 1

    conn.commit()

    # Summary
    cur.execute(
        "SELECT COUNT(*) FROM timeline_events"
    )

    total_events = cur.fetchone()[0]

    print()
    print("=" * 60)
    print("TIMELINE BUILDER COMPLETE")
    print("=" * 60)
    print()
    print(f"Events Created: {created_count}")
    print(f"Total Events:   {total_events}")
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    build_timeline()