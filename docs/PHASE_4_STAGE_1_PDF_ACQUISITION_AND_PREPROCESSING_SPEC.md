# Phase 4 Stage 1: PDF Acquisition and Preprocessing Technical Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 1 TECHNICAL SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Implementation Roadmap:** [`docs/PHASE_4_IMPLEMENTATION_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_IMPLEMENTATION_ROADMAP.md)  
**Parent Pipeline Governance:** [`docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md)  
**Parent Readiness Review:** [`docs/PHASE_4_IMPLEMENTATION_READINESS_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_IMPLEMENTATION_READINESS_REVIEW.md)  

---

## Executive Summary

This document establishes the **authoritative Stage 1 Technical Specification** governing **PDF Acquisition and Preprocessing** within Phase 4.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

This document details the 12 technical requirement modules, input/output contracts, validation rules, quarantine workflows, human review triggers, and acceptance criteria governing incoming PDF drawings prior to Stage 2 vector extraction.

---

## 1. Verified Facts

```text
EVIDENTIARY SPECIFICATION MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Phase 4 Implementation Readiness Authorized                         │ ✅ PASS │
│ 3. Phase 4 Pipeline Governance Rules Formally Defined                  │ ✅ PASS │
│ 4. Incoming PDF Directory Active (`data/incoming_pdfs/`)               │ ✅ PASS │
│ 5. Processed PDF Metadata Directory Active (`data/processed_pdfs/`)    │ ✅ PASS │
│ 6. Quarantine Directory Active (`data/failed_pdfs/`)                   │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Stage 1 Technical Requirements (12 Modules)

### 2.1 Supported PDF Formats
- **Purpose:** Restrict processing to valid, supported architectural PDF specifications.
- **Inputs:** Raw binary files from `data/incoming_pdfs/`.
- **Outputs:** Verified PDF specification compliance status.
- **Validation Rules:** PDF version $\ge 1.4$, unencrypted, non-password protected.
- **Failure Conditions:** Encrypted PDF, invalid PDF header, or corrupted trailer.
- **Governance Requirements:** Reject unsupported PDF versions to quarantine.

### 2.2 Input Directory Conventions
- **Purpose:** Standardize directory locations for incoming, processed, and failed PDF files.
- **Inputs:** `data/incoming_pdfs/` (Incoming), `data/processed_pdfs/` (Processed), `data/failed_pdfs/` (Quarantine).
- **Outputs:** Validated directory file handles.
- **Validation Rules:** All target paths exist within workspace boundaries.
- **Failure Conditions:** Directory path unreadable or missing write permissions.
- **Governance Requirements:** Prevent file ops outside workspace boundary (Principle 12).

### 2.3 File Discovery Workflow
- **Purpose:** Scan incoming directory for new PDF files and compute SHA-256 file hashes.
- **Inputs:** Directory scan on `data/incoming_pdfs/`.
- **Outputs:** File discovery queue item with SHA-256 hash and file timestamp.
- **Validation Rules:** File extension `.pdf` or `.PDF`, non-zero file size.
- **Failure Conditions:** 0-byte file or unreadable permissions.
- **Governance Requirements:** Audit logging of every discovered file (Principle 6).

### 2.4 Duplicate File Detection
- **Purpose:** Prevent duplicate processing of previously ingested PDF files.
- **Inputs:** Calculated SHA-256 file hash + database source log.
- **Outputs:** Unique file confirmation or duplicate flag.
- **Validation Rules:** SHA-256 hash does not exist in `sources` or `data/processed_pdfs/` audit index.
- **Failure Conditions:** Duplicate hash detected.
- **Governance Requirements:** Move duplicate files directly to archive; log duplicate event.

### 2.5 File Integrity Validation
- **Purpose:** Confirm PDF structure integrity before parsing.
- **Inputs:** Raw PDF binary stream.
- **Outputs:** Validated PDF document handle.
- **Validation Rules:** Magic bytes `%PDF-`, valid xref table, valid catalog dictionary.
- **Failure Conditions:** Corrupted xref table or truncated end-of-file marker (`%%EOF`).
- **Governance Requirements:** Quarantine corrupted files immediately to `data/failed_pdfs/`.

### 2.6 Metadata Extraction Requirements
- **Purpose:** Extract document-level metadata (CreationDate, Author, Producer, Title).
- **Inputs:** PDF info dictionary.
- **Outputs:** JSON metadata payload.
- **Validation Rules:** Extract available standard key-value pairs.
- **Failure Conditions:** Missing info dictionary (non-fatal, fall back to default metadata).
- **Governance Requirements:** Store metadata in document tracking record.

### 2.7 Page Counting Requirements
- **Purpose:** Count total pages and isolate individual architectural drawing sheets.
- **Inputs:** PDF page tree.
- **Outputs:** Page count integer $N \ge 1$.
- **Validation Rules:** Page count $> 0$.
- **Failure Conditions:** 0 pages reported.
- **Governance Requirements:** Multi-page PDFs split into single-sheet page streams for processing.

### 2.8 Rotation Detection Requirements
- **Purpose:** Detect page orientation (0°, 90°, 180°, 270°) and normalize to landscape/upright view.
- **Inputs:** PDF page `/Rotate` key + OCR text orientation angle.
- **Outputs:** Normalized page rendering stream (rotated to 0° upright orientation).
- **Validation Rules:** Orientation angle $\in \{0, 90, 180, 270\}$.
- **Failure Conditions:** Ambiguous text orientation.
- **Governance Requirements:** Flag 180° upside-down pages for human review gate.

### 2.9 Title Block Extraction Requirements
- **Purpose:** Isolate drawing title block area (typically bottom-right quadrant) for metadata parsing.
- **Inputs:** Page bounding box geometry ($X_{\text{min}}, Y_{\text{min}}, X_{\text{max}}, Y_{\text{max}}$).
- **Outputs:** Cropped title block region bounding box.
- **Validation Rules:** Title block area covers lower-right 25% of page area.
- **Failure Conditions:** Missing or obscured title block region.
- **Governance Requirements:** Route pages with unparseable title blocks to human review.

### 2.10 Sheet Code Extraction Requirements
- **Purpose:** Parse drawing sheet code (e.g., `A-A-18`, `A-A-121`, `S-1`, `M-7`) from title block text.
- **Governing Standard:** Principle 2 (*Cite Sources*).
- **Inputs:** Title block text bounding box.
- **Outputs:** Verified sheet code string.
- **Validation Rules:** Match canonical WTC sheet code regex pattern (`^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$`).
- **Failure Conditions:** Regex mismatch or missing sheet code.
- **Governance Requirements:** Sheet code extraction is MANDATORY; missing sheet code blocks Stage 2.

### 2.11 Failure Handling Requirements
- **Purpose:** Provide graceful exception isolation without crashing batch execution.
- **Inputs:** Exception signals during Stages 2.1–2.10.
- **Outputs:** Formatted error log + quarantine disposition.
- **Validation Rules:** Catch all PDF parsing exceptions (`PyMuPDFError`, `PDFSyntaxError`).
- **Failure Conditions:** Unhandled exception crash.
- **Governance Requirements:** Log stack trace to `data/failed_pdfs/error.log` and move PDF to quarantine.

### 2.12 Quarantine Requirements
- **Purpose:** Quarantine unparseable, duplicate, or corrupted PDF files.
- **Inputs:** Failed PDF file handle + error disposition.
- **Outputs:** File moved to `data/failed_pdfs/[HASH]_[FILENAME]`.
- **Validation Rules:** Source file removed from `data/incoming_pdfs/` after move.
- **Failure Conditions:** Move operation fails.
- **Governance Requirements:** Quarantine folder must be reviewed during weekly human review gate.

---

## 3. Input & Output Contracts

### Input Contract (`Stage 1 Input`)
```json
{
  "file_path": "data/incoming_pdfs/drawing_aa18.pdf",
  "expected_format": "PDF-1.4+",
  "max_file_size_bytes": 104857600
}
```

### Output Contract (`Stage 1 Output`)
```json
{
  "file_path": "data/incoming_pdfs/drawing_aa18.pdf",
  "sha256_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "status": "VALIDATED",
  "page_count": 1,
  "sheet_code": "A-A-18",
  "drawing_title": "SUB-GRADE FLOOR PLAN B1 & B2",
  "rotation_angle": 0,
  "title_block_found": true,
  "quarantined": false
}
```

---

## 4. Human Review & Acceptance Criteria

### Human Review Triggers
1. Unparseable drawing sheet code.
2. 180° upside-down page rotation.
3. Obscured or non-standard title block.

### Stage 1 Acceptance Criteria
- 100% of incoming PDFs processed into either `VALIDATED` output contracts or `QUARANTINED` files.
- Zero 0-byte or corrupted files left in `data/incoming_pdfs/`.
- 100% of validated outputs contain a non-empty `sheet_code` matching Principle 2.

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 4 STAGE 1 TECHNICAL SPECIFICATION COMPLETE — READY FOR STAGE 1 CODE IMPLEMENTATION
