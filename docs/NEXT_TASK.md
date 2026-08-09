# Next Task

## Reconnect Existing Automated Evidence Gathering

### Status

🔄 **In Progress**

## Milestone Progress

- ✅ **M0 – Pre-flight backup** — Complete and passed. Production database backed up, restored into a scratch database, row counts and schema object counts matched, scratch database cleaned up.
- ✅ **M1 – Architecture decisions** — Complete and approved. Decisions recorded below.
- ✅ **M2 – Source-registry reconciliation** — Complete.
- ✅ **M3 – Limited writer role** — Complete. Role `wtc_writer` created with least-privilege grants on approved tables and sequences. Catalog verification passed. Runtime verification revealed additional SELECT privileges may be required for some operational queries; this will be addressed in a later milestone if necessary.
- ✅ **M4 – First small schema migration** — Complete.
- ✅ **M5 – Package/import repair** — Complete. An M5 regression (unqualified import in `main.py`) was discovered during the M6 audit and repaired as part of M6 implementation.
- ✅ **M6 – Source seeding repair** — Complete. Source seeding is now idempotent with URL upsert support, accurate per-row status reporting, module-relative path resolution, and all-or-nothing transaction safety.
- ✅ **M7 – Search-request generation** — Complete. Search requests generated for 3 sources with verified search URL templates into `search_candidates` with `record_type = 'search_request'`. Idempotent via `ON CONFLICT DO NOTHING` backed by the M4 unique constraint. Legacy NULL `record_type` rows corrected. 4 sources deferred pending verified search URL templates. Package-safe execution verified.
- ✅ **M8 – Controlled source search** — Complete. One controlled source search executed (Wikimedia Commons, "World Trade Center Plaza"). 20 evidence URL candidates extracted and stored in `search_candidates` with `record_type = 'evidence_candidate'`. Idempotent via `ON CONFLICT DO NOTHING` backed by the M4 unique constraint. `discoveries` and `discovery_queue` confirmed untouched. Package-safe execution verified.
- ✅ **M9 – Human review and manual promotion** — Complete. `manual_promote.py` rewritten to read `evidence_candidate` rows from `search_candidates` and promote approved candidates into the canonical `discoveries` table with status `'approved'`. Package-safe imports, transaction safety, command-line ID selection, and application-level idempotency (query filters to `record_type='evidence_candidate' AND status='pending'` plus SELECT-before-INSERT). `export_candidates.py` updated with `--type` filtering. `export_discoveries.py` updated to read from `discoveries`. Two candidates promoted and verified. No schema changes.
- ✅ **M10 – Discovery queue** — Complete. `queue_discoveries.py` rewritten to read from canonical `discoveries` table and INSERT into `discovery_queue` with `discovery_id` FK populated. Idempotent via LEFT JOIN on `discovery_id` plus `ON CONFLICT(target_url) DO NOTHING`. Silent-loss bug eliminated (unconditional UPDATE replaced by RETURNING clause). Package-safe imports, transaction safety. Two discoveries queued; discovery-to-queue linkage verified. No schema changes. 54 legacy queue rows preserved untouched.
- ✅ **M11 – Downloader schema additions** — Complete. `assets.file_hash` (text, unique index) and `assets.content_type` (text) columns added idempotently. `asset_sources` table created with 8 columns (`id`, `asset_id`, `source_id`, `original_url`, `normalised_url`, `final_effective_url`, `retrieved_at`, `created_at`) plus FK constraints to `assets` and `sources`. All DDL idempotent via `IF NOT EXISTS`; rerun confirmed no-op. Legacy rows preserved (4 assets, file_hash/content_type NULL). No duplicate ordinary index on `file_hash`. Migration file: `database/migrations/001_add_downloader_schema.sql`.
- ✅ **M12 – `asset_sources` registration + privilege grant** — Complete. `agents/downloader/register_asset.py` created with idempotent registration via unique constraint on `(asset_id, COALESCE(source_id, -1), original_url)`. Unique index migration (`database/migrations/002_add_asset_sources_unique.sql`) applied. Writer role granted INSERT on `asset_sources` and USAGE/SELECT on `asset_sources_id_seq`. Registration tested: first call inserts, repeated call is a no-op, different URL creates new retrieval event.
- ✅ **M13 – R2 testability, then downloader implementation** — Complete. `agents/downloader/main.py` rewritten with package-safe imports, lease/claim queue pattern, SHA-256 hashing, content-type detection, hash-based deduplication (reuses existing asset, skips redundant R2 upload and metadata_queue, still registers asset_sources), failure handling (`failed_permanent` + `last_error`). `test_r2.py` replaced with mocked unit test. Two Wikimedia Commons files downloaded (assets 5, 6) with full provenance.
- ✅ **M14 – Controlled end-to-end test** — Complete. Full independent acquisition path exercised: candidate 123 → discovery 3 → queue 76 → asset 7 → asset_sources 7 → metadata_queue 9. All URL links verified MATCH. Idempotency confirmed across all three stages.
- ✅ **M15 – Orchestrator repair** — Complete. `agents/run_pipeline.py` rewritten with `sys.executable -m` package-safe invocation. `agents/metadata/mock_analyze.py` repaired with package-safe imports. Full orchestrator execution verified across all 6 automated stages.
- ✅ **M16 – Knowledge platform import repair** — Complete. All 20 files across `agents/knowledge/`, `agents/timeline/`, `agents/verification/`, `agents/metadata/`, `agents/search/`, `agents/engine/`, and `agents/router/` now use the shared `get_db_connection()`. Zero remaining `psycopg2.connect()` calls in repaired directories. Engine and health report verified running without import errors.
- ✅ **M17 – Acquisition → Knowledge Pipeline Integration** — Complete. `agents/ingestion/process_acquisition_assets.py` created to query acquisition PDF assets, download from R2, and process through the PDF knowledge pipeline with `source_file` provenance identifiers. `run_engine.py` updated with STEP 1a/1b split. Process_pdf accepts optional source_file for provenance preservation.

## Approved M1 Architecture Decisions

1. **`search_candidates` record types.** `search_candidates` distinguishes `search_request` from `evidence_candidate` via a `record_type` field. A search request is not the same thing as a returned evidence URL.
2. **`asset_sources` retrieval events.** One `asset_sources` row = one retrieval event. A second row represents a separate retrieval event or a separately discovered source reference.
3. **Canonical discovery record.** `discoveries` is the canonical discovery record for all new rows.
4. **Legacy discovery tables.** `discovered_urls` and `search_history` remain legacy data, read-only, outside the new operational path.

## Objective

Audit, reconnect, repair, and test the existing automated evidence-discovery and downloader pipeline.

The completed workflow must automatically discover evidence, create discovery records, download permitted files, prevent duplicate storage, upload evidence to R2, register assets, create processing jobs, and hand those assets into the existing processing and knowledge engine.

## Existing Systems to Reuse

The repository already contains the relevant foundations under:

- `agents/discovery/`
- `agents/downloader/`

These systems must be inspected before any implementation changes are made.

Do not create a competing `agents/acquisition/` subsystem.

Do not replace the existing discovery or downloader architecture without a documented audit and explicit migration decision.

## Intended End-to-End Flow

Configured Sources
↓
Sources Table
↓
Search Definitions
↓
Search Candidates
↓
Candidate Review and Promotion
↓
Discoveries
↓
Discovery Queue
↓
Downloader
↓
HTTP Response and Content Validation
↓
URL and File-Hash Deduplication
↓
R2 Object Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Existing Specialist Processors
↓
Existing Knowledge Engine

## Phase 1: Read-Only Repository Audit

Inspect every relevant file under:

- `agents/discovery/`
- `agents/downloader/`

The audit must record, for every file:

- File path
- Purpose
- Imports
- Dependencies
- Database tables used
- Input records
- Output records
- Files created or downloaded
- Invocation method
- Expected execution order
- Package-import safety
- Completion status
- Duplicate responsibilities
- Missing error handling
- Missing tests
- Known blockers

The audit must not modify files or database records.

## Phase 2: Database Schema Audit

Inspect the current PostgreSQL schemas for:

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `metadata_queue`
- Any processing or failure queues used by the existing code

For each table, record:

- Columns
- Data types
- Primary key
- Foreign keys
- Unique constraints
- Default values
- Status fields
- Required fields
- Indexes
- Tables or scripts that read from it
- Tables or scripts that write to it

Do not perform schema migrations during the initial audit.

## Phase 3: Minimal Repair Plan

After the repository and schema audits, produce the smallest ordered repair plan required to create a working end-to-end acquisition path.

The repair plan must:

1. Reuse existing files where practical
2. Avoid duplicate systems
3. Identify obsolete files
4. Identify broken imports
5. Identify missing queue transitions
6. Identify missing deduplication
7. Identify missing R2 integration
8. Identify missing asset registration
9. Identify missing processing handoff
10. Define a targeted test for each repair

Stop after presenting the audit and repair plan.

Wait for approval before editing code or changing the database.

## Implementation Order

Implementation proceeds through the milestones defined in:

- `docs/plans/MINIMAL_ACQUISITION_REPAIR_PLAN_2026-08-08.md`

The approved milestone order is:

- ✅ **M0 – Pre-flight backup** — Complete
- ✅ **M1 – Architecture decisions** — Complete
- ✅ **M2 – Source-registry reconciliation** — Complete
- ✅ **M3 – Limited writer role** — Complete
- ✅ **M4 – First small schema migration** — Complete
- ✅ **M5 – Package/import repair** — Complete
- ✅ **M6 – Source seeding repair** — Complete
- ✅ **M7 – Search-request generation** — Complete
- ✅ **M8 – Controlled source search** — Complete
- ✅ **M9 – Human review and manual promotion** — Complete
- ✅ **M10 – Discovery queue** — Complete
- ✅ **M11 – Downloader schema additions** — Complete
- ✅ **M12 – `asset_sources` registration + privilege grant** — Complete
- ✅ **M13 – R2 testability, then downloader implementation** — Complete
- ✅ **M14 – Controlled end-to-end test** — Complete
- ✅ **M15 – Orchestrator repair** — Complete
- ✅ **M16 – Knowledge platform import repair** — Complete
- ✅ **M17 – Acquisition → Knowledge Pipeline Integration** — Complete

### M7 – Search-Request Generation (Complete)

Generate source search requests into `search_candidates` (record_type = 'search_request') from the reconciled source config, idempotently.

Files affected:

- `agents/discovery/build_searches.py` (rewritten as operational replacement)

Schema/data changes:

- INSERT into `search_candidates` (unique constraint from M4)
- UPDATE `record_type` on legacy NULL rows

Exact test:

- Run twice; no duplicate search requests

Expected result:

- Search-request set stable across runs; 30 search requests for 3 sources with verified templates; 4 sources skipped

Rollback/recovery:

- Revert commit; dedup via unique constraint

Dependencies:

- M4, M6

Role:

- Writer

### M8 – Controlled Source Search (Complete)

Execute exactly one controlled source search (one approved source, one permitted search) and store returned evidence URL candidates.

Files affected:

- `agents/discovery/find_candidates.py` (candidates only)

Schema/data changes:

- INSERT into `search_candidates` only (record_type = 'evidence_candidate', per M1 decision)

Exact test:

- Run against the one approved source/search; verify candidates written and no discovery or queue writes

Expected result:

- Returned evidence URL candidates stored; `discoveries` and `discovery_queue` untouched

Rollback/recovery:

- Revert commit; preserve the test candidates and mark for review rather than deleting

Dependencies:

- M7 and the M1 record-type decision

Role:

- Writer

### M2 – Source-Registry Reconciliation (Complete)

Reconcile `agents/discovery/sources.json` (7) and `research/sources.json` (4) against `docs/SOURCE_REGISTRY.md`; add status/rights/rate-limit/review fields. No fixed source count is asserted until done.

Files affected:

- `agents/discovery/sources.json`
- `research/sources.json`
- `docs/SOURCE_REGISTRY.md`

Schema/data changes:

- None (files only)

Exact test:

- Load both configs and diff keys against the registry

Expected result:

- One canonical source list, no name/national-archive mismatches

Rollback/recovery:

- Revert config commit

Dependencies:

- M1

Role:

- None (files only)

## Completion Criteria

This task is complete when:

1. Existing discovery and downloader files have been audited
2. Relevant database schemas have been documented
3. Broken package imports have been repaired
4. One approved source can create search candidates
5. One candidate can become a discovery
6. One discovery can enter the downloader queue
7. One permitted file can be downloaded
8. HTTP response and content type are validated
9. URL duplicates are prevented
10. File-hash duplicates are prevented
11. The file is stored in R2
12. A valid asset record is created
13. A processing job is created
14. The asset reaches the existing processing engine
15. Provenance remains traceable to the original discovery URL
16. Targeted tests pass
17. Documentation is updated
18. The Git diff is reviewed
19. A working checkpoint is committed and pushed

## Non-Goals

Do not begin any of the following during this task:

- A new acquisition subsystem
- Digital Twin schema development
- Reconstruction geometry
- Walkthrough development
- Broad AI enrichment
- Unrelated search redesign
- Unrelated database refactoring
- Automatic production scheduling
- Large-scale crawling
- Downloading an uncontrolled archive collection

The purpose of this task is to make one controlled evidence path work end to end before scaling it.

## Safety Rules

- Inspect before editing
- Work on one milestone at a time
- Read complete files before replacing them
- Prefer targeted changes over broad rewrites
- Require approval for database changes
- Do not delete evidence
- Do not commit secrets or API keys
- Do not commit downloaded evidence files
- Do not run destructive commands without explicit approval
- Run targeted tests after each change
- Review `git diff` after each change
- Update documentation only after tests pass
- Do not commit automatically
- Stop when the approved milestone is complete