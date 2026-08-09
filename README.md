# World Trade Center Evidence Engine

<p align="center">
  <img src="https://github.com/user-attachments/assets/8e0099d3-a2a4-468e-a975-e25c5fbdfc26" alt="World Trade Center Evidence Engine" width="100%">
</p>

## Mission

The World Trade Center Evidence Engine is an evidence-driven historical research and reconstruction platform focused on the original World Trade Center complex.

Its purpose is to discover, collect, preserve, verify, cite, and connect historical evidence while maintaining complete provenance, transparency, and traceability.

The long-term goal is to create the most historically accurate evidence-backed digital twin possible, where every major reconstruction element can be traced directly to supporting historical sources.

---

## Core Principles

- Evidence over assumptions
- Provenance for every claim
- Traceable citations
- Transparent confidence levels
- Preservation of uncertainty
- Reproducible research workflows
- Human-verifiable historical reconstruction

---

## Platform Pipeline

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
Evidence-Backed Digital Twin
```

---

## Current Status

### Phase 1 — Foundation & Acquisition Pipeline ✅ Complete

All 16 foundation and acquisition pipeline milestones (M0–M15) are complete. The automated evidence acquisition pipeline is operational under a single orchestrator entry point.

| Milestone | Purpose | Status |
|---|---|---|
| M0 | Pre-flight backup | ✅ |
| M1 | Architecture decisions | ✅ |
| M2 | Source-registry reconciliation | ✅ |
| M3 | Limited writer role | ✅ |
| M4 | First schema migration | ✅ |
| M5 | Package/import repair | ✅ |
| M6 | Source seeding repair | ✅ |
| M7 | Search-request generation | ✅ |
| M8 | Controlled source search | ✅ |
| M9 | Human review & manual promotion | ✅ |
| M10 | Discovery queue repair | ✅ |
| M11 | Downloader schema additions | ✅ |
| M12 | Asset registration & provenance | ✅ |
| M13 | Downloader repair & R2 integration | ✅ |
| M14 | Controlled end-to-end test | ✅ |
| M15 | Orchestrator repair | ✅ |

### Phase 2 — Knowledge Platform Integration ✅ Complete

All 8 knowledge platform milestones (M16–M23) are complete. The acquisition pipeline is integrated with the knowledge engine, AI metadata processing, independent-source verification, and persistent timeline events.

| Milestone | Purpose | Status |
|---|---|---|
| M16 | Knowledge platform import repair | ✅ |
| M17 | Acquisition → knowledge integration | ✅ |
| M18 | Citation provenance integration | ✅ |
| M19 | AI-assisted metadata processing | ✅ |
| M20 | Asset classification & routing | ✅ |
| M21 | Photo processing (OCR + AI) | ✅ |
| M22 | Independent-source verification | ✅ |
| M23 | Timeline event model | ✅ |

### Verified Capabilities

| Capability | Status |
|---|---|
| Package-safe Python invocation (`python -m`) | ✅ |
| Idempotent stage execution (all stages) | ✅ |
| Evidence discovery (Wikimedia Commons) | ✅ |
| Queue lifecycle (pending → in_progress → completed) | ✅ |
| SHA-256 file deduplication | ✅ |
| Content-type detection from HTTP headers | ✅ |
| R2 object storage with provenance | ✅ |
| Asset registration with source_id, file_hash, content_type | ✅ |
| Retrieval-event provenance (asset_sources table) | ✅ |
| AI metadata analysis (OpenRouter) | ✅ |
| Photo OCR (Tesseract + AI description) | ✅ |
| Knowledge extraction (entities, facts) | ✅ |
| Fact cleaning and validation | ✅ |
| Citation loading with asset provenance | ✅ |
| Independent-source verification | ✅ |
| Relationship building (page co-occurrence) | ✅ |
| Timeline events with provenance FKs | ✅ |
| Provenance chain (candidate → discovery → queue → asset → provenance → fact → citation → timeline) | ✅ |

### Architecture Diagram

```text
Sources (sources.json)
    ↓
Source Seeding (agents.discovery.main)
    ↓
Search Request Generation (agents.discovery.build_searches)
    ↓
Candidate Discovery (agents.discovery.find_candidates)
    ↓
Human Review (agents.discovery.manual_promote)
    ↓
Discovery Queue (agents.discovery.queue_discoveries)
    ↓
Downloader (agents.downloader.main)
    ↓
SHA-256 Deduplication & R2 Storage
    ↓
Asset Registration (assets table)
    ↓
Provenance Tracking (asset_sources table)
    ↓
AI Metadata Processing (agents.metadata.ai_analyze)
    ↓
Knowledge Engine (agents.engine.run_engine)
    ├── STEP 1a: Acquisition Asset Processing
    ├── STEP 1b: Local PDF Ingestion
    ├── STEP 2: Citation Loading
    ├── STEP 3: Independent-Source Verification
    ├── STEP 4: Relationship Building
    ├── STEP 5: Timeline Building
    └── STEP 6: Knowledge Graph Build (AI → entities/facts)
```

---

## Phase 3 Planning

The following capabilities are under consideration for Phase 3. This is not a committed roadmap.

### Specialist Processors
- Blueprint processing (drawing numbers, revision tracking)
- Video processing (keyframe extraction, timestamp citations)
- Audio processing (transcription, timestamp citations)
- Route invocation (wiring `route_asset()` into the engine pipeline)

### Evidence Expansion
- Additional evidence sources beyond Wikimedia Commons
- Source-specific search URL templates for deferred sources
- Expanded research search capabilities

### Platform Infrastructure
- API layer for evidence and knowledge access
- Evidence Explorer frontend
- Dashboard enhancements

### Digital Twin Foundations
- Spatial hierarchy modelling (site → building → tower → floor → zone → space)
- Time-aware reconstruction states
- Evidence-backed geometry and materials
- Explorable digital twin viewer

---

## Repository Structure

```text
agents/         Discovery, acquisition, processing, and knowledge agents
dashboard/      Web dashboard for evidence and knowledge exploration
database/       Database schema and migrations (5 migrations)
docs/           Plans, audits, architecture, and project documentation
research/       Research configuration and source definitions
scripts/        Utility scripts and maintenance tools
storage/        Local asset storage (development)
```

---

## Technology Stack

- Python 3
- PostgreSQL (with 5 idempotent migrations)
- Tesseract OCR
- OpenRouter AI (DeepSeek V4 Flash)
- R2 Object Storage
- Docker (PostgreSQL, pgAdmin)

---

## Documentation

Key project documents in `docs/`:

| Document | Purpose |
|---|---|
| `MISSION.md` | Stable project charter |
| `EVIDENCE_STANDARDS.md` | Evidence governance rules |
| `MASTER_PLAN.md` | Enduring end-to-end roadmap |
| `ARCHITECTURE.md` | Current technical architecture |
| `CURRENT_STATE.md` | Current implementation status |
| `NEXT_TASK.md` | Single active task |
| `AI_HANDOFF.md` | Recovery context for new AI sessions |
| `SESSION_LOG.md` | Chronological development history |
| `DEVLOG.md` | Public-facing development journal |
| `KNOWN_FACTS.md` | Human-reviewed baseline claims |
| `SOURCE_REGISTRY.md` | Known and potential evidence sources |

Project development follows a structured workflow:

```text
Audit → Plan → Review → Implement → Verify → Document → Commit
```

---

## Research Focus

The project covers the original World Trade Center complex, including:

- Twin Towers (WTC 1 & WTC 2)
- Supporting buildings
- Plaza areas
- Observation facilities
- Restaurants
- Retail spaces
- Transportation infrastructure
- Structural systems
- Architectural elements
- Construction history
- Operational history
- Changes over time

The project is not limited to the Twin Towers and aims to model the wider World Trade Center complex as a connected historical environment.

---

## Evidence Standards

Every major claim, fact, relationship, reconstruction element, or historical assertion should be:

- Supported by evidence where available
- Linked to sources
- Linked to citations
- Assigned confidence levels
- Open to verification
- Open to challenge
- Traceable back to original material

Evidence remains the source of truth.

---

## Status

This repository is under active development. Phase 1 (M0–M15) and Phase 2 (M16–M23) are complete.

Current version: **0.6.0**

Current branch activity reflects the ongoing construction of the World Trade Center Evidence Engine and its supporting evidence-acquisition, provenance, citation, knowledge-graph, and digital-twin systems.