# World Trade Center Reconstruction Project — Current State

## Last Updated

August 10, 2026

## Purpose

This document provides a concise and current status of the World Trade Center Reconstruction Project, including both the Evidence Engine platform and the parallel evidence corpus acquisition campaign.

It records:

- What is implemented and tested
- What exists but still requires verification
- What is currently being worked on
- What remains planned
- Current reconstruction readiness
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

The evidence-processing and knowledge-engine foundation is working. Phase 1 (M0–M15) and Phase 2 (M16–M23) are complete.

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

The external evidence-gathering pipeline is operational and tested end-to-end.

## Reconstruction Readiness: ~73% (Direct-Evidence Verified Baseline)

In parallel with the Evidence Engine platform, a major evidence extraction and World Model population campaign is underway. The project tracks reconstruction readiness across 9 areas:

| Area | Readiness | Key Evidence |
|---|---|---|
| Site | 40% | Foundation plans, site plan SVGs |
| Plaza | 25% | Site context from architectural drawings |
| Tower A (WTC 1) | 90% | 211 architectural blueprints + Phase 1 extractions (A-A-19, A-A-20, A-A-130) |
| Tower B (WTC 2) | 40% | ST-01..06 structural PNG extractions + exterior wall schedules |
| Concourse | 30% | Sub-level architectural plans |
| WTC 3-6 | 0% | No evidence |
| WTC 7 | 60% | WTC7 OEM spec manual, NCSTAR 1-9 |
| Observation Deck | 95% | 107th Floor architectural plans |
| Windows on the World | 95% | 107th Floor restaurant plans |
| **Overall** | **~73%** | **Direct-Evidence Verified Baseline Readiness** |

### Evidence Corpus

| Category | Files | Size |
|---|---|---|
| Tower A architectural blueprints | 211 PNGs | 119MB |
| Tower A structural sheets (AA20a1) | 895 PNGs | Existing |
| Derived Tower B structural extractions | 12 PNGs | 2.5MB |
| Machine-readable seed JSON datasets | 6 JSONs | `data/*.json` |
| NCSTAR engineering reports | 9 PDFs | 520MB |
| NCSTAR visual evidence | 657 images | 2.9GB |
| WTCI drawing books | 14+ ZIPs + texts | Existing |
| Gerrycan collections | 4 ZIPs | 546MB |
| Exterior wall schedules | Multiple XLS | Existing |
| Site plan SVGs/PNGs | 6 files | Existing |
| **Total** | **~1,806+ files** | **~5.0GB+** |

### Gap Status

| ID | Gap | Status |
|---|---|---|
| CG-1 | Tower B Structural Drawings | ⚠️ 40% Direct Evidence Baseline — ST-01..06 PNG extractions complete (20 entities verified). |
| CG-2 | Architectural Floor Plans | 🔄 Phase 1 In Progress — A-A-19, A-A-20, A-A-130 extractions complete (65 entities verified, 109 relationships). |
| CG-3 | Site Plan & Plaza | ❌ Open — blocks site-level and plaza modeling |
| CG-4 | Tower A Upper Wall Schedules | ✅ Closed — AB2/AB3 XLS covers floors 107-110 |
| Operational | PostgreSQL DB Ingestion | 🔄 In Progress — Seed JSON datasets generated and validated; SQL migration scripts prepared for execution against `wtc_evidence`. |
| IG-1 | Construction Photographs | ⚠️ NCSTAR 1-8 only (657 images, damage-focused) |
| IG-2 | Interior Photographs | ⚠️ NCSTAR 1-8 only (limited) |
| IG-3 | Buildings 3-7 Documentation | ⚠️ WTC7 specs only |
| IG-4 | MEP Drawings | ❌ Open |
| IG-5 | Architectural Elevations | ❌ Open |
| IG-6 | Foundation Documentation | ❌ Open |

### Key Planning Documents

| Document | Purpose |
|---|---|
| `docs/READINESS_50_TO_80_REPLAN.md` | Recalculated path from 50% to 80% (supersedes original 35% baseline) |
| `docs/ARCHITECTURAL_ACQUISITION_CAMPAIGN.md` | Dedicated campaign for CG-2 and CG-3 — 11 sources ranked |
| `docs/GERRYCAN_COLLECTION_ASSESSMENT.md` | Gerrycan collection inventory and readiness impact |
| `docs/SESSION_SUMMARY_2026_08_10.md` | August 10 session summary |

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
- ✅ Citation-to-asset provenance (M18)

### Fact Verification

- ✅ Evidence-based Fact Verification v2
- ✅ Claim status for facts without source records
- ✅ Supported status for facts with one source record
- ✅ Well-supported status for facts with two source records
- ✅ Verified status for facts with three or more source records
- ✅ Operational confidence scoring

### Relationships and Knowledge Graph

- ✅ Seed relationship builder
- ✅ Automatic page-co-occurrence relationship mining
- ✅ Relationship deduplication
- ✅ Relationship evidence counts
- ✅ Relationship confidence scoring
- ✅ Relationship source-method attribution
- ✅ Relationship Search v2
- ✅ Relationship provenance display

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

### Engine Operations

- ✅ Master Engine Runner
- ✅ Citation loading in the engine workflow
- ✅ Fact verification in the engine workflow
- ✅ Relationship rebuilding in the engine workflow
- ✅ Timeline generation in the engine workflow
- ✅ Engine Health Report
- ✅ Knowledge Graph Build (STEP 6)

### Acquisition Pipeline

- ✅ Source seeding (idempotent)
- ✅ Search request generation
- ✅ Candidate discovery (Wikimedia Commons)
- ✅ Manual promotion
- ✅ Discovery queue (lease/claim pattern)
- ✅ Downloader (SHA-256, content-type, dedup)
- ✅ R2 storage
- ✅ Asset registration
- ✅ Asset source provenance
- ✅ AI metadata processing (OpenRouter)
- ✅ Asset classification & routing
- ✅ Photo processing (OCR + AI)
- ✅ Orchestrator (package-safe, 6 stages)
- ✅ End-to-end test (M14)

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

Status: 🧪 **Working Test Harness**

Component: `agents/ingestion/automated_ingestion.py`

This is not the finished automated evidence-acquisition workflow. The completed engine must discover and acquire evidence through the existing discovery and downloader systems without requiring permanent manual file placement.

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
- ✅ Discovery queue creation
- 🟡 URL normalisation
- 🟡 URL deduplication
- ✅ Discovery diagnostics and exports

### Downloader and Storage

- ✅ Discovery-queue consumption
- ✅ HTTP response validation
- ✅ Content-type validation
- ✅ File downloading
- ✅ File-hash calculation
- ✅ File-hash deduplication
- ✅ R2 upload from the downloader
- ✅ Asset creation from downloaded evidence
- ✅ Acquisition failure handling
- 🟡 Retry handling
- ✅ Metadata queue creation
- 🟡 Processing-queue creation

### Classification and Routing

- ✅ Asset classification integration
- ✅ Classification confidence
- 🟡 Routing integration
- 🟡 Routed processor invocation
- 🟡 Processing-status updates
- 🟡 Failure routing

### Specialist Processing

- ✅ Photo processing
- ✅ Image metadata extraction
- ✅ Image OCR
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
- ✅ Metadata-analysis components
- 🟡 Vision-analysis components
- 🟡 R2-to-analysis retrieval
- ✅ AI-provider abstraction

## Current Active Priority

🔄 **Architectural Evidence Acquisition Campaign**

Closing CG-2 (Architectural Floor Plans) and CG-3 (Site Plans) — the two largest remaining blockers.

The authoritative campaign plan is:

- `docs/ARCHITECTURAL_ACQUISITION_CAMPAIGN.md`

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

## Planned Major Capabilities

The following capabilities remain planned:

- ⬜ Scheduled evidence discovery
- ⬜ Source-specific archive connectors
- ⬜ Reliable acquisition retry queues
- ⬜ Failure recovery
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
- ⬜ Living reconstruction with historical state transitions

## Current Database Foundation

### Confirmed Knowledge Tables

- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`
- `timeline_events`

### Known or Expected Operational Tables

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `asset_sources`
- `metadata_queue`
- `ai_analysis`

## Current Development Rule

Do not begin the Digital Twin Layer or create a new acquisition architecture until the existing discovery and downloader pipeline has been audited, repaired, and tested end to end.

Do not ingest evidence into the database. Do not modify code. Do not modify the database schema. The current phase is evidence corpus acquisition and planning only.