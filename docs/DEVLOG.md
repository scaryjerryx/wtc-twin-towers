# Development Log

## 2026-08-09

Completed:
- M6
- M7
- M8
- M9

Major lessons:
- M6 audit discovered an M5 regression (unqualified import in `main.py`). The regression was repaired as part of M6 implementation.
- `ON CONFLICT DO UPDATE` with `RETURNING (xmax = 0) AS inserted` provides accurate per-row status without a second query.
- All-or-nothing transaction semantics are appropriate for small, fast-fail seeding workloads.
- M7: Only sources with verified search URL templates should be included in search-request generation. Inventing URL patterns for untested sources would produce non-functional search requests.
- M7: `ON CONFLICT DO NOTHING` with a separate SELECT+UPDATE for NULL correction provides more accurate per-row reporting than a single `ON CONFLICT DO UPDATE` with a CASE expression, because the RETURNING clause reflects the post-UPDATE state.
- M7: The M4 schema migration (unique constraint + `record_type` column) provided all the schema foundation needed for M7 — no additional migration was required.
- M8: `find_candidates.py` was a 15-line hollow stub with no HTTP, no parsing, no database access. Rewritten to 193 lines with full search execution, HTML parsing, and idempotent evidence_candidate insertion.
- M8: Wikimedia Commons search results use `<a href="/wiki/File:...">` links — a simple domain+path filter was sufficient for candidate extraction without complex CSS selectors.
- M8: The M4 unique constraint on `(source_name, target, search_url)` provided idempotency for free — second run produced 0 inserts, 20 already-present.
- M8: No schema changes were needed — the `record_type` column and unique constraint from M4 were sufficient.
- M8: 20 real WTC evidence candidates discovered from a single controlled search, including historical photographs, aerial views, and architectural images.
- M9: No code path existed from `search_candidates` (evidence_candidate) to `discoveries` — `manual_promote.py` wrote to legacy `discovered_urls` with hardcoded test data. Rewritten with package-safe imports, command-line ID selection, and two-layer idempotency (query filter `record_type='evidence_candidate' AND status='pending'` plus application-level SELECT-before-INSERT).
- M9: Application-level idempotency is sufficient for single-process use when a database unique constraint is not yet available. The query-level status filter provides a first line of defence; the SELECT-before-INSERT provides a second.
- M9: `export_candidates.py` and `export_discoveries.py` were also updated to use package-safe imports and read from the correct canonical tables.
- M9: No schema changes were required — the `discoveries` table and `search_candidates.status` column already existed.

## 2026-08-08

Completed:
- M0
- M1
- M2
- M3
- M4
- M5

Major lessons:
- M4 exposed a record_type omission.
- M3 revealed additional SELECT privileges may be required.
