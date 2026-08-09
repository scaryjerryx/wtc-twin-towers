# Database Schema Read-Only Audit

## World Trade Center Evidence Engine

**Date:** August 8, 2026

**Status:** Read-only audit — the database inspection changed no files, database records, or schemas. This audit report is the only file created afterward.

**Scope:** PostgreSQL `wtc_evidence` — discovery, downloader, asset, queue, and knowledge tables

**Method:** Read-only `information_schema`/`pg_catalog` queries via `psql` using credentials from `.secrets/cline-db.env`. Credentials were never displayed, printed, copied, or included in output.

---

## 1. Executive Summary

The `wtc_evidence` database contains **19 tables**, **0 views**, **19 sequences**, **28 indexes**, and **33 `pg_constraint` records** (19 PRIMARY KEY + 8 UNIQUE + 6 FOREIGN KEY + 0 CHECK).

The discovery and downloader pipeline is **not operational end to end**. The schema confirms the Phase 1 repository audit findings:

- The documented `discoveries` table exists but is **completely unused** (0 rows, no code references).
- The operative discovery tables are `search_history` and `discovered_urls`, which are absent from the documented flow.
- `discovery_queue` contains **11 fabricated `https://example.com/...` URLs** inserted by `agents/discovery/discover.py`.
- `assets` contains **3 duplicate `source_url` rows** (same Wikimedia image) and **1 fabricated `example.com` row**.
- `metadata_queue` is **never populated by any code** — the downloader handoff is missing.
- `assets` has **no `file_hash` or `content_type` columns** — file-hash deduplication is impossible without a schema change, and the downloader cannot persist the validated HTTP Content-Type value in the asset record (validation of the HTTP Content-Type header itself is a code behaviour, not blocked by the schema).
- `discovery_queue` has **no failure/retry columns** — failure handling is impossible without schema changes.
- `search_candidates` and `search_history` lack confirmed uniqueness needed by their current writers;
- `metadata_queue` and `ai_analysis` allow multiple rows per asset;
- the correct idempotency keys for metadata and analysis remain an architecture decision.

---

## 2. Audit Scope and Method

### Queries Performed (all read-only)

1. Table inventory: `information_schema.tables` (all non-system schemas)
2. Column inventory: `information_schema.columns` (all 130 columns across 19 tables)
3. Constraint inventory: `pg_constraint` (33 records)
4. Index inventory: `pg_indexes` (28 records)
5. Sequence inventory: `pg_class` + `pg_sequence` + `pg_depend` (19 sequences)
6. Row counts: `COUNT(*)` for all 19 tables
7. Status-value distribution: `GROUP BY` on all status/flag columns
8. Orphaned-reference check: `LEFT JOIN` on all 6 foreign keys (0 orphans)
9. Duplicate-record check: `GROUP BY ... HAVING COUNT(*) > 1` on all expected-uniqueness columns

### Non-Operations Confirmed

- The database inspection created or modified no files.
- No PostgreSQL database was modified.
- No migrations were run.
- No evidence was downloaded.
- Nothing was uploaded to R2.
- No packages were installed.
- Nothing was committed.

---

## 3. Database Object Inventory

### 3.1 Tables (19, all `public` schema, all BASE TABLE)

| Table | Row Count |
|---|---|
| `ai_analysis` | 8 |
| `assets` | 4 |
| `citations` | 55 |
| `discovered_urls` | 41 |
| `discoveries` | **0** |
| `discovery_queue` | 52 |
| `entities` | 17 |
| `entity_aliases` | 20 |
| `extracted_text` | 0 |
| `fact_sources` | 55 |
| `facts` | 18 |
| `metadata` | 0 |
| `metadata_queue` | 6 |
| `reconstruction_tasks` | 0 |
| `relationships` | 16 |
| `search_candidates` | 30 |
| `search_history` | 40 |
| `sources` | 4 |
| `verification` | 0 |

### 3.2 Views

**None exist.**

### 3.3 Sequences (19)

One sequence per table, all `integer`, start 1, increment 1, no cycle, each owned by its table's `id` column:

`ai_analysis_id_seq`, `assets_id_seq`, `citations_id_seq`, `discovered_urls_id_seq`, `discoveries_id_seq`, `discovery_queue_id_seq`, `entities_id_seq`, `entity_aliases_id_seq`, `extracted_text_id_seq`, `fact_sources_id_seq`, `facts_id_seq`, `metadata_id_seq`, `metadata_queue_id_seq`, `reconstruction_tasks_id_seq`, `relationships_id_seq`, `search_candidates_id_seq`, `search_history_id_seq`, `sources_id_seq`, `verification_id_seq`

### 3.4 Constraints (33 total in `pg_constraint`)

**Primary keys (19):** all tables have `id` PRIMARY KEY.

**UNIQUE constraints (8):**

| Table | Constraint | Columns |
|---|---|---|
| `sources` | `unique_source_name` | `(name)` |
| `discovered_urls` | `discovered_urls_discovered_url_key` | `(discovered_url)` |
| `discovery_queue` | `unique_target_url` | `(target_url)` |
| `entities` | `entities_name_key` | `(name)` |
| `entity_aliases` | `entity_aliases_alias_key_key` | `(alias_key)` |
| `facts` | `unique_fact` | `(fact_text)` |
| `fact_sources` | `unique_fact_source` | `(fact_id, source_file, source_page)` |
| `relationships` | `unique_relationship` | `(source_entity_id, relationship_type, target_entity_id)` |

**Foreign keys (6):**

| Constraint | From | To |
|---|---|---|
| `ai_analysis_asset_id_fkey` | `ai_analysis(asset_id)` | `assets(id)` |
| `assets_source_id_fkey` | `assets(source_id)` | `sources(id)` |
| `fact_sources_fact_id_fkey` | `fact_sources(fact_id)` | `facts(id)` |
| `metadata_asset_id_fkey` | `metadata(asset_id)` | `assets(id)` |
| `metadata_queue_asset_id_fkey` | `metadata_queue(asset_id)` | `assets(id)` |
| `verification_asset_id_fkey` | `verification(asset_id)` | `assets(id)` |

**Check constraints (0):** none exist.

### 3.5 Indexes (28 total in `pg_indexes`)

- **19 PRIMARY KEY indexes** (one per table)
- **8 constraint-backed unique indexes** (backing the 8 UNIQUE constraints above)
- **1 standalone unique index (not a UNIQUE constraint):**
  - `unique_citation_fact_source_page` on `citations(fact_id, source_file, source_page, citation_type)`

**Important:** Citation uniqueness is implemented as a **standalone unique index only**. PostgreSQL does not report a corresponding UNIQUE constraint in `pg_constraint` for `citations`. This is consistent with `agents/knowledge/citation_loader.py`, which issues `CREATE UNIQUE INDEX IF NOT EXISTS unique_citation_fact_source_page`.

**No additional non-constraint indexes exist.** There is no index on `discovery_queue(status)`, `metadata_queue(status)`, `assets(metadata_status)`, `ai_analysis(knowledge_processed)`, or any FK column.

### 3.6 Orphaned References

#### Enforced foreign-key checks

**0 orphans** across all 6 foreign-key constraints (verified by LEFT JOIN):

- `ai_analysis.asset_id` → `assets(id)`: 0
- `assets.source_id` → `sources(id)`: 0
- `fact_sources.fact_id` → `facts(id)`: 0
- `metadata.asset_id` → `assets(id)`: 0
- `metadata_queue.asset_id` → `assets(id)`: 0
- `verification.asset_id` → `assets(id)`: 0

#### Additional logical-reference checks (not enforced FKs)

The following relationships are **not** enforced by foreign-key constraints in the live schema. They were checked logically via LEFT JOIN and all returned 0 orphans, but they are **not foreign keys**:

- `citations.asset_id` — no FK constraint (0 orphans)
- `citations.fact_id` — no FK constraint (despite `citation_loader.py`'s CREATE TABLE code declaring one; the live schema has none) (0 orphans)
- `extracted_text.asset_id` — no FK constraint (0 orphans)
- `facts.entity_id` — no FK constraint (0 orphans)
- `relationships.source_entity_id` — no FK constraint (0 orphans)
- `relationships.target_entity_id` — no FK constraint (0 orphans)

### 3.7 Duplicate Records Relevant to Expected Uniqueness

| Check | Duplicate Groups | Duplicate Rows |
|---|---|---|
| `sources.name` | 0 | 0 |
| `search_candidates.search_url` | 0 | 0 |
| `search_candidates(source_name, target, search_url)` | 0 | 0 |
| `search_history.search_url` | 0 | 0 |
| `discovered_urls.discovered_url` | 0 | 0 |
| `discoveries.discovered_url` | 0 | 0 |
| `discovery_queue.target_url` | 0 | 0 |
| `assets.file_url` | 1 | 4 (all NULL — grouping artifact, not a real duplicate) |
| `assets.source_url` | **1** | **3** (assets 1–3 share `https://upload.wikimedia.org/wikipedia/commons/7/77/Delete_key1.jpg`) |
| `assets.r2_key` | 0 | 0 |
| `metadata_queue.asset_id` | **1** | **4** (all reference asset 4) |
| `ai_analysis.asset_id` | **2** | **7** (3 rows for asset 1, 4 rows for asset 4) |

### 3.8 Existing Status Values

| Table | Field | Values (count) |
|---|---|---|
| `sources` | `active` | `true` (4) |
| `search_candidates` | `status` | `pending` (30) |
| `discovered_urls` | `status` | `pending` (41) |
| `discovered_urls` | `queued` | `true` (41) |
| `discoveries` | `status` | (0 rows) |
| `discovery_queue` | `status` | `completed` (2), `pending` (50) |
| `assets` | `status` | `discovered` (4) |
| `assets` | `download_status` | `downloaded` (4) |
| `assets` | `metadata_status` | `completed` (3), `pending` (1) |
| `assets` | `verification_status` | `pending` (4) |
| `assets` | `processed` | `false` (4) |
| `metadata_queue` | `status` | `completed` (6) |
| `ai_analysis` | `knowledge_processed` | `true` (8) |

---

## 4. Code Readers / Writers per Table

| Table | Writers | Readers |
|---|---|---|
| `sources` | `agents/discovery/main.py` (INSERT, ON CONFLICT DO NOTHING) | `dashboard/app.py` |
| `search_history` | `agents/discovery/build_searches.py` (plain INSERT) | `agents/discovery/promote_searches.py` |
| `search_candidates` | `agents/discovery/build_real_searches.py` (plain INSERT) | `agents/discovery/export_candidates.py` |
| `discovered_urls` | `promote_searches.py`, `manual_promote.py` (INSERT, ON CONFLICT); `queue_discoveries.py` (UPDATE queued) | `queue_discoveries.py`, `export_discoveries.py` |
| `discoveries` | **None** | **None** |
| `discovery_queue` | `discover.py` (INSERT fake URLs); `queue_discoveries.py` (INSERT); `downloader/main.py` (UPDATE status) | `downloader/main.py`, `dashboard/app.py` |
| `assets` | `downloader/main.py` (INSERT); `metadata/mock_analyze.py` + `vision_analyze.py` (UPDATE metadata_status) | `metadata/main.py`, `vision_analyze.py`, `dashboard/app.py` |
| `metadata_queue` | **No INSERT in any code** (6 rows are manual) | `metadata/main.py`, `mock_analyze.py`, `vision_analyze.py` (all UPDATE status) |
| `ai_analysis` | `mock_analyze.py`, `vision_analyze.py` (INSERT); `knowledge_graph_builder.py` (UPDATE knowledge_processed) | `knowledge_graph_builder.py`, `dashboard/app.py` |
| `metadata` | **none** | **none** |
| `verification` | **none** | **none** |
| `reconstruction_tasks` | **none** | **none** |
| `extracted_text` | UNKNOWN (no code reference found) | UNKNOWN |
| `entities` | `knowledge_graph_builder.py`, `pdf_knowledge_pipeline.py`, `knowledge_pipeline.py`, `entity_loader.py`, `entity_resolution.py`, `relationship_builder.py`, `fact_relationship_builder.py` | `entity_resolver.py`, `entity_resolution.py`, `relationship_builder.py`, `fact_relationship_builder.py`, `graph_search.py`, `relationship_search.py`, `health_report.py` |
| `entity_aliases` | `entity_resolution.py` (seed, ON CONFLICT DO UPDATE) | `entity_resolution.py` |
| `facts` | `knowledge_graph_builder.py`, `pdf_knowledge_pipeline.py`, `knowledge_pipeline.py`, `fact_loader.py` (INSERT); `fact_verifier.py` (UPDATE status/confidence); `entity_resolution.py` (UPDATE entity_id) | `query_engine.py`, `graph_search.py`, `relationship_search.py`, `fact_verifier.py`, `timeline_builder.py`, `fact_relationship_builder.py`, `health_report.py` |
| `fact_sources` | `pdf_knowledge_pipeline.py` (INSERT, ON CONFLICT) | `citation_loader.py`, `fact_relationship_builder.py`, `relationship_search.py`, `fact_verifier.py`, `timeline_builder.py`, `health_report.py` |
| `citations` | `citation_loader.py` (INSERT, ON CONFLICT; **also runs CREATE TABLE/ALTER/CREATE INDEX DDL**) | `health_report.py` |
| `relationships` | `relationship_builder.py` (plain INSERT); `fact_relationship_builder.py` (ON CONFLICT DO UPDATE); `entity_resolution.py` (INSERT + DELETE) | `graph_search.py`, `relationship_search.py`, `health_report.py`, `entity_resolution.py` |

---

## 5. Answers to the Eleven Schema Questions

### Q1 — Does a `discoveries` table exist?

**Yes.** Columns: `id` (PK), `source_name` (text, nullable), `target` (text, nullable), `discovered_url` (text, nullable), `status` (text, default `'pending'`), `created_at` (timestamp, default now()). **0 rows. No code reads or writes it.** No unique constraint, no FK. Structurally identical to `discovered_urls` minus the `queued` column.

### Q2 — Are `discovered_urls` and `search_history` real tables?

Yes, both exist and are the **operative** tables in current code. `discovered_urls` (41 rows) has a unique constraint on `discovered_url` and a `queued` boolean. `search_history` (40 rows) has **no unique constraint**. Both are absent from the documented flow (`sources → search_candidates → discoveries → discovery_queue`). They are either legacy leftovers or the de-facto discovery tables — **decision requires approval**.

### Q3 — Source uniqueness?

Yes — `sources` has `UNIQUE (name)` (`unique_source_name`). **No unique constraint on `url`** (url is nullable). The `ON CONFLICT DO NOTHING` in `discovery/main.py` is therefore safe for name-based dedup.

### Q4 — Candidate uniqueness?

**No.** `search_candidates` has **no unique constraint** on `(source_name, target, search_url)` or `search_url` — only PK on `id`. `build_real_searches.py` (plain INSERT) is **non-idempotent**; repeated runs would create duplicates. Current 30 rows have no duplicates only because it ran once.

### Q5 — Discovery-queue uniqueness and statuses?

`discovery_queue` has `UNIQUE (target_url)` (`unique_target_url`). Observed statuses: `'pending'` (50), `'completed'` (2). **No `failed`/`retry` statuses exist.** **No `attempt_count`, `last_error`, or `next_retry` columns exist.** The schema supports only pending→completed; no failure/retry infrastructure.

### Q6 — `assets` schema?

Columns: `id` (PK), `source_id` (int, nullable, FK→sources), `title`, `asset_type`, `file_url`, `discovered_at` (default now), `status` (default `'discovered'`), `processed` (bool, default false), `local_path`, `source_url`, `r2_key`, `download_status` (default `'downloaded'`), `metadata_status` (default `'pending'`), `verification_status` (default `'pending'`).

**Critical gaps:** **No `file_hash` column** (file-hash dedup impossible). **No `content_type` column.** **No unique constraint** on `source_url`, `r2_key`, or `file_url`. All 4 current rows have `source_id = NULL`. Observed statuses: `status='discovered'` (4), `download_status='downloaded'` (4), `metadata_status='completed'` (3)/`'pending'` (1), `verification_status='pending'` (4), `processed=false` (4).

### Q7 — `metadata_queue` schema?

Columns: `id` (PK), `asset_id` (int, nullable, FK → assets), `status` (default `'pending'`), `created_at` (default now). **No unique constraint on `asset_id`** — 4 rows reference asset 4. Observed status: `'completed'` (6). **No code inserts into this table** — the downloader never enqueues; the 6 rows were created manually. This is the missing handoff confirmed at schema level.

### Q8 — `ai_analysis` schema?

Columns: `id` (PK), `asset_id` (int, nullable, FK → assets), `tower`, `floor`, `area`, `estimated_year` (all text, nullable), `confidence_score` (int, nullable), `analysis_json` (jsonb, nullable), `created_at` (default now), `image_description`, `tags`, `analysis_version`, `asset_type_detected`, `asset_type_confidence` (int), `knowledge_processed` (bool, default false). All columns the mock/vision inserts exist and are nullable. **No unique constraint on `asset_id`** — 3 rows for asset 1, 4 rows for asset 4.

### Q9 — Source governance fields?

`sources` has: `id`, `name` (NOT NULL), `url`, `reliability_score` (default 50), `created_at`, `active` (bool, default true), `notes`. **No `status`, `approved`, `rate_limit`, `rights`, or `last_reviewed` columns.** Governance data must remain in `SOURCE_REGISTRY.md` unless a schema migration is approved.

### Q10 — `discoveries` vs `discovered_urls` resolution?

`discoveries` exists but is **completely unused** (0 rows, no code). `discovered_urls` is the operative table (41 rows, unique constraint, `queued` flag). The documented flow `candidates → discoveries → discovery_queue` **cannot be implemented as documented** without either (a) writing to the existing empty `discoveries` table, or (b) formally adopting `discovered_urls` as the discovery record. **This is a schema/architecture decision requiring approval.**

### Q11 — Foreign keys?

The queue/asset tables are **denormalised with text `source_name` columns** as the code implies. FKs that exist (6): `assets.source_id → sources(id)` (nullable, never set by code), `ai_analysis.asset_id → assets(id)`, `metadata.asset_id → assets(id)`, `metadata_queue.asset_id → assets(id)`, `verification.asset_id → assets(id)`, `fact_sources.fact_id → facts(id)`. **No FK** from `discovery_queue`, `discoveries`, `discovered_urls`, `search_candidates`, or `search_history` to `sources` or `discoveries`. **No FK** on `citations.fact_id` or `citations.asset_id` (despite `citation_loader.py`'s CREATE TABLE code declaring `fact_id REFERENCES facts(id)` — the live schema has no such FK).

---

## 6. Schema ↔ Code ↔ Documentation Mismatches

1. **`discoveries` documented but never written** — 0 rows, no code references.
2. **`search_history` + `discovered_urls` used by code but absent from documented flow.**
3. **`discovery_queue` contains 11 fabricated `https://example.com/...` URLs** (from `discover.py`) — evidence-safety violation confirmed in live data.
4. **`assets` has 3 duplicate `source_url` rows** (same Wikimedia image) and 1 fabricated `example.com` row — no dedup guard.
5. **`metadata_queue` never populated by code** — downloader handoff missing; 6 rows are manual.
6. **`assets` lacks `file_hash` and `content_type`** — file-hash deduplication is impossible without a schema change, and the validated HTTP Content-Type cannot be persisted on the asset record (HTTP Content-Type validation itself is a code behaviour in the downloader and is not blocked by the schema). Adding `assets.file_hash` and `assets.content_type` to store the validated values remains a recommended schema addition.
7. **`discovery_queue` lacks failure/retry columns** — Milestone 5 failure handling impossible without schema change.
8. **`sources` lacks governance columns** — Q9.
9. **`search_candidates` and `search_history` lack unique constraints** — non-idempotent writers.
10. **`metadata_queue` and `ai_analysis` lack a uniqueness guarantee on `asset_id`** — multiple rows already exist per asset. Whether `asset_id` should be unique in these tables is an **architecture decision requiring clarification**: repeated processing attempts, retries, analysis versions, or historical analyses may be legitimate. A future idempotency constraint, if adopted, may need to include `asset_id` plus status or job type, `asset_id` plus analysis version, or an explicit idempotency key.
11. **`citation_loader.py` performs DDL (`CREATE TABLE IF NOT EXISTS`, `ALTER TABLE`, `CREATE UNIQUE INDEX`) at runtime** — code mutates schema, violating the read-only/audit principle and the documented "no migrations during audit" rule.
12. **`assets` FK `source_id → sources(id)` exists but is never populated** — all 4 rows have NULL `source_id`; provenance is only in text `source_url`.
13. **`route_asset.py` and `vision_analyze.py` use unqualified imports** (`from processors...`, `from r2_download...`) — not package-safe (Phase 1 finding confirmed).
14. **`extracted_text`, `metadata`, `verification`, `reconstruction_tasks` tables exist with 0 rows and no code references** — UNKNOWN purpose/writers; possibly speculative or planned.

---

## 7. Idempotency Assessment (per table)

| Table | Idempotent? | Basis |
|---|---|---|
| `sources` | ✅ Yes | `ON CONFLICT DO NOTHING` + `unique_source_name` |
| `search_history` | ❌ No | plain INSERT, no unique constraint |
| `search_candidates` | ❌ No | plain INSERT, no unique constraint |
| `discovered_urls` | ✅ Yes | `ON CONFLICT (discovered_url)` + unique constraint |
| `discoveries` | N/A | no code writes |
| `discovery_queue` | ⚠️ Partial | INSERT idempotent (unique target_url), but `queue_discoveries.py` marks `queued=TRUE` even when insert skipped — silent data-loss path |
| `assets` | ❌ No | plain INSERT, no unique constraint on source_url/r2_key |
| `metadata_queue` | N/A | no code writes |
| `ai_analysis` | ❌ No | plain INSERT, no unique constraint — duplicates already present |
| `entities` | ✅ Yes | `ON CONFLICT (name) DO NOTHING` |
| `entity_aliases` | ✅ Yes | `ON CONFLICT (alias_key) DO UPDATE` |
| `facts` | ⚠️ Partial | `pdf_knowledge_pipeline` uses `ON CONFLICT (fact_text)`; `knowledge_graph_builder` + `fact_loader` use plain INSERT |
| `fact_sources` | ✅ Yes | `ON CONFLICT (fact_id, source_file, source_page)` |
| `citations` | ✅ Yes | `ON CONFLICT (fact_id, source_file, source_page, citation_type)` against the standalone unique index |
| `relationships` | ⚠️ Partial | `fact_relationship_builder` uses `ON CONFLICT DO UPDATE`; `relationship_builder.py` uses plain INSERT |

---

## 8. UNKNOWN Items (not confirmed)

- **Writers/readers of `extracted_text`, `metadata`, `verification`, `reconstruction_tasks`** — no code references found; may be written by `pdf_processor.py`/`photo_processor.py`/`video_processor.py` which were not read during this audit.
- **How the 6 `metadata_queue` rows were created** — no INSERT in code; assumed manual.
- **How the 4 `assets` rows were created** — consistent with `downloader/main.py` INSERT pattern, but not confirmed by execution.
- **Whether `discoveries` is intended as the canonical table** — schema exists, documentation says yes, code says no.

---

## 9. Confirmed Schema Facts vs Conclusions vs Recommendations

### Confirmed Schema Facts (live schema)

All 19 tables, columns, data types, nullability, defaults, primary keys, foreign keys, unique constraints, indexes, sequences, row counts, status values, orphan counts, and duplicate counts as documented in Sections 3–5 above.

### Evidence-Based Conclusions

1. The documented `candidates → discoveries → discovery_queue` flow is not implemented; code uses `search_history → discovered_urls → discovery_queue`.
2. The schema cannot support file-hash dedup, retry/failure handling, or governance fields without migration, and cannot persist a validated content type without adding an `assets.content_type` column (validating the HTTP Content-Type header in the downloader code is not blocked by the schema).
3. `discoveries`, `metadata`, `verification`, `reconstruction_tasks`, `extracted_text` are empty and unused.
4. Live data contains fabricated URLs and duplicate asset/analysis records.
5. Citation uniqueness is enforced by a standalone unique index, not a UNIQUE constraint.

### Recommendations Requiring Approval (no action taken)

1. Decide canonical discovery table: write to existing `discoveries` OR adopt `discovered_urls` (Q10).
2. Add unique constraints for idempotent search generation: `search_candidates(source_name, target, search_url)` and `search_history(source_name, target, search_url)`. For `metadata_queue` and `ai_analysis`, **do not assume a unique constraint on `asset_id` is correct** — repeated processing attempts, retries, analysis versions, or historical analyses may be legitimate. Treat any uniqueness on these tables as an **architecture decision requiring clarification**; a future idempotency constraint may need to include `asset_id` plus status or job type, `asset_id` plus analysis version, or an explicit idempotency key. Do not invent the final constraint yet.
3. Add `assets.file_hash` (unique) and `assets.content_type` columns.
4. Add `discovery_queue.attempt_count`, `last_error`, `next_retry` columns.
5. Add `sources.status/approved/rate_limit/rights/last_reviewed` columns (or keep governance in `SOURCE_REGISTRY.md`).
6. Remove/repair `discover.py` fabricated-URL path and `queue_discoveries.py` silent-loss path.
7. Remove runtime DDL from `citation_loader.py` (move to explicit migration).
8. Populate `assets.source_id` FK from `sources` on registration.

---

## 10. Confirmation of Non-Operations

This audit was performed in read-only mode. The database inspection itself created or modified **no files**. The following were **not** performed:

- No PostgreSQL database was accessed for modification.
- No database records or schemas were changed.
- No migrations were run.
- No evidence was downloaded.
- Nothing was uploaded to R2.
- No packages were installed.
- No source code was edited.
- No documentation other than this audit report was modified.
- Nothing was committed.

The **only artifact created** as a result of the audit is this Markdown report: `docs/audits/DATABASE_SCHEMA_AUDIT_2026-08-08.md`.
