import os
import re
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
        e.name,
        f.fact_text,
        f.verification_status
    FROM facts f
    JOIN entities e
        ON f.entity_id = e.id
""")

rows = cur.fetchall()

timeline_events = []

for row in rows:

    entity_name = row[0]
    fact_text = row[1]
    verification = row[2]

    years = re.findall(
        r"(19\d{2}|20\d{2})",
        fact_text
    )

    for year in years:

        timeline_events.append(
            (
                int(year),
                entity_name,
                fact_text,
                verification
            )
        )

timeline_events.sort(
    key=lambda x: x[0]
)

print()
print("=" * 60)
print("WORLD TRADE CENTER TIMELINE")
print("=" * 60)

for event in timeline_events:

    print()
    print(f"Year         : {event[0]}")
    print(f"Entity       : {event[1]}")
    print(f"Fact         : {event[2]}")
    print(f"Verification : {event[3]}")

cur.close()
conn.close()