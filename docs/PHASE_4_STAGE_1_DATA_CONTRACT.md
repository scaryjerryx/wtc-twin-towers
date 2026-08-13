# Phase 4 Stage 1: Data Contract Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 1 DATA CONTRACT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Technical Spec:** [`docs/PHASE_4_STAGE_1_PDF_ACQUISITION_AND_PREPROCESSING_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_1_PDF_ACQUISITION_AND_PREPROCESSING_SPEC.md)  
**Parent Governance Rules:** [`docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md)  
**Contract Version:** `1.0.0`  

---

## Executive Summary

This document establishes the **authoritative Stage 1 Data Contract Specification** defining the exact JSON schema produced by Stage 1 (PDF Acquisition and Preprocessing) and consumed by Stage 2 (Vector Extraction).

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this contract specification document.

This contract freezes the interface between Stage 1 and downstream pipeline stages, detailing every required field, data type, validation rule, quarantine schema, versioning rule, and acceptance criteria.

---

## 1. Verified Facts

```text
CONTRACT SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 1 Technical Specification Formally Defined                    │ ✅ PASS │
│ 3. Contract Version Standardized to Semantic Versioning (`1.0.0`)       │ ✅ PASS │
│ 4. Mandatory Fields Required by Principle 2 (Cite Sources) Included     │ ✅ PASS │
│ 5. Quarantine & Error Reporting Payloads Formally Specified             │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Complete Stage 1 Output Contract Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage1OutputContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "file_hash",
    "file_name",
    "file_path",
    "file_size_bytes",
    "page_count",
    "sheet_code",
    "extraction_timestamp",
    "validation_status",
    "quarantine_status",
    "metadata",
    "title_block_data",
    "processing_errors"
  ],
  "properties": {
    "contract_version": {
      "type": "string",
      "example": "1.0.0"
    },
    "file_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$",
      "example": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    "file_name": {
      "type": "string",
      "example": "drawing_aa18.pdf"
    },
    "file_path": {
      "type": "string",
      "example": "data/incoming_pdfs/drawing_aa18.pdf"
    },
    "file_size_bytes": {
      "type": "integer",
      "minimum": 1,
      "example": 2457600
    },
    "page_count": {
      "type": "integer",
      "minimum": 1,
      "example": 1
    },
    "sheet_code": {
      "type": "string",
      "pattern": "^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$",
      "example": "A-A-18"
    },
    "extraction_timestamp": {
      "type": "string",
      "format": "date-time",
      "example": "2026-08-12T22:19:25Z"
    },
    "validation_status": {
      "type": "string",
      "enum": ["VALIDATED", "WARNING", "FAILED"],
      "example": "VALIDATED"
    },
    "quarantine_status": {
      "type": "boolean",
      "example": false
    },
    "metadata": {
      "type": "object",
      "required": ["pdf_version", "author", "creator", "producer", "creation_date"],
      "properties": {
        "pdf_version": {"type": "string", "example": "1.7"},
        "author": {"type": "string", "example": "Minoru Yamasaki & Associates"},
        "creator": {"type": "string", "example": "AutoCAD 2024"},
        "producer": {"type": "string", "example": "PDFium"},
        "creation_date": {"type": "string", "example": "1973-05-14T00:00:00Z"}
      }
    },
    "title_block_data": {
      "type": "object",
      "required": ["title_block_found", "drawing_title", "sheet_number", "scale", "revision"],
      "properties": {
        "title_block_found": {"type": "boolean", "example": true},
        "drawing_title": {"type": "string", "example": "SUB-GRADE FLOOR PLAN B1 & B2"},
        "sheet_number": {"type": "string", "example": "A-A-18"},
        "scale": {"type": "string", "example": "1/8\" = 1'-0\""},
        "revision": {"type": "string", "example": "Rev 4"}
      }
    },
    "processing_errors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["error_code", "error_message", "severity", "timestamp"],
        "properties": {
          "error_code": {"type": "string", "example": "ERR_SHEET_CODE_MISSING"},
          "error_message": {"type": "string", "example": "Failed to extract sheet code from title block"},
          "severity": {"type": "string", "enum": ["INFO", "WARNING", "CRITICAL"], "example": "WARNING"},
          "timestamp": {"type": "string", "format": "date-time", "example": "2026-08-12T22:19:25Z"}
        }
      }
    }
  }
}
```

---

## 3. Comprehensive Field Definitions

| Field Name | Data Type | Req/Opt | Description | Validation Rules |
| :--- | :--- | :--- | :--- | :--- |
| `contract_version` | `string` | **Required** | Contract semantic version string | Must equal `"1.0.0"` |
| `file_hash` | `string` | **Required** | SHA-256 hash of PDF binary stream | Exactly 64 hex characters (`^[a-f0-9]{64}$`) |
| `file_name` | `string` | **Required** | Basename of original PDF file | Non-empty string, `.pdf` extension |
| `file_path` | `string` | **Required** | Absolute or workspace relative file path | Valid readable file path |
| `file_size_bytes` | `integer` | **Required** | Size of PDF file in bytes | Integer $> 0$ |
| `page_count` | `integer` | **Required** | Total page count of document | Integer $\ge 1$ |
| `sheet_code` | `string` | **Required** | Drawing sheet identifier (Principle 2) | Regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$` |
| `extraction_timestamp` | `string` | **Required** | ISO 8601 UTC timestamp of parsing | Format `YYYY-MM-DDTHH:MM:SSZ` |
| `validation_status` | `string` | **Required** | Stage 1 validation outcome status | Enum `VALIDATED`, `WARNING`, `FAILED` |
| `quarantine_status` | `boolean` | **Required** | Flag indicating if file was quarantined | `true` or `false` |
| `metadata` | `object` | **Required** | PDF document catalog metadata | Contains `pdf_version`, `author`, `creator` |
| `title_block_data` | `object` | **Required** | Parsed title block metadata fields | Contains `drawing_title`, `scale`, `revision` |
| `processing_errors` | `array` | **Required** | List of non-fatal/fatal processing errors | Array of error objects (empty if no errors) |

---

## 4. Quarantine Contract Specification

If `quarantine_status = true` or `validation_status = FAILED`, Stage 1 MUST output a Quarantine Disposition Payload to `data/failed_pdfs/[HASH]_quarantine.json`:

```json
{
  "contract_version": "1.0.0",
  "file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "file_name": "corrupt_drawing.pdf",
  "quarantine_reason": "CRITICAL_XREF_CORRUPTED",
  "quarantine_timestamp": "2026-08-12T22:19:25Z",
  "quarantined_file_location": "data/failed_pdfs/e3b0c442_corrupt_drawing.pdf",
  "human_review_required": true,
  "processing_errors": [
    {
      "error_code": "ERR_XREF_CORRUPTED",
      "error_message": "PDF trailer dictionary unreadable; invalid xref table",
      "severity": "CRITICAL",
      "timestamp": "2026-08-12T22:19:25Z"
    }
  ]
}
```

---

## 5. Downstream Dependencies & Contract Freeze Status

- **Downstream Consumer:** Stage 2 Vector Extraction & Stage 3 Vision Parser.
- **Contract Interface Status:** **FROZEN AT VERSION 1.0.0**.
- **Governance Sign-off:** ✅ Approved for pipeline interface usage.
