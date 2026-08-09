from agents.discovery.database import get_db_connection


def get_entity_id(entity_name):

    conn = get_db_connection()
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