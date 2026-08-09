import re

from agents.discovery.database import get_db_connection


def extract_year_from_fact(fact_text):

    if not fact_text.startswith(
        "Referenced year"
    ):
        return None

    match = re.search(
        r"\b(19\d{2}|20\d{2})\b",
        fact_text
    )

    if not match:
        return None

    year = int(
        match.group(1)
    )

    if 1800 <= year <= 2100:
        return year

    return None


def load_timeline_events(cur):

    cur.execute(
        """
        SELECT
            f.id,
            f.fact_text,
            f.confidence,
            f.verification_status,
            fs.source_file,
            fs.source_page,
            fs.confidence AS source_confidence
        FROM facts f
        LEFT JOIN fact_sources fs
            ON f.id = fs.fact_id
        ORDER BY
            f.id,
            fs.source_page
        """
    )

    rows = cur.fetchall()

    events = []

    for row in rows:

        fact_id = row[0]
        fact_text = row[1]
        fact_confidence = row[2]
        verification_status = row[3]
        source_file = row[4]
        source_page = row[5]
        source_confidence = row[6]

        year = extract_year_from_fact(
            fact_text
        )

        if year is None:
            continue

        events.append(
            {
                "year": year,
                "fact_id": fact_id,
                "fact_text": fact_text,
                "fact_confidence": fact_confidence,
                "verification_status": verification_status,
                "source_file": source_file,
                "source_page": source_page,
                "source_confidence": source_confidence
            }
        )

    return sorted(
        events,
        key=lambda event: (
            event["year"],
            event["fact_text"],
            event["fact_id"]
        )
    )


def print_timeline(events):

    print()
    print("=" * 60)
    print("WTC KNOWLEDGE TIMELINE")
    print("=" * 60)
    print()

    if not events:

        print("No timeline events found.")
        print()
        return

    current_year = None

    for event in events:

        year = event["year"]

        if year != current_year:

            current_year = year

            print()
            print("-" * 60)
            print(f"YEAR: {year}")
            print("-" * 60)

        print()
        print(f"Fact ID             : {event['fact_id']}")
        print(f"Fact                : {event['fact_text']}")
        print(f"Fact Confidence     : {event['fact_confidence']}")
        print(f"Verification Status : {event['verification_status']}")

        if event["source_file"]:

            print(f"Source File         : {event['source_file']}")

        if event["source_page"]:

            print(f"Source Page         : {event['source_page']}")

        if event["source_confidence"]:

            print(f"Source Confidence   : {event['source_confidence']}")

    print()
    print("=" * 60)
    print(f"Timeline Events: {len(events)}")
    print("=" * 60)
    print()


def build_timeline():

    conn = get_db_connection()
    cur = conn.cursor()

    events = load_timeline_events(
        cur
    )

    print_timeline(
        events
    )

    cur.close()
    conn.close()


if __name__ == "__main__":

    build_timeline()