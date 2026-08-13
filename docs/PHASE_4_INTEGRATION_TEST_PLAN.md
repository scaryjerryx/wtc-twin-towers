# Phase 4 End-to-End Pipeline Integration Test Plan

**Document Status:** ✅ AUTHORITATIVE INTEGRATION TEST PLAN  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Implementation Reviews:**  
1. [`docs/STAGE_1_IMPLEMENTATION_VALIDATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/STAGE_1_IMPLEMENTATION_VALIDATION_REVIEW.md)  
2. [`docs/STAGE_2_IMPLEMENTATION_VALIDATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/STAGE_2_IMPLEMENTATION_VALIDATION_REVIEW.md)  
3. [`docs/STAGE_3_IMPLEMENTATION_VALIDATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/STAGE_3_IMPLEMENTATION_VALIDATION_REVIEW.md)  
4. [`docs/STAGE_5_IMPLEMENTATION_VALIDATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/STAGE_5_IMPLEMENTATION_VALIDATION_REVIEW.md)  
5. [`docs/STAGE_6_IMPLEMENTATION_VALIDATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/STAGE_6_IMPLEMENTATION_VALIDATION_REVIEW.md)  
6. [`docs/PHASE_4_PIPELINE_INTERFACE_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_PIPELINE_INTERFACE_REVIEW.md)  
**Pipeline Under Test:** `Stage 1` ──► `Stage 2` ──► `Stage 3` ──► `Stage 5` ──► `Stage 6`  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL INTEGRATION TEST PLAN DECISION:** **`[X] Integration Testing Ready To Execute`**  

---

## Executive Summary

This document establishes the **authoritative End-to-End Pipeline Integration Test Plan** governing full execution testing for the Phase 4 Automated PDF Parsing Pipeline.

Zero code modifications, zero new features, zero architecture changes, and zero web searches were created in this test plan document.

The integration plan defines 12 testing modules, test dataset selections, end-to-end execution workflows, contract compliance verification, quarantine handling, human review enforcement, and PostgreSQL/PostGIS database transaction verification.

The single selected recommendation is **`[X] Integration Testing Ready To Execute`**.

---

## 1. Verified Facts

```text
INTEGRATION TEST BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Stage 1 PDF Preprocessor Implemented & Approved                     │ ✅ PASS │
│ 2. Stage 2 Vector Extraction Engine Implemented & Approved             │ ✅ PASS │
│ 3. Stage 3 AI Vision Layout Parser Implemented & Approved              │ ✅ PASS │
│ 4. Stage 5 PostGIS Deduplication Engine Implemented & Approved         │ ✅ PASS │
│ 5. Stage 6 Transactional Database Engine Implemented & Approved        │ ✅ PASS │
│ 6. All Stage Contracts Standardized to Version 1.0.0                   │ ✅ PASS │
│ 7. Live PostgreSQL 16.14 + PostGIS 3.6.4 Baseline (`wtc_evidence`) Active│ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Integration Test Strategy (12 Modules)

### 2.1 Integration Test Environment
- **Purpose:** Provide an isolated, reproducible execution environment mimicking production PostgreSQL 16.14 + PostGIS 3.6.4.
- **Inputs:** Local workspace directories (`data/incoming_pdfs/`, `data/processed_pdfs/`, `data/failed_pdfs/`) + active database `wtc_evidence`.
- **Outputs:** Verified test environment initialization.
- **Validation Method:** Run automated environment pre-check script verifying PostGIS extension state and directory permissions.
- **Failure Conditions:** PostGIS package uninitialized or database connection failure.

### 2.2 Test Dataset Selection
- **Purpose:** Select representative architectural drawing PDFs (clean PDFs, complex multi-floor plans, corrupt files, low-confidence scans).
- **Inputs:** PDF drawing suite (`drawing_aa18.pdf`, `drawing_aa121.pdf`, `corrupt_drawing.pdf`).
- **Outputs:** Tagged test dataset inventory.
- **Validation Method:** SHA-256 hash registration and metadata catalog audit.
- **Failure Conditions:** Missing test dataset files.

### 2.3 End-to-End Execution Workflow
- **Purpose:** Execute full sequential pipeline execution: `Stage 1` ──► `Stage 2` ──► `Stage 3` ──► `Stage 5` ──► `Stage 6`.
- **Inputs:** Raw input PDF in `data/incoming_pdfs/`.
- **Outputs:** Committed PostgreSQL database rows in `entities`, tier tables, and `relationships`.
- **Validation Method:** Sequential execution runner tracking JSON contract handoffs across all 5 stages.
- **Failure Conditions:** Stage execution crash or unhandled pipeline exception.

### 2.4 Contract Compatibility Verification
- **Purpose:** Verify data contract JSON schema compliance (`v1.0.0`) at every stage boundary.
- **Inputs:** `Stage1OutputContract`, `Stage2VectorContract`, `Stage3LayoutContract`, `Stage5DeduplicationContract`, `Stage6IngestionContract`.
- **Outputs:** JSON Schema validation report.
- **Validation Method:** Automated JSON Schema validator checking 100% of mandatory fields.
- **Failure Conditions:** Schema mismatch or missing required field.

### 2.5 Quarantine Workflow Verification
- **Purpose:** Verify that corrupted PDFs or low-confidence predictions are safely quarantined into `data/failed_pdfs/` without database corruption.
- **Inputs:** `corrupt_drawing.pdf` (invalid binary signature).
- **Outputs:** `quarantine_status = true` payload in `data/failed_pdfs/[HASH]_quarantine.json`.
- **Validation Method:** Inspect `data/failed_pdfs/` for file copy and JSON telemetry log.
- **Failure Conditions:** Corrupted file reaches Stage 6 or bypasses quarantine.

### 2.6 Human Review Workflow Verification
- **Purpose:** Verify that candidate predictions requiring human sign-off are blocked from database ingestion until sign-off is logged.
- **Inputs:** Stage 3/5 contract with `requires_human_review = true` and `review_signoff_timestamp = null`.
- **Outputs:** Stage 6 execution block and transaction rollback (`transaction_status = "ROLLED_BACK"`).
- **Validation Method:** Attempt to ingest unreviewed candidate; assert rollback execution.
- **Failure Conditions:** Unreviewed candidate committed to database.

### 2.7 Entity Creation Verification
- **Purpose:** Verify Master Entity Registry (`entities` ADR-005) inserts and physical tier table population (`spaces`, `elements`).
- **Inputs:** Validated Stage 5 contract payload.
- **Outputs:** Primary key records in `entities` and child tier tables.
- **Validation Method:** Run SQL `SELECT COUNT(*)` queries against `wtc_evidence`.
- **Failure Conditions:** Missing master entity registry row or missing physical tier row.

### 2.8 Deduplication Verification
- **Purpose:** Verify spatial IoU matching ($\text{IoU} \ge 0.90$) and entity lifecycle state promotion to `CORROBORATED`.
- **Inputs:** Re-ingested duplicate drawing sheet.
- **Outputs:** Citation count increment in `entity_evidence_citations`; lifecycle state `CORROBORATED`.
- **Validation Method:** Query `entity_evidence_citations` to verify citation merging without duplicate primary key creation.
- **Failure Conditions:** Duplicate primary key collision or missing citation link.

### 2.9 Citation Verification
- **Purpose:** Enforce Principle 2 (*Cite Sources*), verifying 100% of inserted entities reference valid drawing sheet codes (`A-A-18`, `A-A-121`).
- **Inputs:** Committed database rows.
- **Outputs:** Active junction rows in `entity_evidence_citations`.
- **Validation Method:** SQL query checking `entity_id` foreign key references in `entity_evidence_citations`.
- **Failure Conditions:** Uncited orphan entity record.

### 2.10 Database Ingestion Verification
- **Purpose:** Verify atomic database commit (`COMMIT;`) and zero orphan catalog records across all 12 schema tables.
- **Inputs:** Stage 6 transaction execution.
- **Outputs:** `transaction_status = "COMMITTED"`.
- **Validation Method:** Execute database integrity audit query checking single-parent `CHECK` constraints (`= 1`).
- **Failure Conditions:** Single-parent constraint violation or foreign key mismatch.

### 2.11 Rollback Verification
- **Purpose:** Verify atomic `ROLLBACK;` execution when a database error or constraint exception occurs during Stage 6.
- **Inputs:** Stage 6 execution payload with forced foreign key error.
- **Outputs:** `transaction_status = "ROLLED_BACK"`, 0 uncommitted catalog rows.
- **Validation Method:** Record pre-transaction row counts, trigger failure, and assert post-rollback row counts match exactly.
- **Failure Conditions:** Partial transaction commit or uncommitted orphan row remaining.

### 2.12 Success Criteria
- **Purpose:** Define non-negotiable quantitative criteria for Phase 4 Integration Test Plan sign-off.
- **Inputs:** End-to-end integration scorecard.
- **Outputs:** Phase 4 integration sign-off.
- **Validation Method:** 100% pass rate across all 11 test cases; 0 schema violations.
- **Failure Conditions:** Any test case failure.

---

## 3. Comprehensive Integration Test Cases

```text
INTEGRATION TEST CASE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Test Case ID & Title                                                   │ Expected│
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ TC-E2E-01: Clean Single-Sheet Ingestion (A-A-18)                        │ COMMITTED│
│ TC-E2E-02: Corrupted Binary PDF Quarantine Handling                    │ QUARANT │
│ TC-E2E-03: Low AI Confidence (<80) Quarantine Handling                 │ QUARANT │
│ TC-E2E-04: Human Review Gate Enforcement (Missing Signoff)             │ ROLLBACK│
│ TC-E2E-05: Duplicate Drawing Sheet Corroboration & Deduplication       │ CORROB  │
│ TC-E2E-06: ADR-005 Master Entity Registry Top-Down Order Check         │ COMMITTED│
│ TC-E2E-07: Single-Parent CHECK Constraint Integrity Audit               │ COMMITTED│
│ TC-E2E-08: Foreign Key ON DELETE RESTRICT Enforcement                  │ COMMITTED│
│ TC-E2E-09: PostGIS EPSG:2263 Spatial Transformation Integrity           │ COMMITTED│
│ TC-E2E-10: Forced Transaction Failure Atomic Rollback Audit            │ ROLLBACK│
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 4. Final Recommendation

```text
FINAL INTEGRATION TEST SELECTION:
[ ] Integration Testing Not Ready
[ ] Integration Testing Ready With Conditions
[X] Integration Testing Ready To Execute ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Integration Testing Ready To Execute`:
All 5 stage engines (`pdf_acquisition_preprocessor.py`, `vector_extraction_engine.py`, `ai_vision_layout_parser.py`, `deduplication_engine.py`, `database_ingestion_engine.py`) have been fully implemented, unit tested (19/19 tests passed), and validated for production use. The integration test plan is **FULLY READY TO EXECUTE**.
