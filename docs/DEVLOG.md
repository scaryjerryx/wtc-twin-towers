# Development Log

## 2026-08-09

Completed:
- M6
- M7

Major lessons:
- M6 audit discovered an M5 regression (unqualified import in `main.py`). The regression was repaired as part of M6 implementation.
- `ON CONFLICT DO UPDATE` with `RETURNING (xmax = 0) AS inserted` provides accurate per-row status without a second query.
- All-or-nothing transaction semantics are appropriate for small, fast-fail seeding workloads.
- M7: Only sources with verified search URL templates should be included in search-request generation. Inventing URL patterns for untested sources would produce non-functional search requests.
- M7: `ON CONFLICT DO NOTHING` with a separate SELECT+UPDATE for NULL correction provides more accurate per-row reporting than a single `ON CONFLICT DO UPDATE` with a CASE expression, because the RETURNING clause reflects the post-UPDATE state.
- M7: The M4 schema migration (unique constraint + `record_type` column) provided all the schema foundation needed for M7 — no additional migration was required.

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
