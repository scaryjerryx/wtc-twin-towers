from flask import Flask, render_template
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)


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

    cur.execute("SELECT COUNT(*) FROM assets")
    total_assets = cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*)
        FROM assets
        WHERE metadata_status = 'pending'
    """)
    pending_metadata = cur.fetchone()[0]

    cur.execute("""
        SELECT COUNT(*)
        FROM assets
        WHERE metadata_status = 'completed'
    """)
    completed_metadata = cur.fetchone()[0]

    cur.execute("""
        SELECT id, title, asset_type, r2_key
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


@app.route("/assets")
def assets():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            title,
            asset_type,
            metadata_status,
            r2_key,
            source_url
        FROM assets
        ORDER BY id DESC
    """)

    assets = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "assets.html",
        assets=assets
    )


@app.route("/analysis")
def analysis():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            id,
            asset_id,
            tower,
            floor,
            area,
            estimated_year,
            confidence_score
        FROM ai_analysis
        ORDER BY id DESC
    """)

    analysis_records = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "analysis.html",
        analysis_records=analysis_records
    )


@app.route("/queues")
def queues():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM discovery_queue
        ORDER BY id DESC
    """)
    discovery_queue = cur.fetchall()

    cur.execute("""
        SELECT *
        FROM metadata_queue
        ORDER BY id DESC
    """)
    metadata_queue = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "queues.html",
        discovery_queue=discovery_queue,
        metadata_queue=metadata_queue
    )


@app.route("/sources")
def sources():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT *
        FROM sources
        ORDER BY id ASC
    """)

    sources = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "sources.html",
        sources=sources
    )


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )