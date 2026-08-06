import json
import urllib.parse
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

    encoded = urllib.parse.quote(target)

    searches = [
        (
            "Library of Congress",
            target,
            f"https://www.loc.gov/search/?q={encoded}"
        ),
        (
            "Internet Archive",
            target,
            f"https://archive.org/search?query={encoded}"
        ),
        (
            "Wikimedia Commons",
            target,
            f"https://commons.wikimedia.org/w/index.php?search={encoded}"
        )
    ]

    for source_name, target_name, search_url in searches:

        cur.execute(
            """
            INSERT INTO search_candidates
            (
                source_name,
                target,
                search_url
            )
            VALUES
            (%s,%s,%s)
            """,
            (
                source_name,
                target_name,
                search_url
            )
        )

        print(
            f"Stored: {source_name} -> {target_name}"
        )

conn.commit()

cur.close()
conn.close()