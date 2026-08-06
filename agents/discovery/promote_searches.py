import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
    SELECT
        source_name,
        target,
        search_url
    FROM search_history
""")

rows = cur.fetchall()

for row in rows:

    source_name = row[0]
    target = row[1]
    search_url = row[2]

    cur.execute(
        """
        INSERT INTO discovered_urls
        (
            source_name,
            target,
            discovered_url
        )
        VALUES
        (%s,%s,%s)
        ON CONFLICT (discovered_url)
        DO NOTHING
        """,
        (
            source_name,
            target,
            search_url
        )
    )

    print(
        f"Discovered: {target}"
    )

conn.commit()

cur.close()
conn.close()