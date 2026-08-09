# World Trade Center Evidence Engine Current State

## Last Updated

August 9, 2026

## Purpose

This document provides a concise and current status of the World Trade Center Evidence Engine.

It records:

- What is implemented and tested
- What exists but still requires verification
- What is currently being worked on
- What remains planned
- The immediate next milestone

For the enduring roadmap, see:

- `docs/MASTER_PLAN.md`

For the current technical architecture, see:

- `docs/ARCHITECTURE.md`

For the single active task, see:

- `docs/NEXT_TASK.md`

## Status Definitions

- ✅ **Working**: Implemented and tested during development
- 🟡 **Requires Verification**: Code or schema exists, but current end-to-end behaviour must be confirmed
- 🔄 **In Progress**: Current active development priority
- ⬜ **Planned**: Required but not yet implemented
- 🧪 **Test Harness**: Working development mechanism, but not the finished production workflow
- 📚 **Historical**: Retained for project history, but not current operational guidance

## Current Overall State

The evidence-processing and knowledge-engine foundation is working.

The engine has successfully processed a scanned 39-page engineering PDF and demonstrated:

- OCR
- Page-level extraction
- Entity extraction
- Engineering fact extraction
- Fact normalisation
- Fact cleaning
- Fact deduplication
- Source-file provenance
- Source-page provenance
- Citation loading
- Evidence-based fact verification
- Relationship mining
- Relationship confidence scoring
- Relationship search
- Timeline filtering
- Engine health reporting

The external evidence-gathering pipeline is not yet confirmed as working end to end.

The immediate priority is to inspect, reconnect, test, and complete the existing discovery and downloader systems.

## Working Components

### Package and Runtime Foundation

- ✅ Python package structure under `agents/`
- ✅ Package-qualified internal imports
- ✅ Root `requirements.txt`
- ✅ Python virtual environment
- ✅ PostgreSQL connection
- ✅ R2 integration foundation
- ✅ Tesseract OCR
- ✅ Poppler PDF rendering
- ✅ Git checkpoint workflow

### PDF and OCR Processing

- ✅ Embedded PDF text extraction
- ✅ Detection of insufficient embedded text
- ✅ OCR fallback for scanned PDFs
- ✅ PDF-page rendering
- ✅ Whole-document OCR extraction
- ✅ Page-level OCR extraction
- ✅ Source-page preservation
- ✅ PDF analyser
- ✅ PDF knowledge pipeline
- ✅ Scanned engineering PDF test completed successfully

### Knowledge Extraction

- ✅ Known-entity extraction
- ✅ Engineering fact extraction
- ✅ Drawing-book extraction
- ✅ Column-type extraction
- ✅ Spandrel-type extraction
- ✅ Strut-type extraction
- ✅ Section-reference extraction
- ✅ Exterior-wall reference extraction
- ✅ Explicit year-reference extraction
- ✅ Fact normalisation
- ✅ Fact cleaning
- ✅ Fact deduplication
- ✅ Canonical fact storage

### Entity Resolution

- ✅ Entity alias table
- ✅ Alias seeding
- ✅ Canonical entity creation
- ✅ Alias resolution
- ✅ Relationship reassignment during entity merging
- ✅ Entity Resolution v2

### Provenance and Citations

- ✅ Source-file attribution
- ✅ Source-page attribution
- ✅ `fact_sources` provenance table
- ✅ Fact-source deduplication constraint
- ✅ Citation table
- ✅ Citation Loader
- ✅ Citation deduplication
- ✅ Fact-to-source traceability

### Fact Verification

- ✅ Evidence-based Fact Verification v2
- ✅ Claim status for facts without source records
- ✅ Supported status for facts with one source record
- ✅ Well-supported status for facts with two source records
- ✅ Verified status for facts with three or more source records
- ✅ Operational confidence scoring

Current limitation:

Source-record count is not yet the same as independent-source count.

Several pages from one document may currently increase verification strength without representing independent evidence.

### Relationships and Knowledge Graph

- ✅ Seed relationship builder
- ✅ Automatic page-co-occurrence relationship mining
- ✅ Relationship deduplication
- ✅ Relationship evidence counts
- ✅ Relationship confidence scoring
- ✅ Relationship source-method attribution
- ✅ Relationship Search v2
- ✅ Relationship provenance display

Current limitation:

Page co-occurrence establishes an association signal.

Page co-occurrence does not prove causation, containment, structural dependency, or design intent.

### Timeline and Search

- ✅ Timeline Builder v2
- ✅ Rejection of engineering identifiers that resemble years
- ✅ Relationship search
- ✅ Relationship confidence display
- ✅ Relationship evidence-count display
- ✅ Fact confidence display
- ✅ Verification-status display
- ✅ Supporting source-file display
- ✅ Supporting source-page display

Current limitation:

Timeline extraction currently depends on explicit date-oriented fact patterns and does not yet represent a complete historical event model.

### Engine Operations

- ✅ Master Engine Runner
- ✅ Citation loading in the engine workflow
- ✅ Fact verification in the engine workflow
- ✅ Relationship rebuilding in the engine workflow
- ✅ Timeline generation in the engine workflow
- ✅ Engine Health Report

### Development Workflow

- ✅ Repository documentation designated as project memory
- ✅ Cline installed in the server-side VS Code environment
- ✅ Cline accessed through an SSH localhost tunnel
- ✅ OpenRouter configured
- ✅ DeepSeek V4 Flash selected for initial planning and routine development
- ✅ Plan-first workflow adopted
- ✅ File edits and commands remain approval-controlled
## Working Development Test Harness

### Automated Local PDF Processing

Status:

🧪 **Working Test Harness**

Component:

`agents/ingestion/automated_ingestion.py`

Current behaviour:

- Reads PDFs from `data/incoming_pdfs/`
- Processes each PDF
- Moves successful files to `data/processed_pdfs/`
- Moves failed files to `data/failed_pdfs/`
- Rebuilds fact relationships after processing

Important:

This is not the finished automated evidence-acquisition workflow.

The completed engine must discover and acquire evidence through the existing discovery and downloader systems without requiring permanent manual file placement.

## Components Requiring Verification

The following components are documented or present in the repository, but their current end-to-end behaviour must be inspected before they are marked working.

### Discovery

- ✅ Trusted-source seeding
- ✅ Source database integration
- ✅ Search-definition generation
- ✅ Source-specific search generation
- ✅ Search-candidate creation
- 🟡 Candidate relevance assessment
- ✅ Candidate promotion
- ✅ Manual candidate promotion
- ✅ Discovery records
- 🟡 Discovery queue creation
- 🟡 URL normalisation
- 🟡 URL deduplication
- ✅ Discovery diagnostics and exports

### Downloader and Storage

- 🟡 Discovery-queue consumption
- 🟡 HTTP response validation
- 🟡 Content-type validation
- 🟡 File downloading
- 🟡 File-hash calculation
- 🟡 File-hash deduplication
- 🟡 R2 upload from the downloader
- 🟡 Asset creation from downloaded evidence
- 🟡 Acquisition failure handling
- 🟡 Retry handling
- 🟡 Metadata queue creation
- 🟡 Processing-queue creation

### Classification and Routing

- 🟡 Asset classification integration
- 🟡 Classification confidence
- 🟡 Routing integration
- 🟡 Routed processor invocation
- 🟡 Processing-status updates
- 🟡 Failure routing

### Specialist Processing

- 🟡 Photo processing
- 🟡 Image metadata extraction
- 🟡 Image OCR
- 🟡 Blueprint and drawing processing
- 🟡 Drawing-number and revision extraction
- 🟡 Video processing
- 🟡 Video keyframe extraction
- 🟡 Video timestamp citations
- 🟡 Audio processing
- 🟡 Audio transcription
- 🟡 Audio timestamp citations

### Additional Search and Analysis

- 🟡 General query engine
- 🟡 Graph-search components
- 🟡 Metadata-analysis components
- 🟡 Vision-analysis components
- 🟡 R2-to-analysis retrieval
- 🟡 AI-provider abstraction

These components must not be marked complete solely because files or database tables exist.

## Current Active Priority

🔄 **Reconnect Existing Automated Evidence Gathering**

Use the existing systems under:

- `agents/discovery/`
- `agents/downloader/`

Do not create a competing acquisition subsystem.

## Milestone Progress

- ✅ **M0 – Pre-flight backup** — Complete and passed.
- ✅ **M1 – Architecture decisions** — Complete and approved.
- ✅ **M2 – Source-registry reconciliation** — Complete.
- ✅ **M3 – Limited writer role** — Complete. Role `wtc_writer` created with least-privilege grants on approved tables and sequences. Catalog verification passed. Runtime verification revealed additional SELECT privileges may be required for some operational queries; this will be addressed in a later milestone if necessary.
- ✅ **M4 – First small schema migration** — Complete. `discovery_queue` gained `discovery_id`, `attempt_count`, `last_error`, and `next_retry` columns. `search_candidates` gained a unique constraint.
- ✅ **M5 – Package/import repair** — Complete. `agents/discovery/main.py` import changed to package-qualified form. An M5 regression (unqualified import) was discovered during the M6 audit and repaired as part of M6 implementation.
- ✅ **M6 – Source seeding repair** — Complete. Source seeding is now idempotent with URL upsert support, accurate per-row status reporting, module-relative path resolution, and all-or-nothing transaction safety. Package-safe execution verified.
- ✅ **M7 – Search-request generation** — Complete. Search requests generated for 3 sources with verified search URL templates into `search_candidates` with `record_type = 'search_request'`. Idempotent via `ON CONFLICT DO NOTHING` backed by the M4 unique constraint. Legacy NULL `record_type` rows corrected. 4 sources deferred pending verified search URL templates. Package-safe execution verified.
- ✅ **M8 – Controlled source search** — Complete. One controlled source search executed (Wikimedia Commons, "World Trade Center Plaza"). 20 evidence URL candidates extracted and stored in `search_candidates` with `record_type = 'evidence_candidate'`. Idempotent via `ON CONFLICT DO NOTHING` backed by the M4 unique constraint. `discoveries` and `discovery_queue` confirmed untouched. Package-safe execution verified.
- ✅ **M9 – Human review and manual promotion** — Complete. `manual_promote.py` rewritten to read `evidence_candidate` rows from `search_candidates` and promote approved candidates into the canonical `discoveries` table with status `'approved'`. Package-safe imports, transaction safety, command-line ID selection, and application-level idempotency (query filters to `record_type='evidence_candidate' AND status='pending'` plus SELECT-before-INSERT). `export_candidates.py` updated with `--type` filtering. `export_discoveries.py` updated to read from `discoveries`. Two candidates promoted and verified. No schema changes.
- 🔄 **M10 – Discovery queue** — Next active milestone.

The intended flow is:

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
File Hashing and Deduplication
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

The first step is a read-only, file-by-file and schema-aware audit.

The authoritative implementation instructions are maintained in:

- `docs/NEXT_TASK.md`

## Planned Major Capabilities

The following capabilities remain planned after automated evidence gathering is operational:

- ⬜ Scheduled evidence discovery
- ⬜ Source-specific archive connectors
- ⬜ Reliable acquisition retry queues
- ⬜ Failure recovery
- ⬜ Independent-source verification
- ⬜ Contradiction management
- ⬜ AI-assisted relevance classification
- ⬜ AI-assisted document summarisation
- ⬜ AI-assisted fact suggestions
- ⬜ AI-assisted relationship suggestions
- ⬜ Evidence-linked image analysis
- ⬜ Evidence-linked drawing interpretation
- ⬜ Video keyframe and timestamp processing
- ⬜ Audio transcription and timestamp citations
- ⬜ Expanded research search
- ⬜ Research review interface
- ⬜ Digital Twin knowledge schema
- ⬜ Building and tower modelling
- ⬜ Floor, zone, and space modelling
- ⬜ Time-aware reconstruction states
- ⬜ Evidence-backed geometry
- ⬜ Evidence-backed materials and objects
- ⬜ Explorable digital twin
- ⬜ Evidence-linked historical walkthrough

## Current Database Foundation

### Confirmed Knowledge Tables

- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`

### Known or Expected Operational Tables

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `metadata_queue`
- `ai_analysis`

The operational discovery, downloader, asset, and queue schemas must be inspected before further integration work.

## Current Evidence Test

The scanned engineering document:

`WTCI-000721-L.PDF`

was used to validate:

- OCR across 39 pages
- Page-level text extraction
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

This source document is test evidence and should not be committed to Git.

## Immediate Next Milestone

The next milestone is M9 – Human review and manual promotion.

Review the 20 evidence candidates produced by M8 and manually promote approved candidates into the canonical `discoveries` table.

The next milestone is complete when:

1. Evidence candidates from M8 are reviewed
2. Approved candidates are promoted to `discoveries`
3. `discovery_queue` remains untouched during promotion
4. Package-safe execution is verified
5. Targeted tests pass
6. Documentation is updated
7. The Git diff is reviewed

## Current Development Rule

Do not begin the Digital Twin Layer or create a new acquisition architecture until the existing discovery and downloader pipeline has been audited, repaired, and tested end to end.