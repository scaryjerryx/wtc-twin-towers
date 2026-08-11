# Governance Execution Priority & Analysis

**Document Status:** ✅ APPROVED EXECUTION PRIORITIZATION  
**Date:** August 11, 2026  
**Author:** Research Lead  
**Governing Charter:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md)  
**Basis Document:** [`docs/GOVERNANCE_REMEDIATION_PLAN_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/GOVERNANCE_REMEDIATION_PLAN_2026.md)  

---

## Executive Overview

This document establishes the detailed evaluation, impact analysis, effort estimation, and strict ranking for all 13 governance remediation items identified in [`docs/GOVERNANCE_REMEDIATION_PLAN_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/GOVERNANCE_REMEDIATION_PLAN_2026.md).

Each item is evaluated across 5 core dimensions:
1. **Supporting Evidence** (citations to codebase, evidence logs, and principles)
2. **Affected Documentation** (files requiring modification)
3. **Estimated Effort** (time and complexity to resolve)
4. **Expected Readiness Impact** (effect on project readiness metrics)
5. **Expected World Model Impact** (effect on PostgreSQL database schema, data integrity, and API payloads)

---

## Detailed Item Evaluation & Ranking

### 1. Tower B Readiness Recalculation & Symmetry Disclaimer
- **Severity Rank:** **CRITICAL** (Rank 1)
- **Supporting Evidence:**
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md#L48): Rates Tower B at 65% readiness based on "applicable Tower A floor plans".
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md#L25-L46): Lists Tower B structural (CG-1) and architectural (CG-2) as "Not in corpus".
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 7): *"Tower B must not be assumed to match Tower A unless supported by evidence."*
- **Affected Documentation:** [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md), [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md)
- **Estimated Effort:** Low (30 minutes)
- **Expected Readiness Impact:** Recalculates Tower B readiness from 65% down to **25%** (direct evidence only: exterior wall schedules and site position). Recalculates overall complex readiness from ~65–70% down to **~60–62%**, establishing an honest, evidence-backed baseline.
- **Expected World Model Impact:** Mandates that all Tower B spatial entities in PostgreSQL derived from Tower A patterns carry a confidence cap of *50% Provisional* or *25% Speculative* in `confidence_scores`.

---

### 2. CG-2 Scope Splitting (CG-2A vs CG-2B)
- **Severity Rank:** **HIGH** (Rank 2)
- **Supporting Evidence:**
  - [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md#L271): CG-2 declared "substantially closed for Tower A" (211 blueprints acquired).
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md#L37): CG-2 listed as "Not in corpus" across the entire complex.
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 3): *"Separate Evidence From Inference"*.
- **Affected Documentation:** [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md)
- **Estimated Effort:** Low (20 minutes)
- **Expected Readiness Impact:** Eliminates tracking ambiguity by establishing **CG-2A (Tower A Architectural Plans — CLOSED / 85% ready)** and **CG-2B (Tower B & Buildings 3–6 Architectural Plans — OPEN / 0–25% ready)**.
- **Expected World Model Impact:** Configures automated acquisition discovery (`search_candidates`) to target CG-2B specifically without generating redundant queries for Tower A drawings.

---

### 3. Confidence Level Scale & Taxonomy Standardization
- **Severity Rank:** **HIGH** (Rank 3)
- **Supporting Evidence:**
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 6): Establishes 5-tier scale (95% Verified, 85% Well Supported, 70% Supported, 50% Provisional, 25% Speculative).
  - [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md#L78): Lists unquantified qualitative tags (*Inferred*, *Unknown*).
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md#L587): Implements 4 rules in `fact_verifier.py` (50, 70, 85, 95).
- **Affected Documentation:** [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md), `agents/verification/fact_verifier.py`
- **Estimated Effort:** Low–Medium (45 minutes)
- **Expected Readiness Impact:** Indirect positive impact by standardizing readiness audit calculations across all 9 complex areas.
- **Expected World Model Impact:** Standardizes PostgreSQL `confidence_scores` table schema and API payloads to return unified integer confidence scores (95, 85, 70, 50, 25) with matching level strings.

---

### 4. Unverified Tower B Symmetry Disclaimers in Spatial Hierarchy
- **Severity Rank:** **HIGH** (Rank 4)
- **Supporting Evidence:**
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md#L57-L97): Defines tower spatial hierarchy without explicit disclaimers regarding Tower B structural/interior differences (outdoor deck, mechanical heights).
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 7): *"No Symmetry Assumptions"*.
- **Affected Documentation:** [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)
- **Estimated Effort:** Low (30 minutes)
- **Expected Readiness Impact:** Clarifies that Tower B spatial hierarchy features derived from Tower A carry a max confidence cap of 50%.
- **Expected World Model Impact:** Prevents procedural geometry generators or API endpoints (`/api/world/towers/2`) from serving Tower A geometry as verified Tower B data.

---

### 5. Runtime AI Independence Boundary Specification
- **Severity Rank:** **HIGH** (Rank 5)
- **Supporting Evidence:**
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md#L500-L514): Describes OpenRouter API integration in metadata extraction.
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 10): *"AI Is A Development Tool... AI is not a runtime dependency."*
- **Affected Documentation:** [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md), [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md)
- **Estimated Effort:** Medium (45 minutes)
- **Expected Readiness Impact:** Ensures high architectural readiness for Platform deployment by guaranteeing zero external LLM latency or API dependency for end users.
- **Expected World Model Impact:** Guarantees PostgreSQL database serves as the sole standalone provider for REST/GraphQL API responses (`/api/world/*`), keeping OpenRouter/LLM operations confined to offline ingestion tools (`agents/metadata/`).

---

### 6. Promote Blueprint Processor to Active Phase 3 Execution
- **Severity Rank:** **HIGH** (Rank 6)
- **Supporting Evidence:**
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md#L201): Lists Blueprint processing as a "Phase 3 consideration".
  - [`docs/TOWER_A_ARCHITECTURAL_CORPUS_ASSESSMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/TOWER_A_ARCHITECTURAL_CORPUS_ASSESSMENT.md#L7-L10): 211 blueprint PNGs (119MB) sitting unparsed in `WTC_CORPUS/floor-plans/911research-blueprints/`.
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 14): *"Preserve Buildability... Research work should maximize reconstruction readiness."*
- **Affected Documentation:** [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)
- **Estimated Effort:** Low documentation update (15 mins); Medium implementation effort (2 hours)
- **Expected Readiness Impact:** Unlocks Tower A spatial population, moving Tower A floor readiness from blueprint availability (85%) to database population (95%+).
- **Expected World Model Impact:** Converts 211 blueprint image files into thousands of structured `floors`, `zones`, `spaces`, and `elements` rows in PostgreSQL.

---

### 7. Spatial Hierarchy Database Schema Alignment
- **Severity Rank:** **HIGH** (Rank 7)
- **Supporting Evidence:**
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md#L660-L678): Database focus centered on harvest tables (`metadata_queue`, `search_candidates`).
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md#L181-L270): Defines PostGIS spatial tables (`sites`, `buildings`, `floors`, `spaces`, `elements`).
- **Affected Documentation:** [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)
- **Estimated Effort:** Medium (1 hour documentation alignment)
- **Expected Readiness Impact:** Bridges the gap between Evidence Engine harvest data and 3D Reconstruction Platform rendering.
- **Expected World Model Impact:** Instantiates spatial hierarchy tables as primary schema entities with direct `evidence_references` foreign key linkages.

---

### 8. 35-Day Timeline Release Schedule Synchronization
- **Severity Rank:** **MEDIUM** (Rank 8)
- **Supporting Evidence:**
  - [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md#L195-L202): 1 day = 1 year mapping (35 days).
  - [`docs/HISTORICAL_TIMELINE_EXPERIENCE.md`](file:///opt/wtc/wtc-twin-towers/docs/HISTORICAL_TIMELINE_EXPERIENCE.md#L25-L52): Phase-based schedule (Days 1–8 Construction, Days 9–29 Operational, Days 30–35 Final).
- **Affected Documentation:** [`docs/PROJECT_VISION_2026.md`](file:///opt/wtc/wtc-twin-towers/docs/PROJECT_VISION_2026.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)
- **Estimated Effort:** Low (20 minutes)
- **Expected Readiness Impact:** Unifies public product specifications for temporal state features.
- **Expected World Model Impact:** Aligns temporal state query parameters (`historical_states` table) with the 3-era public timeline release schedule.

---

### 9. WTC 3–6 Unknown Status Classification
- **Severity Rank:** **MEDIUM** (Rank 9)
- **Supporting Evidence:**
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md#L95-L105): WTC 3–6 documented as 0% readiness.
  - [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md#L42): WTC 3–6 listed in spatial hierarchy without status flags.
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 4): *"Preserve Uncertainty"*.
- **Affected Documentation:** [`docs/WORLD_MODEL_ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_ARCHITECTURE.md), [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md)
- **Estimated Effort:** Low (15 minutes)
- **Expected Readiness Impact:** Accurate reflection of 0% readiness for low-rise buildings.
- **Expected World Model Impact:** Marks `buildings` table records for WTC 3–6 with `status = 'unknown'` and `confidence_score = 0`.

---

### 10. Upper Floor Exterior Wall Panel Classification
- **Severity Rank:** **MEDIUM** (Rank 10)
- **Supporting Evidence:**
  - [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md#L58-L68): CG-4 notes exterior wall XLS covers only floors 1–9.
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principle 3): *"Separate Evidence From Inference"*.
- **Affected Documentation:** [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md)
- **Estimated Effort:** Low (15 minutes)
- **Expected Readiness Impact:** Prevents overstating tower envelope readiness.
- **Expected World Model Impact:** Tags upper floor exterior wall elements in PostgreSQL as *Supported Inference (70%)*.

---

### 11. Phase 1 & 2 Status Update to 100% Complete
- **Severity Rank:** **MEDIUM** (Rank 11)
- **Supporting Evidence:**
  - [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md#L98-L135): Phase 1 (M0–M15) and Phase 2 (M16–M23) fully complete.
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md): Detailed focus on active Phase 1/2 milestones.
- **Affected Documentation:** [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md), [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)
- **Estimated Effort:** Low (15 minutes)
- **Expected Readiness Impact:** Focuses development energy on active Phase 3 goals.
- **Expected World Model Impact:** None directly on DB schema; clarifies active operational state.

---

### 12. Principles 13 & 14 Enforcement Protocols
- **Severity Rank:** **MEDIUM** (Rank 12)
- **Supporting Evidence:**
  - [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 13 & 14): *"Reconstruction Before Enhancement"* and *"Preserve Buildability"*.
- **Affected Documentation:** [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)
- **Estimated Effort:** Low (20 minutes)
- **Expected Readiness Impact:** Maximizes reconstruction velocity by preventing premature work on decorative or audio features.
- **Expected World Model Impact:** Prioritizes spatial geometry parsing over enrichment metadata.

---

### 13. Legacy Database Table Cleanup (`discovered_urls`)
- **Severity Rank:** **LOW** (Rank 13)
- **Supporting Evidence:**
  - [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md#L255): `discovered_urls` and `search_history` declared legacy read-only tables.
- **Affected Documentation:** [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md)
- **Estimated Effort:** Low (10 minutes)
- **Expected Readiness Impact:** Minor code legibility improvement.
- **Expected World Model Impact:** Cleans up redundant table references in architecture documentation.

---

## Recommended First Three Execution Items

The following **exactly three items** must be executed first to achieve immediate governance compliance:

### Execution Item 1: Recalculate Tower B Readiness
- **Action:** Lower Tower B readiness in [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md) and [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) from **65%** to **25%**. Update overall complex readiness to **~60–62%**.
- **Rationale:** Resolves a **Critical** violation of Principle 7 (*No Symmetry Assumptions*).

### Execution Item 2: Split Gap CG-2 Scope
- **Action:** Split CG-2 into **CG-2A (Tower A Architectural Floor Plans — CLOSED / 85% ready)** and **CG-2B (Tower B & Buildings 3–6 Architectural Floor Plans — OPEN / 0–25% ready)** across [`docs/EVIDENCE_GAP_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/EVIDENCE_GAP_REPORT.md) and [`README.md`](file:///opt/wtc/wtc-twin-towers/README.md).
- **Rationale:** Resolves a **High** severity tracking contradiction between documents.

### Execution Item 3: Standardize Confidence Level Scale
- **Action:** Standardize confidence taxonomy across [`docs/RECONSTRUCTION_PLATFORM_VISION.md`](file:///opt/wtc/wtc-twin-towers/docs/RECONSTRUCTION_PLATFORM_VISION.md) and [`docs/ARCHITECTURE.md`](file:///opt/wtc/wtc-twin-towers/docs/ARCHITECTURE.md) to adopt the 5-tier percentage scale established in [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) Principle 6 (*95%, 85%, 70%, 50%, 25%*).
- **Rationale:** Resolves a **High** severity data integrity discrepancy.

---

**Document Prepared:** August 11, 2026  
**Status:** ✅ EXECUTION PRIORITIZATION COMPLETE — READY FOR REMEDIATION PHASE
