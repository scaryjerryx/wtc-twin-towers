# World Trade Center Reconstruction Project

<p align="center">
  <img src="https://github.com/user-attachments/assets/8e0099d3-a2a4-468e-a975-e25c5fbdfc26" alt="World Trade Center Reconstruction Platform" width="100%">
</p>

## Mission

The World Trade Center Reconstruction Project is building a **historically accurate, evidence-backed, browser-based, interactive reconstruction of the World Trade Center** — a living historical platform where every major reconstruction element can be traced directly to supporting historical sources.

The project exists to preserve, reconstruct, cite, and share the architectural legacy of one of the most important building complexes of the 20th century.

---

## What We Are Building

| Component | Role |
|-----------|------|
| **Reconstruction Platform** | The product. A browser-based 3D experience of the WTC complex. |
| **World Model** | The core asset. A structured, time-aware, evidence-backed digital representation. |
| **Evidence Engine** | The supporting system. Automated discovery, acquisition, processing, and citation. |

The Evidence Engine builds the World Model. The World Model powers the Reconstruction Platform. The Reconstruction Platform delivers the public experience.

---

## Core Principles

- Evidence over assumptions
- Provenance for every claim
- Traceable citations
- Transparent confidence levels
- Preservation of uncertainty
- Browser-first accessibility (no installation required)
- AI as a development tool, not a runtime dependency

---

## Reconstruction Readiness: ~65-70%

The project tracks reconstruction readiness across 9 areas of the WTC complex:

| Area | Readiness | Key Evidence |
|---|---|---|
| Site | 40% | Foundation plans, site plan SVGs |
| Plaza | 25% | Site context from architectural drawings |
| **Tower A (WTC 1)** | **85%** | **211 architectural blueprints + AA20a1 structural sheets** |
| Tower B (WTC 2) | 65% | Exterior wall schedules, applicable Tower A floor plans |
| Concourse | 30% | Sub-level architectural plans |
| WTC 3-6 | 0% | No evidence |
| WTC 7 | 60% | WTC7 OEM spec manual, NCSTAR 1-9 |
| **Observation Deck** | **95%** | **107th Floor architectural plans** |
| **Windows on the World** | **95%** | **107th Floor restaurant plans** |
| **Overall** | **~65-70%** | |

### Evidence Corpus

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

### What Can Be Reconstructed Today

- **Tower A complete architectural layout** — all 110 floors + 5 sub-levels (211 blueprints)
- **Windows on the World** — full restaurant layout (107th Floor)
- **Observation Deck** — complete deck layout (107th Floor)
- **Sky Lobby 44** — full lobby layout
- **All mechanical floors** — 7-8, 41-42, 75-76, 108-109
- **All elevator zones** — 26 elevator/escalator drawings
- **Tower A structural skeleton** — AA20a1 structural sheets
- **Foundation and sub-levels** — Sub-Levels 1-5

### Remaining Critical Blockers

| Blocker | Gap | Impact |
|---|---|---|
| Sky Lobby 78 drawings | CG-2 (remaining) | Upper zone vertical circulation |
| Tower B architectural drawings | CG-2 (Tower B) | Tower B interior modeling |
| Site plans | CG-3 | Site-level and plaza modeling |
| Construction photographs | IG-1 | Visual reference and as-built verification |

### Prototype 0.1

At ~65-70% readiness, Prototype 0.1 is now **enabled**: Tower A structural + architectural model with special spaces, evidence citations, and construction timeline.

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

All 8 knowledge platform milestones (M16–M23) are complete.

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
- Architectural evidence acquisition campaign (CG-2, CG-3)

### Platform Infrastructure
- API layer for evidence and knowledge access
- Evidence Explorer frontend
- Dashboard enhancements

### Digital Twin Foundations
- Spatial hierarchy modelling (site → building → tower → floor → zone → space)
- Time-aware reconstruction states
- Evidence-backed geometry and materials
- Explorable digital twin viewer
- Living reconstruction with historical state transitions

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
WTC_CORPUS/     Evidence corpus (excluded from source control)
```

---

## Technology Stack

### Evidence Engine (Current)
- Python 3
- PostgreSQL (with 5 idempotent migrations)
- Tesseract OCR
- OpenRouter AI (DeepSeek V4 Flash)
- R2 Object Storage
- Docker (PostgreSQL, pgAdmin)

### Reconstruction Platform (Target)
- **PostgreSQL** — World Model database
- **API Layer** — REST/GraphQL serving world data
- **Next.js** — Application shell and routing
- **React Three Fiber** — Browser-based 3D rendering
- **Evidence Citation System** — Click-to-cite overlay

**Browser-first.** No installation. No app store. Works on desktop, tablet, and mobile.

---

## Documentation

Key project documents in `docs/`:

| Document | Purpose |
|---|---|
| `PROJECT_VISION_2026.md` | **NEW** — Complete project vision and strategic direction |
| `RECONSTRUCTION_PLATFORM_VISION.md` | **NEW** — Browser-based platform definition |
| `WORLD_MODEL_ARCHITECTURE.md` | **NEW** — World Model schema and API design |
| `HISTORICAL_TIMELINE_EXPERIENCE.md` | **NEW** — Time-release construction journey |
| `TOWER_A_ARCHITECTURAL_CORPUS_ASSESSMENT.md` | **NEW** — 211-drawing blueprint assessment |
| `ARCHITECTURAL_READINESS_UPDATE.md` | **NEW** — Readiness recalculation |
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
| `EVIDENCE_GAP_REPORT.md` | All identified evidence gaps |

Project development follows a structured workflow:

```text
Audit → Plan → Review → Implement → Verify → Document → Commit
```

---

## Research Focus

The project covers the original World Trade Center complex, including:

- Twin Towers (WTC 1 & WTC 2)
- Supporting buildings (WTC 3-7)
- Austin J. Tobin Plaza
- Underground concourse and transportation infrastructure
- Observation Deck (WTC 1, floor 107)
- Windows on the World restaurant (WTC 1, floor 107)
- Structural systems (columns, spandrels, core, exterior wall)
- Architectural elements (elevations, cladding, lobbies)
- Construction history (1966-1973)
- Operational history (1973-2001)
- 1993 bombing damage and repairs
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

Current version: **0.8.0**

**August 11, 2026 — Strategic Milestone:** The Tower A architectural corpus (211 blueprints) has been acquired and assessed. CG-2 (Architectural Floor Plans) is substantially closed for Tower A. The project has shifted from "Can reconstruction be done?" to "How should reconstruction be represented and experienced?"

---

## FINAL VISION

A user opens a browser. They walk through the plaza, concourse, towers, restaurants, observation deck, and office floors. They travel through time from 1966 to 2001. They click any element and see the evidence that supports it. They understand how confident the reconstruction is.

Every major reconstruction element can explain where it came from, what evidence supports it, and how confident the reconstruction is.

This is not merely a model. This is a living historical reconstruction platform.
