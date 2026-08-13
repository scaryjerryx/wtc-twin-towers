# Phase 5 Gemini Reconstruction Architecture Specification

**Document Status:** ✅ AUTHORITATIVE PHASE 5 RECONSTRUCTION ARCHITECTURE SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Record:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
**Parent Strategic Review:** [`docs/PHASE_5_STRATEGIC_REALIGNMENT_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_STRATEGIC_REALIGNMENT_REVIEW.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

---

## Executive Summary

This document establishes the **authoritative Phase 5 Gemini Reconstruction Architecture Specification** translating ADR-006 into an actionable operational processing flow.

Zero code modifications, zero database schema changes, zero implementation artifacts, and zero web searches were created in this architecture specification document.

The specification defines the precise operational mechanics by which **Gemini Multi-Modal AI Reasoning acts as the PRIMARY RECONSTRUCTION ENGINE**, receiving high-resolution drawing visual evidence and supporting CAD vector primitives, discovering architectural entities and spatial relationships, attaching epistemic evidence citations, generating composite confidence ratings ($[80, 100]$), passing candidate records through human review gates, and transferring clean payloads to Stage 5 Deduplication and Stage 6 Database Ingestion.

---

## 1. Verified Facts

```text
ARCHITECTURE SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. ADR-006 Formally Adopted & Active                                   │ ✅ PASS │
│ 2. Gemini Multi-Modal Analysis Established as Primary Engine           │ ✅ PASS │
│ 3. Stage 1 Reclassified as SUPPORTING UTILITY                          │ ✅ PASS │
│ 4. Stage 2 Vector Extraction Reclassified as SUPPORTING EVIDENCE SOURCE│ ✅ PASS │
│ 5. Stage 5 Deduplication Classified as DATABASE QUALITY INFRASTRUCTURE │ ✅ PASS │
│ 6. Stage 6 Database Ingestion Classified as PERSISTENCE INFRASTRUCTURE │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Gemini Reconstruction Pipeline Workflow

```text
ADR-006 AUTHORITATIVE RECONSTRUCTION WORKFLOW:
Blueprint PDF (Stage 1 Support)
   │
   ├───────► Stage 2 CAD Vector & Text Extraction (SUPPORTING EVIDENCE)
   │
   ▼
Gemini Multi-Modal Architectural Analysis (PRIMARY RECONSTRUCTION ENGINE)
   │ ──► Multi-Sheet Architectural Spatial Reasoning
   │ ──► Entity Discovery (Spaces, Zones, Columns 501-1008, Core Elevator Banks)
   │ ──► Relationship Discovery (CONTAINS, BOUNDS, ADJACENT_TO, CONNECTS_TO)
   │ ──► Evidence Attribution (Sheet code citations & Stage 2 vector WKT bounds)
   │ ──► Epistemic Confidence Assessment ($[80, 100]$ score bounds)
   ▼
Human Review Gate (Enforces sign-off for scores in [70, 79] or overlap ambiguity)
   ▼
Stage 5 PostGIS Deduplication Engine (DATABASE QUALITY INFRASTRUCTURE)
   ▼
Stage 6 Transactional Database Ingestion Engine (DATABASE PERSISTENCE INFRASTRUCTURE)
   ▼
World Model PostgreSQL 16.14 / PostGIS 3.6.4 Baseline (`wtc_evidence`)
```

---

## 3. Reclassified Stage Responsibilities & Authority Levels

```text
STAGE RESPONSIBILITY & AUTHORITY MATRIX:
┌───────────────────────────┬────────────────────────────────────────────┬─────────────────────────────┐
│ Stage Component           │ Primary Operational Responsibility         │ Enforced Authority Level    │
├───────────────────────────┼────────────────────────────────────────────┼─────────────────────────────┤
│ Stage 1: PDF Preparation  │ Discover, hash, & render 300 DPI images    │ SUPPORTING UTILITY          │
│ Stage 2: Vector Extraction│ Extract CAD lines, polylines, & text WKT   │ SUPPORTING EVIDENCE SOURCE  │
│ Stage 3: Gemini Engine    │ Multi-Modal Architectural Spatial Discovery│ PRIMARY RECONSTRUCTION      │
│ Stage 5: Deduplication    │ PostGIS spatial overlap & entity resolution│ DATABASE QUALITY INFRASTR.  │
│ Stage 6: DB Ingestion     │ Atomic transaction load into PostgreSQL DB │ DATABASE PERSISTENCE INFRA. │
└───────────────────────────┴────────────────────────────────────────────┴─────────────────────────────┘
```

### Detailed Operational Definitions:

1. **Stage 1 (SUPPORTING UTILITY):**
   - **Primary Responsibility:** Discovers PDF drawing sheets in `data/incoming_pdfs/`, computes SHA-256 binary file hashes, validates magic bytes (`%PDF-`), extracts sheet codes (`A-A-18`, `A-A-121`), normalizes rotation, and renders 300 DPI RGB page raster images.
   - **Inputs:** Raw PDF files.
   - **Outputs:** `Stage1OutputContract` v1.0.0 + 300 DPI PNG page raster image.
   - **Authority Level:** `SUPPORTING UTILITY`.

2. **Stage 2 (SUPPORTING EVIDENCE SOURCE):**
   - **Primary Responsibility:** Extracts native CAD vector primitives (polylines, polygons, text annotations) and transforms page coordinates into PostGIS `EPSG:2263` Well-Known Text (WKT).
   - **Inputs:** `Stage1OutputContract` v1.0.0.
   - **Outputs:** `Stage2VectorContract` v1.0.0.
   - **Authority Level:** `SUPPORTING EVIDENCE SOURCE` (Provides evidence citations; CANNOT discover entities independently).

3. **Stage 3: Gemini Reconstruction Engine (PRIMARY RECONSTRUCTION ENGINE):**
   - **Primary Responsibility:** Performs multi-modal architectural analysis across 300 DPI drawing images and supporting CAD vector evidence, discovering entities (spaces, zones, core columns 501–1008), inferring spatial relationships, attaching drawing sheet citations, and evaluating composite confidence scores ($[80, 100]$).
   - **Inputs:** `Stage1OutputContract` + `Stage2VectorContract` + 300 DPI page image.
   - **Outputs:** `Stage3LayoutContract` v1.0.0.
   - **Authority Level:** `PRIMARY RECONSTRUCTION ENGINE` (Authoritative discovery mechanism).

4. **Stage 5 (DATABASE QUALITY INFRASTRUCTURE):**
   - **Primary Responsibility:** Performs PostGIS spatial overlap queries (`ST_Intersects`, $\text{IoU} \ge 0.90$), attribute fuzzy matching, evidence link merging (`DRAFT_SEED` ──► `CORROBORATED`), and stored repository precedence conflict resolution.
   - **Inputs:** `Stage3LayoutContract` v1.0.0 + active database state (`wtc_evidence`).
   - **Outputs:** `Stage5DeduplicationContract` v1.0.0.
   - **Authority Level:** `DATABASE QUALITY INFRASTRUCTURE`.

5. **Stage 6 (DATABASE PERSISTENCE INFRASTRUCTURE):**
   - **Primary Responsibility:** Manages atomic PostgreSQL database transactions (`BEGIN; ... COMMIT;`), ADR-005 Master Entity Registry (`entities`) inserts, physical tier table loads (`spaces`, `elements`), foreign key validations, and atomic error rollbacks.
   - **Inputs:** `Stage5DeduplicationContract` v1.0.0.
   - **Outputs:** `Stage6IngestionContract` v1.0.0.
   - **Authority Level:** `DATABASE PERSISTENCE INFRASTRUCTURE`.

---

## 4. Non-Negotiable Evidence Integration & Governance Rules

```text
EVIDENCE INTEGRATION & GOVERNANCE RULES:
1. OCR MAY provide evidence; OCR MAY NOT provide authority.
2. Vector extraction MAY provide evidence; vector extraction MAY NOT provide authority.
3. NO entity MAY exist solely because OCR detected text.
4. NO relationship MAY exist solely because OCR detected text.
5. Gemini architectural reasoning IS the primary reconstruction mechanism.
6. Repository evidence (Principle 2) and governance (ADR-005) REMAIN authoritative.
```

---

## 5. Architectural Conflict Resolution Matrix

```text
ARCHITECTURAL CONFLICT RESOLUTION MATRIX:
┌───────────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Conflict / Ambiguity Scenario                         │ Enforced Architectural Resolution Action               │
├───────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. Vector CAD text conflicts with OCR text            │ Vector CAD text PREVAILS; OCR saved as alias (Rule 2.2)│
│ 2. Gemini spatial prediction conflicts with stored DB │ Stored DB PREVAILS; Gemini candidate sent to review    │
│ 3. Gemini score in human review range [70, 79]        │ Candidate FLAGGED; requires reviewer sign-off         │
│ 4. Gemini score < 70                                  │ Candidate REJECTED to quarantine (`data/failed_pdfs/`) │
│ 5. Multiple overlapping visual symbol predictions     │ Spatial IoU tie-breaker applied; lower IoU flagged     │
└───────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 6. Final Architecture Status

- **Status:** **FROZEN & AUTHORITATIVE AT VERSION 1.0.0**
- **Governing Standard:** ADR-006 (`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`).  
- **Governance Sign-off:** ✅ Approved for Phase 5 Gemini multi-modal architectural reconstruction engine execution.
