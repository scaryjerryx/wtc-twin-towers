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
    SELECT id, asset_id
    FROM metadata_queue
    WHERE status = 'pending'
    LIMIT 1
""")

item = cur.fetchone()

if item:

    queue_id = item[0]
    asset_id = item[1]

    cur.execute("""
        INSERT INTO ai_analysis
        (
            asset_id,
            tower,
            floor,
            area,
            estimated_year,
            confidence_score,
            analysis_json
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """,
    (
        asset_id,
        "Unknown",
        "Unknown",
        "Unknown",
        "Unknown",
        50,
        '{"agent":"mock"}'
    ))

    cur.execute("""
        UPDATE metadata_queue
        SET status = 'completed'
        WHERE id = %s
    """, (queue_id,))

    cur.execute("""
        UPDATE assets
        SET metadata_status = 'completed'
        WHERE id = %s
    """, (asset_id,))

    conn.commit()

    print(f"Processed Asset {asset_id}")

else:

    print("No pending metadata items")

cur.close()
conn.close()