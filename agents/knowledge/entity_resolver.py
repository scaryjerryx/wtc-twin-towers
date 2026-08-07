import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()


def get_entity_id(entity_name):

    conn = psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    cur = conn.cursor()

    cur.execute(
        """
        SELECT id
        FROM entities
        WHERE name = %s
        """,
        (entity_name,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return row[0]

    return None