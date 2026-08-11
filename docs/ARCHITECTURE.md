# World Trade Center Reconstruction Project — Architecture

## Purpose

This document describes the technical architecture of the World Trade Center Reconstruction Project, including the Evidence Engine (current), the World Model (core asset), and the Reconstruction Platform (target).

For the complete project vision, see:

- `docs/PROJECT_VISION_2026.md`

For the reconstruction platform definition, see:

- `docs/RECONSTRUCTION_PLATFORM_VISION.md`

For the World Model architecture, see:

- `docs/WORLD_MODEL_ARCHITECTURE.md`

For the historical timeline experience, see:

- `docs/HISTORICAL_TIMELINE_EXPERIENCE.md`

For the enduring roadmap, see:

- `docs/MASTER_PLAN.md`

For current implementation status, see:

- `docs/CURRENT_STATE.md`

## System Architecture Overview

The project consists of three major systems:

```
EVIDENCE ENGINE (Current — Operational)
        ↓
    Builds and populates
        ↓
WORLD MODEL (Core Asset — Being designed)
        ↓
    Powers
        ↓
RECONSTRUCTION PLATFORM (Target — Browser-based 3D experience)
```

| System | Role | Status |
|--------|------|--------|
| **Evidence Engine** | Automated discovery, acquisition, processing, and knowledge extraction | ✅ Operational |
| **World Model** | Operational Seed Data Tier — Machine-Readable Data Output Layer (65 Verified Entities) | 🔧 Operational Seed Data |
| **Reconstruction Platform** | Browser-based 3D experience with evidence citations | 📋 Planned |

### Key Architectural Decision

**AI is a development tool, not a runtime dependency.**

AI systems (Claude, Gemini, future multimodal models) assist with blueprint interpretation, evidence understanding, and code generation during development. The final Reconstruction Platform must function without requiring an active AI model.

## Architectural Principles

The architecture must follow these principles:

1. Evidence must remain traceable to its original source.
2. Automated gathering must reuse the existing discovery and downloader systems.
3. Manual incoming directories are development test harnesses, not the final acquisition workflow.
4. Duplicate URLs, files, facts, citations, and relationships must be controlled.
5. Deterministic extraction must remain distinguishable from AI-assisted interpretation.
6. AI output must not become an uncited source of truth.
7. Existing subsystems must be inspected before replacement systems are introduced.
8. Database changes require explicit review and migration planning.
9. Processing stages should be idempotent where practical.
10. Every working milestone must be tested, documented, reviewed, committed, and pushed.
11. The Reconstruction Platform must be browser-first with no installation required.
12. The World Model is the core asset — the Evidence Engine serves it, the Platform consumes it.

## High-Level Data Flow

```text
Historical Sources
        ↓
Discovery
        ↓
Acquisition
        ↓
Assets & Provenance
        ↓
AI Analysis
        ↓
OCR & Text Extraction
        ↓
Knowledge Extraction (Entities, Facts)
        ↓
Citations
        ↓
Independent-Source Verification
        ↓
Relationships
        ↓
Timeline Events
        ↓
World Model Population
        ↓
API Layer
        ↓
Reconstruction Platform (React Three Fiber)
```

## Reconstruction Platform (Target)

The Reconstruction Platform is the browser-based 3D experience that is the product of the project.

### Target Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **World Database** | PostgreSQL | Structured WTC world model |
| **API Layer** | TBD (Python/Node.js) | Serve world data to frontend |
| **Frontend Framework** | Next.js | Application shell and routing |
| **3D Rendering** | React Three Fiber | Browser-based 3D reconstruction |
| **Evidence System** | Custom | Citation lookup and display |

### Browser-First Requirements

- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Android Chrome)
- Tablet browsers
- No installation required
- No downloadable client
- No app-store dependency

### Spatial Hierarchy

```
World Trade Center Complex
 └── Site (16-acre superblock)
      ├── Building (WTC 1, WTC 2, WTC 3, WTC 4, WTC 5, WTC 6, WTC 7)
      │    └── Tower
      │         └── Floor
      │              ├── Zone (Core, Tenant, Mechanical, Service)
      │              └── Space (Office, Corridor, Elevator, Stairwell, Lobby, Restroom)
      ├── Plaza (Austin J. Tobin Plaza)
      │    └── Concourse (Underground mall, PATH station, subway connections)
      └── Infrastructure (Transportation, utilities, services)
```

### Evidence Citation System

Every reconstruction element supports evidence lookup:

```
Reconstruction Element (Wall, Column, Room)
        ↓
Evidence Reference (Blueprint, Photo, Report)
        ↓
Source (Organization, Archive, Collection)
        ↓
Confidence (Verified, Supported, Inferred)
        ↓
Provenance (Acquisition date, URL, file hash)
```

### Historical Timeline Experience

The public experiences the WTC as a construction journey released over 35 days:

- Day 1 (1966) → Day 35 (2001)
- Users can travel backward but not forward
- After Day 35, full timeline unlocks as permanent archive

### Current Reconstruction Readiness: ~73% (Direct-Evidence Verified Baseline)

| Area | Readiness |
|---|---|
| Site | 40% |
| Plaza | 25% |
| **Tower A (WTC 1)** | **90%** |
| Tower B (WTC 2) | 40% |
| Concourse | 30% |
| WTC 3-6 | 0% |
| WTC 7 | 60% |
| **Observation Deck** | **95%** |
| **Windows on the World** | **95%** |
| **Overall** | **~73%** |

## Current Integration Boundary

The processing and knowledge layers have been tested using a scanned engineering PDF.

The external evidence-gathering path is operational and tested end-to-end (M14).

The current integration task is:

Configured Sources
↓
Existing Discovery Layer
↓
Existing Downloader Layer
↓
R2 and Asset Registration
↓
Processing Queues
↓
Existing Processing and Knowledge Engine

No competing `agents/acquisition/` system should be created.

# Discovery Layer

## Location

`agents/discovery/`

## Purpose

Discover potentially relevant evidence from configured historical and archive sources.

## Known Components

The repository contains components such as:

- `agents/discovery/main.py`
- `agents/discovery/database.py`
- `agents/discovery/discover.py`
- `agents/discovery/build_searches.py`
- `agents/discovery/build_real_searches.py`
- `agents/discovery/find_candidates.py`
- `agents/discovery/promote_searches.py`
- `agents/discovery/manual_promote.py`
- `agents/discovery/queue_discoveries.py`
- `agents/discovery/export_candidates.py`
- `agents/discovery/export_discoveries.py`
- `agents/discovery/sources.json`

## Intended Flow

`sources.json`
↓
Sources Table
↓
Search Requests (`record_type = 'search_request'`)
↓
Evidence Candidates (`record_type = 'evidence_candidate'`)
↓
Candidate Review or Promotion
↓
Discoveries
↓
Discovery Queue

## Search-Candidate Representation

`search_candidates` distinguishes two record types via a `record_type` field:

- `search_request` — a generated query URL for one source and target
- `evidence_candidate` — a returned evidence URL produced by executing a search request

A search request is not the same thing as a returned evidence URL.

Legacy tables `discovered_urls` and `search_history` are preserved as read-only legacy data and are excluded from the new operational path.

## Current Status

**Operational** — tested end-to-end in M14.

# Downloader Layer

## Location

`agents/downloader/`

## Known Components

- `agents/downloader/main.py`
- `agents/downloader/r2.py`
- `agents/downloader/register_asset.py`
- `agents/downloader/test_r2.py`

## Purpose

Convert queued discoveries into stored and registered evidence assets.

## Intended Flow

Discovery Queue
↓
Download Request
↓
Response and Content Validation
↓
File Hashing
↓
Duplicate Detection
↓
R2 Upload
↓
Asset Record
↓
Metadata and Processing Queue

## Current Status

**Operational** — tested end-to-end in M14.

# Storage Layer

## R2 Object Storage

R2 is intended to store acquired evidence files.

Each stored object should be associated with:

- Object key
- Original file name
- Original URL
- Source organisation
- MIME type
- File size
- File hash
- Acquisition date
- Rights information
- Asset identifier
- Processing status

## PostgreSQL

Primary database:

`wtc_evidence`

PostgreSQL stores:

- Discovery records
- Operational queues
- Asset metadata
- Analysis output
- Entities
- Facts
- Provenance
- Citations
- Relationships
- Verification status
- Aliases
- Timeline events

# Asset and Queue Layer

## Assets

The asset registry represents acquired evidence.

Expected fields include:

- Asset identifier
- Original URL
- Source identifier
- R2 object key
- File name
- File type
- File hash
- Classification
- Acquisition status
- Processing status
- Creation timestamp
- Update timestamp

## Asset Sources (Retrieval Events)

`asset_sources` records retrieval-event provenance for assets.

One `asset_sources` row = one retrieval event.

Expected fields include:

- `asset_id`
- `source_id`
- `original_url`
- `normalised_url`
- `final_effective_url`
- `retrieved_at`
- `created_at`

A second row represents a separate retrieval event or a separately discovered source reference. Two rows are not expected merely because `original_url` and `final_effective_url` differ.

## Queues

Known or intended queues include:

- Discovery queue
- Metadata queue
- Processing queues
- Failure queues
- Retry queues

Queue records should support:

- Status
- Attempt count
- Last error
- Last attempt
- Next retry
- Creation timestamp
- Update timestamp

## Current Status

**Operational** — tested end-to-end in M14.

# Classification Layer

## Location

`agents/classification/`

## Known Component

`agents/classification/asset_classifier.py`

## Purpose

Determine the evidence type and assign a classification confidence.

## Expected Types

- Photograph
- Blueprint
- Floor plan
- Architectural drawing
- Engineering drawing
- PDF
- Report
- Document
- Newspaper
- Map
- Video
- Audio
- Unknown

## Current Status

**Operational** — M20 complete.

# Routing Layer

## Location

`agents/router/`

## Known Component

`agents/router/route_asset.py`

## Purpose

Route classified assets to specialist processors.

## Current Status

**Requires verification** — routing invocation deferred.

# Processing Layer

## Location

`agents/processors/`

## PDF Text Extractor

File: `agents/processors/pdf_text_extractor.py`

Status: **Working**

## PDF Analyzer

File: `agents/processors/pdf_analyzer.py`

Status: **Working**

## PDF Processor

File: `agents/processors/pdf_processor.py`

Status: **Requires integration verification**

## Photo Processor

File: `agents/processors/photo_processor.py`

Status: **Working** — M21 complete (Tesseract OCR + AI description + entity/fact extraction)

## Blueprint Processor

File: `agents/processors/blueprint_processor.py`

Status: **Requires repository verification**

# Metadata and AI Analysis Layer

## Location

`agents/metadata/`

## Components

- `agents/metadata/ai_analyze.py` — Provider-selectable metadata processing
- `agents/metadata/ai_client.py` — OpenRouter API client
- `agents/metadata/vision_analyze.py`
- `agents/metadata/vision_client.py`
- `agents/metadata/r2_download.py`
- `agents/metadata/mock_analyze.py` — Mock fallback

## Current Status

**Operational** — M19 complete.

# Knowledge Layer

## Location

`agents/knowledge/`

## Knowledge Extractor

File: `agents/knowledge/knowledge_extractor.py`

Status: **Working for current test documents**

## Fact Normalizer

File: `agents/knowledge/fact_normalizer.py`

Status: **Working**

## Fact Cleaner

File: `agents/knowledge/fact_cleaner.py`

Status: **Working**

## PDF Knowledge Pipeline

File: `agents/knowledge/pdf_knowledge_pipeline.py`

Status: **Working**

## General Knowledge Pipeline

File: `agents/knowledge/knowledge_pipeline.py`

Status: **Working for its current input source**

## Entity Resolution

File: `agents/knowledge/entity_resolution.py`

Status: **Working**

## Fact Relationship Builder

File: `agents/knowledge/fact_relationship_builder.py`

Status: **Working**

## Citation Loader

File: `agents/knowledge/citation_loader.py`

Status: **Working** — M18 complete (citation-to-asset provenance)

## Knowledge Graph Builder

File: `agents/knowledge/knowledge_graph_builder.py`

Status: **Working** — M21 complete (STEP 6 in engine)

# Verification Layer

## Location

`agents/verification/`

## Fact Verifier

File: `agents/verification/fact_verifier.py`

Status: **Working**

Current operational rules:

- Zero sources: claim, confidence 50
- One source: supported, confidence 70
- Two sources: well supported, confidence 85
- Three or more sources: verified, confidence 95

# Search Layer

## Location

`agents/search/`

## Relationship Search v2

File: `agents/search/relationship_search.py`

Status: **Working**

## Additional Search Components

- `agents/search/query_engine.py`
- `agents/search/graph_search.py`

Status: **Requires verification**

# Timeline Layer

## Location

`agents/timeline/`

## Timeline Builder

File: `agents/timeline/timeline_builder.py`

Status: **Working** — M23 complete.

# Engine Orchestration Layer

## Location

`agents/engine/`

## Master Engine Runner

File: `agents/engine/run_engine.py`

Current workflow:

1. STEP 1a: Acquisition Asset Processing
2. STEP 1b: Local PDF Ingestion
3. STEP 2: Citation Loading
4. STEP 3: Independent-Source Verification
5. STEP 4: Relationship Building
6. STEP 5: Timeline Building
7. STEP 6: Knowledge Graph Build

Status: **Working**

## Engine Health Report

File: `agents/engine/health_report.py`

Status: **Working**

# Database Architecture

## Primary Database

`wtc_evidence`

## Known Core Tables

Known knowledge and operational tables include:

- `sources`
- `assets`
- `asset_sources`
- `metadata_queue`
- `ai_analysis`
- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`
- `timeline_events`
- `search_candidates`
- `discoveries`
- `discovery_queue`

## Evidence Corpus

The evidence corpus is stored in `WTC_CORPUS/` (excluded from source control via `.gitignore`).

| Category | Files | Size |
|---|---|---|
| Tower A architectural blueprints | 211 PNGs | 119MB |
| Tower A structural sheets (AA20a1) | 895 PNGs | Existing |
| NCSTAR engineering reports | 9 PDFs | 520MB |
| NCSTAR visual evidence | 657 images | 2.9GB |
| WTCI drawing books | 14+ ZIPs + texts | Existing |
| Gerrycan collections | 4 ZIPs | 546MB |
| Exterior wall schedules | Multiple XLS | Existing |
| Site plan SVGs/PNGs | 6 files | Existing |
| **Total** | **~1,788+ files** | **~5.0GB+** |
