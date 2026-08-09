"""M8 – Controlled Source Search.

Execute exactly one controlled source search (one approved source, one
permitted search) and store returned evidence URL candidates into
search_candidates with record_type = 'evidence_candidate'.

Does NOT write to discoveries or discovery_queue.
"""

import time
import urllib.parse

import requests
from bs4 import BeautifulSoup

from agents.discovery.database import get_db_connection

# ---------------------------------------------------------------------------
# Controlled-search configuration
# ---------------------------------------------------------------------------

# Exactly one approved source for the controlled test.
CONTROLLED_SOURCE = "Wikimedia Commons"

# Exactly one permitted target.
CONTROLLED_TARGET = "World Trade Center Plaza"

# Conservative delay between the single request and any future scaling.
REQUEST_DELAY_SECONDS = 1.0

# HTTP request timeout.
REQUEST_TIMEOUT_SECONDS = 30

# User-Agent identifying this as an automated research tool.
USER_AGENT = (
    "WTC-Evidence-Engine/1.0 "
    "(automated historical research; contact via repository)"
)

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_absolute_url(href: str, base: str = "https://commons.wikimedia.org") -> str:
    """Convert a relative or protocol-relative href to an absolute URL."""
    if href.startswith("http://") or href.startswith("https://"):
        return href
    if href.startswith("//"):
        return f"https:{href}"
    if href.startswith("/"):
        return f"{base.rstrip('/')}{href}"
    return f"{base.rstrip('/')}/{href}"


def _is_evidence_candidate_url(url: str) -> bool:
    """Return True if *url* looks like a Wikimedia Commons file page."""
    parsed = urllib.parse.urlparse(url)
    # Commons file pages live under /wiki/File: or /wiki/Special:FilePath
    if parsed.netloc not in ("commons.wikimedia.org", "upload.wikimedia.org"):
        return False
    path = parsed.path
    if path.startswith("/wiki/File:") or path.startswith("/wiki/Special:FilePath"):
        return True
    # Direct upload URLs (actual media files) are also evidence candidates.
    if path.startswith("/wikipedia/commons/") and not path.endswith("/"):
        return True
    return False


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    conn = get_db_connection()
    cur = conn.cursor()

    try:
        # ---- 1. Read exactly one search_request --------------------------------
        cur.execute(
            """
            SELECT id, source_name, target, search_url
            FROM search_candidates
            WHERE record_type = 'search_request'
              AND source_name = %s
              AND target = %s
            LIMIT 1
            """,
            (CONTROLLED_SOURCE, CONTROLLED_TARGET),
        )
        row = cur.fetchone()

        if row is None:
            print(
                f"No search_request found for "
                f"source={CONTROLLED_SOURCE!r} target={CONTROLLED_TARGET!r}"
            )
            return

        search_id, source_name, target, search_url = row
        print(f"Search request: id={search_id}")
        print(f"  Source : {source_name}")
        print(f"  Target : {target}")
        print(f"  URL    : {search_url}")

        # ---- 2. Execute exactly one HTTP request -------------------------------
        time.sleep(REQUEST_DELAY_SECONDS)

        print(f"\nFetching search results page ...")
        response = requests.get(
            search_url,
            headers={"User-Agent": USER_AGENT},
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "html" not in content_type.lower():
            print(
                f"WARNING: Unexpected Content-Type {content_type!r} — "
                f"expected HTML.  Proceeding with parse attempt."
            )

        print(f"  HTTP {response.status_code}  {len(response.text)} bytes")

        # ---- 3. Parse exactly one response page --------------------------------
        soup = BeautifulSoup(response.text, "html.parser")

        # ---- 4. Extract evidence-candidate URLs ---------------------------------
        candidate_urls: set[str] = set()

        for link in soup.find_all("a", href=True):
            href = link["href"]
            absolute = _build_absolute_url(href)
            if _is_evidence_candidate_url(absolute):
                candidate_urls.add(absolute)

        print(f"\nExtracted {len(candidate_urls)} candidate URLs.")

        # ---- 5. Insert evidence_candidate rows (idempotent) --------------------
        inserted = 0
        already = 0

        for url in sorted(candidate_urls):
            cur.execute(
                """
                INSERT INTO search_candidates
                (source_name, target, search_url, record_type)
                VALUES (%s, %s, %s, 'evidence_candidate')
                ON CONFLICT (source_name, target, search_url)
                DO NOTHING
                RETURNING id
                """,
                (source_name, target, url),
            )
            if cur.fetchone() is not None:
                inserted += 1
                print(f"  Inserted: {url}")
            else:
                already += 1
                print(f"  Already present: {url}")

        conn.commit()

        print()
        print("Controlled source search complete.")
        print(f"  Search request id : {search_id}")
        print(f"  Candidates found  : {len(candidate_urls)}")
        print(f"  Inserted          : {inserted}")
        print(f"  Already present   : {already}")
        print(f"  discoveries       : untouched")
        print(f"  discovery_queue   : untouched")

    except Exception:
        conn.rollback()
        raise

    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()