# Minimal Acquisition Repair Plan

## World Trade Center Evidence Engine

**Date:** August 8, 2026

**Status:** Approved planning artifact — advisory only; nothing implemented.

---

## A. Approved Architecture Decisions

1. **Canonical discovery record.** `discoveries` is the canonical discovery record for all new rows. `discovered_urls` (41 rows) and `search_history` (40 rows) are preserved as legacy data, read-only, excluded from the new operational path. **No unique constraint is added to `search_history`**; its schema is not modified unless a later migration requires it.

2. **Queue-state derivation.** No `discoveries.queued` field exists or will be invented. A discovery is "queued" if and only if a `discovery_queue` row references it.

3. **Discovery-to-queue relationship.** Add a **nullable `discovery_id` FK** on `discovery_queue → discoveries(id)`. Prefer this stable identifier over joining only by `target_url`. Legacy queue rows remain valid during transition: `discovery_id` stays NULL for them, and joins fall back to `target_url` only for legacy rows. Legacy rows are not rewritten in this milestone.

4. **`asset_sources` semantics.** One `asset_sources` row = **one retrieval event** containing `asset_id`, `source_id`, `original_url`, `normalised_url`, `final_effective_url`, `retrieved_at`, `created_at`. Do not expect two rows merely because `original_url` and `final_effective_url` differ. A second row represents a separate retrieval event or a separately discovered source reference. The exact idempotency key is an **open approval decision** (candidate: `asset_id + source_id + normalised_url + retrieved_at`, or similar) to preserve repeated retrieval of a changing URL.

5. **URL/file identity.** SHA-256 is authoritative file identity (`assets.file_hash`, unique). Preserve all three URL forms plus `retrieved_at` in `asset_sources`.

6. **Queue lifecycle.** `pending → in_progress → completed`, branches to `retry_scheduled` (with `next_retry`), `failed_permanent`, `quarantined`. Stale-claim recovery reclaims `in_progress` claims older than a threshold. Timeout and retry limits require approval.

7. **Storage boundary.** PostgreSQL is authoritative provenance storage. R2 object metadata stays small and technical (content-type, sha256, r2 key, content length); no evidence-descriptive metadata in R2 tags.

8. **Writer role timing and privileges.** The writer role is created **before `asset_sources` exists**, granting privileges only on existing approved tables initially. After `asset_sources` is created, its privileges are added via a separately reviewed grant. Include USAGE and SELECT on the specific sequences needed for serial inserts. Do not grant: DELETE, DDL, schema ownership, table ownership, superuser, or unrestricted privileges.

9. **Legacy asset handling.** The 3 assets sharing `source_url` are **not quarantined** — without hashes, URL equality does not prove file equality. They are preserved and flagged for legacy review. Only records confirmed to contain fabricated `example.com` URLs are quarantined (11 queue rows and the 1 fabricated asset row), by setting a quarantine state, never deleting.

10. **Discovery stages.** Define separately: **source search request** (a generated query URL), **returned evidence URL candidate** (a URL returned by the search), **human-reviewed candidate**, and **promoted discovery**. A search request is not the same thing as a returned evidence URL. Approval needed on whether `search_candidates` can represent both using an explicit record-type field (e.g., `record_type` = 'search_request' | 'evidence_candidate'), or whether another existing structure should hold returned candidates. **No new table invented in this revision.**

11. **`run_pipeline.py`.** Not changed until the independent acquisition path passes its controlled end-to-end test.

---

## B. Milestone 1 Open Items (required)

Milestone 1 (Architecture decisions) must resolve:

1. Whether `search_candidates` gains a `record_type` column (e.g., 'search_request' | 'evidence_candidate') or uses another representation for search requests versus returned evidence URL candidates. A search request is not the same thing as a returned evidence URL. If the current schema cannot represent the distinction cleanly, this is an architecture decision requiring approval; no new table is invented without approval.

2. The exact `asset_sources` retrieval-event idempotency key. Candidate: `(asset_id, source_id, normalised_url, retrieved_at)` or similar. The key must preserve repeated retrieval of a changing URL as separate retrieval events.

---

## C. Final Corrected Milestone Order

Each milestone has one primary concern and includes: objective, files affected, schema/data changes, exact test, expected result, rollback/recovery, dependencies, required DB role.

### M0 – Pre-flight backup (no code)

- **Objective:** Ensure recoverability before any change.
- **Files affected:** None (backups external to repository).
- **Schema/data changes:** Full logical backup of `wtc_evidence`.
- **Exact test:** Restore the backup into a scratch database; compare table row counts and essential schema objects.
- **Expected result:** Row counts and essential schema objects match.
- **Rollback/recovery:** Restore from backup.
- **Dependencies:** None.
- **Role:** Administrator.

### M1 – Architecture decisions (no code)

- **Objective:** Record the approved decisions in section A; resolve the two Milestone 1 open items (record_type representation; asset_sources idempotency key).
- **Files affected:** `docs/NEXT_TASK.md`, `docs/ARCHITECTURE.md`, `docs/SESSION_LOG.md`.
- **Schema/data changes:** None.
- **Exact test:** Documentation review for consistency.
- **Expected result:** Decisions recorded and approved.
- **Rollback/recovery:** Revert documentation commit.
- **Dependencies:** M0.
- **Role:** Administrator.

### M2 – Source-registry reconciliation (no schema)

- **Objective:** Reconcile `agents/discovery/sources.json` (7) and `research/sources.json` (4) against `docs/SOURCE_REGISTRY.md`; add status/rights/rate-limit/review fields. No fixed source count is asserted until done.
- **Files affected:** `agents/discovery/sources.json`, `research/sources.json`, `docs/SOURCE_REGISTRY.md`.
- **Schema/data changes:** None.
- **Exact test:** Load both configs and diff keys against the registry.
- **Expected result:** One canonical source list, no name/national-archive mismatches.
- **Rollback/recovery:** Revert config commit.
- **Dependencies:** M1.
- **Role:** None (files only).

### M3 – Limited writer role (manual)

- **Objective:** Create least-privilege writer role; privileges only on existing approved tables; USAGE + SELECT on needed sequences; no DELETE / DDL / ownership / superuser.
- **Files affected:** SQL migration artifacts only.
- **Schema/data changes:** Role + grants.
- **Exact test:** Connect as the role; attempt DDL and DELETE (must fail) and a permitted insert (must succeed).
- **Expected result:** Role cannot DDL or DELETE; permitted writes succeed.
- **Rollback/recovery:** `DROP ROLE` (no data loss).
- **Dependencies:** M0.
- **Role:** Administrator.

### M4 – First small schema migration (manual)

- **Objective:** Add only discovery-side structures required by the new operational path: `discovery_queue.discovery_id` (nullable FK → discoveries), `attempt_count`, `last_error`, `next_retry`, new status values, index on `discovery_queue(status)`, and a unique constraint on `search_candidates` (only if required by the new path). **Do not add a unique constraint to `search_history`.**
- **Files affected:** SQL migration artifact.
- **Schema/data changes:** As listed; forward-only, idempotent.
- **Exact test:** Rerun migration (no-op); verify via `information_schema`; confirm `search_history` unchanged.
- **Expected result:** New columns/constraints/index present; `search_history` and legacy rows unchanged.
- **Rollback/recovery:** Forward-fix only; no destructive rollback of populated columns.
- **Dependencies:** M0, M1.
- **Role:** Administrator.

### M5 – Package/import repair

- **Objective:** Make `agents/discovery/` package-safe (`from agents.discovery.database import get_db_connection` in `main.py`); do not touch `run_pipeline.py`.
- **Files affected:** `agents/discovery/main.py`.
- **Schema/data changes:** None.
- **Exact test:** `python -m agents.discovery.main` dry-run; `python -m py_compile`.
- **Expected result:** Package invocation succeeds.
- **Rollback/recovery:** Revert commit.
- **Dependencies:** M2.
- **Role:** None (code only).

### M6 – Source seeding repair

- **Objective:** Idempotent seeding of `sources` from the reconciled config.
- **Files affected:** `agents/discovery/main.py`.
- **Schema/data changes:** Upserts into `sources` (ON CONFLICT name).
- **Exact test:** Run twice; row count unchanged.
- **Expected result:** `sources` matches reconciled config with no duplicates.
- **Rollback/recovery:** Revert commit; no destructive deletes.
- **Dependencies:** M2, M5.
- **Role:** Writer (INSERT `sources`).

### M7 – Search-request generation

- **Objective:** Generate source search requests into `search_candidates` (record_type = 'search_request', per M1 decision) from the reconciled config, idempotently.
- **Files affected:** Replacement for `build_real_searches.py` (legacy scripts excluded from operational path).
- **Schema/data changes:** INSERT into `search_candidates` (unique constraint from M4).
- **Exact test:** Run twice; no duplicate search requests.
- **Expected result:** Search-request set stable across runs.
- **Rollback/recovery:** Revert commit; dedup via unique constraint.
- **Dependencies:** M4, M6.
- **Role:** Writer.

### M8 – Controlled source search

- **Objective:** Execute exactly one controlled source search (one approved source, one permitted search) and store returned evidence URL candidates.
- **Files affected:** `agents/discovery/find_candidates.py` (candidates only).
- **Schema/data changes:** INSERT into `search_candidates` only (record_type = 'evidence_candidate', per M1 decision).
- **Exact test:** Run against the one approved source/search; verify candidates written and no discovery or queue writes.
- **Expected result:** Returned evidence URL candidates stored; `discoveries` and `discovery_queue` untouched.
- **Rollback/recovery:** Revert commit; preserve the test candidates and mark for review rather than deleting.
- **Dependencies:** M7 and the M1 record-type decision.
- **Role:** Writer.

### M9 – Human review and manual promotion

- **Objective:** Human reviews candidates; manual promotion writes approved rows into canonical `discoveries`.
- **Files affected:** `agents/discovery/manual_promote.py` (rewritten to write `discoveries`, not `discovered_urls`).
- **Schema/data changes:** INSERT into `discoveries`.
- **Exact test:** Promote one approved candidate; verify a single `discoveries` row with source/provenance.
- **Expected result:** Canonical discovery created; no auto-promotion.
- **Rollback/recovery:** Revert commit; preserve the test discovery and mark for review rather than deleting.
- **Dependencies:** M4, M8.
- **Role:** Writer.

### M10 – Discovery queue

- **Objective:** Queue approved discoveries into `discovery_queue` with `discovery_id` set; fix the `queue_discoveries.py` silent-loss path (wrap in transaction; never mark queued when insert is skipped).
- **Files affected:** `agents/discovery/queue_discoveries.py`.
- **Schema/data changes:** INSERT into `discovery_queue`; no UPDATE of `discoveries.queued` (field does not exist).
- **Exact test:** Run twice; single queue row per discovery; crash-mid-run leaves no queued-but-not-inserted state.
- **Expected result:** Queue rows reference `discovery_id`; repeated runs safe.
- **Rollback/recovery:** Revert commit; preserve test queue rows and mark for review.
- **Dependencies:** M4, M9.
- **Role:** Writer.

### M11 – Downloader schema additions (manual)

- **Objective:** Add `assets.file_hash` (unique), `assets.content_type`, and create `asset_sources` (fields per A4). No duplicate ordinary index on `file_hash` — the reviewed unique index is the only index on that column.
- **Files affected:** SQL migration artifact.
- **Schema/data changes:** `assets` columns; create `asset_sources`; unique index on `assets.file_hash`.
- **Exact test:** Rerun migration (no-op); verify `asset_sources` columns and `file_hash` unique index.
- **Expected result:** Schema supports hashing and retrieval-event provenance.
- **Rollback/recovery:** Forward-fix only.
- **Dependencies:** M0, M1.
- **Role:** Administrator.

### M12 – `asset_sources` registration + privilege grant

- **Objective:** Implement `asset_sources` registration (one row per retrieval event); add its privileges to the writer role via a separately reviewed grant.
- **Files affected:** Registration code; SQL grant artifact.
- **Schema/data changes:** INSERT into `asset_sources`; separate grant on `asset_sources` and its sequence.
- **Exact test:** Register one asset with one retrieval event; verify a single `asset_sources` row with all three URL forms and `retrieved_at`. Run twice → a second row (new retrieval event) only if a new retrieval occurred.
- **Expected result:** One row per retrieval event; writer role gains only `asset_sources` privileges.
- **Rollback/recovery:** Revert commit; preserve test rows and mark for review.
- **Dependencies:** M11, M10.
- **Role:** Writer (after separate grant).

### M13 – R2 testability, then downloader implementation

- **Objective:** First replace `test_r2.py` with a mocked unit test (R2 testability), then implement downloader hardening.
- **Files affected:** `agents/downloader/test_r2.py`, `agents/downloader/r2.py`, `agents/downloader/main.py`.
- **Schema/data changes:** INSERT `assets`, `asset_sources`, `metadata_queue`.
- **Exact test:** Mocked R2 test; download of one permitted file; verify hash, dedup, asset record, metadata handoff.
- **Expected result:** One asset, one R2 object, one metadata_queue row; repeated download deduplicated by hash.
- **Rollback/recovery:** Revert commit; preserve test records and mark for review.
- **Dependencies:** **M10 (discovery queue), M11 (downloader schema), M12 (asset_sources), M3 (writer-role permissions), and R2 testability work.** Must not begin without M10.
- **Role:** Writer.

### M14 – Controlled end-to-end test

- **Objective:** One approved source, one permitted search, one manually approved evidence URL, one permitted file; verify full lifecycle and provenance.
- **Files affected:** None (test run).
- **Schema/data changes:** One search request, one evidence candidate, one discovery, one queue row, one asset, one asset_sources row, one metadata_queue row.
- **Exact test:** Run the full independent path; rerun; verify no duplicates (URL + hash) and queue transitions.
- **Expected result:** End-to-end success, idempotent, provenance complete.
- **Rollback/recovery:** Do not delete test records as routine rollback. Use a clearly labelled controlled test run; after review, preserve and quarantine or mark test records. Only an explicitly approved administrator operation may delete them.
- **Dependencies:** M8–M13.
- **Role:** Writer.

### M15 – Orchestrator repair (only after M14 passes)

- **Objective:** Fix `run_pipeline.py` invocation mode (package-qualified) and wire the now-operational acquisition path.
- **Files affected:** `agents/run_pipeline.py`.
- **Schema/data changes:** None.
- **Exact test:** Run `python -m agents.run_pipeline`; verify discovery → queue → downloader → metadata chain.
- **Expected result:** Orchestrator runs the independent path without import errors.
- **Rollback/recovery:** Revert commit.
- **Dependencies:** M14 (must pass first).
- **Role:** Writer.

---

## D. Risks and Unknowns

- **`asset_sources` idempotency key** is an open decision; a wrong choice either loses repeated-retrieval history or allows unintended duplicates.
- **Search-request vs returned-evidence-candidate representation** is unresolved; if `search_candidates` cannot cleanly hold both via a record-type field, another existing structure is needed (no new table without approval).
- **Legacy rows** remain unverified without hashes; only confirmed fabricated example.com rows are quarantined.
- **Stale-claim recovery thresholds and retry limits** are unvalidated; a mis-set threshold risks duplicate downloads or abandoned claims.
- **`metadata_queue` / `ai_analysis` idempotency** is unresolved; multiple rows per asset already exist and may be legitimate.
- **Run-time DDL in `citation_loader.py`** is a latent schema-governance risk outside acquisition scope.
- **Unknown writers/readers** of `extracted_text`, `metadata`, `verification`, `reconstruction_tasks` could interact with later milestones.
- **No automated tests exist** for discovery/downloader; M14 is the first real validation.
- **Source reconciliation** depends on `SOURCE_REGISTRY.md` authority; mismatches require human resolution.

---

## E. Confirmation of Non-Operation

Nothing was changed. No files were read, created, edited, or deleted beyond this planning artifact; no commands or tools were run; no PostgreSQL was queried; no migrations, quarantines, grants, or R2 operations were performed. This is an advisory plan only.