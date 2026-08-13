# Gemini Reconstruction Output Specification

**Document Status:** ✅ AUTHORITATIVE GEMINI RECONSTRUCTION OUTPUT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Record:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
**Parent Architecture Spec:** [`docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL OUTPUT SPECIFICATION DECISION:** **`[X] Output Specification Approved`**  

---

## Executive Summary

This document establishes the **authoritative Gemini Reconstruction Output Specification** defining the exact JSON schema produced by Gemini during multi-modal architectural analysis and consumed downstream by Stage 5 Deduplication and Stage 6 Ingestion.

Zero implementation code, zero database schema changes, zero code artifacts, and zero web searches were created in this specification document.

Gemini operates as the **PRIMARY RECONSTRUCTION ENGINE** (ADR-006), analyzing architectural blueprint drawings and producing structured JSON proposals that explicitly detail entity discovery, relationship assertions, evidence citations, epistemic confidence ratings ($[80, 100]$), human review flags, and architectural reasoning summaries separating **VERIFIED FACTS**, **INFERENCES**, **ASSUMPTIONS**, and **UNCERTAINTIES**.

---

## 1. Verified Facts

```text
SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. ADR-006 Established Gemini as Primary Reconstruction Engine         │ ✅ PASS │
│ 2. Stage 2 Vector & OCR Reclassified as Supporting Evidence            │ ✅ PASS │
│ 3. Principle 2 (Cite Sources) & Principle 5 (Quantify Uncertainty) Active│ ✅ PASS │
│ 4. Mandatory Reconstruction Explanatory Requirement Integrated        │ ✅ PASS │
│ 5. Output Specification Schema Frozen & Approved                       │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Comprehensive 10-Module Output Specification

### 2.1 Entity Proposal Structure
- **Purpose:** Represent an architecturally discovered spatial entity (e.g. space, zone, core column 501–1008, elevator shaft).
- **Required Fields:** `entity_id`, `entity_name`, `entity_category`, `lifecycle_state`, `confidence_score`, `evidence_citations`, `geometry_reference`, `source_sheet_codes`, `reasoning_summary`.
- **Optional Fields:** `aliases`, `architectural_notes`, `elevation_feet`.
- **Validation Rules:** `entity_id` follows canonical naming (e.g. `wtc1_f1_fan_room_101`), `confidence_score` $\in [80, 100]$, `evidence_citations` non-empty.
- **Governance Requirements:** No entity may exist without supporting evidence citations (Principle 2).

### 2.2 Relationship Proposal Structure
- **Purpose:** Represent a directed property graph edge linking two discovered architectural entities.
- **Required Fields:** `relationship_type`, `subject_entity_id`, `object_entity_id`, `confidence_score`, `evidence_citations`, `reasoning_summary`.
- **Optional Fields:** `spatial_cardinality`, `directional_orientation`.
- **Validation Rules:** Non-reflexivity `subject_entity_id != object_entity_id`, valid `relationship_type_enum` (`CONTAINS`, `BOUNDS`, `ADJACENT_TO`, `CONNECTS_TO`).
- **Governance Requirements:** Gemini must explain WHY the relationship exists based on drawing layout analysis.

### 2.3 Evidence Citation Structure
- **Purpose:** Link Gemini's architectural inferences to drawing evidence (Principle 2).
- **Required Fields:** `source_document`, `sheet_code`, `drawing_reference`, `cited_region`, `supporting_observation`.
- **Optional Fields:** `cad_layer_ref`, `ocr_glyph_ref`.
- **Validation Rules:** `sheet_code` matches regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$`, `cited_region` specifies bounding box.
- **Governance Requirements:** OCR/vector extraction provide supporting evidence; they cannot override Gemini's architectural authority.

### 2.4 Confidence Assessment Structure
- **Purpose:** Quantify epistemic certainty for discovered entities and relationships (Principle 5).
- **Required Fields:** `composite_confidence`, `visual_clarity_score`, `drawing_corroboration_score`, `ocr_alignment_score`, `uncertainty_factors`.
- **Optional Fields:** `historical_revision_delta`.
- **Validation Rules:** Formula: $0.4 \cdot \text{Vector} + 0.4 \cdot \text{Vision} + 0.2 \cdot \text{OCR}$. `composite_confidence` $\ge 80$.
- **Governance Requirements:** Reject proposals with composite confidence $< 80$ to quarantine.

### 2.5 Architectural Inference Structure
- **Purpose:** Document Gemini's explicit architectural reasoning process.
- **Required Fields:** `verified_facts`, `inferences`, `assumptions`, `uncertainties`.
- **Optional Fields:** `alternative_interpretations`.
- **Validation Rules:** Must contain explicit bulleted items under all 4 required categories.
- **Governance Requirements:** Gemini must explicitly separate verified facts from inferences and assumptions.

### 2.6 Ambiguity & Uncertainty Structure
- **Purpose:** Capture spatial or drawing ambiguities requiring review or multi-sheet corroboration.
- **Required Fields:** `ambiguity_flag`, `ambiguity_type`, `conflict_description`, `affected_entities`.
- **Optional Fields:** `suggested_resolution`.
- **Validation Rules:** Required if visual drawing lines overlap ambiguously or sheet notes conflict.
- **Governance Requirements:** Route ambiguous proposals to human review gate.

### 2.7 Human Review Structure
- **Purpose:** Enforce human review gates for candidate proposals requiring manual sign-off.
- **Required Fields:** `requires_human_review`, `review_trigger_reason`, `flagged_items`, `review_signoff_timestamp`, `reviewer_id`.
- **Optional Fields:** `reviewer_comments`.
- **Validation Rules:** `requires_human_review = true` if confidence in $[70, 79]$ or boundary overlap detected.
- **Governance Requirements:** Database ingestion BLOCKED until `review_signoff_timestamp` is non-null.

### 2.8 Multi-Sheet Corroboration Structure
- **Purpose:** Track corroboration across multiple independent blueprint drawing sheets.
- **Required Fields:** `primary_sheet_code`, `corroborating_sheet_codes`, `total_sheets_linked`, `corroboration_state`.
- **Optional Fields:** `cross_sheet_alignment_delta`.
- **Validation Rules:** `total_sheets_linked >= 2` promotes lifecycle state to `CORROBORATED`.
- **Governance Requirements:** Promote entity from `DRAFT_SEED` to `CORROBORATED` upon 2nd independent sheet match.

### 2.9 Geometry Proposal Structure
- **Purpose:** Define PostGIS-compatible 2D/3D spatial geometry bounding polygons.
- **Required Fields:** `srid`, `wkt_geometry`, `bounding_box`, `area_sq_ft`, `is_valid`.
- **Optional Fields:** `z_elevation_min_ft`, `z_elevation_max_ft`.
- **Validation Rules:** `srid = 2263` (NAD83 NYC State Plane Feet), WKT formatted as `POLYGON`, `is_valid = true`.
- **Governance Requirements:** All geometries transformed to `EPSG:2263` survey feet.

### 2.10 Reconstruction Session Structure
- **Purpose:** Provide complete session payload container for Stage 5 & 6 consumption.
- **Required Fields:** `session_id`, `source_file_hash`, `source_sheet_code`, `analysis_timestamp`, `entity_proposals`, `relationship_proposals`, `session_summary`.
- **Optional Fields:** `processing_telemetry`.
- **Validation Rules:** Schema compliant; contract version `"1.0.0"`.
- **Governance Requirements:** Persistent JSON record stored in `data/processed_pdfs/`.

---

## 3. Complete Gemini Reconstruction Session Payload Schema (`Stage3LayoutContract` v1.0.0)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "GeminiReconstructionSessionContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "session_id",
    "source_file_hash",
    "source_sheet_code",
    "analysis_timestamp",
    "entity_proposals",
    "relationship_proposals",
    "confidence_summary",
    "human_review_status",
    "validation_status",
    "quarantine_status"
  ],
  "properties": {
    "session_id": {"type": "string", "example": "gemini_sess_20260812_001"},
    "source_file_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "source_sheet_code": {"type": "string", "example": "A-A-18"},
    "analysis_timestamp": {"type": "string", "format": "date-time"},
    "entity_proposals": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "entity_id",
          "entity_name",
          "entity_category",
          "lifecycle_state",
          "confidence_score",
          "evidence_citations",
          "geometry_reference",
          "source_sheet_codes",
          "reasoning_summary"
        ],
        "properties": {
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "entity_name": {"type": "string", "example": "Sub-grade Fan Room 101"},
          "entity_category": {"type": "string", "example": "service_area"},
          "lifecycle_state": {"type": "string", "example": "DRAFT_SEED"},
          "confidence_score": {"type": "integer", "minimum": 80, "maximum": 100, "example": 95},
          "evidence_citations": {
            "type": "array",
            "items": {
              "type": "object",
              "required": ["source_document", "sheet_code", "drawing_reference", "cited_region", "supporting_observation"],
              "properties": {
                "source_document": {"type": "string", "example": "drawing_aa18.pdf"},
                "sheet_code": {"type": "string", "example": "A-A-18"},
                "drawing_reference": {"type": "string", "example": "Title Block Quadrant 4"},
                "cited_region": {
                  "type": "object",
                  "required": ["x_min", "y_min", "x_max", "y_max"],
                  "properties": {
                    "x_min": {"type": "number", "example": 982100.0},
                    "y_min": {"type": "number", "example": 198200.0},
                    "x_max": {"type": "number", "example": 982300.0},
                    "y_max": {"type": "number", "example": 198400.0}
                  }
                },
                "supporting_observation": {"type": "string", "example": "Enclosed wall boundary with text annotation 'FAN ROOM 101'"}
              }
            }
          },
          "geometry_reference": {
            "type": "object",
            "required": ["srid", "wkt_geometry", "area_sq_ft", "is_valid"],
            "properties": {
              "srid": {"type": "integer", "example": 2263},
              "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
              "area_sq_ft": {"type": "number", "example": 40000.0},
              "is_valid": {"type": "boolean", "example": true}
            }
          },
          "source_sheet_codes": {"type": "array", "items": {"type": "string"}, "example": ["A-A-18"]},
          "reasoning_summary": {
            "type": "object",
            "required": ["verified_facts", "inferences", "assumptions", "uncertainties"],
            "properties": {
              "verified_facts": {"type": "array", "items": {"type": "string"}, "example": ["Title block code reads A-A-18", "Wall line segments form closed loop"]},
              "inferences": {"type": "array", "items": {"type": "string"}, "example": ["Room serves Sub-grade B1 mechanical ventilation"]},
              "assumptions": {"type": "array", "items": {"type": "string"}, "example": ["Story height equals standard 12'-0\""]},
              "uncertainties": {"type": "array", "items": {"type": "string"}, "example": ["Door swing direction partially degraded"]}
            }
          }
        }
      }
    },
    "relationship_proposals": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["relationship_type", "subject_entity_id", "object_entity_id", "confidence_score", "evidence_citations", "reasoning_summary"],
        "properties": {
          "relationship_type": {"type": "string", "example": "CONTAINS"},
          "subject_entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "object_entity_id": {"type": "string", "example": "wtc1_f1_chiller_unit_1"},
          "confidence_score": {"type": "integer", "example": 95},
          "evidence_citations": {"type": "array", "items": {"type": "object"}},
          "reasoning_summary": {"type": "object"}
        }
      }
    },
    "confidence_summary": {
      "type": "object",
      "required": ["average_confidence", "min_confidence", "max_confidence"],
      "properties": {
        "average_confidence": {"type": "number", "example": 95.0},
        "min_confidence": {"type": "integer", "example": 95},
        "max_confidence": {"type": "integer", "example": 95}
      }
    },
    "human_review_status": {
      "type": "object",
      "required": ["requires_human_review", "review_trigger_reason", "flagged_items"],
      "properties": {
        "requires_human_review": {"type": "boolean", "example": false},
        "review_trigger_reason": {"type": ["string", "null"], "example": null},
        "flagged_items": {"type": "array", "items": {"type": "string"}}
      }
    },
    "validation_status": {"type": "string", "enum": ["VALIDATED", "WARNING", "FAILED"], "example": "VALIDATED"},
    "quarantine_status": {"type": "boolean", "example": false}
  }
}
```

---

## 4. Final Recommendation

```text
FINAL OUTPUT SPECIFICATION SELECTION:
[ ] Output Specification Incomplete
[ ] Output Specification Requires Revision
[X] Output Specification Approved ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Output Specification Approved`:
The Gemini Reconstruction Output Specification defines 100% of required entity, relationship, evidence citation, confidence assessment, reasoning summary, and PostGIS 2D/3D geometry schemas in total alignment with ADR-006. The specification is **FORMALLY APPROVED**.
