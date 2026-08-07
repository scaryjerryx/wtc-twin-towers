import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def store_fact(entity_id, fact_text):

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO facts
        (
            entity_id,
            fact_text,
            confidence
        )
        VALUES
        (%s,%s,%s)
        """,
        (
            entity_id,
            fact_text,
            50
        )
    )

    conn.commit()

    cur.close()
    conn.close()