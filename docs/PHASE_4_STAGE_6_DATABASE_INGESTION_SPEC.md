# Phase 4 Stage 6: Transactional Database Ingestion Technical Specification

**Document Status:** ✅ AUTHORITATIVE STAGE 6 TECHNICAL SPECIFICATION  
**Classification:** **DATABASE PERSISTENCE INFRASTRUCTURE (ADR-006)**  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
**Parent Architecture Record:** [`docs/ENTITY_REGISTRY_ARCHITECTURE_DECISION.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_REGISTRY_ARCHITECTURE_DECISION.md) (ADR-005)  
**Frozen Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  
**Frozen DDL Migration:** [`database/migrations/V1_1__create_world_model_schema_revised.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_1__create_world_model_schema_revised.sql)  

> [!NOTE]
> **ADR-006 Classification Notice:** Stage 6 functions as **DATABASE PERSISTENCE INFRASTRUCTURE**. It manages atomic PostgreSQL transactions (`BEGIN; ... COMMIT;`), ADR-005 Master Entity Registry (`entities`) registration, foreign key checks, and atomic rollbacks.


---

## Executive Summary

This document establishes the **authoritative Stage 6 Technical Specification** governing **Transactional Database Ingestion** within Phase 4.

Zero implementation code, zero Python scripts, zero ETL scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this specification document.

Stage 6 consumes deduplicated entity payloads (`Stage5DeduplicationContract`), managing transactional database execution (`BEGIN; ... COMMIT;`), Master Entity Registry (`entities` ADR-005) registration, physical tier table upserts, epistemic citation linking, property graph edge creation, constraint validation, error quarantine, and atomic rollback procedures.

---

## 1. Verified Facts

```text
SPECIFICATION BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Executed Migration `V1_1__create_world_model_schema_revised.sql`     │ ✅ PASS │
│ 3. Master Entity Registry (`entities`) Architecture Active (ADR-005)    │ ✅ PASS │
│ 4. Stage 5 Deduplication Contract Formally Frozen                      │ ✅ PASS │
│ 5. Single-Parent `CHECK` Constraints (`= 1`) Active on Tier Tables     │ ✅ PASS │
│ 6. Declarative FKs with `ON DELETE RESTRICT` Active Across Schema      │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Stage 6 Technical Requirements (12 Modules)

### 2.1 Stage 6 Inputs
- **Purpose:** Ingest Stage 5 deduplicated payloads (`Stage5DeduplicationContract`).
- **Inputs:** `Stage5DeduplicationContract` (version `1.0.0`) from Stage 5.
- **Outputs:** Verified database load job payload.
- **Validation Rules:** `validation_status` equals `"VALIDATED"`, `quarantine_status` equals `false`, non-empty `resolved_entities` list.
- **Failure Conditions:** Input payload unvalidated or missing contract parameters.
- **Governance Requirements:** Require validated Stage 5 deduplication payload before opening database transaction.

### 2.2 Entity Ingestion Workflow
- **Purpose:** Execute top-down spatial tier table inserts (`sites` ──► `buildings` ──► `floors` ──► `zones` ──► `spaces` ──► `elements`).
- **Inputs:** Resolved entity action list (`INSERT_NEW`, `UPDATE_EXISTING`).
- **Outputs:** Database table rows inserted or updated.
- **Validation Rules:** Top-down insertion order mandatory; target table match `entity_category_enum`.
- **Failure Conditions:** Foreign key violation or missing parent tier record.
- **Governance Requirements:** All entity inserts must specify `confidence_score >= 80` and valid `lifecycle_state_enum`.

### 2.3 Relationship Ingestion Workflow
- **Purpose:** Ingest directed property graph edges into `relationships` table.
- **Inputs:** Resolved relationship tuples (`subject_entity_id`, `relationship_type`, `object_entity_id`).
- **Outputs:** Property graph edge rows in `relationships`.
- **Validation Rules:** Non-reflexivity `check_no_self_loops` (`subject_entity_id != object_entity_id`), foreign key endpoints exist in `entities`.
- **Failure Conditions:** Endpoint foreign key violation or self-loop edge.
- **Governance Requirements:** Execute `ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO UPDATE SET confidence_score = EXCLUDED.confidence_score`.

### 2.4 Evidence Citation Ingestion Workflow
- **Purpose:** Ingest epistemic drawing sheet citations into `entity_evidence_citations` (Principle 2: *Cite Sources*).
- **Inputs:** Citation tuples (`citation_id`, `entity_id`, `source_id`, `sheet_code`).
- **Outputs:** Citation junction rows in `entity_evidence_citations`.
- **Validation Rules:** `entity_id` exists in `entities`, `source_id` exists in `sources`.
- **Failure Conditions:** Orphan citation or invalid source reference.
- **Governance Requirements:** Execute `ON CONFLICT (entity_id, source_id, sheet_code) DO NOTHING`.

### 2.5 Entity Registry Integration Workflow
- **Purpose:** Enforce Architectural Decision Record 005 (ADR-005), inserting master records into `entities` BEFORE inserting tier table rows.
- **Inputs:** Candidate entity payload.
- **Outputs:** Registry row in `entities(entity_id, entity_category, building_id, confidence_score, lifecycle_state)`.
- **Validation Rules:** Primary Key `entity_id` registered cleanly in `entities`.
- **Failure Conditions:** Primary Key collision or missing category ENUM.
- **Governance Requirements:** Execute `ON CONFLICT (entity_id) DO UPDATE SET confidence_score = EXCLUDED.confidence_score, updated_at = CURRENT_TIMESTAMP`.

### 2.6 Transaction Management Rules
- **Purpose:** Manage transactional atomicity (`BEGIN; ... COMMIT;`) during database ingestion.
- **Inputs:** SQL statement batch.
- **Outputs:** Transaction commit (`COMMIT;`) or rollback (`ROLLBACK;`).
- **Validation Rules:** Execute entire ingestion payload inside a single PostgreSQL transaction block.
- **Failure Conditions:** Any single SQL exception triggers immediate transaction rollback.
- **Governance Requirements:** Zero partial commits permitted; all or nothing execution.

### 2.7 Constraint Validation Requirements
- **Purpose:** Verify database constraints (`NOT NULL`, `FOREIGN KEY`, `CHECK`, `UNIQUE`) during SQL execution.
- **Inputs:** Active PostgreSQL engine constraint checks.
- **Outputs:** Constraint pass confirmation.
- **Validation Rules:** Single-parent `CHECK` constraint (`((parent_a IS NOT NULL)::int + ...) = 1`), `confidence_score BETWEEN 0 AND 100`.
- **Failure Conditions:** `check_violation` (SQLSTATE 23514), `foreign_key_violation` (SQLSTATE 23503), or `not_null_violation` (SQLSTATE 23502).
- **Governance Requirements:** Capture constraint violation stack trace and roll back transaction.

### 2.8 Human Review Enforcement Requirements
- **Purpose:** Block database ingestion for candidate payloads flagged for human review until sign-off is recorded.
- **Inputs:** Human review status payload (`human_review_status.requires_human_review`).
- **Outputs:** Ingestion approval or review block.
- **Validation Rules:** If `requires_human_review = true`, `human_review_signoff_timestamp` MUST be non-null.
- **Failure Conditions:** Attempting to ingest flagged candidate without human review sign-off.
- **Governance Requirements:** Reject flagged payloads without human sign-off directly to quarantine.

### 2.9 Quarantine Handling Requirements
- **Purpose:** Quarantine failed transaction payloads into `data/failed_pdfs/` without corrupting active database state.
- **Inputs:** Transaction exception signal + failed payload.
- **Outputs:** Stage 6 quarantine JSON log.
- **Validation Rules:** Write failed payload + SQLSTATE error code to `data/failed_pdfs/ingestion_failure_[HASH].json`.
- **Failure Conditions:** File write error during quarantine logging.
- **Governance Requirements:** Ensure database state remains untouched following rollback.

### 2.10 Rollback Requirements
- **Purpose:** Restores database catalog to its exact pre-transaction state upon SQL execution failure.
- **Inputs:** SQL error signal.
- **Outputs:** Transaction rollback execution (`ROLLBACK;`).
- **Validation Rules:** Zero orphan rows or uncommitted data left in system catalog.
- **Failure Conditions:** Unhandled transaction state.
- **Governance Requirements:** Verify catalog row counts post-rollback match pre-transaction counts.

### 2.11 Audit Logging Requirements
- **Purpose:** Record immutable audit logs of all committed database ingestion operations (Principle 6: *Auditable Traceability*).
- **Inputs:** Transaction commit success signal + processing metadata.
- **Outputs:** Ingestion audit record in `data/processed_pdfs/ingestion_audit_[HASH].json`.
- **Validation Rules:** Log record contains SHA-256 file hash, sheet code, inserted entity count, timestamp, and transaction ID.
- **Failure Conditions:** Missing audit log.
- **Governance Requirements:** Store audit log in persistent filesystem.

### 2.12 Acceptance Criteria
- **Purpose:** Define non-negotiable quantitative criteria for Stage 6 completion.
- **Inputs:** Stage 6 execution scorecard.
- **Outputs:** Stage 6 completion sign-off.
- **Validation Rules:** 100% of candidate entities and relationships committed with 0 constraint exceptions, 0 orphan catalog rows.
- **Failure Conditions:** Transaction failure or uncommitted records.
- **Governance Requirements:** Total compliance with Principle 4 (*Transactional Integrity*).

---

## 3. Mandatory Governance Scenario Answers Matrix

```text
MANDATORY GOVERNANCE ANSWERS MATRIX:
┌───────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Scenario / Exception Condition                    │ Enforced Stage 6 Database Action                       │
├───────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. Entity already exists                          │ `ON CONFLICT (entity_id) DO UPDATE` executes cleanly   │
│ 2. Relationship already exists                    │ `ON CONFLICT (subj, type, obj) DO UPDATE` executes     │
│ 3. Citation already exists                        │ `ON CONFLICT (entity_id, source_id, sheet) DO NOTHING` │
│ 4. Confidence score drops below threshold (< 80)  │ Entity insertion BLOCKED; candidate QUARANTINED        │
│ 5. Human review has not occurred                  │ Ingestion BLOCKED; candidate sent to review queue      │
│ 6. Foreign key violation occurs (SQLSTATE 23503)  │ Transaction ROLLED BACK immediately; payload quarantined│
│ 7. CHECK constraint violation occurs (23514)      │ Transaction ROLLED BACK immediately; payload quarantined│
│ 8. Transaction partially succeeds                 │ IMPOSSIBLE; `ROLLBACK` executes, 0 rows committed      │
└───────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 4. Final Specification Status

- **Status:** **FROZEN AT VERSION 1.0.0**
- **Consumer:** Stage 6 Database Ingestion Script (`scripts/ingest_pipeline.py`).  
- **Governance Sign-off:** ✅ Approved for Stage 6 transactional ingestion implementation.
