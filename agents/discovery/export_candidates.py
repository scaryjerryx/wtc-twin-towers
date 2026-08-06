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
    FROM search_candidates
    ORDER BY id
""")

rows = cur.fetchall()

for row in rows:

    print()
    print(f"Source : {row[0]}")
    print(f"Target : {row[1]}")
    print(f"URL    : {row[2]}")

cur.close()
conn.close()