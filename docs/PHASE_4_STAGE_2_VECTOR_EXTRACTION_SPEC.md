# Phase 4 Stage 2: Vector Extraction Technical Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 2 TECHNICAL SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Output Contract:** [`docs/PHASE_4_STAGE_1_DATA_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_1_DATA_CONTRACT.md)  
**Parent Implementation Roadmap:** [`docs/PHASE_4_IMPLEMENTATION_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_IMPLEMENTATION_ROADMAP.md)  
**Frozen Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

---

## Executive Summary

This document establishes the **authoritative Stage 2 Technical Specification** governing **Vector Extraction** within Phase 4.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

Stage 2 consumes the validated Stage 1 data contract (`Stage1OutputContract`) and extracts raw CAD vector primitives (polylines, polygons, arcs, text annotation bounding boxes), normalizing them into PostGIS-compatible 2D spatial geometries in `EPSG:2263`.

---

## 1. Verified Facts

```text
SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 1 Data Contract Formally Frozen (`Stage1OutputContract` 1.0.0)│ ✅ PASS │
│ 3. PostGIS 2D Spatial Indices Active in `EPSG:2263`                    │ ✅ PASS │
│ 4. Stage 2 Vector Extraction Requirements Defined Across 12 Modules    │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Stage 2 Technical Requirements (12 Modules)

### 2.1 Stage 2 Inputs
- **Purpose:** Ingest validated Stage 1 JSON contract payloads (`Stage1OutputContract`).
- **Inputs:** `Stage1OutputContract` (version `1.0.0`) from Stage 1.
- **Outputs:** Verified vector parsing queue item.
- **Validation Rules:** `validation_status` must equal `"VALIDATED"`, `quarantine_status` must equal `false`, non-empty `sheet_code`.
- **Failure Conditions:** Input payload validation failure or missing PDF file.
- **Governance Requirements:** Block unvalidated Stage 1 outputs from entering Stage 2.

### 2.2 Supported Vector Object Types
- **Purpose:** Specify supported native PDF vector primitives for extraction.
- **Inputs:** PDF graphics stream primitives.
- **Outputs:** Structured vector primitive records (`Line`, `Polyline`, `ClosedPolygon`, `Arc`, `TextAnnotation`).
- **Validation Rules:** Primitives must possess valid page coordinates.
- **Failure Conditions:** Unsupported path command or corrupted graphics stream.
- **Governance Requirements:** Log unhandled vector object types without crashing parser.

### 2.3 Polyline Extraction Rules
- **Purpose:** Parse continuous 2D line segments forming structural grid lines and wall boundaries.
- **Inputs:** PDF path construction operators (`m`, `l`, `c`, `v`, `y`).
- **Outputs:** 2D Polyline geometry coordinate arrays `[(x1, y1), (x2, y2), ...]`.
- **Validation Rules:** Polyline contains $\ge 2$ distinct vertices.
- **Failure Conditions:** Zero-length line segments ($p_1 = p_2$).
- **Governance Requirements:** Filter zero-length line artifacts to prevent spatial index distortion.

### 2.4 Polygon Extraction Rules
- **Purpose:** Construct closed 2D polygon footprints for zones, spaces, and structural columns.
- **Inputs:** Closed polyline paths (`h` operator or matching start/end vertex $p_{\text{start}} = p_{\text{end}}$).
- **Outputs:** PostGIS-compatible 2D Polygon rings (`POLYGON((x1 y1, x2 y2, ..., x1 y1))`).
- **Validation Rules:** Closed polygon contains $\ge 4$ vertices (including closing vertex); non-self-intersecting.
- **Failure Conditions:** Open path or self-intersecting polygon (`ST_IsValid = false`).
- **Governance Requirements:** Execute polygon closing algorithms on open paths within 0.5pt vertex tolerance.

### 2.5 Text Extraction Rules
- **Purpose:** Extract text labels, room names, column tags (e.g., `Col 501`, `Elevator 50`), and spatial bounding boxes.
- **Inputs:** PDF text operators (`Tj`, `TJ`, `ET`) + text matrix transformations.
- **Outputs:** Text string + 2D bounding box geometry (`BBOX(x_min, y_min, x_max, y_max)`).
- **Validation Rules:** Text string non-empty; bounding box area $> 0$.
- **Failure Conditions:** Encoded font glyph mapping failure.
- **Governance Requirements:** Associate text labels with nearest intersecting polygon footprint.

### 2.6 Coordinate Normalization Rules
- **Purpose:** Transform PDF page coordinates (72 points/inch, origin bottom-left) into PostGIS NAD83 / NYC State Plane Feet (`EPSG:2263`).
- **Inputs:** Raw PDF vector coordinates + drawing scale metadata (e.g., `1/8" = 1'-0"`).
- **Outputs:** Transformed 2D spatial coordinates in `EPSG:2263`.
- **Validation Rules:** Linear scaling transform applied; coordinates within NYC WTC spatial extent bounds.
- **Failure Conditions:** Missing drawing scale or coordinate out-of-bounds.
- **Governance Requirements:** Require drawing scale metadata for spatial transformation; flag unscaled vectors.

### 2.7 Layer Classification Rules
- **Purpose:** Classify vector primitives into architectural layers (`GRID_LINES`, `WALLS`, `COLUMNS`, `STAIRS`, `ANNO`).
- **Inputs:** PDF Optional Content Groups (OCG) / layer names + line style properties (color, stroke width, dash pattern).
- **Outputs:** Layer-tagged vector objects.
- **Validation Rules:** Tagged with valid layer ENUM string.
- **Failure Conditions:** Unlayered vector stream (fall back to style-based classification).
- **Governance Requirements:** Log layer classification confidence score.

### 2.8 Geometry Validation Rules
- **Purpose:** Execute PostGIS spatial validation checks (`ST_IsValid`, `ST_IsSimple`, `ST_Area`).
- **Inputs:** Transformed 2D polygon footprints in `EPSG:2263`.
- **Outputs:** Validated 2D PostGIS polygon objects.
- **Validation Rules:** `ST_IsValid(geom) = true`, `ST_SRID(geom) = 2263`, `ST_Area(geom) > 0.0`.
- **Failure Conditions:** Self-intersecting polygon or invalid topology.
- **Governance Requirements:** Route invalid geometries to PostGIS `ST_MakeValid` auto-repair engine; flag for review if repair fails.

### 2.9 Output Requirements
- **Purpose:** Produce structured Stage 2 output contract (`Stage2VectorContract`) consumed by Stage 3 AI Vision & Stage 4 Ingestion.
- **Inputs:** Processed vector objects + spatial geometries.
- **Outputs:** `Stage2VectorContract` JSON payload.
- **Validation Rules:** Schema compliant; non-empty vector lists.
- **Failure Conditions:** JSON serialization failure.
- **Governance Requirements:** Freeze output contract schema at version `1.0.0`.

### 2.10 Quarantine Conditions
- **Purpose:** Quarantine PDFs with unparseable or severely corrupted vector layers.
- **Inputs:** Extraction exception signals.
- **Outputs:** Quarantine disposition payload.
- **Validation Rules:** Quarantined if 0 valid vector primitives extracted or $> 50\%$ invalid geometries.
- **Failure Conditions:** Vector stream parsing crash.
- **Governance Requirements:** Move file to `data/failed_pdfs/` and log error stack trace.

### 2.11 Human Review Requirements
- **Purpose:** Flag complex or un-repairable vector geometries for human review.
- **Inputs:** Failed `ST_MakeValid` auto-repair objects or unscaled vector layers.
- **Outputs:** Human review queue ticket.
- **Validation Rules:** Human review triggered on ambiguous layer classification or geometry repair failure.
- **Failure Conditions:** Bypassing human review for flagged geometries.
- **Governance Requirements:** Enforce human sign-off before flagged geometries enter ingestion queue.

### 2.12 Acceptance Criteria
- **Purpose:** Define quantitative acceptance thresholds for Stage 2 completion.
- **Inputs:** Stage 2 validation scorecard.
- **Outputs:** Stage 2 completion sign-off.
- **Validation Rules:** $\ge 95\%$ of vector polygons pass `ST_IsValid = true`, 100% of spatial coordinates transformed to `EPSG:2263`.
- **Failure Conditions:** Vector extraction pass rate $< 95\%$.
- **Governance Requirements:** Total compliance with Principle 1 (*Evidence Over Assumptions*).

---

## 3. Vector Extraction Output Contract Schema (`Stage2VectorContract`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage2VectorContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "file_hash",
    "sheet_code",
    "srid",
    "extraction_timestamp",
    "extracted_polygons",
    "extracted_polylines",
    "extracted_text_labels",
    "vector_summary"
  ],
  "properties": {
    "contract_version": {"type": "string", "example": "1.0.0"},
    "file_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "sheet_code": {"type": "string", "example": "A-A-18"},
    "srid": {"type": "integer", "example": 2263},
    "extraction_timestamp": {"type": "string", "format": "date-time"},
    "extracted_polygons": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["polygon_id", "layer", "wkt_geometry", "is_valid"],
        "properties": {
          "polygon_id": {"type": "string", "example": "poly_aa18_101"},
          "layer": {"type": "string", "example": "WALLS"},
          "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
          "is_valid": {"type": "boolean", "example": true}
        }
      }
    },
    "extracted_polylines": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["polyline_id", "layer", "wkt_geometry"],
        "properties": {
          "polyline_id": {"type": "string", "example": "line_aa18_50"},
          "layer": {"type": "string", "example": "GRID_LINES"},
          "wkt_geometry": {"type": "string", "example": "LINESTRING(982100 198200, 982100 199000)"}
        }
      }
    },
    "extracted_text_labels": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["label_id", "text", "bounding_box_wkt"],
        "properties": {
          "label_id": {"type": "string", "example": "txt_aa18_12"},
          "text": {"type": "string", "example": "FAN ROOM B-1"},
          "bounding_box_wkt": {"type": "string", "example": "POLYGON((982150 198250, 982250 198250, 982250 198280, 982150 198280, 982150 198250))"}
        }
      }
    },
    "vector_summary": {
      "type": "object",
      "required": ["total_polygons", "total_polylines", "total_text_labels", "valid_geometry_percentage"],
      "properties": {
        "total_polygons": {"type": "integer", "example": 142},
        "total_polylines": {"type": "integer", "example": 380},
        "total_text_labels": {"type": "integer", "example": 89},
        "valid_geometry_percentage": {"type": "number", "example": 98.5}
      }
    }
  }
}
```

---

## 4. Final Specification Status

- **Status:** **FROZEN AT VERSION 1.0.0**
- **Consumer:** Stage 3 AI Vision Layout Parser & Stage 5 Deduplication/Ingestion.  
- **Governance Sign-off:** ✅ Approved for vector parser implementation.
