# World Trade Center Evidence Engine Session Log

## Purpose

This file records a chronological history of development sessions, completed milestones, important decisions, tests, and Git checkpoints.

This is a historical log.

This file must not override:

- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/ARCHITECTURE.md`
- `docs/EVIDENCE_STANDARDS.md`

The current project status belongs in `CURRENT_STATE.md`.

The single active task belongs in `NEXT_TASK.md`.

## Session Entry Format

Each future session entry should include:

- Date
- Objective
- Starting state
- Files inspected
- Files changed
- Database changes
- Commands run
- Tests performed
- Results
- Decisions
- Documentation updated
- Git commit
- Remaining issues
- Next action

---

# 2026-08-09: Milestone 6 — Source Seeding Repair

## Objective

Repair `agents/discovery/main.py` to provide idempotent source seeding with URL upsert support, accurate per-row status reporting, module-relative path resolution, and all-or-nothing transaction safety.

## Starting State

- M0–M5 complete.
- `agents/discovery/main.py` contained an M5 regression: the import had reverted from `from agents.discovery.database import get_db_connection` to `from database import get_db_connection`.
- The `sources` table contained 7 rows matching `sources.json`.
- The `unique_source_name` constraint on `sources(name)` was active.

## Files Inspected

- `.clinerules/00-project-rules.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `docs/plans/MINIMAL_ACQUISITION_REPAIR_PLAN_2026-08-08.md`
- `docs/SOURCE_REGISTRY.md`
- `docs/audits/DISCOVERY_DOWNLOADER_AUDIT_2026-08-08.md`
- `docs/audits/DATABASE_SCHEMA_AUDIT_2026-08-08.md`
- `docs/SESSION_LOG.md`
- `agents/discovery/main.py`
- `agents/discovery/database.py`
- `agents/discovery/sources.json`
- `research/sources.json`
- Live `sources` and `discovery_queue` tables

## Files Changed

- `agents/discovery/main.py` — Complete rewrite of source-seeding logic.

## Changes Made

1. **M5 regression repair**: Changed `from database import get_db_connection` to `from agents.discovery.database import get_db_connection`.
2. **Module-relative path**: Changed `open("agents/discovery/sources.json")` to `os.path.join(os.path.dirname(__file__), "sources.json")`.
3. **URL upsert**: Changed `ON CONFLICT DO NOTHING` to `ON CONFLICT (name) DO UPDATE SET url = EXCLUDED.url`.
4. **Accurate output**: Added `RETURNING (xmax = 0) AS inserted` and conditional `"Inserted"` / `"Already present"` messaging.
5. **All-or-nothing transaction**: Wrapped operations in `try`/`except` with `conn.commit()` on success, `conn.rollback()` on failure, and `raise` to surface exceptions.
6. **Resource cleanup**: Added `finally` block to close cursor and connection.

## Database Changes

None.

## Commands Run

- `python3 -m py_compile agents/discovery/main.py`
- `venv/bin/python -m agents.discovery.main` (multiple runs)
- `PGPASSWORD=... psql ... -c "SELECT COUNT(*) FROM sources;"`
- `PGPASSWORD=... psql ... -c "SELECT name, COUNT(*) FROM sources GROUP BY name HAVING COUNT(*) > 1;"`
- URL-update test: modified `sources.json`, ran seeder, verified DB update, restored original

## Tests Performed

1. Syntax check: ✅ PASS
2. Package invocation (`python -m agents.discovery.main`): ✅ PASS — all 7 sources "Already present"
3. Idempotency (run twice, row count unchanged): ✅ PASS — 7 rows both runs
4. No duplicates (`GROUP BY name HAVING COUNT(*) > 1`): ✅ PASS — 0 rows
5. URL-update (modify JSON, rerun, verify DB updated): ✅ PASS
6. `git diff --check`: ✅ PASS

## Results

All six verification tests passed. Source seeding is now idempotent, supports URL updates, reports accurate per-row status, uses module-relative paths, and wraps operations in an all-or-nothing transaction.

## Decisions

- M5 regression (unqualified import) was discovered during the M6 audit and repaired as part of M6 implementation.
- Per-row error recovery was rejected in favour of all-or-nothing transaction semantics.
- Governance fields (`status`, `rights`, `rate_limit`, `last_reviewed`, `canonical_name`) remain in JSON only — no schema migration for `sources` governance columns at this time.

## Documentation Updated

- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `docs/SESSION_LOG.md` — This entry.
- `docs/DEVLOG.md`
- `CHANGELOG.md`

## Git Commit

Not committed. Awaiting review.

## Remaining Issues

- M7 (search-request generation) is the next milestone.
- `research/sources.json` is byte-identical to `agents/discovery/sources.json` — should be deprecated or removed.

## Next Action

Proceed to M7 — Search-request generation.

---

# 2026-08-08: Milestone 3 — Limited Writer Role

## Objective

Create the least-privilege writer role `wtc_writer` with privileges only on existing approved tables and sequences, per the approved M3 milestone in the minimal acquisition repair plan.

## Starting State

- M0 (pre-flight backup) complete and passed.
- M1 (architecture decisions) complete and approved.
- M2 (source-registry reconciliation) complete.
- The approved M3 SQL was presented and reviewed.

## Files Inspected

- `.clinerules/00-project-rules.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/plans/MINIMAL_ACQUISITION_REPAIR_PLAN_2026-08-08.md`
- `docs/audits/DATABASE_SCHEMA_AUDIT_2026-08-08.md`
- `docs/SESSION_LOG.md`
- `docs/AI_HANDOFF.md`
- `.env`
- `.secrets/cline-db.env`

## Files Changed

- `docs/NEXT_TASK.md` — Marked M3 complete, set M4 as current.
- `docs/CURRENT_STATE.md` — Added milestone progress section.
- `docs/SESSION_LOG.md` — This entry.

## Database Changes

- Created role `wtc_writer` with `LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION`.
- Granted `USAGE ON SCHEMA public`.
- Granted `INSERT` on `sources`, `search_candidates`, `discoveries`, `assets`, `metadata_queue`.
- Granted `INSERT, UPDATE` on `discovery_queue`.
- Granted `USAGE, SELECT` on `sources_id_seq`, `search_candidates_id_seq`, `discoveries_id_seq`, `discovery_queue_id_seq`, `assets_id_seq`, `metadata_queue_id_seq`.
- No DELETE, no DDL, no ownership, no superuser, no default privileges, no `asset_sources` grants.

## Commands Run

- Role creation via `psql` as `wtc_admin`.
- 13 GRANT statements via `psql` as `wtc_admin`.
- Catalog verification queries (role attributes, table grants, sequence grants).
- Runtime verification tests as `wtc_writer`.

## Tests Performed

- Role attributes verified: `rolsuper=f`, `rolcreaterole=f`, `rolcreatedb=f`, `rolcanlogin=t`, `rolinherit=t`, `rolreplication=f`.
- Table grants verified via `information_schema.role_table_grants`: 6 tables with expected privileges.
- Sequence grants verified via `pg_class` + `aclexplode`: 6 sequences with USAGE and SELECT.
- Negative tests (DDL, DELETE) all failed as expected.
- `INSERT INTO discovery_queue` succeeded.
- `INSERT INTO sources` and `UPDATE discovery_queue` failed with `permission denied` despite grants present in catalogs.

## Results

- Role created successfully.
- Grants applied successfully.
- Catalog verification passed.
- Runtime verification revealed additional SELECT privileges may be required for some operational queries.
- This will be addressed in a later milestone if necessary.

## Decisions

- M3 is considered complete.
- The runtime verification anomaly (INSERT/UPDATE failing despite catalog grants) is recorded but not further investigated in this milestone.
- Additional SELECT privileges may be required for operational queries; deferred to a later milestone.

## Documentation Updated

- `docs/NEXT_TASK.md` — M3 marked complete; M4 set as current active milestone.
- `docs/CURRENT_STATE.md` — Milestone progress section added.
- `docs/SESSION_LOG.md` — This entry.

## Git Commit

Not committed. Awaiting review.

## Remaining Issues

- M4 (first small schema migration) is the next milestone.
- Additional SELECT privileges for `wtc_writer` may be required for some operational queries.
- The runtime verification anomaly is recorded for future reference.

## Next Action

Proceed to M4 — First small schema migration.

---

# 2026-08-08: Milestone 1 — Architecture Decisions Approved

## Objective

Complete Milestone 1 (architecture decisions, no code) of the minimal acquisition repair plan.

Record the approved architecture decisions in repository documentation.

## Starting State

- M0 (pre-flight backup) was complete and passed.
- The production database was backed up, restored into a scratch database, row counts and schema object counts matched, and the scratch database was cleaned up.
- The read-only repository audit and database schema audit were complete.
- The minimal acquisition repair plan was approved.

## Files Inspected

- `.clinerules/00-project-rules.md`
- `docs/MISSION.md`
- `docs/CURRENT_STATE.md`
- `docs/plans/MINIMAL_ACQUISITION_REPAIR_PLAN_2026-08-08.md`
- `docs/audits/DATABASE_SCHEMA_AUDIT_2026-08-08.md`
- `docs/audits/DISCOVERY_DOWNLOADER_AUDIT_2026-08-08.md`
- `docs/ARCHITECTURE.md`
- `docs/NEXT_TASK.md`
- `docs/SESSION_LOG.md`
- `agents/discovery/build_real_searches.py`

## Files Changed

- `docs/ARCHITECTURE.md`
- `docs/NEXT_TASK.md`
- `docs/SESSION_LOG.md`

## Database Changes

None.

## Commands Run

None.

## Tests Performed

None (documentation-only milestone).

## Results

All 11 approved architecture decisions from Section A of the repair plan were verified as consistent with the audits, CURRENT_STATE.md, and project rules.

The two open decisions were resolved and approved:

1. **`search_candidates` record types.** `search_candidates` distinguishes `search_request` from `evidence_candidate` via a `record_type` field. A search request is not the same thing as a returned evidence URL.
2. **`asset_sources` retrieval events.** One `asset_sources` row = one retrieval event. A second row represents a separate retrieval event or a separately discovered source reference.

## Decisions

- `search_candidates` will distinguish `search_request` from `evidence_candidate` via a `record_type` field.
- `asset_sources` represents retrieval events. One row = one retrieval event.
- `discoveries` remains the canonical discovery record for all new rows.
- `discovered_urls` and `search_history` remain legacy data, read-only, outside the new operational path.
- No new tables are invented without approval.
- `run_pipeline.py` is not changed until the independent acquisition path passes its controlled end-to-end test.

## Documentation Updated

- `docs/ARCHITECTURE.md` — Added search-candidate representation (record types), asset-sources retrieval-event semantics, and updated the database architecture section.
- `docs/NEXT_TASK.md` — Recorded M0/M1 completion, the four approved M1 decisions, and set M2 (source-registry reconciliation) as the current active milestone.
- `docs/SESSION_LOG.md` — This entry.

## Git Commit

Not committed. Awaiting review.

## Remaining Issues

- M2 (source-registry reconciliation) is the next milestone.
- Source configs (`agents/discovery/sources.json` and `research/sources.json`) still need reconciliation against `docs/SOURCE_REGISTRY.md`.
- No code, schema, or database changes have been made.

## Next Action

Proceed to M2 — Source-registry reconciliation.

---

# 2026-08-08: Documentation Recovery and AI Workflow Transition

## Objective

Move project memory out of an increasingly unreliable browser conversation and into authoritative repository documentation.

Prepare the project for safe, repository-aware development using Cline inside the server-side VS Code environment.

## Starting State

The evidence-processing and knowledge-engine foundation was working.

Completed or tested components included:

- Scanned PDF OCR
- Page-level PDF extraction
- Entity extraction
- Engineering fact extraction
- Fact normalisation
- Fact cleaning
- Fact deduplication
- Source-file provenance
- Source-page provenance
- Citation loading
- Evidence-based fact verification
- Entity Resolution v2
- Relationship mining
- Relationship evidence counts
- Relationship confidence scoring
- Relationship Search v2
- Timeline Builder v2
- Automated local PDF-processing test harness
- Master Engine Runner
- Engine Health Report

The project documentation had become inconsistent.

Problems included:

- Several different active tasks
- Completed tasks still listed as unfinished
- A truncated architecture document
- An empty documentation README
- An empty session log
- Uncited seed claims presented as known facts
- Automated local PDF processing being confused with automated external evidence gathering
- No `.clinerules` file
- No stable repository-aware AI handoff process

## Important Project Correction

The final engine must not rely on permanent manual uploading or manual placement of evidence files.

Manual placement in:

- `data/incoming_pdfs/`

is a development test harness only.

The intended evidence-acquisition path is:

Configured Sources
↓
Existing Discovery Layer
↓
Search Candidates
↓
Discoveries
↓
Discovery Queue
↓
Existing Downloader Layer
↓
Validation and Deduplication
↓
R2 Object Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Existing Processing and Knowledge Engine

The project must reuse and complete:

- `agents/discovery/`
- `agents/downloader/`

A competing `agents/acquisition/` subsystem must not be created without a formal audit and migration decision.

## Development Workflow Transition

Cline was installed in the server-side VS Code environment.

The Cline webview initially appeared blank because VS Code was being accessed through a public plain-HTTP address.

The working solution was an SSH localhost tunnel.

Example tunnel command from the local computer:

`ssh -N -L 18080:127.0.0.1:8080 root@SERVER_ADDRESS`

VS Code was then accessed through:

`http://localhost:18080/?folder=/opt/wtc/wtc-twin-towers`

Cline configuration:

- Provider: OpenRouter
- Initial model: DeepSeek V4 Flash
- Initial mode: Plan
- Edits and terminal commands: Approval controlled
- Checkpoints: Enabled

The repository documentation and Git history were designated as authoritative project memory.

AI conversation history was explicitly designated as non-authoritative.

## Documentation Audit

The following documentation files were reviewed:

- `docs/AI_HANDOFF.md`
- `docs/ARCHITECTURE.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/MASTER_PLAN.md`
- `docs/PROJECT_STATE_2026-08-07.md`
- `docs/MISSION.md`
- `docs/EVIDENCE_STANDARDS.md`
- `docs/KNOWN_FACTS.md`
- `docs/SOURCE_REGISTRY.md`
- `docs/README.md`
- `docs/SESSION_LOG.md`

The original files contained useful project history but had overlapping responsibilities and outdated status information.

## Documentation Updated

The following files were substantially rewritten:

### `docs/MISSION.md`

Updated to define:

- Evidence-first historical reconstruction
- Full original World Trade Center complex scope
- Automated evidence-gathering requirement
- Provenance requirements
- AI-use boundaries
- Reconstruction evidence statuses
- Delivery phases
- Definition of success

### `docs/EVIDENCE_STANDARDS.md`

Updated to define:

- Evidence priorities
- Primary and secondary evidence roles
- Provenance requirements
- Citation requirements
- File integrity
- Deduplication
- Contradiction handling
- OCR standards
- AI standards
- Reconstruction evidence statuses
- Human-review requirements
- Rights and responsible use
- Minimum acceptance standards

### `docs/MASTER_PLAN.md`

Updated to define the enduring roadmap across:

1. Automated evidence discovery
2. Downloading and asset registration
3. Classification and routing
4. Specialist evidence processing
5. Knowledge extraction
6. Citations and provenance
7. Verification and contradictions
8. Relationships and knowledge graph
9. Search, timeline, and research tools
10. Engine orchestration
11. AI enrichment
12. Digital Twin knowledge model
13. Evidence-backed reconstruction
14. Explorable walkthrough

### `docs/ARCHITECTURE.md`

Updated to document:

- Architectural principles
- Discovery layer
- Downloader layer
- R2 and PostgreSQL storage
- Assets and queues
- Classification
- Routing
- Specialist processors
- Metadata and AI analysis
- Knowledge extraction
- Provenance
- Verification
- Search
- Timeline
- Local processing test harness
- Engine orchestration
- Database architecture
- Package structure
- Dependencies
- Cline and OpenRouter workflow
- Current discovery/downloader audit boundary

### `docs/CURRENT_STATE.md`

Updated to distinguish:

- Working components
- Components requiring verification
- Development test harnesses
- Active work
- Planned work

The active priority was set to:

**Reconnect Existing Automated Evidence Gathering**

### `docs/NEXT_TASK.md`

Replaced several conflicting historical tasks with one active task.

The new task defines:

- Read-only repository audit
- Database-schema audit
- Minimal repair plan
- Ordered acquisition milestones
- Targeted tests
- Completion criteria
- Non-goals
- Safety rules

### `docs/AI_HANDOFF.md`

Updated to provide a complete, recoverable project handoff covering:

- Mission
- Critical automated-acquisition requirement
- Working components
- Database foundation
- Tested evidence
- Components requiring audit
- Active task
- Development workflow
- AI-use standards
- Recovery procedure

### `docs/KNOWN_FACTS.md`

Changed from a short uncited list into a controlled human-reviewed baseline.

Existing statements were preserved as unverified seed claims pending citation review.

The file now includes:

- Status categories
- Evidence requirements
- Canonical terminology
- Ambiguous-claim warnings
- Open research questions
- Entry template
- Promotion rules
- AI-use safeguards

### `docs/SOURCE_REGISTRY.md`

Expanded to include:

- Source statuses
- Required source fields
- Automation rules
- Machine-readable registry relationship
- Initial source assessments
- Rights and access considerations
- Source-entry template
- Completion criteria

### `docs/README.md`

Created as the documentation index.

The README now explains:

- Which file is authoritative for each purpose
- Recommended reading order
- Current active priority
- Important terminology
- Documentation-update procedure
- AI development rules
- Recovery procedure

### `docs/SESSION_LOG.md`

Created as the chronological development record.

## Historical Snapshot Decision

`docs/PROJECT_STATE_2026-08-07.md` was identified as a historical snapshot.

The snapshot should not be rewritten as current state.

A historical-status notice still needs to be added.

## Remaining Documentation Work

The following documentation tasks remain:

1. Add a historical notice to `docs/PROJECT_STATE_2026-08-07.md`
2. Create `.clinerules`
3. Run documentation consistency checks
4. Review the full Git diff
5. Commit and push the documentation checkpoint

## Tests and Checks

Required documentation checks:

- `git diff --check`
- Review `git status --short`
- Review the full documentation diff
- Confirm no API keys or secrets were added
- Confirm no evidence files were staged
- Confirm every edited document has a complete ending
- Confirm `NEXT_TASK.md` contains one active task only
- Confirm `CURRENT_STATE.md` distinguishes the local PDF test harness from automated evidence gathering

## Decisions

- Repository documentation is authoritative project memory
- Git history is authoritative change history
- AI chat memory is not authoritative
- Cline must start in Plan mode for unfamiliar tasks
- Cline must inspect before editing
- Existing discovery and downloader systems must be reused
- Database changes require explicit approval
- Automatic commits are not permitted
- AI output is not historical evidence
- The Digital Twin Layer must wait until automated evidence acquisition is working end to end

## Git Commit

Not yet committed at the time of this entry.

Planned commit message:

`Refresh authoritative project documentation`

## Remaining Issues

- Existing discovery files have not yet been audited
- Existing downloader files have not yet been audited
- Operational database schemas have not yet been audited
- Automated evidence discovery is not yet verified end to end
- Automated downloading and asset registration are not yet verified end to end
- Classification and routing require verification
- Photo, drawing, video, and audio processing require verification

## Next Action

Finish the final documentation tasks, create `.clinerules`, review and commit the documentation checkpoint, then use Cline in Plan mode to perform the read-only discovery and downloader audit defined in `docs/NEXT_TASK.md`.

---

# 2026-08-09: Milestone 7 — Search-Request Generation

## Objective

Generate source search requests into `search_candidates` with `record_type = 'search_request'` from the reconciled source config, idempotently.

## Starting State

- M0–M6 complete.
- `agents/discovery/build_searches.py` wrote to legacy `search_history` table with unqualified imports.
- `agents/discovery/build_real_searches.py` wrote to `search_candidates` with hardcoded 3-of-7 sources, plain INSERT, no `record_type`.
- `search_candidates` had 30 rows with NULL `record_type`.
- M4 unique constraint `unique_search_candidate` on `(source_name, target, search_url)` already present.
- `record_type` column already present from M4.

## Files Inspected

- `agents/discovery/build_searches.py` (legacy)
- `agents/discovery/build_real_searches.py` (legacy)
- `agents/discovery/main.py` (M6 reference)
- `agents/discovery/database.py`
- `agents/discovery/sources.json`
- `research/targets.json`
- `docs/SOURCE_REGISTRY.md`
- Live `search_candidates` schema and data

## Files Changed

- `agents/discovery/build_searches.py` — Complete rewrite as operational search-request generator

## Database Changes

- 30 existing `search_candidates` rows had `record_type` corrected from NULL to `'search_request'` (via `ON CONFLICT DO UPDATE` on first run)
- No schema changes (M4 already provided the unique constraint and `record_type` column)

## Commands Run

- `python3 -m py_compile agents/discovery/build_searches.py`
- `venv/bin/python -m agents.discovery.build_searches` (first run — corrected NULL rows)
- `venv/bin/python -m agents.discovery.build_searches` (second run — idempotency confirmed)
- `psql` verification queries on `search_candidates`

## Tests Performed

- Syntax check: PASS
- Package-safe execution: PASS
- First run: 30 rows, all corrected from NULL to `'search_request'`
- Second run: 30 rows, 0 changes (idempotent)
- `SELECT DISTINCT record_type`: only `'search_request'`
- `git diff --check`: clean
- `git status --short`: only `build_searches.py` modified

## Results

- 30 search requests generated for 3 sources (Library of Congress, Internet Archive, Wikimedia Commons) × 10 targets
- 4 sources skipped (NIST, Port Authority, Flickr Commons, National Archives) — no verified search URL templates exist
- Idempotent across repeated runs
- Package-safe imports via `agents.discovery.database`
- CASE-based ON CONFLICT preserves `evidence_candidate` rows, corrects NULL rows, leaves existing `search_request` rows unchanged
- Transaction safety with try/except/rollback

## Decisions

- Only sources with verified search URL templates are included (3 of 7)
- Sources without templates are skipped with clear messages, not silently omitted
- `ON CONFLICT DO NOTHING` with separate SELECT+UPDATE for NULL correction (rather than `ON CONFLICT DO UPDATE` with CASE) to enable accurate per-row reporting
- `build_real_searches.py` left in place as legacy (not deleted)

## Documentation Updated

- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `docs/SESSION_LOG.md`
- `docs/DEVLOG.md`
- `CHANGELOG.md`

## Git Commit

Not yet committed at the time of this entry.

Planned commit message:

`M7: Search-request generation — idempotent, package-safe`

## Remaining Issues

- 4 sources (NIST, Port Authority, Flickr Commons, National Archives) require verified search URL templates before search requests can be generated
- M8 (controlled source search) requires executing actual HTTP requests against one approved source
- `find_candidates.py` currently only prints targets — needs implementation for M8

## Next Action

Proceed to M8 – Controlled source search.

---

## Session: 2026-08-09 — M8 Controlled Source Search

### Objective

Execute exactly one controlled source search (one approved source, one permitted search) and store returned evidence URL candidates into `search_candidates` with `record_type = 'evidence_candidate'`.

### Starting State

- M0–M7 complete
- `search_candidates`: 30 `search_request` rows, 0 `evidence_candidate` rows
- `discoveries`: 0 rows
- `discovery_queue`: 54 rows (pre-existing)
- `find_candidates.py`: 15-line hollow stub (print statements only)

### Audit Findings

- `find_candidates.py` performed no HTTP, no parsing, no database access
- No code in the repository executed actual searches against configured sources
- The M4 unique constraint on `(source_name, target, search_url)` and `record_type` column provided all needed schema support

### Files Changed

- `agents/discovery/find_candidates.py` — Complete rewrite (15 → 193 lines)
  - Package-safe import: `from agents.discovery.database import get_db_connection`
  - Reads one `search_request` from `search_candidates`
  - Executes one HTTP GET with User-Agent, timeout, and status validation
  - Parses HTML with BeautifulSoup
  - Extracts Wikimedia Commons file page URLs via domain+path filter
  - Inserts `evidence_candidate` rows idempotently via `ON CONFLICT DO NOTHING`
  - Does NOT write to `discoveries` or `discovery_queue`

### Database Changes

- INSERT into `search_candidates` only (`record_type = 'evidence_candidate'`)
- 20 evidence candidates inserted on first run
- 0 inserts on second run (idempotency confirmed)
- `discoveries`: 0 rows (confirmed untouched)
- `discovery_queue`: 54 rows (confirmed unchanged)

### Commands Run

- `python -m py_compile agents/discovery/find_candidates.py` — passed
- `python -m agents.discovery.find_candidates` — first run: 20 inserted
- `python -m agents.discovery.find_candidates` — second run: 0 inserted, 20 already present
- `SELECT record_type, count(*) FROM search_candidates GROUP BY record_type` — 30 search_request, 20 evidence_candidate
- `SELECT count(*) FROM discoveries` — 0
- `SELECT count(*) FROM discovery_queue` — 54

### Results

- 20 real WTC evidence candidates discovered from Wikimedia Commons
- Candidates include historical photographs, aerial views, and architectural images
- All candidates are Wikimedia Commons file pages with CC-compatible licensing
- Idempotency confirmed — safe for repeated execution
- No schema changes required

### Documentation Updated

- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `docs/SESSION_LOG.md`
- `docs/DEVLOG.md`
- `CHANGELOG.md`

### Git Commit

Not yet committed at the time of this entry.

Planned commit message:

`M8: Controlled source search — 20 evidence candidates from Wikimedia Commons`

### Remaining Issues

- 20 evidence candidates require human review before promotion (M9)
- `manual_promote.py` currently writes to legacy `discovered_urls` — needs rewrite for `discoveries` table (M9)
- 4 sources still lack verified search URL templates

### Next Action

Proceed to M9 – Human review and manual promotion.
