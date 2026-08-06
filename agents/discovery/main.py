import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="wtc_evidence",
    user="wtc_admin",
    password="ChangeThisToSomethingLongAndRandom"
)

cur = conn.cursor()

with open("agents/discovery/sources.json", "r") as f:
    sources = json.load(f)

for source in sources:

    cur.execute(
        """
        INSERT INTO sources (name, url)
        VALUES (%s, %s)
        ON CONFLICT DO NOTHING
        """,
        (
            source["name"],
            source["url"]
        )
    )

    print(
        f"Stored source: {source['name']}"
    )

conn.commit()
cur.close()
conn.close()