# Phase 2 Database Design Preparation Roadmap

**Document Status:** ✅ AUTHORITATIVE PHASE 2 ROADMAP  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Evaluated Datasets & Specs:** [`docs/PHASE_1_WORLD_MODEL_COMPLETION.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_1_WORLD_MODEL_COMPLETION.md), [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md), [`docs/CANONICAL_WORLD_MODEL_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/CANONICAL_WORLD_MODEL_REVIEW.md)  
**Target Milestone:** Authoritative Roadmap for **Phase 2 — Database Design Preparation**  

---

## Executive Summary

This document establishes the **authoritative roadmap for Phase 2: Database Design Preparation** for the World Trade Center Reconstruction Project.

Zero SQL DDL scripts, zero database migrations, zero PostgreSQL table creations, zero database schemas, zero API designs, zero frontend designs, and zero web searches were created in this document.

This roadmap defines the necessary preparation work, architectural resolutions, entity/relationship storage specifications, evidence linkage requirements, AI involvement criteria, phase completion conditions, and ordered execution sequence required **BEFORE any PostgreSQL schema implementation (Phase 3) can officially begin**.

---

## 1. Segregation of Facts, Interpretations, and Projections

```text
┌────────────────────────────────────────────────────────────────────────┐
│ VERIFIED FACTS (Physical Data Saved on Disk in data/*.json & docs/*.md)│
├────────────────────────────────────────────────────────────────────────┤
│ • Phase 1 MVWM target PASSED (164 verified entities vs 150 target)     │
│ • World Model Specification v1.0 APPROVED                              │
│ • Canonical 6-Tier Spatial Containment Hierarchy APPROVED              │
│ • World Model Governance & Lifecycle Rules APPROVED                    │
│ • 82 Master Unique Relationships mapped across 6 anchor elevations    │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ INTERPRETATIONS (Roadmap Readiness & Status Audits)                    │
├────────────────────────────────────────────────────────────────────────┤
│ • World Model Construction Phase: 100% COMPLETE & CLOSED              │
│ • Database Design Preparation Phase: ACTIVE                            │
│ • PostgreSQL DDL Schema Implementation: FUTURE DELIVERABLE (Phase 3)   │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ PROJECTIONS (Future Implementation Estimates)                          │
├────────────────────────────────────────────────────────────────────────┤
│ • Resolution of 3 remaining spatial/graph architecture decisions      │
│ • Successful execution of automated Python pre-ingestion test suite   │
│ • Phase 3 DDL schema generation for 164 verified entities             │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Section 1: Phase 1 Closure Validation

The prerequisite milestones required to initiate Phase 2 are **100% CONFIRMED AND APPROVED**:

- [X] **MVWM Target Achieved:** Exceeded the 150-entity threshold by cataloging **164 verified unique entities** (144 WTC 1 + 20 WTC 2) and 82 master relationships across 6 vertical anchor elevations (-3.5m to +410.0m).
- [X] **World Model Specification v1.0 Approved:** Formally published in [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md).
- [X] **Canonical Hierarchy Approved:** Formally adopted the streamlined **6-Tier Spatial Containment Hierarchy** (`Site` ──► `Building` ──► `Floor` ──► `Zone` ──► `Space` ──► `Element`) in [`docs/CANONICAL_WORLD_MODEL_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/CANONICAL_WORLD_MODEL_REVIEW.md).
- [X] **Lifecycle Rules Approved:** Formally published governance, evidence citation, and confidence scoring rules in [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md).

---

## 3. Section 2: Phase 2 Objectives

The primary goals of **Database Design Preparation** are:

1. **Map Ontology to Storage Patterns:** Map the 6-tier spatial tree and directed property graph to efficient database storage patterns without creating DDL.
2. **Define PostGIS 3D Coordinate Geometry Standards:** Establish precise 3D spatial bounding box and polygon coordinate standards (`GEOMETRY(POLYGONZ)` & `GEOMETRY(POINTZ)`) based on Port Authority datum (+310.0 ft PA).
3. **Specify Epistemic Metadata Storage:** Standardize non-null storage patterns for `evidence_sources`, `evidence_classification`, and `confidence_score`.
4. **Develop Pre-Ingestion Test Suite:** Build automated Python validation scripts to verify all 164 seed JSON entities against specification constraints before database DDL is written.

---

## 4. Section 3: Remaining Architecture Decisions

Prior to writing PostgreSQL DDL, the following **3 architectural questions MUST be formally resolved**:

```text
REMAINING ARCHITECTURE DECISIONS:
1. PostGIS 3D PolygonZ vs 2D Footprint + Z-Elevation Range Representation
2. Multi-Floor Element Storage: Direct Building Parent vs Junction Table
3. JSONB Epistemic Metadata vs Normalized Evidence Junction Tables
```

1. **Decision 1: PostGIS Spatial Geometry Representation:**  
   - *Question:* Should 3D spatial volumes (zones, spaces) be stored as native PostGIS 3D geometries (`POLYGONZ`) or as 2D plan footprints (`POLYGON`) paired with explicit numeric elevation bounds (`z_min`, `z_max`)?
2. **Decision 2: Multi-Floor Element Junction Structure:**  
   - *Question:* Should vertical multi-floor elements (Stairs A/B/C, Freight Elevator 50, Core Columns) rely solely on graph relationships (`PASSES_THROUGH`) or also utilize a dedicated physical junction table (`element_floor_junction`) for fast floor-level SQL lookups?
3. **Decision 3: Evidence Metadata Normalization:**  
   - *Question:* Should `evidence_sources` arrays be stored as `JSONB` within the entity table or normalized into a separate `evidence_citations` table?

---

## 5. Section 4: Entity Storage Preparation

Before entity table storage design begins, the following principles MUST be specified:

- **Entity Identity:** Primary keys MUST be immutable, human-readable string keys matching canonical entity IDs (e.g. `wtc1_f107_windows_on_the_world_main_dining_room`).
- **Structure Type Classification:** Building entity records MUST enforce `structure_type` classifications (`high_rise_tower`, `podium_building`, `hotel_slab`, `substation_base`, `transit_terminal`).
- **Parent Hierarchy Foreign Keys:** Every entity record (except root `Site`) MUST contain a non-null `parent_entity_id` referencing its immediate spatial parent in the 6-tier tree.

---

## 6. Section 5: Relationship Storage Preparation

Before relationship table storage design begins, the following principles MUST be specified:

- **Directed Property Graph Model:** Relationships MUST be stored in a dedicated directed graph table with columns: `id`, `subject_entity_id`, `relationship_type` (10 ENUMs), `object_entity_id`, `confidence_score`, `evidence_classification`.
- **Graph Traversal Indexing:** Indexing strategies MUST support fast multi-hop graph queries (e.g., tracing 13.8kV power distribution loops or chilled water riser lines across 110 floors).

---

## 7. Section 6: Evidence & Confidence Storage Preparation

Before evidence storage design begins, the following constraints MUST be specified:

- **Non-Null Metadata Enforcement:** Database schemas MUST reject any record where `evidence_classification` or `confidence_score` is NULL.
- **Confidence Range Enforcement:** Database schemas MUST enforce `confidence_score BETWEEN 0 AND 100`, rejecting records with `confidence_score < 80` from production tables.

---

## 8. Section 7: Model / AI Involvement Criteria

To maximize project velocity and reasoning quality during Phase 2:

### Work Managed by Current Agent (Gemini / Antigravity):
- Execution of blueprint seed data validation.
- Construction of automated Python pre-ingestion test suites.
- Authoring of spatial geometry and relational graph preparation specs.
- Idempotent seed JSON consolidation and verification.

### Work Triggering Specialized Subagent / Reasoning Model Involvement:
- **Complex Architecture Stress-Testing:** Involving specialized reasoning subagents to stress-test PostGIS 3D spatial indexing performance across 10,000+ projected future elements.
- **Multi-Building Schema Escalations:** Reviewing schema scalability across WTC 3 (Marriott), WTC 7, and PATH station sub-grade boundaries.

---

## 9. Section 8: Phase Completion Criteria

Phase 2 (Database Design Preparation) will be officially complete and **Phase 3 (PostgreSQL DDL Execution)** authorized when:

1. All 3 remaining architectural decisions (Section 4) are formally resolved and documented.
2. Specifications for Entity Storage, Relationship Storage, and Evidence Storage are finalized.
3. Automated Python pre-ingestion test suite passes 100% against all 164 seed entities in `data/*.json`.
4. Phase 3 PostgreSQL DDL Execution Roadmap is published and approved.

---

## 10. Section 9: Recommended Execution Sequence

```text
TASK 2.1: Spatial Geometry & 3D Coordinate Specification
          └─► Resolve PostGIS 3D POLYGONZ vs 2D Footprint + Z-Elevation Bounds

TASK 2.2: Relational Graph & Multi-Floor Riser Storage Specification
          └─► Resolve Element-Floor Junction Table vs Relational Graph Links

TASK 2.3: Epistemic Metadata & Evidence Citation Normalization Spec
          └─► Resolve JSONB Array vs Normalized Evidence Junction Tables

TASK 2.4: Automated Python Pre-Ingestion Validation Test Suite
          └─► Build & run validation script against all 164 seed JSON entities

TASK 2.5: Phase 2 Closure & Phase 3 PostgreSQL DDL Authorization Review
          └─► Authorize transition to Phase 3: PostgreSQL Schema DDL Creation
```

---

**Roadmap Finalized:** August 12, 2026  
**Status:** ✅ PHASE 2 DATABASE PREPARATION ROADMAP APPROVED — READY FOR TASK 2.1 EXECUTION
