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
        discovered_url
    FROM discovered_urls
    ORDER BY id
""")

rows = cur.fetchall()

for row in rows:
    print(
        f"{row[0]} | "
        f"{row[1]} | "
        f"{row[2]}"
    )

cur.close()
conn.close()