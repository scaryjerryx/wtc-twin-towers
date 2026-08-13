# Phase 4 Stage 2: Vector Data Contract Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 2 VECTOR DATA CONTRACT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Technical Spec:** [`docs/PHASE_4_STAGE_2_VECTOR_EXTRACTION_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_2_VECTOR_EXTRACTION_SPEC.md)  
**Parent Upstream Contract:** [`docs/PHASE_4_STAGE_1_DATA_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_1_DATA_CONTRACT.md)  
**Contract Version:** `1.0.0`  

---

## Executive Summary

This document establishes the **authoritative Stage 2 Vector Data Contract Specification** defining the exact JSON schema produced by Stage 2 (Vector Extraction) and consumed by Stage 3 (AI Vision Parsing).

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this contract specification document.

This contract freezes the vector geometry interface, detailing every required field, data type, polyline/polygon schema, text annotation schema, PostGIS spatial reference system (`EPSG:2263`), validation rule, quarantine payload, and acceptance criteria.

---

## 1. Verified Facts

```text
CONTRACT SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 1 Data Contract Formally Frozen (`Stage1OutputContract` 1.0.0)│ ✅ PASS │
│ 3. Stage 2 Technical Specification Formally Defined                    │ ✅ PASS │
│ 4. Contract Version Standardized to Semantic Versioning (`1.0.0`)       │ ✅ PASS │
│ 5. PostGIS 2D Spatial Reference System (`EPSG:2263`) Integrated        │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Complete Stage 2 Vector Output Contract Schema (`Stage2VectorContract`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage2VectorContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "source_file_hash",
    "source_sheet_code",
    "extraction_timestamp",
    "coordinate_system",
    "vector_objects",
    "geometry_validation",
    "confidence_score",
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
    "extraction_timestamp": {
      "type": "string",
      "format": "date-time",
      "example": "2026-08-12T22:21:30Z"
    },
    "coordinate_system": {
      "type": "object",
      "required": ["srid", "projection_name", "drawing_scale", "unit"],
      "properties": {
        "srid": {"type": "integer", "example": 2263},
        "projection_name": {"type": "string", "example": "NAD83 / New York Long Island (ftUS)"},
        "drawing_scale": {"type": "string", "example": "1/8\" = 1'-0\""},
        "unit": {"type": "string", "example": "us_survey_feet"}
      }
    },
    "vector_objects": {
      "type": "object",
      "required": ["polylines", "polygons", "text_annotations"],
      "properties": {
        "polylines": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["line_id", "cad_layer", "vertex_count", "wkt_geometry"],
            "properties": {
              "line_id": {"type": "string", "example": "line_aa18_101"},
              "cad_layer": {"type": "string", "example": "GRID_LINES"},
              "vertex_count": {"type": "integer", "minimum": 2, "example": 2},
              "wkt_geometry": {"type": "string", "example": "LINESTRING(982100 198200, 982100 199000)"}
            }
          }
        },
        "polygons": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["polygon_id", "cad_layer", "vertex_count", "wkt_geometry", "area_sq_ft", "is_valid"],
            "properties": {
              "polygon_id": {"type": "string", "example": "poly_aa18_501"},
              "cad_layer": {"type": "string", "example": "WALLS"},
              "vertex_count": {"type": "integer", "minimum": 4, "example": 5},
              "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
              "area_sq_ft": {"type": "number", "minimum": 0.0, "example": 40000.0},
              "is_valid": {"type": "boolean", "example": true}
            }
          }
        },
        "text_annotations": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["text_id", "text_content", "cad_layer", "bounding_box_wkt", "associated_polygon_id"],
            "properties": {
              "text_id": {"type": "string", "example": "txt_aa18_12"},
              "text_content": {"type": "string", "example": "SUB-GRADE BOOSTER PUMP ROOM"},
              "cad_layer": {"type": "string", "example": "ANNO"},
              "bounding_box_wkt": {"type": "string", "example": "POLYGON((982150 198250, 982250 198250, 982250 198280, 982150 198280, 982150 198250))"},
              "associated_polygon_id": {"type": ["string", "null"], "example": "poly_aa18_501"}
            }
          }
        }
      }
    },
    "geometry_validation": {
      "type": "object",
      "required": ["total_geometries", "valid_geometries", "repaired_geometries", "invalid_geometries", "pass_rate_percentage"],
      "properties": {
        "total_geometries": {"type": "integer", "example": 522},
        "valid_geometries": {"type": "integer", "example": 515},
        "repaired_geometries": {"type": "integer", "example": 7},
        "invalid_geometries": {"type": "integer", "example": 0},
        "pass_rate_percentage": {"type": "number", "example": 100.0}
      }
    },
    "confidence_score": {
      "type": "integer",
      "minimum": 0,
      "maximum": 100,
      "example": 98
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
          "error_code": {"type": "string", "example": "WARN_POLYGON_AUTO_REPAIRED"},
          "error_message": {"type": "string", "example": "Self-intersecting ring auto-repaired via ST_MakeValid"},
          "severity": {"type": "string", "enum": ["INFO", "WARNING", "CRITICAL"], "example": "WARNING"},
          "timestamp": {"type": "string", "format": "date-time", "example": "2026-08-12T22:21:30Z"}
        }
      }
    }
  }
}
```

---

## 3. Detailed Vector Field Definitions Table

| Field Name | Data Type | Req/Opt | Description | Validation Rules |
| :--- | :--- | :--- | :--- | :--- |
| `contract_version` | `string` | **Required** | Contract semantic version string | Must equal `"1.0.0"` |
| `source_file_hash` | `string` | **Required** | SHA-256 binary hash of source PDF | Exactly 64 hex characters |
| `source_sheet_code` | `string` | **Required** | Drawing sheet ID (Principle 2) | Regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$` |
| `extraction_timestamp` | `string` | **Required** | ISO 8601 UTC parsing timestamp | Format `YYYY-MM-DDTHH:MM:SSZ` |
| `coordinate_system` | `object` | **Required** | PostGIS spatial reference object | Contains `srid: 2263`, `projection_name` |
| `vector_objects` | `object` | **Required** | Extracted vector graphics collection | Contains `polylines`, `polygons`, `text` |
| `geometry_validation` | `object` | **Required** | PostGIS `ST_IsValid` audit scorecard | `pass_rate_percentage >= 95.0` |
| `confidence_score` | `integer` | **Required** | Extraction confidence rating | Integer $[80, 100]$ (Principle 5) |
| `validation_status` | `string` | **Required** | Stage 2 validation outcome status | Enum `VALIDATED`, `WARNING`, `FAILED` |
| `quarantine_status` | `boolean` | **Required** | Flag indicating if file was quarantined | `true` or `false` |
| `processing_errors` | `array` | **Required** | List of non-fatal/fatal processing errors | Array of error objects (empty if clean) |

---

## 4. Quarantine Contract Specification

If `quarantine_status = true` or `geometry_validation.pass_rate_percentage < 95.0`, Stage 2 MUST output a Vector Quarantine Payload to `data/failed_pdfs/[HASH]_vector_quarantine.json`:

```json
{
  "contract_version": "1.0.0",
  "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "source_sheet_code": "A-A-18",
  "quarantine_reason": "GEOMETRY_PASS_RATE_BELOW_THRESHOLD",
  "pass_rate_percentage": 82.4,
  "quarantine_timestamp": "2026-08-12T22:21:30Z",
  "processing_errors": [
    {
      "error_code": "ERR_GEOMETRY_INVALID",
      "error_message": "25 polygons failed PostGIS ST_IsValid check and ST_MakeValid repair",
      "severity": "CRITICAL",
      "timestamp": "2026-08-12T22:21:30Z"
    }
  ]
}
```

---

## 5. Stage 3 Dependencies & Contract Freeze Status

- **Downstream Consumer:** Stage 3 AI Vision Layout Parser & Stage 5 Deduplication/Ingestion.
- **Contract Interface Status:** **FROZEN AT VERSION 1.0.0**.
- **Governance Sign-off:** ✅ Approved for vector output usage.
