# Strategic Changelog 2026

## Date: August 11, 2026

## Purpose

This document records the permanent strategic milestone reached on August 11, 2026, following the acquisition and assessment of the Tower A architectural corpus (211 blueprints from 911Research.net).

---

## What Changed

### Before (Pre-August 11, 2026)

The project was framed as an **"Evidence Engine"** — a system for discovering, collecting, processing, and citing historical evidence. The reconstruction was a future aspiration described in the "Reconstruction Layer (Planned)" section of the architecture document. The project's primary question was: "Can reconstruction be done?"

### After (August 11, 2026)

The project is now framed as a **"Reconstruction Platform"** — a browser-based, interactive, evidence-backed 3D experience of the World Trade Center. The Evidence Engine remains important but is now correctly positioned as a supporting system. The project's new question is: "How should reconstruction be represented and experienced?"

---

## Why It Changed

Three factors drove this strategic shift:

1. **Tower A Architectural Corpus Acquisition:** The 211-drawing blueprint collection from 911Research.net fundamentally changed the evidence landscape. Tower A is now architecturally documented from Sub-Level 5 through the 110th Floor roof.

2. **CG-2 Closure:** The Critical Gap for Architectural Floor Plans (CG-2) is now substantially closed for Tower A. The most significant blocker to reconstruction has been removed.

3. **Readiness Milestone:** Overall project readiness increased from ~50% to ~65-70%. Tower A readiness increased from 65% to 85%. Prototype 0.1 is now enabled.

The project crossed a threshold where the question shifted from "Can we reconstruct?" to "How should reconstruction be delivered?"

---

## New Project Direction

### Three-System Architecture

| System | Role | Status |
|--------|------|--------|
| **Reconstruction Platform** | The product — browser-based 3D experience | Target |
| **World Model** | The core asset — structured digital representation | Being designed |
| **Evidence Engine** | The supporting system — automated evidence pipeline | Operational |

### Key Principle

```
Evidence → Understanding → Reconstruction Data Model → PostgreSQL World Database → API Layer → React Three Fiber World → Public Historical Experience
```

---

## Architectural Decisions

### 1. Reconstruction Platform is the Product

The browser-based 3D experience is what users interact with. It is not an afterthought or a future phase — it is the defining purpose of the project.

### 2. World Model is the Core Asset

The structured, time-aware, evidence-backed digital representation of the WTC complex is the most valuable artifact the project produces. The Evidence Engine populates it. The Reconstruction Platform consumes it.

### 3. Evidence Engine is Supporting Infrastructure

The Evidence Engine (discovery, acquisition, processing, knowledge extraction, citations, verification) remains essential but is now correctly classified as construction scaffolding — necessary during development but not what the public sees.

### 4. AI is a Development Tool, Not a Runtime Dependency

AI systems (Claude, Gemini, future multimodal models) assist with blueprint interpretation, evidence understanding, and code generation. The final Reconstruction Platform must function without requiring an active AI model.

### 5. Browser-First Delivery

The platform must work in any modern browser on desktop, tablet, or mobile. No installation. No app store. No downloadable client.

---

## Technology Decisions

### Target Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **World Database** | PostgreSQL | Structured WTC world model |
| **API Layer** | TBD (Python/Node.js) | Serve world data to frontend |
| **Frontend Framework** | Next.js | Application shell and routing |
| **3D Rendering** | React Three Fiber | Browser-based 3D reconstruction |
| **Evidence System** | Custom | Citation lookup and display |

### Current Stack (Evidence Engine)

| Layer | Technology |
|-------|-----------|
| Language | Python 3 |
| Database | PostgreSQL (5 migrations) |
| OCR | Tesseract |
| AI | OpenRouter (DeepSeek V4 Flash) |
| Storage | R2 Object Storage |
| Infrastructure | Docker |

---

## Timeline Experience Decision

The public will experience the WTC as a **construction journey**, not a completed timeline.

- **35-day release schedule:** Day 1 = 1966, Day 35 = 2001
- Users can travel backward but not forward
- After Day 35, full timeline unlocks as permanent archive
- Construction visualization includes cranes, steel erection, facade installation
- Every construction state links to supporting evidence

---

## Role of Evidence Engine

The Evidence Engine remains the automated pipeline for:

- Discovering historical evidence from configured sources
- Downloading and registering evidence assets
- Processing documents, images, and drawings
- Extracting entities, facts, and relationships
- Preserving provenance, citations, and confidence
- Building the knowledge graph
- Populating the World Model

The Evidence Engine is **construction scaffolding** — essential during development, invisible to end users.

---

## Role of Reconstruction Platform

The Reconstruction Platform is the browser-based experience for:

- Rendering the WTC complex in 3D (React Three Fiber)
- Allowing users to walk through spaces
- Supporting time travel (1966-2001)
- Displaying evidence citations on click
- Showing confidence levels visually
- Working on all devices without installation

The Reconstruction Platform is **the building** — what the public experiences.

---

## Evidence Citation System

Every reconstruction element will support evidence lookup:

```
Element → Evidence Reference → Source → Confidence → Provenance
```

Users click any wall, column, room, or space and see what evidence supports it, where it came from, and how confident the reconstruction is.

---

## Documents Created

| Document | Purpose |
|----------|---------|
| `docs/PROJECT_VISION_2026.md` | Complete project vision and strategic direction |
| `docs/RECONSTRUCTION_PLATFORM_VISION.md` | Browser-based platform definition |
| `docs/WORLD_MODEL_ARCHITECTURE.md` | World Model schema, API, and data model |
| `docs/HISTORICAL_TIMELINE_EXPERIENCE.md` | Time-release construction journey |
| `docs/STRATEGIC_CHANGELOG_2026.md` | This document |

## Documents Updated

| Document | Changes |
|----------|---------|
| `README.md` | New mission, readiness (~65-70%), tech stack, component roles, FINAL VISION section |
| `docs/ARCHITECTURE.md` | System architecture overview, target stack, evidence citation, updated corpus |

---

## Current State (August 11, 2026)

| Metric | Value |
|--------|-------|
| Tower A Readiness | 85% |
| Overall Project Readiness | ~65-70% |
| CG-2 Status | Substantially closed (Tower A) |
| Prototype 0.1 | Enabled |
| Evidence Engine | Operational (M0-M23 complete) |
| World Model | Being designed |
| Reconstruction Platform | Planned |
| Version | 0.8.0 |

---

**Changelog prepared:** August 11, 2026  
**Status:** ✅ PERMANENT STRATEGIC RECORD