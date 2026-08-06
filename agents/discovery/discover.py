import json
import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

with open("research/targets.json", "r") as f:
    targets = json.load(f)

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

for target in targets:

    cur.execute(
        """
        INSERT INTO discovery_queue
        (
            source_name,
            title,
            target_url
        )
        VALUES
        (%s, %s, %s)
        ON CONFLICT (target_url) DO NOTHING
        """,
        (
            "Discovery Agent",
            target,
            f"https://example.com/{target.lower().replace(' ', '-')}"
        )
    )

    print(f"Queued: {target}")

conn.commit()

cur.close()
conn.close()