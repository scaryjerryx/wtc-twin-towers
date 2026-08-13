# Phase 4 Stage 5: PostGIS Deduplication Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 5 TECHNICAL SPECIFICATION  
**Classification:** **DATABASE QUALITY INFRASTRUCTURE (ADR-006)**  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
**Parent Output Contract:** [`docs/PHASE_4_STAGE_3_LAYOUT_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_3_LAYOUT_CONTRACT.md)  
**Parent Governance Rules:** [`docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_PIPELINE_GOVERNANCE_AND_REVIEW_RULES.md)  
**Frozen Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

> [!NOTE]
> **ADR-006 Classification Notice:** Stage 5 functions as **DATABASE QUALITY INFRASTRUCTURE**. It consumes Gemini reconstruction proposals, executes PostGIS spatial deduplication ($\text{IoU} \ge 0.90$), resolves conflicts, and manages evidence link merging.


---

## Executive Summary

This document establishes the **authoritative Stage 5 Technical Specification** governing **PostGIS Deduplication and Entity Resolution** within Phase 4.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

Stage 5 consumes candidate visual/vector entity records from Stage 3 (`Stage3LayoutContract`), queries the live PostgreSQL database (`wtc_evidence`), and executes spatial overlap tests (`ST_Intersects`, `ST_Equals`, `ST_Area`), attribute alignment checks, evidence link merges, confidence score reconciliations, and upsert resolutions before passing clean entities to Stage 6 for transactional ingestion.

---

## 1. Verified Facts

```text
SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 3 Layout Data Contract Formally Frozen (`Stage3LayoutContract`)│ ✅ PASS │
│ 3. PostGIS 2D Spatial Indices Active in `EPSG:2263`                    │ ✅ PASS │
│ 4. Master Entity Registry (`entities`) Active (ADR-005)                │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Stage 5 Technical Requirements (12 Modules)

### 2.1 Stage 5 Inputs
- **Purpose:** Ingest Stage 3 layout payloads (`Stage3LayoutContract`) and live database catalog state from `wtc_evidence`.
- **Inputs:** `Stage3LayoutContract` (version `1.0.0`) + active PostgreSQL database tables (`entities`, `sites`..`elements`).
- **Outputs:** Deduplication candidate evaluation queue.
- **Validation Rules:** `Stage3LayoutContract.validation_status` equals `"VALIDATED"`, non-empty `detected_entities` list.
- **Failure Conditions:** Database connection failure or unvalidated Stage 3 contract input.
- **Governance Requirements:** Block unvalidated Stage 3 outputs from entering Stage 5.

### 2.2 Duplicate Detection Rules
- **Purpose:** Detect whether a candidate entity represents an existing database entity or a new entity.
- **Inputs:** Candidate entity payload (`entity_id`, `category`, `wkt_geometry`).
- **Outputs:** Match classification (`EXACT_MATCH`, `SPATIAL_OVERLAP_MATCH`, `NEW_ENTITY`).
- **Validation Rules:** Execute Primary Key check (`entity_id`), spatial intersection query (`ST_Intersects`), and name attribute fuzzy match.
- **Failure Conditions:** Ambiguous spatial match across multiple entity categories.
- **Governance Requirements:** Never overwrite a validated database record without citation corroboration.

### 2.3 Spatial Matching Rules
- **Purpose:** Calculate PostGIS Spatial Intersection over Union ($\text{IoU}$) between candidate geometry and stored database geometries in `EPSG:2263`.
- **Inputs:** Candidate 2D polygon footprint + stored tier table geometries (`geometry_2d`).
- **Outputs:** Spatial $\text{IoU}$ score $[0.0, 1.0]$.
- **Validation Rules:**
  - $\text{IoU} \ge 0.90$: Classify as `EXACT_SPATIAL_MATCH` (Same physical entity).
  - $0.50 \le \text{IoU} < 0.90$: Classify as `SPATIAL_OVERLAP` (Potential sub-zone or boundary refinement).
  - $\text{IoU} < 0.50$: Classify as `SPATIAL_DISJOINT` (Distinct entity).
- **Failure Conditions:** Invalid spatial geometry (`ST_IsValid = false`).
- **Governance Requirements:** Route $\text{IoU} \in [0.50, 0.89]$ matches to human review gate.

### 2.4 Attribute Matching Rules
- **Purpose:** Compare entity category, name, and floor level between candidate and database record.
- **Inputs:** Candidate entity attributes + matched database entity attributes.
- **Outputs:** Attribute Similarity Score $[0, 100]$.
- **Validation Rules:** Category match MANDATORY; name stringLevenshtein distance $\ge 80\%$.
- **Failure Conditions:** Mismatched entity categories (e.g., candidate `space` vs stored `element`).
- **Governance Requirements:** Prevent category mutation on pre-existing database records.

### 2.5 Evidence Reconciliation Rules
- **Purpose:** Merge drawing sheet citations when a candidate entity corroborates an existing database entity (Principle 2: *Cite Sources*).
- **Inputs:** Candidate citation (`source_id`, `sheet_code`) + stored entity citations in `entity_evidence_citations`.
- **Outputs:** Merged citation list + updated corroboration count.
- **Validation Rules:** Insert new `(entity_id, source_id, sheet_code)` tuple into `entity_evidence_citations` on conflict `DO NOTHING`.
- **Failure Conditions:** Missing drawing sheet code.
- **Governance Requirements:** Update lifecycle state from `DRAFT_SEED` to `CORROBORATED` upon second independent drawing citation link.

### 2.6 Confidence Reconciliation Rules
- **Purpose:** Reconcile candidate confidence score with pre-existing database entity score (Principle 5: *Quantify Uncertainty*).
- **Inputs:** Candidate `confidence_score` + stored entity `confidence_score`.
- **Outputs:** Reconciled database `confidence_score`.
- **Validation Rules:**
  - If candidate corroborates stored record: Assign $\max(S_{\text{stored}}, S_{\text{candidate}}) + 2$ (capped at 100).
  - If candidate conflicts with stored record: Maintain $S_{\text{stored}}$ and lower candidate score.
- **Failure Conditions:** Reconciled score $< 80$.
- **Governance Requirements:** Repository stored confidence PREVAILS over AI candidate confidence.

### 2.7 Conflict Resolution Rules
- **Purpose:** Enforce governance conflict resolution matrix when candidate data contradicts stored database data.
- **Inputs:** Conflicting candidate vs stored attribute values.
- **Outputs:** Enforced resolution action.
- **Validation Rules:**
  - Spatial disagreement: Stored geometry PREVAILS.
  - Category mismatch: Stored category PREVAILS.
  - Name string disagreement: Stored name PREVAILS; candidate name saved as alias in `entity_aliases`.
- **Failure Conditions:** Bypassing repository precedence rules.
- **Governance Requirements:** Total compliance with repository evidence precedence.

### 2.8 Human Review Triggers
- **Purpose:** Flag ambiguous spatial overlap or unresolved attribute conflicts for human sign-off.
- **Inputs:** Stage 5 match evaluation results.
- **Outputs:** Human review ticket payload.
- **Validation Rules:** Trigger human review if $\text{IoU} \in [0.50, 0.89]$, conflicting drawing citations, or multi-parent boundary ambiguity.
- **Failure Conditions:** Bypassing human review for flagged deduplication candidates.
- **Governance Requirements:** Human sign-off required prior to committing flagged upserts.

### 2.9 Quarantine Requirements
- **Purpose:** Quarantine candidates that violate relational integrity or spatial bounds.
- **Inputs:** Rejected candidate entity payload.
- **Outputs:** Stage 5 quarantine JSON record in `data/failed_pdfs/`.
- **Validation Rules:** Quarantined if duplicate `entity_id` contains mismatched category tier.
- **Failure Conditions:** Unhandled database error.
- **Governance Requirements:** Write quarantine log entry and proceed with next candidate.

### 2.10 Output Requirements
- **Purpose:** Produce structured Stage 5 output payload (`Stage5DeduplicationContract`) consumed by Stage 6 Transactional Ingestion.
- **Inputs:** Resolved entity actions list (`INSERT_NEW`, `UPDATE_EXISTING`, `CORROBORATE_CITATION`).
- **Outputs:** `Stage5DeduplicationContract` JSON payload.
- **Validation Rules:** Compliant with Stage 5 Schema; version `"1.0.0"`.
- **Failure Conditions:** Serialization error.
- **Governance Requirements:** Freeze Stage 5 contract interface at version `1.0.0`.

### 2.11 Validation Requirements
- **Purpose:** Validate post-deduplication entity list against Master Entity Registry (`entities`) and single-parent `CHECK` constraints (`= 1`).
- **Inputs:** Resolved entity action list.
- **Outputs:** Pre-ingestion validation scorecard.
- **Validation Rules:** 100% of candidate entity IDs registered in `entities`, single-parent `CHECK` satisfied.
- **Failure Conditions:** Single-parent constraint violation or missing master entity ID.
- **Governance Requirements:** Pre-ingestion validation MUST pass 100% before passing payload to Stage 6.

### 2.12 Acceptance Criteria
- **Purpose:** Define quantitative acceptance thresholds for Stage 5 completion.
- **Inputs:** Stage 5 batch processing scorecard.
- **Outputs:** Stage 5 completion sign-off.
- **Validation Rules:** 100% of candidate entities classified cleanly into `INSERT_NEW`, `UPDATE_EXISTING`, or `CORROBORATE_CITATION`; zero duplicate primary key collisions.
- **Failure Conditions:** Deduplication resolution failure rate $> 0\%$.
- **Governance Requirements:** Total compliance with Principle 3 (*Preserve Relational Integrity*).

---

## 3. Stage 5 Output Contract Schema (`Stage5DeduplicationContract`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage5DeduplicationContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "source_file_hash",
    "source_sheet_code",
    "resolution_timestamp",
    "resolved_entities",
    "deduplication_summary",
    "validation_status",
    "quarantine_status",
    "processing_errors"
  ],
  "properties": {
    "contract_version": {"type": "string", "example": "1.0.0"},
    "source_file_hash": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "source_sheet_code": {"type": "string", "example": "A-A-18"},
    "resolution_timestamp": {"type": "string", "format": "date-time"},
    "resolved_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["entity_id", "resolution_action", "category", "wkt_geometry", "confidence_score", "lifecycle_state"],
        "properties": {
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "resolution_action": {"type": "string", "enum": ["INSERT_NEW", "UPDATE_EXISTING", "CORROBORATE_CITATION"], "example": "INSERT_NEW"},
          "category": {"type": "string", "example": "service_area"},
          "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
          "confidence_score": {"type": "integer", "minimum": 80, "maximum": 100, "example": 95},
          "lifecycle_state": {"type": "string", "example": "CORROBORATED"}
        }
      }
    },
    "deduplication_summary": {
      "type": "object",
      "required": ["new_entities_count", "updated_entities_count", "corroborated_citations_count", "human_review_count"],
      "properties": {
        "new_entities_count": {"type": "integer", "example": 12},
        "updated_entities_count": {"type": "integer", "example": 3},
        "corroborated_citations_count": {"type": "integer", "example": 15},
        "human_review_count": {"type": "integer", "example": 0}
      }
    },
    "validation_status": {"type": "string", "enum": ["VALIDATED", "WARNING", "FAILED"], "example": "VALIDATED"},
    "quarantine_status": {"type": "boolean", "example": false},
    "processing_errors": {"type": "array", "items": {"type": "object"}}
  }
}
```

---

## 4. Final Specification Status

- **Status:** **FROZEN AT VERSION 1.0.0**
- **Consumer:** Stage 6 Transactional Database Ingestion Pipeline.  
- **Governance Sign-off:** ✅ Approved for Stage 5 PostGIS deduplication engine implementation.
