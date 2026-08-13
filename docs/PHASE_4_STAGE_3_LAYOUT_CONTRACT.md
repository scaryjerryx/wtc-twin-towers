# Phase 4 Stage 3: Layout Data Contract Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 3 LAYOUT DATA CONTRACT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Technical Spec:** [`docs/PHASE_4_STAGE_3_AI_VISION_LAYOUT_PARSER_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_3_AI_VISION_LAYOUT_PARSER_SPEC.md)  
**Parent Upstream Contract:** [`docs/PHASE_4_STAGE_2_VECTOR_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_2_VECTOR_CONTRACT.md)  
**Contract Version:** `1.0.0`  

---

## Executive Summary

This document establishes the **authoritative Stage 3 Layout Data Contract Specification** defining the exact JSON schema produced by Stage 3 (AI Vision Layout Parser) and consumed by downstream pipeline stages (Stage 5 Deduplication and Stage 6 Ingestion).

Zero implementation code, zero model prompts, zero AI agents, zero SQL modifications, zero database schema changes, and zero web searches were created in this contract specification document.

This contract freezes the AI layout recognition interface, detailing every required field, data type, OCR result schema, symbol recognition schema, visual bounding box schema, confidence scoring rules ($[80, 100]$), human review status schema, evidence linkage schema, quarantine contract, and acceptance criteria.

---

## 1. Verified Facts

```text
CONTRACT SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 2 Vector Data Contract Formally Frozen (`Stage2VectorContract`)│ ✅ PASS │
│ 3. Stage 3 Technical Specification Formally Defined                    │ ✅ PASS │
│ 4. Contract Version Standardized to Semantic Versioning (`1.0.0`)       │ ✅ PASS │
│ 5. Mandatory Conflict Resolution Matrix Integrated                     │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Complete Stage 3 Layout Output Contract Schema (`Stage3LayoutContract`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage3LayoutContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "source_file_hash",
    "source_sheet_code",
    "parsing_timestamp",
    "detected_entities",
    "ocr_results",
    "symbol_detections",
    "confidence_summary",
    "human_review_status",
    "validation_status",
    "quarantine_status",
    "processing_errors"
  ],
  "properties": {
    "contract_version": {
      "type": "string",
      "example": "1.0.0"
    },
    "source_file_hash": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$",
      "example": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    },
    "source_sheet_code": {
      "type": "string",
      "pattern": "^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$",
      "example": "A-A-18"
    },
    "parsing_timestamp": {
      "type": "string",
      "format": "date-time",
      "example": "2026-08-12T22:23:52Z"
    },
    "detected_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "entity_id",
          "entity_name",
          "category",
          "bounding_box",
          "wkt_geometry",
          "confidence_score",
          "evidence_citation"
        ],
        "properties": {
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "entity_name": {"type": "string", "example": "Sub-grade Fan Room 101"},
          "category": {"type": "string", "example": "service_area"},
          "bounding_box": {
            "type": "object",
            "required": ["x_min", "y_min", "x_max", "y_max"],
            "properties": {
              "x_min": {"type": "number", "example": 982100.0},
              "y_min": {"type": "number", "example": 198200.0},
              "x_max": {"type": "number", "example": 982300.0},
              "y_max": {"type": "number", "example": 198400.0}
            }
          },
          "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
          "confidence_score": {"type": "integer", "minimum": 80, "maximum": 100, "example": 95},
          "evidence_citation": {
            "type": "object",
            "required": ["source_id", "sheet_code"],
            "properties": {
              "source_id": {"type": "string", "example": "src_yamasaki_drawings"},
              "sheet_code": {"type": "string", "example": "A-A-18"}
            }
          }
        }
      }
    },
    "ocr_results": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["ocr_id", "extracted_text", "confidence", "bounding_box", "associated_entity_id"],
        "properties": {
          "ocr_id": {"type": "string", "example": "ocr_aa18_12"},
          "extracted_text": {"type": "string", "example": "SUB-GRADE FAN ROOM 101"},
          "confidence": {"type": "integer", "minimum": 0, "maximum": 100, "example": 92},
          "bounding_box": {
            "type": "object",
            "required": ["x_min", "y_min", "x_max", "y_max"],
            "properties": {
              "x_min": {"type": "number", "example": 982150.0},
              "y_min": {"type": "number", "example": 198250.0},
              "x_max": {"type": "number", "example": 982250.0},
              "y_max": {"type": "number", "example": 198280.0}
            }
          },
          "associated_entity_id": {"type": ["string", "null"], "example": "wtc1_f1_fan_room_101"}
        }
      }
    },
    "symbol_detections": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["symbol_id", "symbol_type", "orientation_deg", "confidence_score"],
        "properties": {
          "symbol_id": {"type": "string", "example": "sym_north_1"},
          "symbol_type": {"type": "string", "example": "NORTH_ARROW"},
          "orientation_deg": {"type": "integer", "example": 0},
          "confidence_score": {"type": "integer", "example": 99}
        }
      }
    },
    "confidence_summary": {
      "type": "object",
      "required": ["average_confidence", "min_confidence", "max_confidence", "low_confidence_count"],
      "properties": {
        "average_confidence": {"type": "number", "example": 94.5},
        "min_confidence": {"type": "integer", "example": 82},
        "max_confidence": {"type": "integer", "example": 100},
        "low_confidence_count": {"type": "integer", "example": 0}
      }
    },
    "human_review_status": {
      "type": "object",
      "required": ["requires_human_review", "review_reason", "flagged_entity_ids"],
      "properties": {
        "requires_human_review": {"type": "boolean", "example": false},
        "review_reason": {"type": ["string", "null"], "example": null},
        "flagged_entity_ids": {"type": "array", "items": {"type": "string"}}
      }
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
    "processing_errors": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["error_code", "error_message", "severity", "timestamp"],
        "properties": {
          "error_code": {"type": "string", "example": "INFO_OCR_TEXT_RECONCILED"},
          "error_message": {"type": "string", "example": "OCR text aligned with vector CAD label"},
          "severity": {"type": "string", "enum": ["INFO", "WARNING", "CRITICAL"], "example": "INFO"},
          "timestamp": {"type": "string", "format": "date-time", "example": "2026-08-12T22:23:52Z"}
        }
      }
    }
  }
}
```

---

## 3. Detailed Field Definitions Table

| Field Name | Data Type | Req/Opt | Description | Validation Rules |
| :--- | :--- | :--- | :--- | :--- |
| `contract_version` | `string` | **Required** | Semantic version string | Must equal `"1.0.0"` |
| `source_file_hash` | `string` | **Required** | SHA-256 binary hash of source PDF | Exactly 64 hex characters |
| `source_sheet_code` | `string` | **Required** | Drawing sheet ID (Principle 2) | Regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$` |
| `parsing_timestamp` | `string` | **Required** | ISO 8601 UTC parsing timestamp | Format `YYYY-MM-DDTHH:MM:SSZ` |
| `detected_entities` | `array` | **Required** | List of visual entity candidates | Contains category, bounding_box, geometry |
| `ocr_results` | `array` | **Required** | List of OCR character recognition records | `confidence >= 80`, text string |
| `symbol_detections` | `array` | **Required** | Recognized architectural CAD symbols | Contains `symbol_type`, `orientation_deg` |
| `confidence_summary` | `object` | **Required** | Aggregated AI confidence metrics | `min_confidence >= 80` (Principle 5) |
| `human_review_status` | `object` | **Required** | Review gate triggers & flagged IDs | Object containing `requires_human_review` |
| `validation_status` | `string` | **Required** | Stage 3 validation outcome status | Enum `VALIDATED`, `WARNING`, `FAILED` |
| `quarantine_status` | `boolean` | **Required** | Flag indicating if job was quarantined | `true` or `false` |
| `processing_errors` | `array` | **Required** | List of processing error objects | Array of error objects (empty if clean) |

---

## 4. Quarantine Contract Specification

If `quarantine_status = true` or `confidence_summary.min_confidence < 80`, Stage 3 MUST output a Layout Quarantine Payload to `data/failed_pdfs/[HASH]_layout_quarantine.json`:

```json
{
  "contract_version": "1.0.0",
  "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "source_sheet_code": "A-A-18",
  "quarantine_reason": "AI_CONFIDENCE_BELOW_MINIMUM_THRESHOLD",
  "min_confidence_observed": 68,
  "quarantine_timestamp": "2026-08-12T22:23:52Z",
  "processing_errors": [
    {
      "error_code": "ERR_CONFIDENCE_LOW",
      "error_message": "12 visual layout candidates scored composite confidence < 80",
      "severity": "CRITICAL",
      "timestamp": "2026-08-12T22:23:52Z"
    }
  ]
}
```

---

## 5. Downstream Dependencies & Contract Freeze Status

- **Downstream Consumer:** Stage 5 PostGIS Deduplication & Stage 6 Transactional Database Ingestion.
- **Contract Interface Status:** **FROZEN AT VERSION 1.0.0**.
- **Governance Sign-off:** ✅ Approved for Stage 3 AI Vision layout contract usage.
