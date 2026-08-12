# Next Task

## Phase 2 Database Design Preparation — Task 2.1: Spatial Geometry & 3D Coordinate Specification

### Status

🔄 **In Progress**

## Objective

Resolve PostGIS spatial geometry and 3D coordinate system standards (Task 2.1 in [`docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md)) based on [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md).

Specifically, evaluate:
- Native PostGIS 3D spatial volumes (`GEOMETRY(POLYGONZ)`) vs 2D plan footprints (`GEOMETRY(POLYGON)`) paired with numeric elevation bounds (`z_min`, `z_max`).
- Alignment with Port Authority zero-datum elevation (+310.0 ft PA).

The authoritative specifications and roadmap documents are:
- `docs/WORLD_MODEL_SPECIFICATION_V1.md`
- `docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`
- `docs/PHASE_2_DATABASE_PREPARATION_ROADMAP.md`
- `docs/PHASE_1_WORLD_MODEL_COMPLETION.md`

## Current Reconstruction Readiness: ~75% (Direct-Evidence Verified Baseline)

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

## Fastest Route: 50% → 70%

### Phase 1: Immediate — Local Processing (1 day)

| Step | Action | Gain | Cumulative |
|---|---|---|---|
| 1 | Extract floor plan figures from NCSTAR 1-1 App C-G (`pdftoppm`) | +5% | 55% |
| 2 | Extract egress plans from NCSTAR 1-7 | +3% | 58% |
| 3 | Manually download Wikimedia full-res site plan SVGs | +5% | 63% |
| 4 | Catalog NCSTAR 1-8 images for architectural content | +2% | 65% |

### Phase 2: Short-term — External Public Archives (1-4 weeks)

| Step | Action | Gain | Cumulative |
|---|---|---|---|
| 5 | Download LoC Gottscho-Schleisner WTC photographs | +6% | 71% |
| 6 | File NYC DOB FOIL request for building permit drawings | +10% | 81% |
| 7 | Download HABS/HAER WTC survey (if available) | +5% | 86% |

### Phase 3: Long-term — Formal Requests (4-8 weeks)

| Step | Action | Gain | Cumulative |
|---|---|---|---|
| 8 | File Port Authority formal request (floor plans, site, plaza, concourse, interior) | +15% | 86% |
| 9 | Request NYC DOT concourse/subway maps | +5% | 91% |

## 11 Known Architectural Evidence Sources

Ranked by gain/effort:

| Priority | Source | Gain | Likelihood | Effort |
|---|---|---|---|---|
| 1 | NCSTAR 1-1 App C-G extraction | +5% | Medium | Low |
| 2 | NCSTAR 1-7 egress plan extraction | +3% | High | Low |
| 3 | Wikimedia full-res site plan SVGs | +5% | Med-High | Low |
| 4 | NYC DOB FOIL — building permits | +10% | Med-High | Medium |
| 5 | LoC Gottscho-Schleisner photos | +6% | High | Low |
| 6 | NCSTAR 1-8 visual cataloging | +2% | High | Low |
| 7 | Port Authority formal request | +15% | Medium | High |
| 8 | NYC DOT concourse maps | +5% | Medium | Medium |
| 9 | HABS/HAER Collection | +5% | Low-Med | Medium |
| 10 | Yamasaki Associates records | +10% | Low | High |
| 11 | Emery Roth & Sons records | +10% | Low | High |

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

## Current Phase Rules

- Do not ingest evidence into the database
- Do not modify code
- Do not modify the database schema
- Focus on evidence corpus acquisition and planning only
- Produce analysis documents, not implementation

## Non-Goals

Do not begin any of the following during this phase:

- Digital Twin schema development
- Reconstruction geometry
- Walkthrough development
- Broad AI enrichment
- Unrelated search redesign
- Unrelated database refactoring
- Automatic production scheduling
- Large-scale crawling

## Safety Rules

- Inspect before editing
- Work on one milestone at a time
- Read complete files before replacing them
- Prefer targeted changes over broad rewrites
- Require approval for database changes
- Do not delete evidence
- Do not commit secrets or API keys
- Do not commit downloaded evidence files
- Do not run destructive commands without explicit approval
- Run targeted tests after each change
- Review `git diff` after each change
- Update documentation only after tests pass
- Do not commit automatically
- Stop when the approved milestone is complete