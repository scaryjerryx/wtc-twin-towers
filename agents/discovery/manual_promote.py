import os
import psycopg2

from dotenv import load_dotenv

load_dotenv()

REAL_DISCOVERIES = [
    {
        "source": "Wikimedia Commons",
        "target": "World Trade Center Plaza",
        "url": "https://upload.wikimedia.org/wikipedia/commons/7/77/Delete_key1.jpg"
    }
]

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

for item in REAL_DISCOVERIES:

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
            item["source"],
            item["target"],
            item["url"]
        )
    )

    print(
        f"Added: {item['target']}"
    )

conn.commit()

cur.close()
conn.close()