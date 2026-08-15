# World Trade Center (1966-1973) Simulation

A highly immersive, historically accurate 3D simulation of the construction of the original World Trade Center. Built with React Three Fiber, Vite, and modern web standards.

## Evidence Before Geometry

This project does not begin with 3D models.

It begins with evidence.

Every reconstruction originates from:
- Port Authority documentation
- Engineering drawings
- Contracts
- Historical photography
- Archival film
- Construction reports
- Oral histories

The autonomous production system does not invent history.

The autonomous production system transforms verified evidence into explorable scenes.

**Core Principle:**
Evidence defines truth.
Production creates representation.

---

## Historical Reconstruction Methodology

Every corridor, column, fixture, and duct is reconstructed directly from authoritative historical archives:

- **Original Port Authority Blueprint Series:** Reconstructed directly from original PANYNJ contract drawings (`S` Structural, `M` Mechanical, `E` Electrical, `P` Plumbing, `A-A` Architectural).
- **Archival Photography & Film Alignment:** Cross-referenced with historical construction footage, aerial photography, and oral histories.
- **Zero Speculative Inference:** 100% of physical entities in the spatial model trace directly back to verified primary sources.

---

## Autonomous Production Studio

The teams operate on top of the evidence system. They do not replace the historical evidence; they transform it into 3D environments through a strict governance pipeline.

- **Project Director**: Sets high-level vision, approves milestones, and establishes policy.
- **Team B (Research & Assets)**: Ingests historical evidence to generate architectural reference and authenticate details.
- **Team A (Implementation)**: Responsible for the `/frontend/src/` codebase, blocking out scenes, and integrating PBR materials based strictly on evidence.
- **Team D (Critic)**: Enforces the 10-point evaluation criteria (Technical, Historical, Narrative, Realism) before any milestone is escalated.
- **Team C (Production Manager)**: Governs the repository, coordinates agents, maintains the Production Board, and escalates to the Project Director.

---

## Current Development Status

**Active Development Phase:**
Day 1 (August 1966)

**Completed Major Scenes:**
- SHOT009 – Bathtub Excavation
- SHOT002 – Suspended PATH Tubes
- SHOT003 – Icanda Slurry Wall Operation
- SHOT004 – Radio Row Demolition Edge
- SHOT005 – Public Observation Deck

**Current Project State:**
Refer to [PROJECT_STATE_001.md](docs/production/PROJECT_STATE_001.md) and [DAY1_PROGRESS_REPORT_001.md](docs/production/DAY1_PROGRESS_REPORT_001.md)

---

## Long-Term Vision

*Note: The complete 1966–2001 experience does not yet exist. The following outlines the intended future experience.*

### The Temporal Experience
Set your temporal date anywhere between **1966 and 2001**. Watch steel columns rise, floor slabs pour, curtain walls seal, and tenant spaces fit out.

### The 16 Reconstructed Subsystem Worlds
The complex will eventually be experienced across 16 interconnected physical and operational domains:
1. Structural Systems
2. Pedestrian Circulation
3. Mass Transit
4. Vertical Transportation
5. Observation & Tourism
6. Means of Egress
7. Operational Support
8. Facilities Operations
9. Mechanical Systems
10. Electrical Systems
11. Plumbing Systems
12. Communications & IT
13. Fire Protection
14. Life Safety
15. Security Systems
16. Building Automation

---

## Behind the Scenes: The Underlying Engine

*The database, graph queries, APIs, and validation frameworks exist solely to power this historical experience under the hood. They are the engine, not the experience.*

- **Spatial & Blueprint Engine (PostgreSQL 16 + PostGIS 3.6):** Stores spatial geometry polygons, blueprint bounding box citations, and historical logs.
- **Connectivity Engine (Neo4j v5.15 + APOC):** Traces multi-hop physical paths for power, water, air, and fiber data signals.
- **REST Gateway (FastAPI Python 3.11):** Exposes spatial endpoints for interactive 3D and web viewports.

---

## Quick Start
1. `npm install`
2. `npm run dev`
3. Open `http://localhost:5173`
