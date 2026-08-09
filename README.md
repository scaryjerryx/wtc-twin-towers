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
Processing
        ↓
Evidence & Knowledge Graph
        ↓
Evidence-Backed Digital Twin
```

The platform is being developed to support:

- Automated evidence discovery
- Source validation
- Historical document processing
- Image processing
- OCR and text extraction
- Citation generation
- Fact extraction
- Entity extraction
- Provenance tracking
- Relationship analysis
- Knowledge graph construction
- Evidence-backed reconstruction workflows

---

## Current Status

### Acquisition Pipeline Phase — Complete

All 16 foundation and acquisition pipeline milestones (M0–M15) have been implemented, tested, and verified end-to-end.

The automated evidence acquisition pipeline is operational under a single orchestrator entry point.

| Milestone | Purpose |
|---|---|
| M0 | Pre-flight backup |
| M1 | Architecture decisions |
| M2 | Source-registry reconciliation |
| M3 | Limited writer role |
| M4 | First schema migration |
| M5 | Package/import repair |
| M6 | Source seeding repair |
| M7 | Search-request generation |
| M8 | Controlled source search |
| M9 | Human review & manual promotion |
| M10 | Discovery queue repair |
| M11 | Downloader schema additions |
| M12 | Asset registration & provenance |
| M13 | Downloader repair & R2 integration |
| M14 | Controlled end-to-end test |
| M15 | Orchestrator repair |

### Verified Acquisition Pipeline

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
Metadata Processing (agents.metadata.mock_analyze)
```

### What Has Been Verified

| Capability | Status |
|---|---|
| Package-safe Python invocation (`python -m`) | ✅ |
| Idempotent stage execution (all 6 automated stages) | ✅ |
| Queue lifecycle (pending → in_progress → completed) | ✅ |
| SHA-256 file deduplication | ✅ |
| Content-type detection from HTTP headers | ✅ |
| R2 object storage with provenance | ✅ |
| Asset registration with source_id, file_hash, content_type | ✅ |
| Retrieval-event provenance (asset_sources table) | ✅ |
| Metadata processing handoff (metadata_queue → ai_analysis) | ✅ |
| Orchestrator execution (`sys.executable -m`) | ✅ |
| Provenance chain traceability (candidate → discovery → queue → asset → provenance → metadata) | ✅ |

---

## Roadmap

### Foundation & Acquisition Pipeline

✅ M0 – M15 Complete

All 16 foundation and acquisition pipeline milestones are complete. See the Current Status section above for the full milestone table and verified capabilities.

---

### Knowledge Platform

⬜ Knowledge Extraction Improvements

⬜ Evidence Graph Expansion

⬜ Citation Verification Improvements

⬜ Entity Resolution Enhancements

⬜ Timeline Reconstruction

---

### Digital Twin

⬜ Structural Model Framework

⬜ Building & Floor Hierarchies

⬜ Spatial Knowledge Integration

⬜ Evidence-Backed Reconstruction System

⬜ Interactive Digital Twin

---

### Long-Term Vision

Create the most complete evidence-backed digital reconstruction of the original World Trade Center complex, where every major reconstruction element can be traced to supporting historical sources, citations, and provenance records.


## Development Roadmap

### Phase 1 — Evidence Acquisition Engine

Build a reliable evidence acquisition pipeline capable of:

- Discovery
- Candidate generation
- Human review
- Downloading
- Validation
- Deduplication
- Asset registration

### Phase 2 — Knowledge Platform

Transform acquired evidence into:

- Structured facts
- Citations
- Relationships
- Research tools
- Searchable knowledge

### Phase 3 — Evidence-Backed Reconstruction

Generate historically grounded reconstruction assets using verified evidence and documented provenance.

### Phase 4 — Explorable Digital Twin

Create a navigable digital reconstruction of the original World Trade Center complex with evidence links attached to reconstruction elements.

---

## Repository Structure

```text
agents/         Discovery, acquisition and processing agents
dashboard/      User interfaces and tooling
database/       Database schema and migrations
docs/           Plans, audits, architecture and project documentation
research/       Research configuration and source definitions
scripts/        Utility scripts and maintenance tools
storage/        Asset storage integrations
```

---

## Technology Stack

- Python
- PostgreSQL
- OCR Processing
- Historical Evidence Pipelines
- Provenance Tracking
- Citation Loading
- Knowledge Graph Workflows
- Digital Twin Research

---

## Documentation

Key project documents:

- Mission
- Current State
- Next Task
- Architecture
- Master Plan
- AI Handoff
- Session Log

Project development follows a structured workflow:

```text
Audit
 ↓
Plan
 ↓
Review
 ↓
Implement
 ↓
Verify
 ↓
Document
 ↓
Commit
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

This repository is under active development.

Current branch activity reflects the ongoing construction of the World Trade Center Evidence Engine and its supporting evidence-acquisition, provenance, citation, knowledge-graph, and digital-twin systems.
