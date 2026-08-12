# World Trade Center Reconstruction Project — Current State

## Last Updated

August 12, 2026

## Purpose

This document provides a concise and current status of the World Trade Center Reconstruction Project, including the Evidence Engine, World Model seed datasets, and Phase 2 Database Design Preparation.

## Current Overall State

- **Phase 1 World Model Construction Phase:** **✅ COMPLETE**. 164 verified unique entities and 82 master relationships cataloged across 6 vertical anchor elevations (-3.5m to +410.0m). Minimum Viable World Model (MVWM) target milestone passed (+14 entities over threshold).
- **Phase 2 Database Design Preparation Phase:** **🔄 OPEN (Active Phase)**. Currently executing Task 2.1 (Spatial Geometry & 3D Coordinate Specification) following [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md) and [`docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md).

## Reconstruction Readiness: ~75% (Direct-Evidence Verified Baseline)

The project tracks reconstruction readiness across 9 areas of the WTC complex:

| Area | Readiness | Key Evidence |
|---|---|---|
| Site | 40% | Foundation plans, site plan SVGs |
| Plaza | 25% | Site context from architectural drawings |
| **Tower A (WTC 1)** | **95%** | **211 architectural blueprints + Phase 1 extractions (A-A-18, A-A-19, A-A-20, A-A-31, A-A-121, A-A-130, A-A-145)** |
| Tower B (WTC 2) | 40% | ST-01..06 structural PNG extractions + exterior wall schedules |
| **Concourse** | **90%** | **Sub-level architectural plans (A-A-18)** |
| WTC 3-6 | 0% | No evidence |
| WTC 7 | 60% | WTC7 OEM spec manual, NCSTAR 1-9 |
| **Observation Deck** | **95%** | **107th Floor architectural plans (A-A-145)** |
| **Windows on the World** | **95%** | **107th Floor restaurant plans (A-A-145)** |
| **Overall** | **~75%** | **Direct-Evidence Verified Baseline Readiness** |

### Evidence Corpus & Seed Datasets

| Category | Files | Size |
|---|---|---|
| Tower A architectural blueprints | 211 PNGs | 119MB |
| Tower A structural sheets (AA20a1) | 895 PNGs | Existing |
| Derived Tower B structural extractions | 12 PNGs | 2.5MB |
| Machine-readable seed JSON datasets | 7 JSONs | `data/*.json` (164 verified entities, 82 relationships) |
| NCSTAR engineering reports | 9 PDFs | 520MB |
| NCSTAR visual evidence | 657 images | 2.9GB |
| WTCI drawing books | 14+ ZIPs + texts | Existing |
| Gerrycan collections | 4 ZIPs | 546MB |
| Exterior wall schedules | Multiple XLS | Existing |
| Site plan SVGs/PNGs | 6 files | Existing |
| **Total** | **~1,807+ files** | **~5.0GB+** |

### Gap Status

| ID | Gap | Status |
|---|---|---|
| CG-1 | Tower B Structural Drawings | ⚠️ 40% Direct Evidence Baseline — ST-01..06 PNG extractions complete (20 entities verified). |
| CG-2 | Architectural Floor Plans | ✅ Phase 1 Complete — A-A-18, 19, 20, 31, 121, 130, 145 extractions complete (144 WTC 1 entities verified, 82 master relationships). |
| CG-3 | Site Plan & Plaza | ❌ Open — blocks site-level and plaza modeling |
| CG-4 | Tower A Upper Wall Schedules | ✅ Closed — AB2/AB3 XLS covers floors 107-110 |
| Operational | PostgreSQL DB Ingestion | 🔄 Phase 2 Active — Seed JSON datasets generated and validated; PostgreSQL PostGIS DDL schema design in preparation under `WORLD_MODEL_SPECIFICATION_V1.md`. |
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