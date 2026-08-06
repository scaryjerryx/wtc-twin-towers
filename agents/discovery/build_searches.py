import json
import os
import urllib.parse
import psycopg2

from dotenv import load_dotenv

load_dotenv()

with open("research/targets.json", "r") as f:
    targets = json.load(f)

with open("research/sources.json", "r") as f:
    sources = json.load(f)

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

for source in sources:

    for target in targets:

        search_url = (
            f"{source['url']}?search="
            f"{urllib.parse.quote(target)}"
        )

        cur.execute(
            """
            INSERT INTO search_history
            (
                source_name,
                target,
                search_url
            )
            VALUES
            (%s,%s,%s)
            """,
            (
                source["name"],
                target,
                search_url
            )
        )

        print(
            f"Stored {source['name']} -> {target}"
        )

conn.commit()

cur.close()
conn.close()