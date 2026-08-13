# Phase 4 Stage 5: Deduplication Data Contract Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 5 DEDUPLICATION DATA CONTRACT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Technical Spec:** [`docs/PHASE_4_STAGE_5_DEDUPLICATION_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_5_DEDUPLICATION_SPEC.md)  
**Parent Upstream Contract:** [`docs/PHASE_4_STAGE_3_LAYOUT_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_3_LAYOUT_CONTRACT.md)  
**Parent Downstream Spec:** [`docs/PHASE_4_STAGE_6_DATABASE_INGESTION_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_6_DATABASE_INGESTION_SPEC.md)  
**Contract Version:** `1.0.0`  

---

## Executive Summary

This document establishes the **authoritative Stage 5 Deduplication Data Contract Specification** defining the exact JSON schema produced by Stage 5 (PostGIS Deduplication and Entity Resolution) and consumed by Stage 6 (Transactional Database Ingestion).

Zero implementation code, zero Python scripts, zero ETL scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this contract specification document.

This contract freezes the deduplicated entity payload interface, detailing every required field, data type, deduplicated entity/relationship schema, evidence citation reconciliation payload, confidence score reconciliation schema, conflict resolution log, quarantine contract, audit metadata, and acceptance criteria.

---

## 1. Verified Facts

```text
CONTRACT SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Stage 3 Layout Data Contract Formally Frozen (`Stage3LayoutContract`)│ ✅ PASS │
│ 3. Stage 5 Technical Specification Formally Defined                    │ ✅ PASS │
│ 4. Stage 6 Ingestion Technical Specification Formally Defined          │ ✅ PASS │
│ 5. Contract Version Standardized to Semantic Versioning (`1.0.0`)       │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Complete Stage 5 Output Contract Schema (`Stage5DeduplicationContract`)

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
    "deduplicated_entities",
    "deduplicated_relationships",
    "evidence_reconciliation",
    "confidence_reconciliation",
    "conflict_resolution_log",
    "human_review_status",
    "validation_status",
    "quarantine_status",
    "processing_errors",
    "audit_metadata"
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
    "resolution_timestamp": {
      "type": "string",
      "format": "date-time",
      "example": "2026-08-12T22:28:14Z"
    },
    "deduplicated_entities": {
      "type": "array",
      "items": {
        "type": "object",
        "required": [
          "entity_id",
          "resolution_action",
          "category",
          "name",
          "wkt_geometry",
          "confidence_score",
          "lifecycle_state"
        ],
        "properties": {
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "resolution_action": {"type": "string", "enum": ["INSERT_NEW", "UPDATE_EXISTING", "CORROBORATE_CITATION"], "example": "INSERT_NEW"},
          "category": {"type": "string", "example": "service_area"},
          "name": {"type": "string", "example": "Sub-grade Fan Room 101"},
          "wkt_geometry": {"type": "string", "example": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"},
          "confidence_score": {"type": "integer", "minimum": 80, "maximum": 100, "example": 95},
          "lifecycle_state": {"type": "string", "example": "CORROBORATED"}
        }
      }
    },
    "deduplicated_relationships": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["relationship_id", "subject_entity_id", "relationship_type", "object_entity_id", "confidence_score"],
        "properties": {
          "relationship_id": {"type": "string", "example": "rel_aa18_10"},
          "subject_entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "relationship_type": {"type": "string", "example": "CONTAINS"},
          "object_entity_id": {"type": "string", "example": "wtc1_f1_chiller_unit_1"},
          "confidence_score": {"type": "integer", "example": 95}
        }
      }
    },
    "evidence_reconciliation": {
      "type": "object",
      "required": ["total_citations_linked", "new_sources_registered", "corroborated_citations"],
      "properties": {
        "total_citations_linked": {"type": "integer", "example": 15},
        "new_sources_registered": {"type": "integer", "example": 0},
        "corroborated_citations": {"type": "integer", "example": 12}
      }
    },
    "confidence_reconciliation": {
      "type": "object",
      "required": ["average_reconciled_confidence", "min_reconciled_confidence", "max_reconciled_confidence"],
      "properties": {
        "average_reconciled_confidence": {"type": "number", "example": 95.5},
        "min_reconciled_confidence": {"type": "integer", "example": 85},
        "max_reconciled_confidence": {"type": "integer", "example": 100}
      }
    },
    "conflict_resolution_log": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["conflict_id", "entity_id", "conflict_type", "resolution_outcome"],
        "properties": {
          "conflict_id": {"type": "string", "example": "cnf_001"},
          "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
          "conflict_type": {"type": "string", "example": "NAME_STRING_DISAGREEMENT"},
          "resolution_outcome": {"type": "string", "example": "STORED_NAME_PREVAILED_CANDIDATE_SAVED_AS_ALIAS"}
        }
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
      "items": {"type": "object"}
    },
    "audit_metadata": {
      "type": "object",
      "required": ["pipeline_stage", "processor_id", "execution_duration_ms"],
      "properties": {
        "pipeline_stage": {"type": "string", "example": "Stage_5_PostGIS_Deduplication"},
        "processor_id": {"type": "string", "example": "dedup_engine_v1"},
        "execution_duration_ms": {"type": "integer", "example": 450}
      }
    }
  }
}
```

---

## 3. Detailed Field Definitions Table

| Field Name | Data Type | Req/Opt | Description | Validation Rules |
| :--- | :--- | :--- | :--- | :--- |
| `contract_version` | `string` | **Required** | Contract semantic version string | Must equal `"1.0.0"` |
| `source_file_hash` | `string` | **Required** | SHA-256 hash of source PDF | Exactly 64 hex characters |
| `source_sheet_code` | `string` | **Required** | Drawing sheet ID (Principle 2) | Regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$` |
| `resolution_timestamp` | `string` | **Required** | Timestamp of deduplication | ISO 8601 UTC format |
| `deduplicated_entities` | `array` | **Required** | Resolved entity action list | Action `INSERT_NEW`, `UPDATE_EXISTING`, `CORROBORATE` |
| `deduplicated_relationships` | `array` | **Required** | Property graph edges | `subject != object` (no self-loops) |
| `evidence_reconciliation` | `object` | **Required** | Citation merging scorecard | Contains `total_citations_linked` |
| `confidence_reconciliation`| `object` | **Required** | Reconciled confidence metrics | `min_reconciled_confidence >= 80` |
| `conflict_resolution_log` | `array` | **Required** | Enforced resolution audit log | Stored DB data PREVAILS |
| `human_review_status` | `object` | **Required** | Review gate triggers | Object containing `requires_human_review` |
| `validation_status` | `string` | **Required** | Stage 5 result status | Enum `VALIDATED`, `WARNING`, `FAILED` |
| `quarantine_status` | `boolean` | **Required** | Quarantine flag | `true` or `false` |
| `processing_errors` | `array` | **Required** | Processing error list | Array of error objects (empty if clean) |
| `audit_metadata` | `object` | **Required** | Stage 5 execution telemetry | Contains `pipeline_stage`, `duration_ms` |

---

## 4. Quarantine Contract Specification

If `quarantine_status = true` or `validation_status = FAILED`, Stage 5 MUST output a Deduplication Quarantine Payload to `data/failed_pdfs/[HASH]_dedup_quarantine.json`:

```json
{
  "contract_version": "1.0.0",
  "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "source_sheet_code": "A-A-18",
  "quarantine_reason": "UNRESOLVABLE_CATEGORY_TIER_MISMATCH",
  "quarantine_timestamp": "2026-08-12T22:28:14Z",
  "processing_errors": [
    {
      "error_code": "ERR_CATEGORY_MISMATCH",
      "error_message": "Candidate category 'space' conflicts with stored category 'element' for entity ID wtc1_f1_core_zone",
      "severity": "CRITICAL",
      "timestamp": "2026-08-12T22:28:14Z"
    }
  ]
}
```

---

## 5. Stage 6 Dependencies & Contract Freeze Status

- **Downstream Consumer:** Stage 6 Transactional Database Ingestion Pipeline (`scripts/ingest_pipeline.py`).
- **Contract Interface Status:** **FROZEN AT VERSION 1.0.0**.
- **Governance Sign-off:** ✅ Approved for Stage 5 PostGIS deduplication output usage.
