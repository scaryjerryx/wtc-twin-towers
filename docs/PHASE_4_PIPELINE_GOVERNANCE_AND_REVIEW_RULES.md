# Phase 4 Pipeline Governance and Review Rules

**Document Status:** ✅ AUTHORITATIVE PHASE 4 PIPELINE GOVERNANCE SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md), [`docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md)  
**Parent Architecture:** [`docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md)  
**Frozen Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  
**Frozen DDL Migration:** [`database/migrations/V1_1__create_world_model_schema_revised.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_1__create_world_model_schema_revised.sql)  

> [!NOTE]
> **ADR-006 & ADR-006A Realignment Notice:** Stage 3 Gemini Multi-Modal Architectural Analysis is the **PRIMARY RECONSTRUCTION ENGINE**. OCR and Vector Extraction are **SUPPORTING EVIDENCE SOURCES**. OCR and Vector extraction may provide evidence, but may NOT provide authority. Composite confidence scoring follows the ADR-006A Option B Evidence-Quality model.


---

## Executive Summary

This document establishes the **authoritative Pipeline Governance and Review Rules Specification** governing **Phase 4: Automated PDF Parsing Pipeline**.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this governance document.

This specification details the 12 non-negotiable governance mechanisms, human review gates, confidence scoring boundaries ($[80, 100]$), epistemic evidence requirements (Principle 2: *Cite Sources*), quarantine rules, conflict resolution rules, rollback procedures, audit trails, and acceptance criteria required before writing Phase 4 implementation code.

---

## 1. Verified Facts

```text
EVIDENTIARY BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. Phase 3 Database Foundation Frozen & Active (`wtc_evidence`)        │ ✅ PASS │
│ 2. Executed Migration `V1_1__create_world_model_schema_revised.sql`     │ ✅ PASS │
│ 3. Master Entity Registry (`entities`) Architecture Active (ADR-005)    │ ✅ PASS │
│ 4. PDF Incoming Directory Active (`data/incoming_pdfs/`)               │ ✅ PASS │
│ 5. Phase 4 Scope & Implementation Roadmap Formally Defined             │ ✅ PASS │
│ 6. Principle 5 (Quantify Uncertainty: score >= 80) Active               │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. 12 Core Pipeline Governance Specifications

### 2.1 Human Review Gates
- **Purpose:** Prevent unverified AI extraction outputs from entering the production database without human sign-off.
- **Governing Principle:** Principle 1 (*Evidence Over Assumptions*) & Principle 14 (*Human-in-the-Loop Authority*).
- **Inputs:** Candidate entity JSON payloads, confidence scores, and source drawing overlays.
- **Outputs:** Approved entity batch queue or human review flag.
- **Approval Criteria:** Human reviewer confirms entity category, spatial geometry, and drawing sheet code link.
- **Failure Conditions:** Discrepancy detected between AI prediction and source drawing image.

### 2.2 Confidence Scoring Rules
- **Purpose:** Enforce quantitative uncertainty bounds on all extracted entities and relationships.
- **Governing Principle:** Principle 5 (*Quantify Uncertainty*).
- **Inputs:** Raw confidence model probability outputs $[0.0, 1.0]$.
- **Outputs:** Scaled integer confidence score $[0, 100]$.
- **Approval Criteria:** Calculated confidence score $\ge 80$.
- **Failure Conditions:** Score $< 80$ triggers immediate routing to quarantine.

### 2.3 Evidence Citation Requirements
- **Purpose:** Ensure 100% of database entities link directly to a primary source drawing sheet.
- **Governing Principle:** Principle 2 (*Cite Sources*).
- **Inputs:** Extracted entity payload + drawing title block metadata (`sheet_code`, `source_id`).
- **Outputs:** Epistemic citation record in `entity_evidence_citations`.
- **Approval Criteria:** Valid drawing sheet code (`A-A-18`, `A-A-121`, etc.) attached to entity.
- **Failure Conditions:** Missing drawing sheet code or unlinked source reference.

### 2.4 Entity Approval Rules
- **Purpose:** Validate entity schema compliance and Master Entity Registry (`entities`) registration.
- **Governing Principle:** Principle 3 (*Preserve Relational Integrity*) & ADR-005.
- **Inputs:** Candidate entity payload.
- **Outputs:** Validated entity record ready for `entities` master table upsert.
- **Approval Criteria:** Entity ID exists in `entities` table registry, valid category ENUM, single-parent `CHECK` satisfied (`= 1`).
- **Failure Conditions:** Multi-parent violation, unregistered entity ID, or invalid category string.

### 2.5 Relationship Approval Rules
- **Purpose:** Verify non-reflexivity and endpoint existence for directed property graph edges.
- **Governing Principle:** ADR-002 & Principle 3 (*Preserve Relational Integrity*).
- **Inputs:** Candidate relationship tuple (`subject_entity_id`, `relationship_type`, `object_entity_id`).
- **Outputs:** Validated relationship record ready for `relationships` table insertion.
- **Approval Criteria:** `subject_entity_id` $\ne$ `object_entity_id`, valid relationship ENUM, both endpoints exist in `entities`.
- **Failure Conditions:** Self-loop edge, unproven endpoint ID, or invalid edge ENUM.

### 2.6 Quarantine Rules
- **Purpose:** Isolate invalid PDF drawings and low-confidence extraction payloads without stopping the batch processing pipeline.
- **Governing Principle:** System Robustness & Isolated Error Containment.
- **Inputs:** Failed PDF file or entity payload flagged with errors.
- **Outputs:** File moved to `data/failed_pdfs/` + quarantine JSON record in `data/metadata_queue/`.
- **Approval Criteria:** File successfully quarantined and logged.
- **Failure Conditions:** Unwritable quarantine directory or unhandled runtime crash.

### 2.7 Rejection Rules
- **Purpose:** Automatically reject hallucinated or un-evidenced AI extraction candidates.
- **Governing Principle:** Principle 1 (*Evidence Over Assumptions*).
- **Inputs:** Candidate extraction payload.
- **Outputs:** Rejected entity payload logged to audit stream.
- **Approval Criteria:** Rejection triggered on zero citation evidence or invalid PostGIS geometry.
- **Failure Conditions:** Attempting to force-insert an un-evidenced candidate.

### 2.8 Database Ingestion Approval Rules
- **Purpose:** Ensure transactional safety (`BEGIN; ... COMMIT;`) during database load.
- **Governing Principle:** Principle 4 (*Transactional Integrity*).
- **Inputs:** Batch list of validated entities, citations, and relationships.
- **Outputs:** Committed PostgreSQL transaction.
- **Approval Criteria:** 100% clean SQL execution with zero constraint violations.
- **Failure Conditions:** Any SQL error triggers immediate `ROLLBACK;`.

### 2.9 Rollback & Recovery Procedures
- **Purpose:** Guarantee database clean state restoration upon processing exceptions.
- **Governing Principle:** Transactional Atomicity.
- **Inputs:** PostgreSQL exception signal.
- **Outputs:** Complete transactional rollback; zero orphan rows in catalog.
- **Approval Criteria:** Catalog table row counts prior to transaction match counts post-rollback.
- **Failure Conditions:** Partial transaction commit.

### 2.10 Audit Trail Requirements
- **Purpose:** Maintain complete historical audit trail of all ingestion attempts, modifications, and quarantines.
- **Governing Principle:** Principle 6 (*Auditable Traceability*).
- **Inputs:** Ingestion logs, timestamps, user/agent ID, source file hash.
- **Outputs:** Structured audit record in `data/processed_pdfs/` metadata.
- **Approval Criteria:** Log entry contains timestamp, source file SHA-256 hash, and status code.
- **Failure Conditions:** Missing audit log entry.

### 2.11 Pipeline Validation Requirements
- **Purpose:** Validate extracted spatial geometries using PostGIS functions (`ST_IsValid`, `ST_SRID`).
- **Governing Principle:** Physical Spatial Geometry Accuracy.
- **Inputs:** Candidate 2D polygon footprint.
- **Outputs:** PostGIS geometry object in `EPSG:2263`.
- **Approval Criteria:** `ST_IsValid = true` and `ST_SRID = 2263`.
- **Failure Conditions:** Self-intersecting polygon (`ST_IsValid = false`) or wrong SRID.

### 2.12 Phase 4 Acceptance Criteria
- **Purpose:** Define non-negotiable quantitative thresholds for Phase 4 sign-off.
- **Governing Principle:** Total System Quality Verification.
- **Inputs:** Consolidated post-processing audit report.
- **Outputs:** Phase 4 completion sign-off artifact.
- **Approval Criteria:** Batch processing pass rate $\ge 95\%$, 100% citation coverage, 0 orphan database records.
- **Failure Conditions:** Pass rate $< 95\%$ or any orphan record detected in system catalog.

---

## 3. Mandatory Governance Questions (Definitive Answers)

```text
MANDATORY GOVERNANCE ANSWERS MATRIX:
┌───────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Scenario / Condition                              │ Mandatory Enforced Governance Action                   │
├───────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 1. confidence_score < 80                          │ Candidate entity is REJECTED from DB & QUARANTINED     │
│ 2. No citation exists                             │ Entity insertion is BLOCKED; Principle 2 violation     │
│ 3. Geometry validation fails (ST_IsValid = false)  │ Candidate geometry is REJECTED & sent to review        │
│ 4. Duplicate entities detected                    │ PostGIS upsert executes; attributes merged cleanly      │
│ 5. Relationship endpoints cannot be proven        │ Graph edge insertion is REJECTED; ADR-002 enforced     │
│ 6. AI extraction disagrees with repository evidence│ Repository evidence prevails; AI prediction REJECTED   │
│ 7. Multiple source documents conflict             │ State marked CORROBORATED; lower score assigned        │
└───────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 4. Final Governance Recommendation

```text
FINAL GOVERNANCE DECISION SELECTION:
[ ] Phase 4 Governance Incomplete
[ ] Phase 4 Governance Requires Revision
[X] Phase 4 Governance Complete And Implementation Authorized ◄── SOLE SELECTED DECISION
```

### Detailed Justification for `[X] Phase 4 Governance Complete And Implementation Authorized`:
All 12 pipeline governance mechanisms, human review gates, quarantine rules, error handling procedures, conflict resolution matrices, and acceptance criteria have been fully defined. Phase 4 governance is **COMPLETE AND IMPLEMENTATION AUTHORIZED**. Phase 4 pipeline code authoring may now begin.
