# Phase 4 Scope and Boundaries

**Document Status:** ✅ AUTHORITATIVE PHASE 4 SCOPE & BOUNDARIES SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Transition Review:** [`docs/REPOSITORY_TRANSITION_STATE_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/REPOSITORY_TRANSITION_STATE_REVIEW.md)  
**Frozen Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  
**Frozen DDL Migration:** [`database/migrations/V1_1__create_world_model_schema_revised.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_1__create_world_model_schema_revised.sql)  

---

## Executive Summary

This document establishes the **authoritative Scope and Boundaries Specification** for **Phase 4: Automated Ingestion, Vector Extraction, and Entity Pipeline Processing**.

Zero implementation code, zero schema modifications, zero DDL migrations, zero architecture alterations, and zero web searches were created in this phase definition document.

Phase 4 defines the automated document processing pipeline designed to extract structural, spatial, and mechanical vector features from raw PDF architectural drawings and ingest them into the frozen Phase 3 PostgreSQL database (`wtc_evidence`).

---

## 1. Verified Facts

```text
EVIDENTIARY BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Executed Migration `V1_1__create_world_model_schema_revised.sql`     │ ✅ PASS │
│ 3. Master Entity Registry (`entities`) Architecture Active (ADR-005)    │ ✅ PASS │
│ 4. 227 Unique Entities & 114 Relationships Active in Live Database     │ ✅ PASS │
│ 5. PostGIS 2D Spatial Indices Active in `EPSG:2263`                    │ ✅ PASS │
│ 6. Raw PDF Drawing Directory Active (`data/incoming_pdfs/`)            │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Phase 4 Objectives

Phase 4 focuses on converting raw unstructured PDF architectural drawings into structured, evidence-backed spatial entities and property graph relationships within the frozen Phase 3 database:

1. **Automated Vector & Geometry Extraction:** Extract 2D PostGIS polygon footprints (`geometry_2d`) from architectural PDF drawings in `data/incoming_pdfs/`.
2. **Multi-Modal AI Vision Entity Recognition:** Extract structural column grids, elevator shafts, stairs, and MEP equipment layouts using vision models.
3. **Automated Epistemic Evidence Linking:** Generate declarative source citation records in `sources` and `entity_evidence_citations` linking extracted entities to drawing sheet codes (`A-A-18`, `A-A-121`, etc.).
4. **Automated Entity Deduplication & Registry Ingestion:** Populate `entities` master registry and physical tier tables (`sites`..`elements`) using strict upsert logic without introducing duplicate records.
5. **Graph Edge Generation:** Auto-discover and populate topological relationships (`CONTAINS`, `ADJACENT_TO`, `CONNECTS_TO`, `PASSES_THROUGH`) in `relationships`.

---

## 3. Phase 4 Deliverables

Phase 4 will produce the following primary software and documentation deliverables:

1. **PDF Vector Extraction Engine (`scripts/extract_pdf_vectors.py`):** Automated tool for parsing line strings, polygons, and text layers from architectural PDF drawings.
2. **AI Vision Layout Parser (`agents/vision_parser.py`):** Multi-modal model pipeline for identifying structural column tags and room boundaries.
3. **Automated Database Ingestion & Deduplication Pipeline (`scripts/ingest_pipeline.py`):** Transactional ETL pipeline loading extracted features into PostgreSQL `wtc_evidence`.
4. **Phase 4 Automated Processing Test Suite (`tests/test_pipeline.py`):** Unit and integration test suite validating ingestion accuracy and constraint adherence.
5. **Phase 4 Completion & Verification Report (`docs/PHASE_4_COMPLETION_REPORT.md`):** Final audit report verifying extracted entity counts and evidence linkage quality.

---

## 4. Phase 4 Non-Goals & Explicit Exclusions

The following areas are **EXPLICITLY EXCLUDED** from Phase 4 scope:

- **NO Schema Redesign:** Zero alterations to table structures, column definitions, or constraints in `wtc_evidence`.
- **NO Migration Rewrites:** Zero modifications to [`database/migrations/V1_1__create_world_model_schema_revised.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_1__create_world_model_schema_revised.sql).
- **NO ADR Revisions:** Zero changes to Architectural Decision Records ADR-001 through ADR-005.
- **NO Procedural 3D Mesh Extrusion:** 3D solid geometry generation (IFC/BIM OBJ/GLTF extrusion) is deferred to Phase 5.
- **NO Manual Data Editing:** Zero manual database edits without source drawing citation evidence.

---

## 5. Phase 4 Dependencies

Phase 4 relies strictly on the frozen Phase 3 database foundation:

1. **PostgreSQL Engine Availability:** Live connection to PostgreSQL 16.14 + PostGIS 3.6.4 on port 5432.
2. **Master Entity Registry Architecture (ADR-005):** Strict adherence to `entities(entity_id)` primary key registry before inserting tier records.
3. **Single-Parent CHECK Constraints:** Compliance with `((parent_a IS NOT NULL)::int + ...) = 1` single-parent rules on `zones`, `spaces`, and `elements`.
4. **PostGIS EPSG:2263 Coordinate System:** All extracted 2D polygon footprints must transform into NAD83 / NYC State Plane Feet (`EPSG:2263`).

---

## 6. Phase 4 Risks and Assumptions

### Risks
- **PDF Vector Noise & Fragmentation:** Raw CAD-converted PDFs may contain fragmented line strings requiring polygon closure algorithms.
- **OCR Text Extraction Errors:** Poor drawing scan resolutions may introduce drawing sheet code reading errors.

### Assumptions
- All incoming PDF drawings in `data/incoming_pdfs/` represent authentic WTC construction drawings (Yamasaki / Emery Roth & Sons).
- The live PostgreSQL database `wtc_evidence` remains running and accessible via environment credentials.

---

## 7. Final Phase Definition

```text
FINAL PHASE DEFINITION STATUS:
[ ] Phase 4 Scope Undefined
[ ] Phase 4 Scope Undecided
[X] Phase 4 Scope Formally Defined And Ready For Execution ◄── SOLE SELECTED DECISION
```

### Detailed Justification for `[X] Phase 4 Scope Formally Defined And Ready For Execution`:
Phase 4 objectives, deliverables, entry criteria, non-goals, dependencies, and risks are fully specified. The phase is **FORMALLY DEFINED AND READY FOR EXECUTION**.
