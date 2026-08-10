# World Trade Center Reconstruction Project

<p align="center">
  <img src="https://github.com/user-attachments/assets/8e0099d3-a2a4-468e-a975-e25c5fbdfc26" alt="World Trade Center Evidence Engine" width="100%">
</p>

## Mission

The World Trade Center Reconstruction Project is an evidence-driven historical research and reconstruction platform focused on the original World Trade Center complex (1966-2001).

Its purpose is to discover, collect, preserve, verify, cite, and connect historical evidence — then use that evidence to produce the most historically accurate digital reconstruction of the WTC complex possible, where every major reconstruction element can be traced directly to supporting historical sources.

### The Living Reconstruction Concept

The reconstruction is not a single static model. It is a **living reconstruction** — a time-aware digital twin that can represent the WTC complex at any point in its history:

- **Construction era (1966-1973):** The towers rising from the Hudson River site, steel erection, facade installation
- **Operational era (1973-2001):** The completed complex with tenant spaces, plaza activity, observation deck, Windows on the World
- **Post-1993 bombing:** Repairs and modifications after the basement-level attack

### Two Timeline Model

The project tracks two parallel timelines:

1. **Historical Timeline:** What actually happened — construction milestones, tenant changes, operational events, the 1993 bombing, and the 2001 attacks
2. **Reconstruction Timeline:** What evidence has been acquired and when — the progressive filling of knowledge gaps as the corpus grows

---

## Core Principles

- Evidence over assumptions
- Provenance for every claim
- Traceable citations
- Transparent confidence levels
- Preservation of uncertainty
- Reproducible research workflows
- Human-verifiable historical reconstruction
- Distinction between design intent and as-built conditions

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

## Reconstruction Readiness: ~50%

The project tracks reconstruction readiness across 9 areas of the WTC complex:

| Area | Readiness | Key Evidence |
|---|---|---|
| Site | 35% | NCSTAR references, Wikimedia SVG previews |
| Plaza | 20% | NCSTAR references (limited) |
| Tower A (WTC 1) | 65% | AA20a1 structural sheets (895 PNGs), exterior wall XLS (floors 1-9 + 107-110), floor 96-A database |
| Tower B (WTC 2) | 60% | Exterior wall schedules (floors 1-9), panel schedule (B2, 25MB), floor 75-B database, upper wall AB2/AB3 |
| Concourse | 10% | NCSTAR references (minimal) |
| WTC 3-6 | 0% | No evidence |
| WTC 7 | 55% | WTC7 OEM spec manual, NCSTAR 1-9 |
| Observation Deck | 10% | NCSTAR references (minimal) |
| Windows on the World | 10% | NCSTAR references (minimal) |
| **Overall** | **~50%** | |

### Evidence Corpus

| Category | Files | Size |
|---|---|---|
| NCSTAR engineering reports | 9 PDFs | 520MB |
| NCSTAR visual evidence | 657 images | 2.9GB |
| WTCI drawing books | 14+ ZIPs + texts | Existing |
| Tower A structural sheets (AA20a1) | 895 PNGs | Existing |
| Gerrycan collections | 4 ZIPs | 546MB |
| Exterior wall schedules | Multiple XLS | Existing |
| Site plan SVGs/PNGs | 6 files | Existing |
| **Total** | **~1,577+ files** | **~4.9GB+** |

### What Can Be Modeled Today

- **Tower A structural skeleton** — high confidence (AA20a1 + NCSTAR 1-1)
- **Tower A exterior wall envelope** — high confidence (XLS schedules, floors 1-9 + 107-110)
- **Tower B exterior wall envelope** — medium-high confidence (panel schedule + wall schedules)
- **Construction timeline 1966-1973** — high confidence (NCSTAR 1-1)
- **WTC 7 structural system** — medium-high confidence (OEM specs + NCSTAR 1-9)

### Remaining Critical Blockers

| Blocker | Gap | Impact |
|---|---|---|
| Architectural floor plans | CG-2 | Blocks all interior spatial modeling |
| Site plans | CG-3 | Blocks site-level and plaza modeling |
| Tower B structural sheet PNGs | CG-1 (remaining) | Blocks Tower B structural skeleton |
| Construction photographs | IG-1 | Blocks visual reference and as-built verification |

### Prototype 0.1

At ~65-70% readiness, Prototype 0.1 becomes feasible: structural skeletons of both towers + site footprint + construction timeline + visual reference photographs. This would demonstrate the evidence-to-reconstruction pipeline end-to-end.

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
| `EVIDENCE_GAP_REPORT.md` | All identified evidence gaps |
| `READINESS_50_TO_80_REPLAN.md` | Path from 50% to 80% readiness |
| `ARCHITECTURAL_ACQUISITION_CAMPAIGN.md` | Campaign for CG-2 and CG-3 |
| `GERRYCAN_COLLECTION_ASSESSMENT.md` | Gerrycan collection inventory |
| `SESSION_SUMMARY_2026_08_10.md` | August 10 session summary |

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

Current version: **0.7.0**

Current branch activity reflects the ongoing construction of the World Trade Center Evidence Engine, its supporting evidence-acquisition, provenance, citation, knowledge-graph, and digital-twin systems, and the parallel evidence corpus acquisition campaign for reconstruction readiness.