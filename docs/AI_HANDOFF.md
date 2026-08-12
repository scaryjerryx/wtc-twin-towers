# AI Handoff: World Trade Center Reconstruction Project

## Purpose of This Document

This document provides the essential context required for an AI development assistant to continue work on the World Trade Center Reconstruction Project safely and accurately.

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

Build an automated, transparent, citation-backed evidence engine capable of supporting the most historically accurate digital reconstruction of the original World Trade Center complex (1966-2001).

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
15. Enable a living reconstruction with time-aware historical states

Evidence takes priority over assumptions.

Artificial intelligence may assist with processing and interpretation, but artificial intelligence must not become an uncited source of historical truth.

## Reconstruction Vision

### Living Reconstruction

The reconstruction is not a single static model. It is a **living reconstruction** — a time-aware digital twin that can represent the WTC complex at any point in its history:

- **Construction era (1966-1973):** The towers rising, steel erection, facade installation
- **Operational era (1973-2001):** Completed complex with tenant spaces, plaza, observation deck, Windows on the World
- **Post-1993 bombing:** Repairs and modifications

### Two Timeline Model

1. **Historical Timeline:** What actually happened — construction milestones, tenant changes, operational events, 1993 bombing, 2001 attacks
2. **Reconstruction Timeline:** What evidence has been acquired and when — progressive filling of knowledge gaps

## C## Reconstruction Readiness: ~75% (Direct-Evidence Verified Baseline)

| Area | Readiness |
|---|---|
| Site | 40% |
| Plaza | 25% |
| Tower A (WTC 1) | 95% |
| Tower B (WTC 2) | 40% |
| Concourse | 90% |
| WTC 3-6 | 0% |
| WTC 7 | 60% |
| Observation Deck | 95% |
| Windows on the World | 95% |
| **Overall** | **~75%** |

### Evidence Corpus & Structured Seed Outputs

- Tower A architectural blueprints: 211 PNGs (119MB)
- Tower A structural sheets (AA20a1): 895 PNGs
- Derived Tower B structural extractions: 12 PNGs (ST-01..06) in `WTC_CORPUS/derived/`
- Machine-readable seed JSON datasets: 7 JSONs in `data/` (`aa18_world_model_seed.json`, `aa19_world_model_seed.json`, `aa20_world_model_seed.json`, `aa31_world_model_seed.json`, `aa121_world_model_seed.json`, `aa130_world_model_seed.json`, `aa145_world_model_seed.json`, `wtc1_world_model_v1.json`, `tower_b_world_model_validated.json`)
- NCSTAR engineering reports: 9 PDFs (520MB)
- NCSTAR visual evidence: 657 images (2.9GB)
- WTCI drawing books: 14+ ZIPs + texts
- Gerrycan collections: 4 ZIPs (546MB)
- Exterior wall schedules: Multiple XLS
- Site plan SVGs/PNGs: 6 files
- **Total: ~1,807+ files, ~5.0GB+ (164 Verified Unique Entities & 82 Master Relationships)**

### Gap & Execution Status

| ID | Gap | Status |
|---|---|---|
| CG-1 | Tower B Structural Drawings | ⚠️ 40% Direct Evidence Baseline — ST-01..06 extractions complete (20 entities verified) |
| CG-2 | Architectural Floor Plans | ✅ Phase 1 Complete — A-A-18, 19, 20, 31, 121, 130, 145 extractions complete (144 WTC 1 entities verified, 82 master relationships) |
| CG-3 | Site Plan & Plaza | ❌ Open |
| CG-4 | Tower A Upper Wall Schedules | ✅ Closed — AB2/AB3 XLS covers floors 107-110 |
| Operational | PostgreSQL DB Ingestion | 🔄 Phase 2 Active — Seed JSON files written & validated; PostgreSQL PostGIS DDL schema design in preparation under `WORLD_MODEL_SPECIFICATION_V1.md` |

### Key Session Handoff Documents (August 12, 2026 Milestone)

- `docs/PHASE_1_WORLD_MODEL_COMPLETION.md` — Official phase closure and handoff report
- `docs/WORLD_MODEL_SPECIFICATION_V1.md` — Authoritative World Model specification v1.0
- `docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md` — Entity & relationship governance rules
- `docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md` — Authoritative roadmap for Phase 2 Database Design Preparation
- `docs/CANONICAL_WORLD_MODEL_REVIEW.md` — Approved 6-tier spatial hierarchy review
- `data/wtc1_world_model_v1.json` — Consolidated master seed dataset (114 WTC 1 unique entities)
- `data/tower_b_world_model_validated.json` — Verified Tower B structural seed dataset (20 entities)ON.md` — Audit and validation report

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

### Provenance and Citations

Working components include:

- Source-file attribution
- Source-page attribution
- `fact_sources`
- Fact-source deduplication
- Citation table
- Citation Loader
- Citation deduplication
- Citation-to-asset provenance (M18)

### Entity Resolution

Working components include:

- Entity alias table
- Alias seeding
- Canonical-name resolution
- Canonical entity creation
- Alias relationship reassignment
- Entity Resolution v2

### Fact Verification

Working components include:

- Evidence-based Fact Verification v2
- Fact confidence updates
- Verification-status updates

Current operational rules:

- Zero source records: `claim`, confidence 50
- One source record: `supported`, confidence 70
- Two source records: `well_supported`, confidence 85
- Three or more source records: `verified`, confidence 95

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

### Timeline

Working component:

- Timeline Builder v2

### Acquisition Pipeline

Working components include:

- Source seeding (idempotent)
- Search request generation
- Candidate discovery (Wikimedia Commons)
- Manual promotion
- Discovery queue (lease/claim pattern)
- Downloader (SHA-256, content-type, dedup)
- R2 storage
- Asset registration
- Asset source provenance
- AI metadata processing (OpenRouter)
- Asset classification & routing
- Photo processing (OCR + AI)
- Orchestrator (package-safe, 6 stages)
- End-to-end test (M14)

### Engine Operations

Working components include:

- Master Engine Runner
- Citation loading
- Fact verification
- Relationship rebuilding
- Timeline generation
- Engine Health Report
- Knowledge Graph Build (STEP 6)

## Confirmed Database Foundation

Primary database: `wtc_evidence`

Confirmed knowledge tables include:

- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`
- `timeline_events`

Known or expected operational tables include:

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `asset_sources`
- `metadata_queue`
- `ai_analysis`

## Writer Role

The `wtc_writer` role exists in `wtc_evidence` with:

- `LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE INHERIT NOREPLICATION`
- `USAGE ON SCHEMA public`
- `INSERT` on `sources`, `search_candidates`, `discoveries`, `assets`, `metadata_queue`, `asset_sources`
- `INSERT, UPDATE` on `discovery_queue`
- `USAGE, SELECT` on relevant sequences
- No DELETE, no DDL, no ownership, no superuser

Credentials are stored in `.secrets/wtc_writer.env` (not committed to Git).

## Current Active Task

The single active task is:

**Architectural Evidence Acquisition Campaign**

Closing CG-2 (Architectural Floor Plans) and CG-3 (Site Plans).

The authoritative task definition is:

- `docs/NEXT_TASK.md`

The authoritative campaign plan is:

- `docs/ARCHITECTURAL_ACQUISITION_CAMPAIGN.md`

## Current Phase Rules

- Do not ingest evidence into the database
- Do not modify code
- Do not modify the database schema
- Focus on evidence corpus acquisition and planning only
- Produce analysis documents, not implementation

## Milestone Progress

- ✅ **M0 – Pre-flight backup** — Complete and passed.
- ✅ **M1 – Architecture decisions** — Complete and approved.
- ✅ **M2 – Source-registry reconciliation** — Complete.
- ✅ **M3 – Limited writer role** — Complete.
- ✅ **M4 – First small schema migration** — Complete.
- ✅ **M5 – Package/import repair** — Complete.
- ✅ **M6 – Source seeding repair** — Complete.
- ✅ **M7 – Search-request generation** — Complete.
- ✅ **M8 – Controlled source search** — Complete.
- ✅ **M9 – Human review and manual promotion** — Complete.
- ✅ **M10 – Discovery queue** — Complete.
- ✅ **M11 – Downloader schema additions** — Complete.
- ✅ **M12 – Asset registration & provenance** — Complete.
- ✅ **M13 – Downloader repair & R2 integration** — Complete.
- ✅ **M14 – Controlled end-to-end test** — Complete.
- ✅ **M15 – Orchestrator repair** — Complete.
- ✅ **M16 – Knowledge platform import repair** — Complete.
- ✅ **M17 – Acquisition → Knowledge Pipeline Integration** — Complete.
- ✅ **M18 – Citation Provenance Integration** — Complete.
- ✅ **M19 – AI-Assisted Metadata Processing** — Complete.
- ✅ **M20 – Asset Classification & Routing** — Complete.
- ✅ **M21 – Photo Processing** — Complete.
- ✅ **M22 – Independent-Source Verification** — Complete.
- ✅ **M23 – Timeline Event Model** — Complete.

## Current Strategic Boundary

Do not begin:

- Digital Twin schema development
- Reconstruction geometry
- Walkthrough development
- Large-scale crawling
- Broad AI enrichment
- Unrelated database redesign

until the architectural evidence acquisition campaign is complete and the existing discovery and downloader pipeline has been audited, repaired, and tested end to end.

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