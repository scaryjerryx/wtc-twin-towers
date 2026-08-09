import json
import os

from agents.discovery.database import get_db_connection

conn = get_db_connection()
cur = conn.cursor()

sources_path = os.path.join(os.path.dirname(__file__), "sources.json")

with open(sources_path, "r") as file:
    sources = json.load(file)

try:
    for source in sources:
        cur.execute(
            """
            INSERT INTO sources
            (name, url)
            VALUES (%s, %s)
            ON CONFLICT (name) DO UPDATE SET url = EXCLUDED.url
            RETURNING (xmax = 0) AS inserted
            """,
            (
                source["name"],
                source["url"],
            ),
        )

        row = cur.fetchone()
        if row and row[0]:
            print(f"Inserted: {source['name']}")
        else:
            print(f"Already present: {source['name']}")

    conn.commit()
    print("Source seeding complete.")

except Exception:
    conn.rollback()
    raise

finally:
    cur.close()
    conn.close()