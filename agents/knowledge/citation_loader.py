from agents.discovery.database import get_db_connection


def ensure_citations_table(cur):

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS citations
        (
            id SERIAL PRIMARY KEY,
            fact_id INTEGER REFERENCES facts(id),
            source_file TEXT,
            source_page INTEGER,
            confidence INTEGER,
            citation_type TEXT DEFAULT 'fact_source',
            created_at TIMESTAMP DEFAULT NOW()
        )
        """
    )

    cur.execute(
        """
        ALTER TABLE citations
        ADD COLUMN IF NOT EXISTS source_file TEXT
        """
    )

    cur.execute(
        """
        ALTER TABLE citations
        ADD COLUMN IF NOT EXISTS source_page INTEGER
        """
    )

    cur.execute(
        """
        ALTER TABLE citations
        ADD COLUMN IF NOT EXISTS confidence INTEGER
        """
    )

    cur.execute(
        """
        ALTER TABLE citations
        ADD COLUMN IF NOT EXISTS citation_type TEXT DEFAULT 'fact_source'
        """
    )

    cur.execute(
        """
        ALTER TABLE citations
        ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT NOW()
        """
    )

    cur.execute(
        """
        CREATE UNIQUE INDEX IF NOT EXISTS unique_citation_fact_source_page
        ON citations
        (
            fact_id,
            source_file,
            source_page,
            citation_type
        )
        """
    )


def _resolve_acquisition_provenance(cur, source_file, asset_id):
    """Resolve provenance FKs from fact_sources asset_id or source_file pattern.

    Returns (asset_id, asset_source_id) or (None, None) for non-acquisition files.
    """

    # If asset_id is already known from fact_sources, use it directly
    if asset_id is not None:
        cur.execute(
            "SELECT id FROM asset_sources WHERE asset_id = %s "
            "ORDER BY retrieved_at DESC LIMIT 1",
            (asset_id,),
        )
        row = cur.fetchone()
        asset_source_id = row[0] if row else None
        return asset_id, asset_source_id

    # Fallback: parse source_file for acquisition_asset_{id} pattern
    import re
    match = re.match(r"^acquisition_asset_(\d+)(?:_ocr)?$", source_file)
    if match is None:
        return None, None

    asset_id = int(match.group(1))

    cur.execute(
        "SELECT id FROM asset_sources WHERE asset_id = %s "
        "ORDER BY retrieved_at DESC LIMIT 1",
        (asset_id,),
    )
    row = cur.fetchone()
    asset_source_id = row[0] if row else None

    return asset_id, asset_source_id


def load_citations():

    conn = get_db_connection()
    cur = conn.cursor()

    ensure_citations_table(
        cur
    )

    cur.execute(
        """
        SELECT
            fact_id,
            source_file,
            source_page,
            confidence,
            asset_id
        FROM fact_sources
        ORDER BY
            fact_id,
            source_file,
            source_page
        """
    )

    fact_sources = cur.fetchall()

    inserted_count = 0

    for row in fact_sources:

        fact_id = row[0]
        source_file = row[1]
        source_page = row[2]
        confidence = row[3]
        fs_asset_id = row[4]

        # Resolve provenance using fact_sources.asset_id when available
        asset_id, asset_source_id = _resolve_acquisition_provenance(
            cur,
            source_file,
            fs_asset_id,
        )

        cur.execute(
            """
            INSERT INTO citations
            (
                fact_id,
                source_file,
                source_page,
                confidence,
                citation_type,
                asset_id,
                asset_source_id
            )
            VALUES
            (
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
                source_file,
                source_page,
                citation_type
            )
            DO NOTHING
            """,
            (
                fact_id,
                source_file,
                source_page,
                confidence,
                "fact_source",
                asset_id,
                asset_source_id,
            )
        )

        inserted_count += cur.rowcount

    conn.commit()

    print()
    print("=" * 60)
    print("CITATION LOADER COMPLETE")
    print("=" * 60)
    print()
    print(
        f"Fact Sources Read: {len(fact_sources)}"
    )
    print(
        f"Citations Inserted: {inserted_count}"
    )
    print()

    cur.close()
    conn.close()


if __name__ == "__main__":

    load_citations()