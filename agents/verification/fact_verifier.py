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
        fact_text
    FROM facts
""")

facts = cur.fetchall()

for fact in facts:

    fact_id = fact[0]

    cur.execute(
        """
        SELECT COUNT(*)
        FROM citations
        WHERE fact_id = %s
        """,
        (fact_id,)
    )

    citation_count = cur.fetchone()[0]

    if citation_count >= 3:
        status = "verified"

    elif citation_count >= 2:
        status = "likely"

    else:
        status = "claim"

    cur.execute(
        """
        UPDATE facts
        SET verification_status = %s
        WHERE id = %s
        """,
        (
            status,
            fact_id
        )
    )

    print(
        f"Fact {fact_id}: {status}"
    )

conn.commit()

cur.close()
conn.close()

print()
print("Verification Complete")