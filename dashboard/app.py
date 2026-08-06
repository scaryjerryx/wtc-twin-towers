from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        host="localhost",
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )


@app.route("/")
def index():

    conn = get_connection()
    cur = conn.cursor()

    # Total Assets
    cur.execute("""
        SELECT COUNT(*)
        FROM assets
    """)
    total_assets = cur.fetchone()[0]

    # Pending Metadata
    cur.execute("""
        SELECT COUNT(*)
        FROM assets
        WHERE metadata_status = 'pending'
    """)
    pending_metadata = cur.fetchone()[0]

    # Completed Metadata
    cur.execute("""
        SELECT COUNT(*)
        FROM assets
        WHERE metadata_status = 'completed'
    """)
    completed_metadata = cur.fetchone()[0]

    # Recent Assets
    cur.execute("""
        SELECT
            id,
            title,
            asset_type,
            r2_key
        FROM assets
        ORDER BY id DESC
        LIMIT 10
    """)
    recent_assets = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "index.html",
        total_assets=total_assets,
        pending_metadata=pending_metadata,
        completed_metadata=completed_metadata,
        recent_assets=recent_assets
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )