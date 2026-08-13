# Phase 4 Stage 6: Ingestion Data Contract Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 6 INGESTION DATA CONTRACT SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Technical Spec:** [`docs/PHASE_4_STAGE_6_DATABASE_INGESTION_SPEC.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_6_DATABASE_INGESTION_SPEC.md)  
**Parent Upstream Contract:** [`docs/PHASE_4_STAGE_5_DEDUPLICATION_CONTRACT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_4_STAGE_5_DEDUPLICATION_CONTRACT.md)  
**Parent Architecture Record:** [`docs/ENTITY_REGISTRY_ARCHITECTURE_DECISION.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_REGISTRY_ARCHITECTURE_DECISION.md) (ADR-005)  
**Contract Version:** `1.0.0`  

---

## Executive Summary

This document establishes the **authoritative Stage 6 Ingestion Data Contract Specification** defining the exact JSON schema produced by Stage 6 (Transactional Database Ingestion) and consumed by repository validation, audit, monitoring, and operational reporting systems.

Zero implementation code, zero Python scripts, zero ETL scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this contract specification document.

This contract freezes the final transactional database output interface, detailing every required field, data type, entity/relationship/citation ingestion result, transaction status, rollback audit payload, operational metrics, and acceptance criteria.

---

## 1. Verified Facts

```text
CONTRACT SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Master Entity Registry (`entities`) Architecture Active (ADR-005)    │ ✅ PASS │
│ 3. Stage 5 Deduplication Contract Formally Frozen (`Stage5Deduplic...`) │ ✅ PASS │
│ 4. Stage 6 Technical Specification Formally Defined                    │ ✅ PASS │
│ 5. Contract Version Standardized to Semantic Versioning (`1.0.0`)       │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Complete Stage 6 Output Contract Schema (`Stage6IngestionContract`)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Stage6IngestionContract",
  "version": "1.0.0",
  "type": "object",
  "required": [
    "contract_version",
    "source_file_hash",
    "source_sheet_code",
    "transaction_id",
    "ingestion_timestamp",
    "ingested_entities",
    "ingested_relationships",
    "ingested_citations",
    "validation_results",
    "transaction_status",
    "rollback_status",
    "human_review_audit",
    "quarantine_audit",
    "processing_errors",
    "operational_metrics"
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
    "transaction_id": {
      "type": "string",
      "example": "tx_20260812_001045"
    },
    "ingestion_timestamp": {
      "type": "string",
      "format": "date-time",
      "example": "2026-08-12T22:29:11Z"
    },
    "ingested_entities": {
      "type": "object",
      "required": ["total_inserted", "total_updated", "entities_inserted", "entities_updated"],
      "properties": {
        "total_inserted": {"type": "integer", "example": 12},
        "total_updated": {"type": "integer", "example": 3},
        "entities_inserted": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["entity_id", "category", "target_table", "confidence_score"],
            "properties": {
              "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
              "category": {"type": "string", "example": "service_area"},
              "target_table": {"type": "string", "example": "spaces"},
              "confidence_score": {"type": "integer", "example": 95}
            }
          }
        },
        "entities_updated": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["entity_id", "updated_attributes"],
            "properties": {
              "entity_id": {"type": "string", "example": "wtc1_floor_1"},
              "updated_attributes": {"type": "array", "items": {"type": "string"}, "example": ["confidence_score", "updated_at"]}
            }
          }
        }
      }
    },
    "ingested_relationships": {
      "type": "object",
      "required": ["total_edges_inserted", "edges_inserted"],
      "properties": {
        "total_edges_inserted": {"type": "integer", "example": 10},
        "edges_inserted": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["relationship_id", "subject_entity_id", "relationship_type", "object_entity_id"],
            "properties": {
              "relationship_id": {"type": "string", "example": "rel_aa18_10"},
              "subject_entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
              "relationship_type": {"type": "string", "example": "CONTAINS"},
              "object_entity_id": {"type": "string", "example": "wtc1_f1_chiller_unit_1"}
            }
          }
        }
      }
    },
    "ingested_citations": {
      "type": "object",
      "required": ["total_citations_inserted", "citations_inserted"],
      "properties": {
        "total_citations_inserted": {"type": "integer", "example": 15},
        "citations_inserted": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["citation_id", "entity_id", "source_id", "sheet_code"],
            "properties": {
              "citation_id": {"type": "string", "example": "cite_wtc1_f1_fan_room_101"},
              "entity_id": {"type": "string", "example": "wtc1_f1_fan_room_101"},
              "source_id": {"type": "string", "example": "src_yamasaki_drawings"},
              "sheet_code": {"type": "string", "example": "A-A-18"}
            }
          }
        }
      }
    },
    "validation_results": {
      "type": "object",
      "required": ["single_parent_check_passed", "foreign_keys_passed", "postgis_srid_passed", "orphan_records_detected"],
      "properties": {
        "single_parent_check_passed": {"type": "boolean", "example": true},
        "foreign_keys_passed": {"type": "boolean", "example": true},
        "postgis_srid_passed": {"type": "boolean", "example": true},
        "orphan_records_detected": {"type": "integer", "example": 0}
      }
    },
    "transaction_status": {
      "type": "string",
      "enum": ["COMMITTED", "ROLLED_BACK", "FAILED"],
      "example": "COMMITTED"
    },
    "rollback_status": {
      "type": "object",
      "required": ["executed_rollback", "rollback_timestamp", "post_rollback_catalog_clean"],
      "properties": {
        "executed_rollback": {"type": "boolean", "example": false},
        "rollback_timestamp": {"type": ["string", "null"], "example": null},
        "post_rollback_catalog_clean": {"type": "boolean", "example": true}
      }
    },
    "human_review_audit": {
      "type": "object",
      "required": ["human_review_required", "review_signoff_timestamp", "reviewer_id"],
      "properties": {
        "human_review_required": {"type": "boolean", "example": false},
        "review_signoff_timestamp": {"type": ["string", "null"], "example": null},
        "reviewer_id": {"type": ["string", "null"], "example": null}
      }
    },
    "quarantine_audit": {
      "type": "object",
      "required": ["quarantined", "quarantine_file_path"],
      "properties": {
        "quarantined": {"type": "boolean", "example": false},
        "quarantine_file_path": {"type": ["string", "null"], "example": null}
      }
    },
    "processing_errors": {
      "type": "array",
      "items": {"type": "object"}
    },
    "operational_metrics": {
      "type": "object",
      "required": ["total_db_query_time_ms", "total_transaction_time_ms", "memory_usage_mb"],
      "properties": {
        "total_db_query_time_ms": {"type": "integer", "example": 120},
        "total_transaction_time_ms": {"type": "integer", "example": 180},
        "memory_usage_mb": {"type": "number", "example": 45.2}
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
| `transaction_id` | `string` | **Required** | PostgreSQL transaction tracking ID | Unique transaction string |
| `ingestion_timestamp` | `string` | **Required** | Timestamp of commit/rollback | ISO 8601 UTC format |
| `ingested_entities` | `object` | **Required** | Entities inserted and updated | `total_inserted >= 0` |
| `ingested_relationships`| `object` | **Required** | Property graph edges inserted | `subject != object` |
| `ingested_citations` | `object` | **Required** | Epistemic citations inserted | `sheet_code` match mandatory |
| `validation_results` | `object` | **Required** | Post-ingestion constraint audit | `orphan_records_detected == 0` |
| `transaction_status` | `string` | **Required** | Transaction outcome status | Enum `COMMITTED`, `ROLLED_BACK`, `FAILED` |
| `rollback_status` | `object` | **Required** | Rollback audit details | `post_rollback_catalog_clean == true` |
| `human_review_audit` | `object` | **Required** | Human sign-off tracking payload | Must be non-null if review required |
| `quarantine_audit` | `object` | **Required** | Quarantine disposition payload | `quarantined == false` for clean commit |
| `processing_errors` | `array` | **Required** | Processing error list | Array of error objects (empty if clean) |
| `operational_metrics` | `object` | **Required** | Execution telemetry | Contains `transaction_time_ms` |

---

## 4. Rollback Audit Contract Specification

If `transaction_status = ROLLED_BACK` or `FAILED`, Stage 6 MUST output a Rollback Audit Payload to `data/failed_pdfs/[HASH]_rollback_audit.json`:

```json
{
  "contract_version": "1.0.0",
  "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "source_sheet_code": "A-A-18",
  "transaction_id": "tx_20260812_001045_FAILED",
  "transaction_status": "ROLLED_BACK",
  "rollback_status": {
    "executed_rollback": true,
    "rollback_timestamp": "2026-08-12T22:29:11Z",
    "post_rollback_catalog_clean": true
  },
  "processing_errors": [
    {
      "error_code": "ERR_FOREIGN_KEY_VIOLATION",
      "error_message": "insert or update on table 'elements' violates foreign key constraint 'elements_space_id_fkey'",
      "sqlstate": "23503",
      "severity": "CRITICAL",
      "timestamp": "2026-08-12T22:29:11Z"
    }
  ]
}
```

---

## 5. Post-Ingestion Dependencies & Contract Freeze Status

- **Consumer Systems:** Operational Reporting Dashboard, Audit Trail Verification, Phase 5 3D Mesh Generation Engine.
- **Contract Interface Status:** **FROZEN AT VERSION 1.0.0**.
- **Governance Sign-off:** ✅ Approved for Stage 6 transactional ingestion contract usage.
