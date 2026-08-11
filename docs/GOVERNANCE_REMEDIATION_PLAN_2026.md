# Governance Remediation Plan 2026

**Document Status:** ✅ APPROVED PLAN  
**Date:** August 11, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md)  
**Basis:** [`docs/PROJECT_GOVERNANCE_AUDIT_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_GOVERNANCE_AUDIT_2026.md)  

---

## Executive Overview

This document provides a comprehensive remediation plan addressing all 13 findings identified in the [`docs/PROJECT_GOVERNANCE_AUDIT_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_GOVERNANCE_AUDIT_2026.md). Each item details the underlying issue, associated project risk, recommended technical resolution, target documentation files, and severity rating.

A prioritized backlog and immediate execution recommendation are provided at the end of this document.

---

## Detailed Remediation Actions

### Finding 1: Tower B Readiness Overstatement & Symmetry Assumption
- **Issue:** `README.md` and `ARCHITECTURE.md` rate Tower B (WTC 2) readiness at 65% based on "applicable Tower A floor plans". However, `EVIDENCE_GAP_REPORT.md` lists Tower B structural (CG-1) and architectural (CG-2) plans as "Not in corpus".
- **Project Risk:** Violates **Principle 1 (*Evidence First*)** and **Principle 7 (*No Symmetry Assumptions*)**. Giving a false impression of Tower B readiness causes developers to construct unverified geometry based on Tower A drawings.
- **Recommended Resolution:** Recalculate Tower B readiness to reflect direct evidence only (~25–30% based on exterior wall schedules and site plans). Reclassify mirrored Tower A geometry as *Provisional (50%)* or *Hypothesis* in the World Model database and documentation.
- **Files to Update:**  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md)  
- **Severity:** **Critical**

---

### Finding 2: CG-2 Scope Ambiguity (Tower A Closed vs. Complex-wide Open)
- **Issue:** `PROJECT_VISION_2026.md` declares CG-2 (*Architectural Floor Plans*) as "substantially closed for Tower A" due to the acquisition of 211 blueprints. However, `EVIDENCE_GAP_REPORT.md` lists CG-2 as "Not in corpus" across the entire complex.
- **Project Risk:** Ambiguity in evidence tracking; developers may assume architectural floor plans are complete across all buildings when Tower B and WTC 3–6 have zero floor plans in the corpus.
- **Recommended Resolution:** Formally split CG-2 into two distinct sub-gaps: **CG-2A (Tower A Architectural Plans — CLOSED)** and **CG-2B (Tower B & Buildings 3–6 Architectural Plans — OPEN)**.
- **Files to Update:**  
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md)  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
  - [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md)  
- **Severity:** **High**

---

### Finding 3: Confidence Level Scale & Taxonomy Discrepancies
- **Issue:** `AI_WORKING_PRINCIPLES.md` (Principle 6) establishes a 5-tier percentage scale (95% Verified, 85% Well Supported, 70% Supported, 50% Provisional, 25% Speculative). `RECONSTRUCTION_PLATFORM_VISION.md` uses unquantified qualitative tags (*Inferred*, *Unknown*). `ARCHITECTURE.md` implements a 4-tier rule set in `fact_verifier.py`.
- **Project Risk:** Inconsistent confidence values across database queries, verification tools, API payloads, and frontend UI overlays. Violates **Principle 6 (*Confidence Scoring*)**.
- **Recommended Resolution:** Standardize all project documentation, API schemas, verification scripts (`agents/verification/fact_verifier.py`), and frontend spec overlays to the 5-tier scale defined in Principle 6 of `AI_WORKING_PRINCIPLES.md`.
- **Files to Update:**  
  - [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md)  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **High**

---

### Finding 4: Timeline Release Model Mapping Mismatch
- **Issue:** `PROJECT_VISION_2026.md` defines a 35-day release schedule mapping 1 day per year (Day 1 → 1966, Day 35 → 2001). `HISTORICAL_TIMELINE_EXPERIENCE.md` maps Days 1–8 → Construction Era (1966–1973), Days 9–29 → Operational Era (1973–1993), Days 30–35 → Final Era (1993–2001).
- **Project Risk:** Conflicting specifications for the public 35-day release experience, leading to mismatched user interface controls and temporal database query structures.
- **Recommended Resolution:** Standardize on the phase-based 35-day release model in `HISTORICAL_TIMELINE_EXPERIENCE.md`, which accurately allocates 8 days to the 1966–1973 construction era. Update `PROJECT_VISION_2026.md` table to match.
- **Files to Update:**  
  - [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md)  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
- **Severity:** **Medium**

---

### Finding 5: Unverified Tower B Internal Core & Elevator Symmetry
- **Issue:** Assumptions in codebase planning models that Tower B core elevator banks, stairwell layouts, and mechanical floors match Tower A identically.
- **Project Risk:** Reconstructing inaccurate Tower B spatial models, misrepresenting historical facts, violating **Principle 7 (*No Symmetry Assumptions*)** and **Principle 2 (*Never Invent Evidence*)**.
- **Recommended Resolution:** Explicitly document in `WORLD_MODEL_ARCHITECTURE.md` that all unverified Tower B spaces carry a confidence score of *50% Provisional* or *25% Speculative* until direct Tower B drawing evidence is acquired.
- **Files to Update:**  
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md)  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
- **Severity:** **High**

---

### Finding 6: Unmapped Placeholders for Buildings 3–6
- **Issue:** Buildings 3 (Marriott Hotel), 4, 5, and 6 have 0% evidence in the corpus, but top-level spatial hierarchy documentation references them without explicit *Unknown* status flags.
- **Project Risk:** Violates **Principle 3 (*Separate Evidence From Inference*)** and **Principle 4 (*Preserve Uncertainty*)**. Risk of developers attempting 3D modeling without supporting drawings.
- **Recommended Resolution:** Update `WORLD_MODEL_ARCHITECTURE.md` spatial entity tables to explicitly set WTC 3–6 building and space statuses to *Unknown (0% confidence)* until evidence is acquired.
- **Files to Update:**  
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md)  
- **Severity:** **Medium**

---

### Finding 7: Upper Floor Exterior Wall Panel Uniformity Assumptions
- **Issue:** Existing exterior wall schedules cover only floors 1–9. Modeling upper tower cladding based on floors 1–9 assumes constant spandrel thickness and column cover geometries up to floor 110.
- **Project Risk:** Violates **Principle 1 (*Evidence First*)**. Inaccurate facade geometry and spandrel transitions on mechanical and upper office floors.
- **Recommended Resolution:** Classify upper floor exterior wall panel elements (floors 10–110) as *Supported Inference (70%)* or *Provisional (50%)* in the database schema, and prioritize CG-4 acquisition.
- **Files to Update:**  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md)  
- **Severity:** **Medium**

---

### Finding 8: Outdated Focus on Ingestion Pipelines (Phase 1 & 2 Complete)
- **Issue:** `README.md` and `docs/ARCHITECTURE.md` describe Phase 1 (M0–M15) acquisition queues and Phase 2 (M16–M23) knowledge engines as active milestones, even though both are complete and the project focus has shifted to World Model population and Reconstruction Platform build.
- **Project Risk:** Developer confusion and stagnation; teams may focus on rebuilding acquisition scaffolding instead of populating spatial tables from the 211 acquired blueprints.
- **Recommended Resolution:** Update status sections in `README.md` and `docs/ARCHITECTURE.md` to highlight Phase 1 & 2 as 100% complete operational scaffolding, framing active Phase 3 around World Model Population and Reconstruction Platform 3D rendering.
- **Files to Update:**  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **Medium**

---

### Finding 9: Deferred Specialist Blueprint Processor
- **Issue:** `README.md` lists blueprint processing (drawing numbers, revision tracking) as a "Phase 3 consideration" backlog item.
- **Project Risk:** 211 blueprint PNGs sitting in `WTC_CORPUS/floor-plans/911research-blueprints/` remain unparsed, creating a bottleneck for World Model database population.
- **Recommended Resolution:** Promote the Blueprint Processor (`agents/processors/blueprint_processor.py`) from backlog to an active execution item in Phase 3.
- **Files to Update:**  
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **High**

---

### Finding 10: Legacy Database Table References
- **Issue:** Earlier docs reference `discovered_urls` and `search_history`, while `ARCHITECTURE.md` notes they are read-only legacy tables superseded by `search_candidates`.
- **Project Risk:** Confusion when reviewing database schemas or writing SQL queries.
- **Recommended Resolution:** Clean up legacy table references across documentation to clarify that `search_candidates` is the single active table.
- **Files to Update:**  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **Low**

---

### Finding 11: AI Ingestion Scaffolding vs. Runtime Platform Independence
- **Issue:** Ingestion scripts (`ai_analyze.py`, `photo_processor.py`) use OpenRouter API. Need to guarantee no AI dependencies bleed into runtime API (`/api/world/*`) or frontend rendering.
- **Project Risk:** Violates **Principle 10 (*AI Is A Development Tool*)**. Runtime performance bottlenecks, API cost overhead, and potential service outages if OpenRouter API is offline.
- **Recommended Resolution:** Formally document the strict runtime boundary in `docs/ARCHITECTURE.md` and `docs/WORLD_MODEL_ARCHITECTURE.md`: API Layer and Next.js frontend query pre-populated PostgreSQL tables directly with zero dynamic AI calls.
- **Files to Update:**  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md)  
  - [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md)  
- **Severity:** **High**

---

### Finding 12: Database Schema Alignment (Ingestion Queues vs. Spatial Hierarchy)
- **Issue:** `wtc_evidence` database schema in `ARCHITECTURE.md` emphasizes ingestion queues (`discovery_queue`, `metadata_queue`) and entity graphs, whereas `WORLD_MODEL_ARCHITECTURE.md` defines a spatial hierarchy (`complexes`, `sites`, `buildings`, `floors`, `spaces`, `elements`).
- **Project Risk:** Schema fragmentation where spatial geometry is stored separately from acquisition evidence.
- **Recommended Resolution:** Reconcile PostgreSQL migration documentation and scripts to instantiate spatial hierarchy tables as primary entities, with `evidence_references` foreign keys linking elements directly to assets.
- **Files to Update:**  
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md)  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **High**

---

### Finding 13: Governance Principle Enforcement Mechanisms (Principles 13 & 14)
- **Issue:** Missing explicit guidelines enforcing **Principle 13 (*Reconstruction Before Enhancement*)** and **Principle 14 (*Preserve Buildability*)**.
- **Project Risk:** Development time wasted on decorative assets, furnishings, or audio/storytelling layers before physical structural geometry is established.
- **Recommended Resolution:** Add a Governance Enforcement section in `docs/ARCHITECTURE.md` mandating physical geometry validation before enrichment features, and ranking discovery tasks by reconstruction impact.
- **Files to Update:**  
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)  
- **Severity:** **Medium**

---

## Prioritized Remediation Backlog

| Rank | Priority | Action Item | Target File(s) | Severity |
|---|---|---|---|---|
| **1** | **Immediate** | **Tower B Readiness Correction** | [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **Critical** |
| **2** | **Immediate** | **CG-2 Gap Scope Splitting** | [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md) | **High** |
| **3** | **Immediate** | **Confidence Level Standardization** | [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **High** |
| **4** | **High** | **Tower B Unverified Symmetry Disclaimers** | [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md) | **High** |
| **5** | **High** | **Runtime AI Independence Boundary Specs** | [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md), [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md) | **High** |
| **6** | **High** | **Promote Blueprint Processor to Active Phase 3** | [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **High** |
| **7** | **High** | **Spatial Hierarchy Database Schema Alignment** | [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **High** |
| **8** | **Medium** | **35-Day Timeline Release Schedule Synchronization** | [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md) | **Medium** |
| **9** | **Medium** | **WTC 3–6 Unknown Status Classification** | [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md) | **Medium** |
| **10** | **Medium** | **Upper Floor Exterior Wall Schedule Classification** | [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md) | **Medium** |
| **11** | **Medium** | **Phase 1 & 2 Status Update to 100% Complete** | [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **Medium** |
| **12** | **Medium** | **Principles 13 & 14 Enforcement Protocol Integration**| [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **Medium** |
| **13** | **Low** | **Legacy Table Cleanup (`discovered_urls`)** | [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) | **Low** |

---

## Recommended Immediate Action Items

The following top 3 items should be executed immediately to resolve critical governance compliance risks:

1. **Recalculate Tower B Readiness in [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md) & [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md):**  
   - Lower Tower B readiness score from **65%** to **25%** (reflecting actual direct evidence: exterior wall schedules and site location only).
   - Add explicit note enforcing **Principle 7 (*No Symmetry Assumptions*)**: Tower A floor plans may not be used as verified Tower B geometry.
2. **Reconcile Gap CG-2 in [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md) & [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md):**  
   - Split CG-2 into **CG-2A (Tower A Architectural Floor Plans — CLOSED)** and **CG-2B (Tower B & Buildings 3–6 Architectural Floor Plans — OPEN)**.
3. **Standardize Confidence Scale in [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md) & [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md):**  
   - Replace qualitative confidence descriptions with the 5-tier percentage scale established in [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) Principle 6 (*95% Verified, 85% Well Supported, 70% Supported, 50% Provisional, 25% Speculative*).

---

**Plan Prepared:** August 11, 2026  
**Status:** ✅ REMEDIATION PLAN READY FOR EXECUTION
