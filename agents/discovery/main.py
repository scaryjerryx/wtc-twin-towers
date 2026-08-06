import json

from database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

with open("agents/discovery/sources.json", "r") as file:
    sources = json.load(file)

for source in sources:

    cur.execute(
        """
        INSERT INTO sources
        (name, url)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        """,
        (
            source["name"],
            source["url"]
        )
    )

    print(f"Stored: {source['name']}")

conn.commit()

cur.close()
conn.close()