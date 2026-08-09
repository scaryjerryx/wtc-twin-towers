# World Trade Center Evidence Engine Documentation

## Purpose

This directory contains the authoritative documentation for the World Trade Center Evidence Engine.

The project is building an automated, transparent, citation-backed evidence system capable of supporting a historically accurate digital reconstruction of the original World Trade Center complex.

Repository documentation and Git history are the authoritative project memory.

AI conversation history is not authoritative project memory.

## Start Here

Read the documents in this order:

1. `MISSION.md`
2. `EVIDENCE_STANDARDS.md`
3. `CURRENT_STATE.md`
4. `NEXT_TASK.md`
5. `ARCHITECTURE.md`
6. `MASTER_PLAN.md`
7. `AI_HANDOFF.md`

During a new AI development session, also read:

- `.clinerules`

## Documentation Index

### `MISSION.md`

Defines:

- Why the project exists
- The evidence-first principle
- The project scope
- The automated evidence-gathering requirement
- AI-use boundaries
- Reconstruction standards
- Delivery phases
- The definition of success

This is the stable project charter.

### `EVIDENCE_STANDARDS.md`

Defines:

- Evidence priorities
- Provenance requirements
- Citation requirements
- File-integrity requirements
- Deduplication rules
- Confidence and verification rules
- Contradiction handling
- OCR standards
- AI evidence rules
- Human-review requirements
- Rights and responsible-use requirements

This is the authoritative evidence-governance document.

### `MASTER_PLAN.md`

Defines:

- The enduring end-to-end roadmap
- Automated evidence discovery
- Downloading and asset registration
- Classification and routing
- Specialist evidence processing
- Knowledge extraction
- Citations and provenance
- Verification
- Relationships
- Search and timeline tools
- Engine orchestration
- AI enrichment
- Digital Twin modelling
- Reconstruction
- The explorable walkthrough

This document is not the current task list.

### `ARCHITECTURE.md`

Defines:

- Current technical architecture
- Existing subsystems
- Known modules
- Current data flows
- Database responsibilities
- Working components
- Components requiring verification
- Package and dependency architecture
- Development AI workflow
- Current integration boundary

Use this document to understand how the system is structured.

### `CURRENT_STATE.md`

Defines:

- What is working
- What is a test harness
- What requires verification
- What is currently in progress
- What remains planned
- The immediate next milestone

This file must remain concise, current, and date-stamped.

### `NEXT_TASK.md`

Defines exactly one active development task.

The file includes:

- Objective
- Scope
- Existing systems to reuse
- Audit requirements
- Database-schema checks
- Implementation milestones
- Tests
- Completion criteria
- Non-goals
- Safety rules

Obsolete tasks must not remain in this file.

Historical tasks belong in Git history or `SESSION_LOG.md`.

### `AI_HANDOFF.md`

Provides the context required for a new AI development assistant to continue safely.

It includes:

- Project mission
- Critical acquisition requirement
- Working components
- Database foundation
- Tested evidence
- Components requiring audit
- Current active task
- Development workflow
- Non-negotiable rules
- Recovery procedure

A new AI session should read this document before proposing changes.

### `KNOWN_FACTS.md`

Contains selected human-reviewed baseline claims and canonical terminology.

This file:

- Is not a replacement for the facts database
- Must distinguish verified facts from seed claims
- Must preserve uncertainty
- Must require citations before promotion
- Must not treat AI output as independent evidence

The PostgreSQL evidence and knowledge tables remain the machine-readable source of truth.

### `SOURCE_REGISTRY.md`

Records known and potential evidence sources.

It includes:

- Source status
- Expected evidence types
- Potential evidence value
- Access methods
- Rights considerations
- Automation status
- Review requirements
- Source-entry templates
- Completion criteria

A source appearing in the registry is not automatically approved for crawling, downloading, reuse, or publication.

### `SESSION_LOG.md`

Records a chronological history of development sessions and completed milestones.

Each entry should include:

- Date
- Objective
- Files changed
- Database changes
- Commands run
- Tests performed
- Results
- Decisions
- Documentation updates
- Git commit
- Next action

This file is historical and must not override `CURRENT_STATE.md` or `NEXT_TASK.md`.

### `PROJECT_STATE_2026-08-07.md`

Historical project snapshot recorded on August 7, 2026.

This file is retained for project history.

It is not the current project status.

Use `CURRENT_STATE.md` and `NEXT_TASK.md` for current information.

## Current Active Priority

The current active priority is:

**Reconnect Existing Automated Evidence Gathering**

The project must inspect, reconnect, repair, and test the existing systems under:

- `agents/discovery/`
- `agents/downloader/`

Do not create a competing acquisition architecture.

The intended path is:

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
Validation and Deduplication
↓
R2 Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Existing Processing and Knowledge Engine

The complete implementation instructions are maintained in:

- `NEXT_TASK.md`

## Important Terminology

### Automated Evidence Gathering

The external workflow that discovers, downloads, validates, deduplicates, stores, registers, and queues historical evidence.

This remains the current active priority.

### Automated Local PDF Processing

The working development test harness under:

- `agents/ingestion/automated_ingestion.py`

This processes manually supplied local PDFs.

This is not the finished evidence-gathering workflow.

### Provenance

The traceable link between knowledge and its original evidence.

Current fact provenance uses:

Facts
↓
Fact Sources
↓
Citations

### Verification

The process of evaluating support for a claim.

Current source-count scoring is an operational first version and does not yet measure independent evidence fully.

### Digital Twin

The future evidence-backed representation of the original World Trade Center complex, including:

- Site
- Buildings
- Towers
- Floors
- Zones
- Spaces
- Structural elements
- Architectural elements
- Materials
- Objects
- Systems
- Time periods
- Supporting evidence
- Confidence and uncertainty

## Development Workflow

Every development task should follow:

Read
↓
Audit
↓
Plan
↓
Approve
↓
Implement One Scoped Change
↓
Compile or Test
↓
Review Git Diff
↓
Update Documentation
↓
Commit
↓
Continue

## Documentation Rules

- Keep `MISSION.md` stable
- Keep `EVIDENCE_STANDARDS.md` authoritative
- Keep `MASTER_PLAN.md` strategic
- Keep `ARCHITECTURE.md` technical
- Keep `CURRENT_STATE.md` concise and current
- Keep `NEXT_TASK.md` limited to one task
- Keep `AI_HANDOFF.md` sufficient for recovery
- Keep `KNOWN_FACTS.md` cited and human reviewed
- Keep `SOURCE_REGISTRY.md` source specific
- Keep `SESSION_LOG.md` chronological
- Keep dated project-state files historical
- Do not duplicate the same active-task instructions across multiple files

## AI Development Rules

The current repository-aware development workflow uses:

- Cline
- OpenRouter
- DeepSeek V4 Flash
- Plan mode before Act mode
- Approval-controlled edits and commands
- Cline checkpoints

Before significant implementation work, the AI assistant must:

1. Read the authoritative documentation
2. Read `.clinerules`
3. Inspect the relevant files
4. Check Git status
5. Confirm the active task
6. Produce a plan
7. Wait for approval before editing

The AI assistant must not:

- Create duplicate architecture
- Edit unrelated files
- Change database schemas without approval
- Delete evidence
- Commit secrets
- Commit downloaded evidence
- Treat AI output as historical evidence
- Commit automatically
- Jump ahead to unrelated roadmap phases

## Documentation Update Procedure

After a tested milestone:

1. Update `CURRENT_STATE.md`
2. Update `NEXT_TASK.md`
3. Update `AI_HANDOFF.md` if architecture or project context changed
4. Update `ARCHITECTURE.md` if components or data flows changed
5. Update `MASTER_PLAN.md` only if the enduring roadmap changed
6. Add an entry to `SESSION_LOG.md`
7. Run `git diff --check`
8. Review the complete Git diff
9. Commit and push the working checkpoint

## Recovery Procedure

If a conversation, editor session, or development agent is lost:

1. Open the repository
2. Run `git status`
3. Inspect the latest Git commits
4. Read this documentation index
5. Read `CURRENT_STATE.md`
6. Read `NEXT_TASK.md`
7. Read `AI_HANDOFF.md`
8. Read the latest `SESSION_LOG.md` entries
9. Continue only from the documented active milestone

The repository must remain sufficient to continue development without access to previous chat history.
