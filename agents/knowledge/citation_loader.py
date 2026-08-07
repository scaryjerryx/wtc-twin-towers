import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def create_citation(fact_id, asset_id):

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO citations
        (
            fact_id,
            asset_id
        )
        VALUES
        (%s, %s)
        """,
        (
            fact_id,
            asset_id
        )
    )

    conn.commit()

    cur.close()
    conn.close()