# Phase 5 Reconstruction Proposal Validation Workflow

**Document Status:** ✅ AUTHORITATIVE PROPOSAL VALIDATION WORKFLOW SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:**  
1. [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
2. [`docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md)  
**Parent Architecture Spec:** [`docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_5_GEMINI_RECONSTRUCTION_ARCHITECTURE.md)  
**Parent Governance Standard:** [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL WORKFLOW DECISION:** **`[X] Workflow Approved`**  

---

## Executive Summary

This document establishes the **authoritative Phase 5 Reconstruction Proposal Validation Workflow Specification** defining how Gemini-generated reconstruction proposals are reviewed, validated, approved, rejected, escalated, and authorized for Stage 5 Deduplication and Stage 6 Database Ingestion.

Zero code modifications, zero database schema changes, zero implementation scripts, and zero web searches were created in this workflow specification document.

The workflow governs how Gemini proposals transition through 5 canonical lifecycle states (**DRAFT_SEED**, **CORROBORATED**, **VALIDATED**, **DEPRECATED**, **ARCHIVED**), enforcing strict evidence attribution rules (Principle 2), ADR-006A composite confidence thresholds ($[80, 100]$), human review gates, and atomic database authorization rules.

The single selected final recommendation is **`[X] Workflow Approved`**.

---

## 1. Verified Facts

```text
GOVERNANCE WORKFLOW BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. ADR-006 Established Gemini as Primary Reconstruction Engine         │ ✅ PASS │
│ 2. Gemini Proposals Require Governance Approval Before Database Load    │ ✅ PASS │
│ 3. 5 Canonical Lifecycle States Defined (DRAFT_SEED .. ARCHIVED)       │ ✅ PASS │
│ 4. Mandatory Human Review Gates Defined for Scores [70, 79]            │ ✅ PASS │
│ 5. Stage 5 & Stage 6 Ingestion Authorization Criteria Defined           │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Proposal Lifecycle State Transitions

```text
CANONICAL LIFECYCLE STATE TRANSITION FLOW:
   Gemini Proposal Creation (Single Sheet Match)
                       │
                       ▼
                 [ DRAFT_SEED ] ◄── Initial candidate entity with 1 sheet citation
                       │
          Multi-Sheet Matching (>= 2 Independent Sheets)
                       │
                       ▼
                 [ CORROBORATED ] ◄── Corroborated across 2+ blueprint sheets
                       │
     Formal Verification & Human Review Sign-Off
                       │
                       ▼
                 [ VALIDATED ] ◄── Verified & committed to PostgreSQL DB (wtc_evidence)
                       │
          Superseded by Newer Historical Revision
                       │
                       ▼
                 [ DEPRECATED ] ◄── Historical revision retained for audit trail
                       │
             Explicit Architectural Retraction
                       │
                       ▼
                 [ ARCHIVED ] ◄── Retracted with immutable rationale log
```

### Detailed Lifecycle State Transition Definitions:

1. **`DRAFT_SEED`:**  
   - **Trigger:** Proposal created from a single primary drawing sheet (e.g. Sheet `A-A-18`) with composite confidence score $\ge 80$.
   - **Evidence Requirement:** 1 primary source sheet citation (`sheet_code`, bounding box, observation text).
   - **Database State:** Stored in Master Entity Registry `entities` with `lifecycle_state = 'DRAFT_SEED'`.

2. **`CORROBORATED`:**  
   - **Trigger:** Entity is independently matched and corroborated across $\ge 2$ distinct drawing sheets (e.g. Floor Plan `A-A-18` + Core Elevation `A-A-121`) with spatial $\text{IoU} \ge 0.90$.
   - **Evidence Requirement:** $\ge 2$ independent primary source sheet citations.
   - **Database State:** Updated in `entities` with `lifecycle_state = 'CORROBORATED'` and composite confidence score increased by $+2$.

3. **`VALIDATED`:**  
   - **Trigger:** Proposal passes Stage 5 PostGIS Deduplication, single-parent `CHECK` constraint audit (`= 1`), and human review gate sign-off (if required).
   - **Evidence Requirement:** Complete evidence citation junction in `entity_evidence_citations`.
   - **Database State:** Committed to PostgreSQL tier tables (`spaces`, `elements`, `relationships`) with `lifecycle_state = 'VALIDATED'`.

4. **`DEPRECATED`:**  
   - **Trigger:** Entity is superseded by a later authoritative historical drawing revision (e.g. 1973 Rev 4 supersedes 1968 Rev 1).
   - **Evidence Requirement:** Historical revision delta citation.
   - **Database State:** Updated in `entities` with `lifecycle_state = 'DEPRECATED'` (retained for auditable historical lineage).

5. **`ARCHIVED`:**  
   - **Trigger:** Entity or relationship is explicitly retracted due to proven architectural drafting error.
   - **Evidence Requirement:** Formal retraction log specifying cause of error.
   - **Database State:** Updated in `entities` with `lifecycle_state = 'ARCHIVED'` (never physically deleted; preserved for Principle 6 auditability).

---

## 3. Decision Point Specifications (12 Workflows)

### 3.1 Workflow 1: Proposal Creation
- **Purpose:** Transform Gemini multi-modal analysis into structured JSON proposal payloads.
- **Inputs:** 300 DPI drawing image + Stage 1/2 contracts.
- **Reviewer:** Gemini Reconstruction Engine (Stage 3).
- **Required Evidence:** Sheet code (`A-A-18`), drawing region bounding box, visual observation.
- **Confidence Requirements:** ADR-006A composite score $\ge 80$.
- **Approval Conditions:** Schema compliant, non-empty evidence citations.
- **Rejection Conditions:** Missing sheet code or composite score $< 80$.
- **Escalation Conditions:** Composite score in $[70, 79]$.

### 3.2 Workflow 2: Proposal Review
- **Purpose:** Evaluate proposal payload against governing principles and PostGIS topology.
- **Inputs:** Gemini Reconstruction Session Payload.
- **Reviewer:** Stage 5 Deduplication Engine & Pipeline Automated Auditor.
- **Required Evidence:** PostGIS polygon WKT string in `EPSG:2263`.
- **Confidence Requirements:** `min_confidence >= 80`.
- **Approval Conditions:** PostGIS `ST_IsValid = true`, `ST_Area > 0`.
- **Rejection Conditions:** Invalid geometry or missing primary key ID.
- **Escalation Conditions:** Boundary overlap $\text{IoU} \in [0.50, 0.89]$.

### 3.3 Workflow 3: Evidence Verification
- **Purpose:** Verify that 100% of proposed entities and relationships reference primary source drawing evidence (Principle 2).
- **Inputs:** `evidence_citations` array.
- **Reviewer:** Governance Automated Validator.
- **Required Evidence:** Sheet code matching regex `^[A-Z]{1,2}-[A-Z0-9]{1,4}-[0-9]{1,4}$`.
- **Confidence Requirements:** Citation quality score $\ge 80$.
- **Approval Conditions:** Valid sheet code and non-null observation text.
- **Rejection Conditions:** Uncited proposal ("ghost entity").
- **Escalation Conditions:** Ambiguous drawing callout reference.

### 3.4 Workflow 4: Confidence Verification
- **Purpose:** Validate ADR-006A Option B composite confidence score calculation.
- **Inputs:** `confidence_summary` object.
- **Reviewer:** Automated Confidence Auditor.
- **Required Evidence:** Breakdown of reasoning, evidence, corroboration, and geometry scores.
- **Confidence Requirements:** Composite score $\ge 80$.
- **Approval Conditions:** Score calculation matches ADR-006A formula.
- **Rejection Conditions:** Composite score $< 70$.
- **Escalation Conditions:** Composite score in $[70, 79]$.

### 3.5 Workflow 5: Cross-Sheet Corroboration
- **Purpose:** Match candidate entities across multiple independent drawing sheets.
- **Inputs:** Multi-sheet drawing sets (`A-A-18` + `A-A-121`).
- **Reviewer:** Stage 5 PostGIS Deduplication Engine.
- **Required Evidence:** Spatial IoU match $\text{IoU} \ge 0.90$.
- **Confidence Requirements:** Reconciled score $\max(S_1, S_2) + 2 \le 100$.
- **Approval Conditions:** Match confirmed across $\ge 2$ distinct sheet codes.
- **Rejection Conditions:** Spatial coordinates conflict ($< 0.50$).
- **Escalation Conditions:** Conflicting sheet notes across revisions.

### 3.6 Workflow 6: Human Review Gate
- **Purpose:** Gate ambiguous or lower-confidence proposals requiring manual human sign-off.
- **Inputs:** Flagged proposal payload (`requires_human_review = true`).
- **Reviewer:** Human Architectural Reviewer.
- **Required Evidence:** Visual drawing crop + human review comments.
- **Confidence Requirements:** Score in $[70, 79]$ elevated to $\ge 80$ post sign-off.
- **Approval Conditions:** Non-null `review_signoff_timestamp` and valid `reviewer_id`.
- **Rejection Conditions:** Human reviewer rejects proposal.
- **Escalation Conditions:** Structural core contradiction requiring Senior Lead review.

### 3.7 Workflow 7: Entity Approval
- **Purpose:** Authorize entity insertion into Master Entity Registry `entities` (ADR-005).
- **Inputs:** Approved entity proposal payload.
- **Reviewer:** Stage 6 Database Ingestion Engine.
- **Required Evidence:** Valid category ENUM string and building association.
- **Confidence Requirements:** Score $\ge 80$.
- **Approval Conditions:** Primary key registered in `entities`.
- **Rejection Conditions:** Duplicate primary key collision with mismatched category.
- **Escalation Conditions:** Missing building parent ID.

### 3.8 Workflow 8: Relationship Approval
- **Purpose:** Authorize property graph edge insertion into `relationships`.
- **Inputs:** Approved relationship proposal payload.
- **Reviewer:** Stage 6 Database Ingestion Engine.
- **Required Evidence:** Foreign key endpoints exist in `entities`.
- **Confidence Requirements:** Score $\ge 80$.
- **Approval Conditions:** Non-reflexivity `subject_entity_id != object_entity_id`.
- **Rejection Conditions:** Self-loop relationship edge or missing endpoint.
- **Escalation Conditions:** Conflicting relationship edge type.

### 3.9 Workflow 9: Rejection Workflow
- **Purpose:** Safely reject unvalidated or invalid proposals to `data/failed_pdfs/`.
- **Inputs:** Exception signal or validation failure.
- **Reviewer:** Automated Error Handler.
- **Required Evidence:** Structured error object (`error_code`, `error_message`, `timestamp`).
- **Confidence Requirements:** Score $< 70$ or invalid geometry.
- **Approval Conditions:** Payload written to `data/failed_pdfs/[HASH]_quarantine.json`.
- **Rejection Conditions:** None (rejection is terminal for candidate).
- **Escalation Conditions:** High-frequency error code pattern.

### 3.10 Workflow 10: Escalation Workflow
- **Purpose:** Escalate complex architectural conflicts to the Research Lead.
- **Inputs:** Escalation ticket payload.
- **Reviewer:** Research Lead / Principal Architect.
- **Required Evidence:** Conflict summary log & drawing sheet crops.
- **Confidence Requirements:** N/A.
- **Approval Conditions:** Principal Architect sign-off recorded.
- **Rejection Conditions:** Unresolved architectural conflict.
- **Escalation Conditions:** Tower A vs Tower B cross-tower baseline conflict.

### 3.11 Workflow 11: Database Authorization
- **Purpose:** Grant formal permission for Stage 6 to execute atomic transaction (`BEGIN; ... COMMIT;`).
- **Inputs:** Validated Stage 5 contract (`Stage5DeduplicationContract` v1.0.0).
- **Reviewer:** Pipeline Controller.
- **Required Evidence:** `validation_status = "VALIDATED"` and `quarantine_status = false`.
- **Confidence Requirements:** All entities score $\ge 80$.
- **Approval Conditions:** 100% pre-ingestion checks passed.
- **Rejection Conditions:** Missing human review sign-off timestamp.
- **Escalation Conditions:** Database lock contention or transaction timeout.

### 3.12 Workflow 12: Lifecycle Promotion
- **Purpose:** Promote entity lifecycle state in `entities` table.
- **Inputs:** Ingestion commit success signal.
- **Reviewer:** Database Lifecycle Controller.
- **Required Evidence:** 2nd independent sheet citation committed.
- **Confidence Requirements:** Score $\ge 80$.
- **Approval Conditions:** SQL `UPDATE entities SET lifecycle_state = 'CORROBORATED'` executed.
- **Rejection Conditions:** Database commit failed.
- **Escalation Conditions:** State transition exception.

---

## 4. Governance Thresholds & Authorization Rules

```text
MANDATORY AUTHORIZATION RULES:
1. WHAT EVIDENCE IS SUFFICIENT? 
   └─ Single sheet citation sufficient for DRAFT_SEED; >= 2 independent sheet citations required for CORROBORATED / VALIDATED.
2. WHAT CONFIDENCE IS SUFFICIENT? 
   └─ ADR-006A composite score >= 80 required for database ingestion.
3. WHEN IS HUMAN REVIEW MANDATORY? 
   └─ Mandatory when score in [70, 79] or spatial boundary overlap IoU in [0.50, 0.89].
4. WHEN IS STAGE 5 DEDUPLICATION AUTHORIZED? 
   └─ Authorized when Stage 3 contract validation_status = "VALIDATED" and quarantine_status = false.
5. WHEN IS STAGE 6 DATABASE INGESTION AUTHORIZED? 
   └─ Authorized when Stage 5 contract validation_status = "VALIDATED" and all human review sign-offs are non-null.
```

---

## 5. Final Recommendation

```text
FINAL WORKFLOW SELECTION:
[ ] Workflow Incomplete
[ ] Workflow Requires Revision
[X] Workflow Approved ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Workflow Approved`:
The Phase 5 Reconstruction Proposal Validation Workflow defines 100% of the 12 decision workflows, 5 canonical lifecycle states (**DRAFT_SEED**..**ARCHIVED**), ADR-006A confidence gates, human review controls, and database ingestion authorization rules. The workflow is **FORMALLY APPROVED**.
