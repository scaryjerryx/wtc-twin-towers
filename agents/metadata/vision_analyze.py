import os
import psycopg2

from dotenv import load_dotenv
from r2_download import download_file

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

queue_item = cur.fetchone()

if not queue_item:

    print("No pending metadata items")

    cur.close()
    conn.close()
    exit()

queue_id = queue_item[0]
asset_id = queue_item[1]

cur.execute("""
    SELECT
        id,
        title,
        r2_key,
        source_url
    FROM assets
    WHERE id = %s
""", (asset_id,))

asset = cur.fetchone()

if not asset:

    print("Asset not found")

    cur.close()
    conn.close()
    exit()

r2_key = asset[2]

local_file = f"tmp/asset_{asset_id}.jpg"

download_file(
    r2_key,
    local_file
)

description = (
    "Image retrieved successfully and awaiting AI vision analysis."
)

tags = (
    "retrieved,pending-analysis"
)

cur.execute("""
    INSERT INTO ai_analysis
    (
        asset_id,
        tower,
        floor,
        area,
        estimated_year,
        confidence_score,
        image_description,
        tags,
        analysis_version,
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
    0,
    description,
    tags,
    "v1",
    '{"agent":"vision_analyze"}'
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

print()
print("Analysis Complete")
print("-----------------")
print(f"Queue ID   : {queue_id}")
print(f"Asset ID   : {asset_id}")
print(f"Title      : {asset[1]}")
print(f"Local File : {local_file}")

cur.close()
conn.close()