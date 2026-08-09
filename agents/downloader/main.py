import os
import requests
import psycopg2

from dotenv import load_dotenv
from agents.downloader.r2 import upload_file

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

cur = conn.cursor()

cur.execute("""
    SELECT id, title, target_url
    FROM discovery_queue
    WHERE status = 'pending'
    LIMIT 1
""")

row = cur.fetchone()

if row:

    queue_id = row[0]
    title = row[1]
    url = row[2]

    print(f"Downloading: {title}")

    response = requests.get(url)

    os.makedirs("storage/raw", exist_ok=True)

    file_path = f"storage/raw/{queue_id}.jpg"

    with open(file_path, "wb") as file:
        file.write(response.content)

    print(f"Saved: {file_path}")

    r2_key = f"images/{queue_id}.jpg"

    upload_file(
        file_path,
        r2_key
    )

    cur.execute("""
        INSERT INTO assets
        (
            title,
            source_url,
            local_path,
            r2_key,
            asset_type
        )
        VALUES
        (
            %s,
            %s,
            %s,
            %s,
            %s
        )
    """,
    (
        title,
        url,
        file_path,
        r2_key,
        "image"
    ))

    cur.execute("""
        UPDATE discovery_queue
        SET status = 'completed'
        WHERE id = %s
    """,
    (
        queue_id,
    ))

    conn.commit()

    print("Asset stored in database")
    print("Queue item completed")

else:

    print("No pending items found")

cur.close()
conn.close()