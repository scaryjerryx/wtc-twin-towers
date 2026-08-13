# Architectural Decision Record (ADR-006)
## Gemini Restored as Primary Reconstruction Engine

**Status:** ✅ ADOPTED  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Strategic Review:** [`docs/PHASE_5_STRATEGIC_REALIGNMENT_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_STRATEGIC_REALIGNMENT_REVIEW.md)  
**Parent World Model Spec:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

---

## 1. Decision

The World Model Reconstruction Project formally adopts **ADR-006**, realigning the repository pipeline architecture to establish **Gemini Multi-Modal Architectural Analysis as the PRIMARY RECONSTRUCTION ENGINE**.

Optical Character Recognition (OCR) and CAD vector primitive extraction are formally reclassified as **SUPPORTING EVIDENCE SOURCES**.

Zero code changes, zero database modifications, zero SQL schema alterations, and zero web searches were created in this architecture decision record.

```text
REALIGNED AUTHORITATIVE PIPELINE ARCHITECTURE (ADR-006):
Blueprint PDF
   ↓
Gemini Multi-Modal Architectural Analysis (PRIMARY RECONSTRUCTION ENGINE)
   ↓
Entity Discovery & Architectural Reasoning
   ↓
Relationship Discovery
   ↓
Evidence Attribution (Stage 2 Vector / OCR Citations)
   ↓
Confidence Assessment ($[80, 100]$ bounds)
   ↓
Human Review Gate
   ↓
Stage 5 Deduplication (DATABASE QUALITY INFRASTRUCTURE)
   ↓
Stage 6 Database Ingestion (DATABASE PERSISTENCE INFRASTRUCTURE)
   ↓
World Model PostgreSQL/PostGIS Database (`wtc_evidence`)
```

---

## 2. Context & Problem Statement

### 2.1 Context
The World Model Reconstruction Project was founded to convert World Trade Center blueprint drawings, engineering schematics, and structural elevations into an evidence-backed 3D spatial database model (`wtc_evidence`).

### 2.2 Problem Statement
During Phase 4 execution, the pipeline suffered architectural drift. The system drifted toward a traditional document parsing ETL pipeline (`PDF ──► OCR ──► Vector Clipping ──► Database`), bypassing multi-modal AI architectural reasoning. Traditional OCR and vector text clipping cannot infer 3D spatial intent, structural core relationships (e.g. core box columns 501–1008), or architectural context across multi-sheet sets.

---

## 3. Mandatory Stage Reclassifications

```text
MANDATORY PIPELINE RECLASSIFICATION TABLE:
┌──────────────────────────────────────┬────────────────────────────────────────┐
│ Pipeline Stage                       │ Authoritative ADR-006 Classification   │
├──────────────────────────────────────┼────────────────────────────────────────┤
│ Stage 1: PDF Preparation             │ SUPPORTING UTILITY                     │
│ Stage 2: Vector Extraction           │ SUPPORTING EVIDENCE SOURCE             │
│ Stage 3: Gemini Architectural Analysis│ PRIMARY RECONSTRUCTION ENGINE          │
│ Stage 5: Deduplication               │ DATABASE QUALITY INFRASTRUCTURE        │
│ Stage 6: Database Ingestion          │ DATABASE PERSISTENCE INFRASTRUCTURE    │
└──────────────────────────────────────┴────────────────────────────────────────┘
```

---

## 4. Non-Negotiable Architectural Rules

```text
NON-NEGOTIABLE ARCHITECTURAL RULES:
1. OCR MAY provide evidence; OCR MAY NOT provide authority.
2. Vector extraction MAY provide evidence; vector extraction MAY NOT provide authority.
3. NO entity MAY exist solely due to OCR output.
4. NO relationship MAY exist solely due to OCR output.
5. Gemini architectural reasoning IS the primary reconstruction mechanism.
6. Repository evidence (Principle 2) and governance (ADR-005) REMAIN authoritative.
```

---

## 5. Detailed Component Roles

### 5.1 Primary Reconstruction Engine (Gemini Multi-Modal AI)
- Gemini performs multi-modal visual reasoning across architectural drawing sheets, structural elevations, core column layouts, and space allocations to discover entities and infer 3D spatial geometry.

### 5.2 Supporting Evidence Sources (OCR & Vector Extraction)
- CAD vector lines, polylines, closed polygon boundaries, and OCR text glyphs provide empirical citation evidence supporting Gemini's architectural reasoning (Principle 2: *Cite Sources*).

### 5.3 Database Infrastructure (PostgreSQL / PostGIS & ADR-005)
- PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`) and Master Entity Registry (`entities` ADR-005) provide immutable transactional persistence, single-parent `CHECK` constraint enforcement (`= 1`), and PostGIS spatial indexing (`EPSG:2263`).

---

## 6. Consequences & Phase 5 Strategic Direction

### 6.1 Positive Consequences
- Restores true architectural intelligence and 3D spatial reasoning to the World Model.
- Eliminates brittle rule-based OCR entity extraction failures.
- Preserves 100% of validated PostgreSQL/PostGIS database infrastructure, governance rules, evidence linking, and deduplication engines.

### 6.2 Phase 5 Strategic Direction
All Phase 5 3D procedural mesh generation, story height extrusions, and core column spatial modeling will be driven by Gemini multi-modal architectural analysis operating over PostGIS 2D baselines.

---

## 7. Final Adoption Recommendation

```text
FINAL ADR-006 ADOPTION SELECTION:
[ ] ADR Rejected
[ ] ADR Requires Revision
[X] ADR Adopted ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] ADR Adopted`:
ADR-006 formally corrects Phase 4 architectural drift, re-establishes Gemini Multi-Modal AI Analysis as the PRIMARY RECONSTRUCTION ENGINE, reclassifies OCR and vector extraction as SUPPORTING EVIDENCE SOURCES, and preserves 100% of validated PostgreSQL/PostGIS database infrastructure. **ADR-006 IS FORMALLY ADOPTED**.
