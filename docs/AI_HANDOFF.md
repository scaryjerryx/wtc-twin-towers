# AI Handoff: World Trade Center Evidence Engine

## Purpose of This Document

This document provides the essential context required for an AI development assistant to continue work on the World Trade Center Evidence Engine safely and accurately.

The repository documentation and Git history are the authoritative project memory.

Conversation history is not authoritative project memory.

Before making significant changes, read:

- `docs/MISSION.md`
- `docs/EVIDENCE_STANDARDS.md`
- `docs/MASTER_PLAN.md`
- `docs/ARCHITECTURE.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `.clinerules`

## Project Mission

Build an automated, transparent, citation-backed evidence engine capable of supporting the most historically accurate digital reconstruction of the original World Trade Center complex.

The completed system must:

1. Discover relevant historical evidence automatically
2. Download and register permitted evidence
3. Prevent duplicate URL and file storage
4. Store evidence in R2
5. Register evidence as database assets
6. Classify and route evidence
7. Process PDFs, photographs, drawings, video, audio, and records
8. Extract entities, facts, events, sources, and relationships
9. Preserve source, page, sheet, frame, and timestamp provenance
10. Create research citations
11. Verify claims and preserve contradictions
12. Build a searchable knowledge graph
13. Support an evidence-backed digital twin
14. Support an evidence-linked historical walkthrough

Evidence takes priority over assumptions.

Artificial intelligence may assist with processing and interpretation, but artificial intelligence must not become an uncited source of historical truth.

## Critical Acquisition Requirement

The final engine must not depend on permanent manual evidence uploads.

The local PDF incoming folder is a development and testing mechanism only.

The intended acquisition path is:

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

The repository already contains acquisition foundations under:

- `agents/discovery/`
- `agents/downloader/`

Do not create a competing `agents/acquisition/` subsystem.

Inspect and reuse the existing systems unless a documented audit proves that replacement is necessary.

## Current Working Foundation

### Package and Runtime

- Python package structure under `agents/`
- Package-qualified internal imports
- Root `requirements.txt`
- Python virtual environment
- PostgreSQL database
- R2 integration foundation
- Tesseract OCR
- Poppler PDF rendering
- Git checkpoint workflow

### PDF and OCR Processing

Working components include:

- Embedded PDF text extraction
- OCR fallback for scanned PDFs
- PDF-page rendering
- Whole-document OCR extraction
- Page-level OCR extraction
- Source-page preservation
- PDF analyser
- PDF knowledge pipeline

Primary file:

- `agents/processors/pdf_text_extractor.py`

Important functions include:

- `extract_with_pypdf2()`
- `extract_with_ocr()`
- `extract_pages()`
- `extract_text()`

### Knowledge Extraction

Working components include:

- Known-entity extraction
- Engineering fact extraction
- Drawing-book extraction
- Column-type extraction
- Spandrel-type extraction
- Strut-type extraction
- Section-reference extraction
- Exterior-wall reference extraction
- Explicit year-reference extraction
- Fact normalisation
- Fact cleaning
- Fact deduplication

Important files include:

- `agents/knowledge/knowledge_extractor.py`
- `agents/knowledge/fact_normalizer.py`
- `agents/knowledge/fact_cleaner.py`
- `agents/knowledge/pdf_knowledge_pipeline.py`
- `agents/knowledge/knowledge_pipeline.py`

### Provenance and Citations

Working components include:

- Source-file attribution
- Source-page attribution
- `fact_sources`
- Fact-source deduplication
- Citation table
- Citation Loader
- Citation deduplication

Important file:

- `agents/knowledge/citation_loader.py`

Current provenance path:

Facts
↓
Fact Sources
↓
Citations

The `fact_sources` table is the authoritative scalable fact-provenance model.

Legacy `source_file` and `source_page` fields may remain in `facts` for compatibility.

### Entity Resolution

Working components include:

- Entity alias table
- Alias seeding
- Canonical-name resolution
- Canonical entity creation
- Alias relationship reassignment
- Entity Resolution v2

Important file:

- `agents/knowledge/entity_resolution.py`

Database support:

- `entity_aliases`

### Fact Verification

Working components include:

- Evidence-based Fact Verification v2
- Fact confidence updates
- Verification-status updates

Important file:

- `agents/verification/fact_verifier.py`

Current operational rules:

- Zero source records: `claim`, confidence 50
- One source record: `supported`, confidence 70
- Two source records: `well_supported`, confidence 85
- Three or more source records: `verified`, confidence 95

Important limitation:

Source-record count is not necessarily independent-source count.

Several pages from one document may currently increase verification strength without representing independent evidence.

### Relationships

Working components include:

- Seed relationships
- Page-co-occurrence relationship mining
- Relationship deduplication
- Relationship evidence counts
- Relationship confidence scoring
- Relationship source methods
- Relationship Search v2
- Relationship provenance display

Important files include:

- `agents/knowledge/relationship_builder.py`
- `agents/knowledge/fact_relationship_builder.py`
- `agents/search/relationship_search.py`

Current automatically generated relationship types include:

- `appears_in`
- `associated_with`

Current automatic source method:

- `page_cooccurrence`

Important limitation:

Page co-occurrence indicates an association signal.

Page co-occurrence does not prove causation, containment, structural dependency, or design intent.

### Timeline

Working component:

- Timeline Builder v2

Important file:

- `agents/timeline/timeline_builder.py`

Current behaviour:

- Accepts explicit referenced-year facts
- Rejects engineering identifiers that merely resemble years
- Displays confidence
- Displays verification status
- Displays available source provenance

Current limitation:

The timeline does not yet represent a complete historical event model.

### Local PDF Processing Test Harness

Working component:

- `agents/ingestion/automated_ingestion.py`

Current directories:

- `data/incoming_pdfs/`
- `data/processed_pdfs/`
- `data/failed_pdfs/`

This component processes manually supplied PDFs and moves successful or failed files into the appropriate directory.

This is a test harness.

This is not the final automated evidence-gathering workflow.

### Engine Operations

Working components include:

- Master Engine Runner
- Citation loading
- Fact verification
- Relationship rebuilding
- Timeline generation
- Engine Health Report

Important files include:

- `agents/engine/run_engine.py`
- `agents/engine/health_report.py`

The current Master Engine Runner operates the existing local processing workflow.

The Master Engine Runner does not yet run a verified end-to-end external discovery and downloader pipeline.

## Confirmed Database Foundation

Primary database:

- `wtc_evidence`

Confirmed knowledge tables include:

- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`

Known or expected operational tables include:

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `metadata_queue`
- `ai_analysis`

The discovery, downloader, asset, and queue schemas must be audited before integration changes are made.

Known constraints include:

- `unique_fact`
- `unique_fact_source`
- `unique_relationship`
- Citation uniqueness protection
- Entity-name uniqueness protection

Do not assume undocumented schema details.

Inspect the live PostgreSQL schema before proposing migrations.

## Tested Evidence

The scanned engineering document:

- `WTCI-000721-L.PDF`

was used to validate:

- OCR across 39 pages
- Page-level extraction
- Entity extraction
- Engineering fact extraction
- Fact normalisation
- Fact cleaning
- Fact provenance
- Citation loading
- Fact verification
- Relationship mining
- Relationship confidence
- Relationship search
- Timeline filtering
- Master engine execution
- Engine health reporting

This source document is test evidence.

Do not commit the PDF to Git.

## Components Requiring Audit

The following areas must not be treated as complete merely because files or database tables exist.

### Discovery

- Trusted-source seeding
- Search generation
- Candidate creation
- Candidate relevance assessment
- Candidate promotion
- Discovery creation
- Discovery queue creation
- URL normalisation
- URL deduplication
- Discovery exports and diagnostics

### Downloader and Storage

- Discovery-queue consumption
- HTTP response validation
- Content-type validation
- File downloading
- File hashing
- File-hash deduplication
- R2 upload from the downloader
- Asset registration
- Failure handling
- Retry handling
- Metadata queue creation
- Processing queue creation

### Classification and Routing

- Asset classification
- Classification confidence
- Routing
- Processor invocation
- Processing-status updates
- Failure routing

### Specialist Processing

- Photograph processing
- Image OCR
- Blueprint processing
- Drawing-number and revision extraction
- Video processing
- Keyframe extraction
- Timestamp citations
- Audio transcription
- Audio timestamp citations

### Additional Search and Analysis

- General query engine
- Graph-search components
- Metadata-analysis components
- Vision-analysis components
- R2 analysis retrieval
- AI-provider abstraction

## Current Active Task

The single active task is:

**Reconnect Existing Automated Evidence Gathering**

The authoritative task definition is:

- `docs/NEXT_TASK.md`

## Milestone Progress

- ✅ **M0 – Pre-flight backup** — Complete and passed.
- ✅ **M1 – Architecture decisions** — Complete and approved.
- ✅ **M2 – Source-registry reconciliation** — Complete.
- ✅ **M3 – Limited writer role** — Complete. Role `wtc_writer` created with least-privilege grants on approved tables and sequences. Catalog verification passed. Runtime verification revealed additional SELECT privileges may be required for some operational queries; this will be addressed in a later milestone if necessary.
- ✅ **M4 – First small schema migration** — Complete.
- ✅ **M5 – Package/import repair** — Complete. An M5 regression (unqualified import in `main.py`) was discovered during the M6 audit and repaired as part of M6 implementation.
- ✅ **M6 – Source seeding repair** — Complete. Source seeding is now idempotent with URL upsert support, accurate per-row status reporting, module-relative path resolution, and all-or-nothing transaction safety.
- 🔄 **M7 – Search-request generation** — Current active milestone.

## Writer Role

The `wtc_writer` role exists in `wtc_evidence` with:

- `LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION`
- `USAGE ON SCHEMA public`
- `INSERT` on `sources`, `search_candidates`, `discoveries`, `assets`, `metadata_queue`
- `INSERT, UPDATE` on `discovery_queue`
- `USAGE, SELECT` on `sources_id_seq`, `search_candidates_id_seq`, `discoveries_id_seq`, `discovery_queue_id_seq`, `assets_id_seq`, `metadata_queue_id_seq`
- No DELETE, no DDL, no ownership, no superuser, no default privileges
- No `asset_sources` grants (deferred to M12)

Credentials are stored in `.secrets/wtc_writer.env` (not committed to Git).

## Development Assistant Workflow

Current development tooling:

- Cline
- OpenRouter
- DeepSeek V4 Flash
- Server-side VS Code
- SSH localhost tunnel
- Plan mode before Act mode
- Approval-controlled edits and commands
- Cline checkpoints

The repository documentation and Git history are the authoritative project memory.

AI chat memory is not authoritative project memory.

## Required Development Process

Every task must follow this sequence:

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

## Non-Negotiable Rules

- Inspect before editing
- Work on one milestone at a time
- Read complete files before replacing them
- Prefer targeted changes over broad rewrites
- Reuse existing architecture
- Do not create duplicate systems
- Require explicit approval for database changes
- Do not delete evidence
- Do not commit downloaded evidence
- Do not commit secrets or API keys
- Do not run destructive commands without approval
- Do not commit automatically
- Do not treat AI output as historical evidence
- Do not allow AI suggestions to overwrite cited evidence
- Run targeted tests after each change
- Review `git diff` after each change
- Update documentation only after tests pass
- Stop when the approved milestone is complete

## AI Use Within the Evidence Engine

AI may later assist with:

- Evidence relevance scoring
- Classification
- Document summarisation
- Structured fact suggestions
- Entity suggestions
- Relationship suggestions
- Image interpretation
- Drawing interpretation
- Contradiction detection
- Research assistance

AI output must:

- Be labelled as AI-assisted or AI-generated
- Retain citations to source evidence
- Preserve provider and model details
- Preserve prompt or prompt-version information
- Be validated before storage as authoritative knowledge
- Remain separate from direct evidence
- Be subject to human review for high-impact claims

## Before Starting a New Development Session

A new AI session must:

1. Read the authoritative documentation
2. Read `.clinerules`
3. Inspect the relevant repository files
4. Confirm the current task
5. Confirm the working-tree status
6. Produce a plan
7. Wait for approval before editing

The initial prompt should explicitly prohibit:

- File edits
- Database changes
- New architecture
- Destructive commands
- Automatic commits

## Current Strategic Boundary

Do not begin:

- Digital Twin schema development
- Reconstruction geometry
- Walkthrough development
- Large-scale crawling
- Broad AI enrichment
- Unrelated database redesign

until the existing discovery and downloader pipeline has been audited, repaired, and tested end to end.

## Recovery Procedure

If a development conversation is lost:

1. Open the repository
2. Check `git status`
3. Read the authoritative documentation
4. Read the latest entries in `docs/SESSION_LOG.md`
5. Read `docs/NEXT_TASK.md`
6. Inspect the latest Git commits
7. Continue only from the documented active milestone

The repository must remain sufficient to continue development without access to previous chat history.