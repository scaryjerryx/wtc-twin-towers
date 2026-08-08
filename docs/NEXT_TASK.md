# Next Task

## Reconnect Existing Automated Evidence Gathering

### Status

🔄 **In Progress**

## Milestone Progress

- ✅ **M0 – Pre-flight backup** — Complete and passed. Production database backed up, restored into a scratch database, row counts and schema object counts matched, scratch database cleaned up.
- ✅ **M1 – Architecture decisions** — Complete and approved. Decisions recorded below.
- ✅ **M2 – Source-registry reconciliation** — Complete.
- ✅ **M3 – Limited writer role** — Complete. Role `wtc_writer` created with least-privilege grants on approved tables and sequences. Catalog verification passed. Runtime verification revealed additional SELECT privileges may be required for some operational queries; this will be addressed in a later milestone if necessary.
- 🔄 **M4 – First small schema migration** — Current active milestone.

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
- 🔄 **M4 – First small schema migration** — Current
- ⬜ **M5 – Package/import repair** — Planned
- ⬜ **M6 – Source seeding repair** — Planned
- ⬜ **M7 – Search-request generation** — Planned
- ⬜ **M8 – Controlled source search** — Planned
- ⬜ **M9 – Human review and manual promotion** — Planned
- ⬜ **M10 – Discovery queue** — Planned
- ⬜ **M11 – Downloader schema additions** — Planned
- ⬜ **M12 – `asset_sources` registration + privilege grant** — Planned
- ⬜ **M13 – R2 testability, then downloader implementation** — Planned
- ⬜ **M14 – Controlled end-to-end test** — Planned
- ⬜ **M15 – Orchestrator repair** — Planned (only after M14 passes)

### M4 – First Small Schema Migration (Current)

Add only discovery-side structures required by the new operational path: `discovery_queue.discovery_id` (nullable FK → discoveries), `attempt_count`, `last_error`, `next_retry`, new status values, index on `discovery_queue(status)`, and a unique constraint on `search_candidates` (only if required by the new path). **Do not add a unique constraint to `search_history`.**

Files affected:

- SQL migration artifact

Schema/data changes:

- As listed; forward-only, idempotent

Exact test:

- Rerun migration (no-op); verify via `information_schema`; confirm `search_history` unchanged

Expected result:

- New columns/constraints/index present; `search_history` and legacy rows unchanged

Rollback/recovery:

- Forward-fix only; no destructive rollback of populated columns

Dependencies:

- M0, M1

Role:

- Administrator

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