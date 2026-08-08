# WTC Evidence Engine Development Rules

## Project Identity

Project:

World Trade Center Evidence Engine

Repository:

`/opt/wtc/wtc-twin-towers`

Primary database:

`wtc_evidence`

## Project Mission

Build an automated, transparent, citation-backed evidence engine capable of supporting the most historically accurate digital reconstruction of the original World Trade Center complex.

The completed system must:

1. Discover historical evidence automatically
2. Download and register permitted evidence
3. Deduplicate URLs, files, records, facts, citations, and relationships
4. Store evidence in R2
5. Register evidence as database assets
6. Classify and route assets
7. Process PDFs, photographs, drawings, video, audio, and records
8. Extract entities, facts, dates, events, and relationships
9. Preserve source, page, sheet, image, frame, and timestamp provenance
10. Create research citations
11. Verify claims and preserve contradictions
12. Build a searchable knowledge graph
13. Support an evidence-backed digital twin
14. Support an evidence-linked historical walkthrough

Evidence takes priority over assumptions.

Artificial intelligence may assist with processing and interpretation, but artificial intelligence must not become an uncited source of historical truth.

## Authoritative Project Memory

Repository documentation and Git history are the authoritative project memory.

Conversation history and model memory are not authoritative.

Before significant work, read these files completely:

1. `docs/MISSION.md`
2. `docs/EVIDENCE_STANDARDS.md`
3. `docs/CURRENT_STATE.md`
4. `docs/NEXT_TASK.md`
5. `docs/ARCHITECTURE.md`
6. `docs/MASTER_PLAN.md`
7. `docs/AI_HANDOFF.md`
8. `docs/README.md`
9. The latest entries in `docs/SESSION_LOG.md`

Read these when relevant:

- `docs/KNOWN_FACTS.md`
- `docs/SOURCE_REGISTRY.md`
- Historical project-state documents

Do not rely on a previous AI conversation when repository documentation provides newer information.

## Document Authority

Each document has one defined responsibility:

- `MISSION.md`: Stable project mission and success criteria
- `EVIDENCE_STANDARDS.md`: Evidence, provenance, citation, confidence, and AI-use rules
- `MASTER_PLAN.md`: Enduring end-to-end roadmap
- `ARCHITECTURE.md`: Current technical structure and data flow
- `CURRENT_STATE.md`: Current verified implementation status
- `NEXT_TASK.md`: One active task only
- `AI_HANDOFF.md`: Recovery context for a new AI session
- `KNOWN_FACTS.md`: Human-reviewed baseline claims and terminology
- `SOURCE_REGISTRY.md`: Known and potential evidence sources
- `SESSION_LOG.md`: Chronological development history
- `README.md`: Documentation index
- Dated project-state files: Historical snapshots only

When documents conflict:

1. Evidence rules in `EVIDENCE_STANDARDS.md` take priority
2. The current task in `NEXT_TASK.md` takes priority over historical tasks
3. Current implementation status in `CURRENT_STATE.md` takes priority over dated snapshots
4. The technical structure in `ARCHITECTURE.md` takes priority over old chat descriptions
5. Ask the user before resolving a serious unresolved contradiction

## Current Active Priority

The current active priority is:

**Reconnect Existing Automated Evidence Gathering**

Use the existing systems under:

- `agents/discovery/`
- `agents/downloader/`

Do not create a competing `agents/acquisition/` subsystem.

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
Response and Content Validation
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
Existing Processing and Knowledge Engine

The manual directory:

`data/incoming_pdfs/`

is a local development test harness.

Manual file placement is not the final evidence-acquisition workflow.

## Session Start Procedure

At the beginning of a new task:

1. Read the authoritative documentation
2. Run or request `git status --short`
3. Inspect the relevant repository files completely
4. Confirm the active task
5. Confirm the current working-tree state
6. Identify uncommitted changes
7. Identify relevant tests
8. Produce a concise plan
9. Wait for approval before entering Act mode or editing files

For unfamiliar or architectural tasks, begin in Plan mode.

Do not begin implementation before understanding the existing code.

## Required Development Sequence

Every implementation task must follow this sequence:

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

Do not skip directly from a request to a broad rewrite.

## Scope Control

Work on one approved milestone at a time.

Do not:

- Jump to unrelated roadmap phases
- Expand the task without approval
- Modify unrelated modules
- Rewrite several systems simultaneously
- Create speculative infrastructure
- Begin Digital Twin development while acquisition remains incomplete
- Begin reconstruction geometry while evidence gathering remains incomplete
- Begin walkthrough development while the Digital Twin knowledge model remains incomplete
- Start uncontrolled or large-scale crawling

Stop when the approved milestone is complete.

## Inspect Before Editing

Before changing a file:

1. Read the complete current file
2. Identify all imports and callers
3. Identify database tables used
4. Identify inputs and outputs
5. Identify tests
6. Identify whether another file already performs the same responsibility
7. Explain the intended change
8. Wait for approval when the change is architectural or potentially destructive

Never replace a file based only on a partial excerpt.

Never assume a file is obsolete because its purpose is unclear.

## Existing Architecture Must Be Reused

Do not create a new subsystem when an existing subsystem already addresses the same responsibility.

In particular:

- Reuse `agents/discovery/`
- Reuse `agents/downloader/`
- Reuse existing R2 integration
- Reuse the assets table
- Reuse operational queues where appropriate
- Reuse existing processors
- Reuse the current knowledge pipeline
- Reuse citation and provenance architecture
- Reuse verification and relationship components

If replacement is necessary:

1. Audit the existing subsystem
2. Explain why repair is insufficient
3. Document the migration plan
4. Identify affected data and callers
5. Obtain explicit approval
6. Preserve recoverability

## File Editing Rules

Prefer minimal, targeted edits over broad rewrites.

When a complete replacement is required:

- Read the original file completely
- Preserve useful behaviour
- Preserve package-safe imports
- Preserve compatible public functions where practical
- Explain removed behaviour
- Run syntax checks
- Run targeted tests
- Review the complete diff

Do not leave:

- Truncated files
- Unterminated strings
- Unfinished Markdown sections
- Placeholder code presented as complete
- Duplicate functions
- Dead imports
- Unresolved merge markers
- Accidental terminal commands inside source files
- API keys inside files

## Python Rules

The `agents` directory is a Python package.

Use package-qualified internal imports.

Preferred example:

`from agents.knowledge.fact_cleaner import clean_facts`

Run package modules from the repository root using:

`python -m agents.package.module`

Before considering an edited Python file complete, run:

`python -m py_compile path/to/file.py`

When relevant, also run:

- Targeted unit tests
- Targeted integration tests
- The affected module
- Existing health checks

Do not claim success before tests complete.

## Database Safety

Database changes require explicit approval.

Before proposing a schema change:

1. Inspect the live schema
2. Identify all readers and writers
3. Identify constraints and indexes
4. Identify existing data
5. Explain the migration
6. Explain rollback
7. Explain data-loss risk
8. Obtain approval

Do not:

- Drop tables without explicit approval
- Drop columns without explicit approval
- Delete production records without explicit approval
- Rewrite large data sets without a backup plan
- Disable foreign-key protection casually
- Remove uniqueness constraints without analysis
- Assume a schema from documentation alone

Prefer idempotent migrations where practical.

Preserve provenance and referential integrity.

## Evidence Safety

Do not delete or overwrite original evidence.

Do not commit evidence files to Git unless explicitly approved and legally appropriate.

Do not commit:

- PDFs
- Downloaded photographs
- Video files
- Audio files
- OCR image output
- R2 credentials
- Database passwords
- OpenRouter keys
- API tokens
- Archive credentials
- Private keys
- Secret configuration

Preserve:

- Original URLs
- Source identifiers
- File hashes
- R2 object keys
- Pages
- Sheets
- Frames
- Timestamps
- Acquisition dates
- Rights metadata
- Processing methods
- Confidence
- Verification status

## Evidence Interpretation Rules

Do not present an inference as verified evidence.

Distinguish between:

- Direct metadata
- Embedded source text
- OCR-derived text
- Deterministic extraction
- AI-assisted extraction
- AI-generated suggestion
- Human-reviewed conclusion

Page co-occurrence is an association signal.

Page co-occurrence does not prove:

- Causation
- Containment
- Structural dependency
- Design intent
- As-built installation

Several pages from one document are not automatically several independent sources.

Design drawings may represent design intent rather than final as-built conditions.

Preserve contradictions instead of silently overwriting them.

## AI Use Rules

AI may assist with:

- Relevance scoring
- Classification
- Summarisation
- Entity suggestions
- Fact suggestions
- Relationship suggestions
- Image interpretation
- Drawing interpretation
- Contradiction detection
- Research assistance

AI output must:

- Be labelled as AI-assisted or AI-generated
- Retain citations to original evidence
- Preserve provider and model details
- Preserve prompt or prompt-version information where practical
- Remain separate from direct evidence
- Be validated before promotion to authoritative knowledge
- Receive human review for high-impact claims

AI output is not independent historical evidence.

Do not invent missing:

- Dates
- Dimensions
- Names
- Roles
- Locations
- Materials
- Relationships
- Citations
- Source identifiers

## Discovery and Download Safety

Initial discovery and downloader work must use one controlled source and one controlled test file.

Do not begin broad crawling.

Before enabling a source:

1. Review `docs/SOURCE_REGISTRY.md`
2. Review access requirements
3. Review rights and restrictions
4. Review robots or crawling policy where applicable
5. Set a conservative rate limit
6. Test one search
7. Test one permitted download
8. Confirm provenance
9. Confirm deduplication
10. Obtain approval before scaling

Automated discovery does not grant permission to download, reuse, or publish content.

## Testing Rules

Every change requires the smallest relevant test.

Possible checks include:

- `python -m py_compile`
- Targeted module execution
- Targeted database query
- Idempotency test
- Duplicate-prevention test
- R2 upload verification
- Asset-record verification
- Queue-transition verification
- Provenance verification
- Citation verification
- Relationship verification
- `git diff --check`

When testing acquisition:

- Use one approved source
- Use one permitted test URL
- Avoid uncontrolled downloads
- Confirm retries do not duplicate records
- Confirm repeated runs remain safe

## Git Rules

Before editing:

`git status --short`

After editing:

`git diff --check`

Review:

`git diff`

Do not commit automatically.

The user must approve the working result before a commit.

Before staging:

- Verify no secrets are present
- Verify no downloaded evidence is present
- Verify no temporary OCR output is present
- Verify only intended files changed
- Verify targeted tests passed

Use small, meaningful commits.

Push working checkpoints after review.

## Documentation Rules

After a tested milestone:

1. Update `docs/CURRENT_STATE.md`
2. Update `docs/NEXT_TASK.md`
3. Update `docs/AI_HANDOFF.md` if project context changed
4. Update `docs/ARCHITECTURE.md` if structure or data flow changed
5. Update `docs/MASTER_PLAN.md` only if the enduring roadmap changed
6. Add an entry to `docs/SESSION_LOG.md`
7. Run `git diff --check`
8. Review the documentation diff
9. Commit only after approval

Do not place old tasks in `NEXT_TASK.md`.

Do not turn dated project-state files into current status documents.

## Cost Control

OpenRouter usage must remain cost-aware.

Default development model:

- DeepSeek V4 Flash

Escalate only when needed:

- DeepSeek V4 Pro
- Another approved stronger model

Use a stronger model when:

- The default model fails repeatedly
- A complex database migration is required
- A multi-module architectural decision is required
- The task has high data-loss risk
- The default model cannot produce a safe verified plan

Keep tasks focused.

Avoid repeatedly rereading the entire repository.

Start a new Cline task after completing a milestone.

Do not spend API credits on uncontrolled loops.

## Current Task Restrictions

During the current discovery and downloader audit:

- Remain in Plan mode
- Read files only
- Inspect schemas only
- Do not edit code
- Do not change database records
- Do not run migrations
- Do not download evidence
- Do not upload to R2
- Do not create a new acquisition system
- Do not alter the Master Engine Runner
- Do not begin AI enrichment
- Do not begin Digital Twin work
- Stop after producing the audit and minimal repair plan

## Recovery Procedure

If a task, editor session, or conversation is lost:

1. Open the repository
2. Run `git status --short`
3. Inspect recent Git commits
4. Read `docs/README.md`
5. Read `docs/CURRENT_STATE.md`
6. Read `docs/NEXT_TASK.md`
7. Read `docs/AI_HANDOFF.md`
8. Read the latest `docs/SESSION_LOG.md` entry
9. Confirm the current milestone
10. Continue only from documented state

The repository must remain sufficient to continue development without access to previous chat history.