# Phase 4 Stage 3: AI Vision Layout Parser Technical Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 3 TECHNICAL SPECIFICATION  
**Classification:** **PRIMARY RECONSTRUCTION ENGINE (ADR-006)**  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md), [`docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md)  
**Parent Output Contract:** [`docs/PHASE_4_STAGE_2_VECTOR_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_2_VECTOR_CONTRACT.md)  
**Parent Governance Rules:** [`docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md)  

> [!IMPORTANT]
> **ADR-006 Realignment:** Stage 3 operates as the **PRIMARY RECONSTRUCTION ENGINE**. Gemini multi-modal architectural analysis discovers entities and spatial relationships. OCR and vector extraction act as **SUPPORTING EVIDENCE SOURCES** only. Confidence scoring follows the ADR-006A Option B Evidence-Quality model.

---

## Executive Summary

This document establishes the **authoritative Stage 3 Technical Specification** governing **Gemini Multi-Modal Architectural Analysis** (PRIMARY RECONSTRUCTION ENGINE).

Zero implementation code, zero Python scripts, zero model prompts, zero AI agents, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

Stage 3 consumes 300 DPI raster page images and supporting Stage 2 CAD vector evidence, executing multi-modal architectural analysis, structural column discovery, relationship edge creation, evidence attribution, and epistemic confidence scoring before passing candidate entity records downstream.

---

## 1. Verified Facts

```text
SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 2 Vector Data Contract Formally Frozen (`Stage2VectorContract`)│ ✅ PASS │
│ 3. 300 DPI Page Rendering Pipeline Standardized                        │ ✅ PASS │
│ 4. Mandatory Governance Conflict Rules Formally Defined                │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Stage 3 Technical Requirements (12 Modules)

### 2.1 Stage 3 Inputs
- **Purpose:** Ingest Stage 2 vector JSON payloads (`Stage2VectorContract`) and 300 DPI page raster images.
- **Inputs:** `Stage2VectorContract` (version `1.0.0`) + 300 DPI PNG page raster image.
- **Outputs:** Integrated visual/vector parsing job payload.
- **Validation Rules:** `Stage2VectorContract.validation_status` equals `"VALIDATED"`, raster resolution $\ge 300$ DPI.
- **Failure Conditions:** Missing raster image or invalid Stage 2 vector payload.
- **Governance Requirements:** Require both vector and raster inputs prior to Stage 3 processing.

### 2.2 Raster Image Requirements
- **Purpose:** Standardize visual image properties for AI vision multi-modal layout model inference.
- **Inputs:** Uncompressed RGB PNG image file rendered from Stage 1 PDF.
- **Outputs:** Normalized 300 DPI image array $(W \times H \times 3)$.
- **Validation Rules:** Resolution 300 DPI, 24-bit color depth, minimum width 2400px.
- **Failure Conditions:** Low DPI rendering ($< 300$ DPI) or image corruption.
- **Governance Requirements:** Re-render image at 300 DPI if lower resolution detected.

### 2.3 Supported Entity Categories
- **Purpose:** Restrict AI visual classifications to canonical World Model entity taxonomies.
- **Inputs:** Vision model layout bounding box predictions.
- **Outputs:** Classified entity candidates mapped to canonical categories.
- **Validation Rules:** Category $\in \{$`site`, `building`, `floor`, `zone`, `space`, `general_space`, `retail_space`, `transit_station`, `kitchen_area`, `service_area`, `corridor`, `structural_element`, `mechanical_area`, `mechanical_element`, `architectural_element`, `elevator_bank`, `elevator`, `stair`, `escalator` $\}$.
- **Failure Conditions:** Classification string outside canonical taxonomy ENUM list.
- **Governance Requirements:** Remap non-standard predictions to `structural_element` or trigger human review.

### 2.4 Visual Detection Requirements
- **Purpose:** Detect visual structural elements (exterior curtain walls, core box columns 501–1008, elevator shafts, stairwells).
- **Inputs:** 300 DPI page image.
- **Outputs:** Bounding box coordinates $(X_1, Y_1, X_2, Y_2)$ + category labels + model probabilities.
- **Validation Rules:** Bounding box area $> 0$, probability $P \ge 0.80$.
- **Failure Conditions:** Bounding box collapse ($X_1 = X_2$).
- **Governance Requirements:** Cross-reference visual bounding box with Stage 2 vector polygon footprints.

### 2.5 OCR Requirements
- **Purpose:** Perform optical character recognition on room labels, column numbers (`Col 501`, `Col 1008`), and elevation markers.
- **Inputs:** High-resolution cropped image patches around text bounding boxes.
- **Outputs:** Text string content + OCR character confidence score $[0, 100]$.
- **Validation Rules:** OCR confidence $\ge 80$.
- **Failure Conditions:** Unreadable text glyphs or low OCR confidence ($< 80$).
- **Governance Requirements:** Reconcile OCR text against Stage 2 vector text annotations (`text_content`).

### 2.6 Symbol Recognition Requirements
- **Purpose:** Detect architectural CAD symbols (north arrows, column grid bubbles, elevator door swings, stair direction arrows).
- **Inputs:** 300 DPI page raster patch.
- **Outputs:** Symbol classification + spatial orientation angle.
- **Validation Rules:** Model confidence $\ge 80$.
- **Failure Conditions:** Ambiguous symbol match.
- **Governance Requirements:** Log recognized symbols into entity metadata dictionary.

### 2.7 Confidence Scoring Requirements
- **Purpose:** Enforce Principle 5 (*Quantify Uncertainty*), generating a composite confidence score $[0, 100]$ for each detected entity.
- **Inputs:** Visual detection score + vector overlap score + OCR match score.
- **Outputs:** Integer composite `confidence_score` $[0, 100]$.
- **Validation Rules:** Composite score calculated via weighted average: $0.4 \cdot \text{Vector} + 0.4 \cdot \text{Vision} + 0.2 \cdot \text{OCR}$.
- **Failure Conditions:** Composite `confidence_score` $< 80$.
- **Governance Requirements:** Reject candidate entities with `confidence_score < 80` to quarantine.

### 2.8 Human Review Triggers
- **Purpose:** Route ambiguous or conflicting AI vision predictions to human review.
- **Inputs:** Stage 3 detection results.
- **Outputs:** Human review ticket payload.
- **Validation Rules:** Trigger review if composite score $[70, 79]$, OCR/vector text mismatch, or multiple overlapping visual symbols.
- **Failure Conditions:** Bypassing human review for flagged entities.
- **Governance Requirements:** Require explicit human reviewer sign-off before flagged candidates enter ingestion queue.

### 2.9 Validation Requirements
- **Purpose:** Validate spatial alignment between AI visual bounding boxes and PostGIS vector polygons in `EPSG:2263`.
- **Inputs:** Visual bounding box + Stage 2 PostGIS polygon.
- **Outputs:** Spatial Intersection over Union (IoU) metric $[0.0, 1.0]$.
- **Validation Rules:** IoU $\ge 0.70$.
- **Failure Conditions:** Spatial IoU $< 0.70$ (visual prediction displaced from vector geometry).
- **Governance Requirements:** Align visual attribute label with vector polygon possessing highest IoU overlap.

### 2.10 Quarantine Requirements
- **Purpose:** Quarantine page parsing jobs with low overall detection confidence or unresolvable spatial conflicts.
- **Inputs:** Stage 3 job parsing results.
- **Outputs:** Stage 3 quarantine JSON record in `data/failed_pdfs/`.
- **Validation Rules:** Quarantined if $> 30\%$ of visual detections have `confidence_score < 80`.
- **Failure Conditions:** Unhandled model exception.
- **Governance Requirements:** Move job metadata to quarantine directory and log error stack trace.

### 2.11 Output Requirements
- **Purpose:** Produce structured Stage 3 output contract (`Stage3LayoutContract`) for Stage 5 deduplication and database ingestion.
- **Inputs:** Validated visual/vector entity candidates.
- **Outputs:** `Stage3LayoutContract` JSON payload.
- **Validation Rules:** Compliant with Stage 3 JSON Schema; contract version `"1.0.0"`.
- **Failure Conditions:** Schema validation error.
- **Governance Requirements:** Freeze Stage 3 contract interface at version `1.0.0`.

### 2.12 Acceptance Criteria
- **Purpose:** Define non-negotiable acceptance thresholds for Stage 3 sign-off.
- **Inputs:** Stage 3 batch processing scorecard.
- **Outputs:** Stage 3 acceptance sign-off.
- **Validation Rules:** $\ge 95\%$ of visual layout predictions achieve `confidence_score >= 80`, 100% of room labels matched to source sheet codes.
- **Failure Conditions:** Detection pass rate $< 95\%$.
- **Governance Requirements:** Total compliance with Principle 1 (*Evidence Over Assumptions*).

---

## 3. Mandatory Governance Conflict Resolution Rules

```text
GOVERNANCE CONFLICT RESOLUTION MATRIX:
┌───────────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Conflict / Scenario                                   │ Enforced Resolution Action                             │
├───────────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. confidence_score < 80                              │ Entity is REJECTED from DB & QUARANTINED               │
│ 2. OCR text conflicts with vector-extracted text       │ Vector CAD text PREVAILS; OCR text logged as alias     │
│ 3. Multiple symbols overlap                            │ Spatial IoU tie-breaker applied; lower IoU flagged     │
│ 4. Entity classification is ambiguous                 │ Entity defaulted to `structural_element` & flagged     │
│ 5. Extracted geometry disagrees with repository DB    │ Repository DB PREVAILS; AI candidate sent to review    │
│ 6. Source drawings contain conflicting information    │ Both cited; state marked `CORROBORATED` (lower score)  │
│ 7. AI confidence and repository confidence differ     │ Repository confidence PREVAILS; AI score logged        │
└───────────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 4. Stage 3 Output Contract Schema (`Stage3LayoutContract`)

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
    "classified_entities",
    "recognized_symbols",
    "parsing_summary",
    "validation_status",
    "quarantine_status",
    "processing_errors"
  ],
  "properties": {
    "contract_version": {"type": "string", "example": "1.0.0"},
    "source_file_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "source_sheet_code": {"type": "string", "example": "A-A-18"},
    "parsing_timestamp": {"type": "string", "format": "date-time"},
    "classified_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entity_id", "entity_name", "category", "wkt_geometry", "confidence_score", "source_drawing"],
        "properties": {
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "entity_name": {"type": "string", "example": "Sub-grade Fan Room 101"},
          "category": {"type": "string", "example": "service_area"},
          "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
          "confidence_score": {"type": "integer", "minimum": 80, "maximum": 100, "example": 95},
          "source_drawing": {"type": "string", "example": "A-A-18"}
        }
      }
    },
    "recognized_symbols": {
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
    "parsing_summary": {
      "type": "object",
      "required": ["total_detected_entities", "high_confidence_entities", "human_review_flagged_entities"],
      "properties": {
        "total_detected_entities": {"type": "integer", "example": 142},
        "high_confidence_entities": {"type": "integer", "example": 138},
        "human_review_flagged_entities": {"type": "integer", "example": 4}
      }
    },
    "validation_status": {"type": "string", "enum": ["VALIDATED", "WARNING", "FAILED"], "example": "VALIDATED"},
    "quarantine_status": {"type": "boolean", "example": false},
    "processing_errors": {"type": "array", "items": {"type": "object"}}
  }
}
```

---

## 5. Final Specification Status

- **Status:** **FROZEN AT VERSION 1.0.0**
- **Consumer:** Stage 5 PostGIS Deduplication & Stage 6 Transactional Database Ingestion.  
- **Governance Sign-off:** ✅ Approved for Stage 3 AI Vision layout parser implementation.
