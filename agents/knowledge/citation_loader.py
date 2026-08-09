import os
import psycopg2

from dotenv import load_dotenv


load_dotenv()


def get_connection():

    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


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


def load_citations():

    conn = get_connection()
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
            confidence
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

        cur.execute(
            """
            INSERT INTO citations
            (
                fact_id,
                source_file,
                source_page,
                confidence,
                citation_type
            )
            VALUES
            (
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
                "fact_source"
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
