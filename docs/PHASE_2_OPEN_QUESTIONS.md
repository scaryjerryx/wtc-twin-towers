# Phase 2 Database Design Preparation: Open Architectural Questions

**Document Status:** ✅ APPROVED OPEN QUESTIONS ASSESSMENT  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md)  
**Target Milestone:** Resolution of Open Architectural Questions Before Phase 3 PostgreSQL DDL Execution  

---

## Executive Summary

This document identifies, categorizes, and classifies all remaining **open architectural questions** that MUST be formally resolved before PostgreSQL database DDL schema design (Phase 3) can begin.

Zero SQL DDL scripts, zero database migrations, zero database tables, and zero web searches were created in this document.

A total of **11 open architectural questions** have been identified across four functional categories (Spatial Geometry, Relational Graph Architecture, Epistemic Metadata Storage, and Temporal Versioning) and classified into **Critical**, **Important**, and **Optional** priorities.

---

## 1. Classification Summary Matrix

```text
CLASSIFICATION SUMMARY:
┌────────────────────────────────────────────────────────────────────────┐
│ CRITICAL  (Must resolve BEFORE DDL schema design begins)  : 4 Questions│
│ IMPORTANT (Must resolve BEFORE database ingestion pipeline) : 5 Questions│
│ OPTIONAL  (Can resolve during Phase 3 implementation)      : 2 Questions│
└────────────────────────────────────────────────────────────────────────┘
```

| Question ID | Category | Architectural Question | Priority Classification |
|---|---|---|---|
| **A.1** | Spatial Geometry | Native PostGIS 3D `POLYGONZ` vs. 2D Footprint + Numeric `z_min`/`z_max` | 🔴 **CRITICAL** |
| **A.2** | Spatial Geometry | Coordinate System & SRID Alignment (WGS84 vs. NYC State Plane vs. PA Datum) | 🔴 **CRITICAL** |
| **A.3** | Spatial Geometry | Element Spatial Geometry Representation (`POINTZ` vs. `BOX3D` vs. Boundary Mesh) | 🟡 **IMPORTANT** |
| **B.1** | Relational Graph | Multi-Floor Element Storage: Direct Building Parent vs. `element_floor_junction` | 🔴 **CRITICAL** |
| **B.2** | Relational Graph | Graph Storage: Relational Junction Table vs. Native Graph Extension (Apache AGE) | 🟡 **IMPORTANT** |
| **B.3** | Relational Graph | Graph Edge Symmetry: Dual Explicit Edges vs. Single Edge + Application Inference | 🟢 **OPTIONAL** |
| **C.1** | Epistemic Metadata | Evidence Source Array Storage: `JSONB` Column vs. Normalized Junction Table | 🔴 **CRITICAL** |
| **C.2** | Epistemic Metadata | Confidence Score Calculation: Database Triggers vs. Application Ingestion Logic | 🟡 **IMPORTANT** |
| **C.3** | Epistemic Metadata | Contradictory Evidence Preservation Model in PostgreSQL | 🟡 **IMPORTANT** |
| **D.1** | Temporal Versioning | Time-Aware Historical Reconstruction: Date Ranges (`valid_from`/`valid_to`) vs. Snapshots | 🟡 **IMPORTANT** |
| **D.2** | Data Management | Seed JSON Ingestion Idempotency & Upsert Strategy (`ON CONFLICT DO UPDATE`) | 🟢 **OPTIONAL** |

---

## 2. Critical Architectural Questions (Must Resolve Before DDL Design)

### 🔴 Question A.1: Native PostGIS 3D `POLYGONZ` vs. 2D Footprint + Numeric `z_min`/`z_max`
- **Description:** Should 3D spatial volumes (zones, spaces) be stored as native PostGIS 3D polygon geometries (`GEOMETRY(POLYGONZ)`) or as 2D plan footprints (`GEOMETRY(POLYGON)`) paired with explicit numeric elevation bounds (`z_min`, `z_max` in PA datum feet/meters)?
- **Trade-off Analysis:** Native 3D `POLYGONZ` allows complex non-planar volumetric intersections but increases PostGIS indexing (`GIST`) complexity and query execution time. 2D footprint + `z_min`/`z_max` provides ultra-fast 2D spatial indexing and simple Z-range filtering, matching standard architectural floor plan representations.
- **Impact:** Dictates PostGIS column data types on `zones` and `spaces` tables.

### 🔴 Question A.2: Coordinate System & SRID Alignment
- **Description:** Which Spatial Reference System ID (SRID) should drive spatial coordinate storage?
- **Options:**
  1. `EPSG:4326` (WGS84 Latitude/Longitude geographic coordinates)
  2. `EPSG:2263` (NAD83 / New York Long Island State Plane Feet)
  3. Custom local origin (0,0,0) aligned to the Port Authority zero datum (+310.0 ft PA / WTC Site Grid Origin)
- **Impact:** Determines spatial coordinate transformation accuracy and sub-foot positioning for structural columns and perimeter walls.

### 🔴 Question B.1: Multi-Floor Element Storage & Physical Junction Tables
- **Description:** Multi-floor vertical elements (Stairs A/B/C, Freight Elevator 50, Core Box Columns 501–1008) are parented to `building_id` in the physical tree. Should floor-by-floor penetrations rely solely on the `relationships` graph table (`PASSES_THROUGH`) or also utilize a dedicated physical junction table (`element_floor_junction`) for fast floor-filtered SQL lookups?
- **Trade-off Analysis:** Sole reliance on `relationships` graph table maintains schema minimalism. Introducing `element_floor_junction` (`element_id`, `floor_id`, `landing_type`) provides $O(1)$ SQL queries for "all elements present on Floor 75".
- **Impact:** Affects database schema normalization and floor-filtered query performance.

### 🔴 Question C.1: Evidence Source Array Storage (`JSONB` vs. Normalized Junction Table)
- **Description:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md) requires tracking multiple corroborating blueprint sheets per entity (`evidence_sources: ["A-A-19", "A-A-20", "A-A-31"]`). Should this array be stored as a `JSONB` column on the `entities` table or normalized into a separate `entity_evidence_citations` junction table referencing a master `evidence_sources` table?
- **Trade-off Analysis:** `JSONB` array column simplifies insertion and single-entity JSON serialization. Normalized junction table enables strict SQL foreign key constraints and fast reverse lookup queries ("find all entities derived from blueprint A-A-19").
- **Impact:** Dictates foreign key referential integrity architecture and citation query performance.

---

## 3. Important Architectural Questions (Must Resolve Before Ingestion Pipeline)

### 🟡 Question A.3: Element Spatial Geometry Representation
- **Description:** How should physical elements (columns, chillers, transformers, stairwells) be spatially represented in PostGIS?
- **Options:** Centroid 3D Point (`POINTZ`), 3D Bounding Box (`BOX3D`), or full 3D boundary mesh (`MULTIPOLYGONZ`).
- **Impact:** Determines geometry column definitions on the `elements` table.

### 🟡 Question B.2: Directed Relational Graph Storage Architecture
- **Description:** Should entity relationships be stored in a standard relational junction table (`subject_entity_id`, `relationship_type_enum`, `object_entity_id`) or leverage a graph extension like Apache AGE?
- **Impact:** Determines query patterns for multi-hop graph traversals (e.g., tracing electrical power or chilled water riser lines across 110 floors).

### 🟡 Question C.2: Confidence Score Trigger Updates vs. Application Ingestion Logic
- **Description:** Should confidence scores (0–100) be updated dynamically via PostgreSQL database triggers when new corroborating evidence citations are added, or calculated by application logic prior to ingestion?
- **Impact:** Controls database trigger complexity and data loading performance.

### 🟡 Question C.3: Contradictory Evidence Preservation Model in PostgreSQL
- **Description:** In compliance with **Principle 6 (*Preserve Contradictions*)**, how should alternative or conflicting evidence claims (e.g., conflicting room dimensions between two blueprint revisions) be stored in PostgreSQL?
- **Impact:** Ensures contradictory historical evidence is preserved without violating SQL unique constraints.

### 🟡 Question D.1: Temporal Reconstruction Model (Time-Aware Historical States)
- **Description:** Should historical time-awareness (1966 construction, 1973 operational, post-1993 repairs) be modeled using `valid_from` / `valid_to` timestamp columns on entity/relationship tables or via discrete historical state snapshot tables?
- **Impact:** Prepares schema for time-release historical walkthroughs without structural schema rewrites later.

---

## 4. Optional Architectural Questions (Can Resolve During Phase 3 Implementation)

### 🟢 Question B.3: Graph Edge Symmetry & Inverse Relationship Storage
- **Description:** Should inverse relationship pairs (e.g., `CONTAINS` vs `INSIDE_OF`) be stored explicitly as dual directed edges or inferred programmatically in application logic from a single directed edge (`CONTAINS`)?
- **Impact:** Optimizes relationship table row count and prevents redundant edge storage.

### 🟢 Question D.2: Seed JSON Ingestion Idempotency & Upsert Strategy
- **Description:** What SQL upsert pattern (`ON CONFLICT (entity_id) DO UPDATE`) should be enforced by the Python ingestion pipeline when re-loading `data/*.json` seed files?
- **Impact:** Guarantees 100% idempotent data loading without manual table truncations.

---

## 5. Recommended Resolution Sequence for Task 2.1

To maintain structured momentum in Phase 2 Database Design Preparation:

```text
STEP 1: Resolve Spatial Geometry Standards (Questions A.1, A.2, A.3)
        └─► Publish docs/POSTGIS_SPATIAL_GEOMETRY_SPECIFICATION.md

STEP 2: Resolve Relational Graph & Multi-Floor Storage (Questions B.1, B.2, B.3)
        └─► Publish docs/RELATIONAL_GRAPH_STORAGE_SPECIFICATION.md

STEP 3: Resolve Epistemic Citation & Contradiction Storage (Questions C.1, C.2, C.3)
        └─► Publish docs/EPISTEMIC_METADATA_STORAGE_SPECIFICATION.md

STEP 4: Resolve Temporal Versioning & Ingestion Upserts (Questions D.1, D.2)
        └─► Publish docs/TEMPORAL_VERSIONING_AND_INGESTION_SPECIFICATION.md
```

---

**Assessment Finalized:** August 12, 2026  
**Status:** ✅ PHASE 2 OPEN ARCHITECTURAL QUESTIONS CLASSIFIED — READY FOR TASK 2.1 SPATIAL GEOMETRY RESOLUTION
