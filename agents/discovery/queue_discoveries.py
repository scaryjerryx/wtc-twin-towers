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
        id,
        source_name,
        target,
        discovered_url
    FROM discovered_urls
    WHERE queued = FALSE
""")

rows = cur.fetchall()

for row in rows:

    discovery_id = row[0]
    source_name = row[1]
    target = row[2]
    discovered_url = row[3]

    cur.execute(
        """
        INSERT INTO discovery_queue
        (
            source_name,
            title,
            target_url
        )
        VALUES
        (%s,%s,%s)
        ON CONFLICT (target_url)
        DO NOTHING
        """,
        (
            source_name,
            target,
            discovered_url
        )
    )

    cur.execute("""
        UPDATE discovered_urls
        SET queued = TRUE
        WHERE id = %s
    """, (discovery_id,))

    print(f"Queued: {target}")

conn.commit()

cur.close()
conn.close()