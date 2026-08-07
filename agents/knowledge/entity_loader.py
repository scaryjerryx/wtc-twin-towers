import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def store_entity(name):

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO entities
        (
            name,
            entity_type
        )
        VALUES
        (%s,%s)
        ON CONFLICT (name)
        DO NOTHING
        """,
        (
            name,
            "unknown"
        )
    )

    conn.commit()

    cur.close()
    conn.close()