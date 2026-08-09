from agents.discovery.database import get_db_connection


def store_entity(name):

    conn = get_db_connection()
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