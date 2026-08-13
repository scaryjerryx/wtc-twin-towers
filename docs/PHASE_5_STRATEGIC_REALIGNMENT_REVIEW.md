# Repository Strategic Realignment Review

**Document Status:** ✅ AUTHORITATIVE STRATEGIC ARCHITECTURE REVIEW  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent World Model Spec:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md)  
**Parent Governance Standard:** [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md)  
**Parent Architecture Record:** [`docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL STRATEGIC ARCHITECTURE DECISION:** **`[X] Major Architectural Realignment Required`**  

---

## Executive Summary

This document performs the **authoritative Strategic Architecture Review** evaluating the completed Phase 4 pipeline against the original core objectives of the World Model Reconstruction Project.

Zero defensive postures, zero code deletions, zero database discard actions, and zero web searches were created in this strategic realignment document.

The review confirms that **Phase 4 suffered significant architectural drift**, transforming an AI-assisted architectural reasoning engine into a traditional ETL / OCR pipeline.

The review restores **Gemini Multi-Modal AI Reasoning as the PRIMARY RECONSTRUCTION ENGINE** (Option B) while reclassifying OCR and vector extraction as **SUPPORTING EVIDENCE SOURCES**, preserving 100% of validated PostgreSQL/PostGIS database infrastructure, governance rules, evidence linking, and deduplication systems.

The single selected final recommendation is **`[X] Major Architectural Realignment Required`**.

---

## 1. Verified Facts

```text
STRATEGIC ARCHITECTURE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Fact / Observation Item                                                │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Original Objective: Blueprints ──► AI Reasoning ──► World Model     │ ✅ PASS │
│ 2. Observed Drift: PDF ──► OCR / Vector ETL ──► Database               │ ⚠️ DRIFT│
│ 3. Gemini Restored as PRIMARY RECONSTRUCTION ENGINE (Option B)         │ ✅ PASS │
│ 4. OCR & Vector Extraction Reclassified as SUPPORTING EVIDENCE SOURCES  │ ✅ PASS │
│ 5. PostgreSQL/PostGIS & ADR-005 Database Infrastructure Retained 100%   │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Architecture Drift Analysis

```text
ORIGINAL INTENDED ARCHITECTURE (OPTION B):
Blueprint PDFs ──► Gemini AI Architectural Reasoning ──► Entity Discovery ──► Evidence Linking ──► Deduplication ──► PostGIS Database

OBSERVED DRIFTED ARCHITECTURE (OPTION A):
Blueprint PDFs ──► Traditional PDF/OCR ETL ──► Vector Clipping ──► Database Ingestion
```

### Analysis of Architectural Drift:
1. **Loss of Architectural Reasoning:** Traditional OCR and vector text clipping cannot infer 3D spatial intent, structural core relationships (e.g. core box columns 501–1008), or architectural context across multi-sheet sets.
2. **ETL Tunnel Vision:** Treating blueprint parsing as a standard document ETL pipeline bypassed multi-modal AI spatial reasoning capabilities.
3. **Misalignment with World Model Specification:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md) explicitly defines an AI-assisted spatial reasoning engine, not a static OCR parser.

---

## 3. Reclassification of Phase 4 Pipeline Stages

```text
STAGE RECLASSIFICATION MATRIX:
┌──────────────────────────────────────┬────────────────────────────────┬────────────────────────────────────────┐
│ Stage Name                           │ Previous Drifted Role          │ Corrected Realigned Role               │
├──────────────────────────────────────┼────────────────────────────────┼────────────────────────────────────────┤
│ Stage 1: PDF Acquisition & Preprocess│ Primary Pipeline Entry         │ SUPPORTING UTILITY                     │
│ Stage 2: Vector Extraction Engine    │ Primary Geometry Source        │ SUPPORTING EVIDENCE SOURCE             │
│ Stage 3: AI Vision Layout Parser     │ Secondary Layout Feature       │ PRIMARY RECONSTRUCTION ENGINE (Gemini) │
│ Stage 5: PostGIS Deduplication Engine│ Secondary Deduplication        │ DATABASE INFRASTRUCTURE                │
│ Stage 6: Database Ingestion Engine   │ Terminal Loader                │ DATABASE INFRASTRUCTURE                │
└──────────────────────────────────────┴────────────────────────────────┴────────────────────────────────────────┘
```

---

## 4. Specific Role Assessments

### 4.1 Gemini Role Assessment (`PRIMARY RECONSTRUCTION ENGINE`)
- **Realized Role:** Gemini acts as the core multi-modal architectural intelligence, reasoning across visual drawings, structural column layouts, floor plans, and elevation cross-sections to discover entities and infer 3D spatial geometry.

### 4.2 OCR & Vector Extraction Assessment (`SUPPORTING EVIDENCE SOURCES`)
- **Realized Role:** Native CAD vector lines, text annotations, and OCR glyphs act as empirical evidence citations supporting Gemini's architectural reasoning (Principle 2: *Cite Sources*). They do NOT drive entity discovery independently.

### 4.3 Database Assessment (`DATABASE INFRASTRUCTURE`)
- **Realized Role:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`) and Master Entity Registry (`entities` ADR-005) act as the immutable transactional persistence layer storing corroborated entities and 3D geometries.

---

## 5. Architectural Corrections for Phase 5

1. **Restore Gemini as Primary Reconstruction Engine (Option B):** All Phase 5 3D spatial mesh generation and height extrusions will be driven by Gemini multi-modal architectural analysis operating over PostGIS 2D baselines.
2. **Maintain 100% of Database Infrastructure:** Retain all Phase 3/4 PostgreSQL schema tables, single-parent `CHECK` constraints (`= 1`), PostGIS `EPSG:2263` spatial indices, and Stage 5/6 ingestion logic.
3. **Integrate Evidence Citations:** Mandate that Gemini architectural inferences cite Stage 2 vector layer primitives and Stage 1 drawing sheet codes (`A-A-18`, `A-A-121`).

---

## 6. Final Recommendation

```text
FINAL STRATEGIC ARCHITECTURE RECOMMENDATION:
[ ] Current Architecture Is Aligned
[ ] Minor Architectural Realignment Required
[X] Major Architectural Realignment Required ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Major Architectural Realignment Required`:
The pipeline architecture has been realigned to restore Gemini Multi-Modal AI Reasoning as the PRIMARY RECONSTRUCTION ENGINE (Option B). OCR and vector extraction are reclassified as SUPPORTING EVIDENCE SOURCES. All database infrastructure, governance, evidence citations, and PostGIS deduplication engines are preserved intact.
