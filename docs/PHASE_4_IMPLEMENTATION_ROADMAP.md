# Phase 4 Implementation Roadmap

**Document Status:** ⚠️ **SUPERSEDED BY ADR-006 & PHASE 5 ARCHITECTURE**  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Superseding Architecture Records:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md), [`docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md), [`docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md)  

> [!WARNING]
> **SUPERSEDED NOTICE:** This document has been superseded by **ADR-006** and **[`docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md)**. Pipeline execution is now governed by Gemini Multi-Modal Architectural Analysis as the PRIMARY RECONSTRUCTION ENGINE. Retained for historical audit lineage.


---

## Executive Summary

This document establishes the **authoritative Implementation Roadmap** for **Phase 4: Automated PDF Parsing Pipeline**.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

This roadmap details the sequential 12-stage workflow pipeline governing PDF acquisition, preprocessing, vector extraction, raster rendering, AI vision parsing, entity detection, evidence citation generation, deduplication, database ingestion, validation, error handling, and acceptance criteria required to process architectural drawings into PostgreSQL `wtc_evidence`.

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
│ 4. PDF Incoming Directory Active (`data/incoming_pdfs/`)               │ ✅ PASS │
│ 5. PostGIS 2D Spatial Indices Active in `EPSG:2263`                    │ ✅ PASS │
│ 6. Phase 4 Scope & Boundaries Formally Defined                         │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. 12-Stage Pipeline Workflow Specifications

### 2.1 PDF Acquisition Workflow
- **Purpose:** Monitor `data/incoming_pdfs/` for new architectural PDF files and register file metadata.
- **Inputs:** PDF drawing files (`.pdf`) placed in `data/incoming_pdfs/`.
- **Outputs:** Verified raw PDF file handle and file hash entry in ingestion queue.
- **Dependencies:** Directory permissions on `data/incoming_pdfs/`.
- **Failure Modes:** File access locked, corrupt PDF header, or 0-byte file.
- **Validation Requirements:** Verify non-zero file size and valid PDF magic bytes (`%PDF-1.`).

### 2.2 PDF Preprocessing Workflow
- **Purpose:** Normalize PDF page orientation, crop title block, and extract embedded drawing metadata (drawing number, revision, scale).
- **Inputs:** Validated raw PDF file.
- **Outputs:** Normalized PDF document stream with extracted title block metadata (`sheet_code`, `drawing_title`).
- **Dependencies:** PyMuPDF / PDFminer libraries.
- **Failure Modes:** Encrypted PDF, missing page tree, or unreadable title block text.
- **Validation Requirements:** Successfully parse drawing sheet code (e.g., `A-A-18`, `A-A-121`).

### 2.3 Vector Extraction Workflow
- **Purpose:** Extract native vector CAD elements (lines, polylines, arcs, polygons, text annotations) from PDF vector layers.
- **Inputs:** Normalized PDF document stream.
- **Outputs:** Raw 2D geometry vector primitives and text label spatial bounding boxes.
- **Dependencies:** Vector extraction parser (`pypdf` / `pdfplumber`).
- **Failure Modes:** Scanned raster PDF lacking vector layer (fallback to Stage 2.4).
- **Validation Requirements:** Extract $\ge 1$ closed polygon path or CAD polyline.

### 2.4 Raster Rendering Workflow
- **Purpose:** Render high-resolution raster images (300 DPI PNG) for fallback optical feature extraction and AI vision analysis.
- **Inputs:** Normalized PDF page.
- **Outputs:** High-resolution RGB page image (`300 DPI PNG`) and coordinate scaling transformation matrix.
- **Dependencies:** Cairo / Poppler rendering library (`pdf2image`).
- **Failure Modes:** Memory allocation failure during high-DPI rendering.
- **Validation Requirements:** Verify rendered image dimensions and color depth.

### 2.5 AI Vision Parsing Workflow
- **Purpose:** Run multi-modal vision models over rendered page rasters to identify structural column grids, room boundaries, and equipment tags.
- **Inputs:** 300 DPI page image + vector label bounding boxes.
- **Outputs:** Structured layout predictions (bounding boxes, category tags, confidence scores).
- **Dependencies:** Vision model endpoint / local multi-modal inference runtime.
- **Failure Modes:** Vision model API timeout, low-confidence inference scores.
- **Validation Requirements:** Return layout predictions with confidence score $\ge 80$.

### 2.6 Entity Detection Workflow
- **Purpose:** Classify extracted vector shapes and layout predictions into canonical World Model entity tiers (`building`, `floor`, `zone`, `space`, `element`).
- **Inputs:** Vector primitives + AI vision layout predictions.
- **Outputs:** Candidate entity JSON payloads conforming to `entities` and physical tier schema specs.
- **Dependencies:** Spatial clustering and polygon closure algorithms.
- **Failure Modes:** Unclosed polygon footprint or ambiguous tier classification.
- **Validation Requirements:** Assign valid ENUM categories and PostGIS 2D polygon footprints (`EPSG:2263`).

### 2.7 Evidence Citation Workflow
- **Purpose:** Bind every detected entity to its source drawing sheet code (Principle 2: *Cite Sources*).
- **Inputs:** Candidate entity payload + title block metadata (`sheet_code`, `source_id`).
- **Outputs:** Epistemic citation tuples ready for `entity_evidence_citations` table insertion.
- **Dependencies:** Master `sources` record availability in database.
- **Failure Modes:** Missing `sheet_code` or unanchored source reference.
- **Validation Requirements:** Link every entity to $\ge 1$ valid source drawing sheet.

### 2.8 Deduplication Workflow
- **Purpose:** Query PostgreSQL database for pre-existing spatial entities and deduplicate overlapping footprints.
- **Inputs:** Candidate entity list + live PostgreSQL `wtc_evidence` catalog.
- **Outputs:** Deduplicated list of new vs. updated entity records.
- **Dependencies:** PostGIS spatial intersection queries (`ST_Intersects`, `ST_Equals`).
- **Failure Modes:** Database connection loss or ambiguous spatial match.
- **Validation Requirements:** Ensure zero duplicate primary key IDs or overlapping identical footprints.

### 2.9 Database Ingestion Workflow
- **Purpose:** Execute transactional SQL ingestion loading entities, citations, and property graph edges into `wtc_evidence`.
- **Inputs:** Deduplicated entity list + evidence citations + relationship tuples.
- **Outputs:** Committed database transactions (`BEGIN; ... COMMIT;`).
- **Dependencies:** Live PostgreSQL 16.14 + PostGIS 3.6.4 connection (`wtc_evidence`).
- **Failure Modes:** Foreign key violation, single-parent `CHECK` violation, or transaction rollback.
- **Validation Requirements:** All inserts commit cleanly with 0 database constraint exceptions.

### 2.10 Validation Workflow
- **Purpose:** Execute automated post-ingestion audit queries verifying data counts and spatial geometries.
- **Inputs:** Live database tables (`entities`, `sites`..`elements`, `relationships`).
- **Outputs:** Post-ingestion audit scorecard (entity count, relationship count, 0 orphan records).
- **Dependencies:** Automated validation test suite.
- **Failure Modes:** Detected orphan records, invalid PostGIS geometry (`ST_IsValid = false`), or confidence score $< 80$.
- **Validation Requirements:** 100% pass rate across all catalog integrity checks.

### 2.11 Error Handling Workflow
- **Purpose:** Catch and isolate processing failures, logging unparseable PDFs to `data/failed_pdfs/` without aborting batch pipeline.
- **Inputs:** Exception signals from Stages 2.1–2.10.
- **Outputs:** Quarantine directory movement (`data/failed_pdfs/`) and error log entries.
- **Dependencies:** File system write access to `data/failed_pdfs/`.
- **Failure Modes:** Unwritable quarantine folder.
- **Validation Requirements:** Ensure failed file is isolated and pipeline resumes next file.

### 2.12 Acceptance Criteria Workflow
- **Purpose:** Evaluate overall batch pipeline performance against non-negotiable success metrics.
- **Inputs:** Consolidated post-ingestion audit report.
- **Outputs:** Final Phase 4 acceptance sign-off.
- **Dependencies:** Completion of Stages 2.1–2.11.
- **Failure Modes:** Processing pass rate $< 95\%$.
- **Validation Requirements:** Clean ingestion of all valid incoming PDFs with zero orphan database records.

---

## 3. Final Implementation Sequence

```text
PHASE 4 SEQUENTIAL IMPLEMENTATION PIPELINE:
┌────────────────────────────────────────────────────────────────────────┐
│ STAGE 1: PDF Acquisition & Preprocessing (`data/incoming_pdfs/`)       │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 2: Vector Extraction & 300 DPI Raster Rendering                  │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 3: Multi-Modal AI Vision Layout Parsing & Entity Classification  │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 4: Epistemic Evidence Citation Generation (Sheet Code Binding)   │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 5: PostGIS Spatial Deduplication & Upsert Resolution             │
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 6: Transactional Database Ingestion into PostgreSQL `wtc_evidence`│
├────────────────────────────────────────────────────────────────────────┤
│ STAGE 7: Automated Catalog Validation & Quarantine Error Isolation     │
└────────────────────────────────────────────────────────────────────────┘
```

---

**Roadmap Approved:** August 12, 2026  
**Status:** ✅ PHASE 4 IMPLEMENTATION ROADMAP COMPLETE — READY FOR PIPELINE CODE AUTHORING
