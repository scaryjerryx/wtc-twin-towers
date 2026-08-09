# Development Log

## 2026-08-09

Completed:
- M6

Major lessons:
- M6 audit discovered an M5 regression (unqualified import in `main.py`). The regression was repaired as part of M6 implementation.
- `ON CONFLICT DO UPDATE` with `RETURNING (xmax = 0) AS inserted` provides accurate per-row status without a second query.
- All-or-nothing transaction semantics are appropriate for small, fast-fail seeding workloads.

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
