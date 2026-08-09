import json
import os
import urllib.parse

from agents.discovery.database import get_db_connection

sources_path = os.path.join(os.path.dirname(__file__), "sources.json")
targets_path = os.path.join(
    os.path.dirname(__file__), "..", "..", "research", "targets.json"
)

with open(sources_path, "r") as file:
    sources = json.load(file)

with open(targets_path, "r") as file:
    targets = json.load(file)

SEARCH_TEMPLATES = {
    "Library of Congress": "https://www.loc.gov/search/?q={encoded}",
    "Internet Archive": "https://archive.org/search?query={encoded}",
    "Wikimedia Commons": "https://commons.wikimedia.org/w/index.php?search={encoded}",
}

conn = get_db_connection()
cur = conn.cursor()

inserted_count = 0
corrected_count = 0
already_count = 0
skipped_sources = []

try:
    for source in sources:
        source_name = source["name"]

        if source_name not in SEARCH_TEMPLATES:
            skipped_sources.append(source_name)
            continue

        template = SEARCH_TEMPLATES[source_name]

        for target in targets:
            encoded = urllib.parse.quote(target)
            search_url = template.format(encoded=encoded)

            cur.execute(
                """
                INSERT INTO search_candidates
                (source_name, target, search_url, record_type)
                VALUES (%s, %s, %s, 'search_request')
                ON CONFLICT (source_name, target, search_url)
                DO NOTHING
                RETURNING id
                """,
                (source_name, target, search_url),
            )

            row = cur.fetchone()

            if row is not None:
                inserted_count += 1
                print(f"Inserted: {source_name} -> {target}")
            else:
                cur.execute(
                    """
                    SELECT record_type
                    FROM search_candidates
                    WHERE source_name = %s
                      AND target = %s
                      AND search_url = %s
                    """,
                    (source_name, target, search_url),
                )
                existing = cur.fetchone()
                existing_record_type = existing[0]

                if existing_record_type is None:
                    cur.execute(
                        """
                        UPDATE search_candidates
                        SET record_type = 'search_request'
                        WHERE source_name = %s
                          AND target = %s
                          AND search_url = %s
                        """,
                        (source_name, target, search_url),
                    )
                    corrected_count += 1
                    print(
                        f"Corrected: {source_name} -> {target} "
                        f"(was NULL)"
                    )
                elif existing_record_type == "search_request":
                    already_count += 1
                    print(f"Already present: {source_name} -> {target}")
                else:
                    already_count += 1
                    print(
                        f"Preserved: {source_name} -> {target} "
                        f"(existing record_type = "
                        f"'{existing_record_type}')"
                    )

    conn.commit()

    for skipped in skipped_sources:
        print(f"Skipped {skipped}: no search URL template defined")

    print()
    print("Search-request generation complete.")
    print(f"  Inserted:          {inserted_count}")
    print(f"  Corrected (NULL):  {corrected_count}")
    print(f"  Already present:   {already_count}")
    print(f"  Skipped sources:   {len(skipped_sources)}")
    print(
        f"  Expected search_request row count: "
        f"{len(SEARCH_TEMPLATES) * len(targets)}"
    )

except Exception:
    conn.rollback()
    raise

finally:
    cur.close()
    conn.close()