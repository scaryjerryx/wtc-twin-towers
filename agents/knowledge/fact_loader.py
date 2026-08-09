from agents.discovery.database import get_db_connection


def store_fact(entity_id, fact_text):

    conn = get_db_connection()
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