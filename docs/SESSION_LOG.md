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