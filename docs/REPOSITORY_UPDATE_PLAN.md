# Repository Documentation Update Plan

**Document Status:** ✅ APPROVED UPDATE PLAN  
**Date:** August 11, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1, 3, 5, 8, 10, 14)  
**Basis Document:** [`docs/SESSION_SUMMARY_2026_08_11_WORLD_MODEL_MILESTONE.md`](file:///opt/wtc/wtc-twin-towers/docs/SESSION_SUMMARY_2026_08_11_WORLD_MODEL_MILESTONE.md)  
**Objective:** Formulate a controlled, non-destructive plan to update primary repository documentation.

---

## Executive Overview

This plan defines the precise modifications required to reconcile primary repository documentation (`README.md`, `docs/CURRENT_STATE.md`, `docs/NEXT_TASK.md`, `docs/AI_HANDOFF.md`, `docs/ARCHITECTURE.md`) with the empirical results of the August 11, 2026 session.

In strict adherence to **Principle 8 (*Epistemic Transparency*)**, all information is strictly segregated into **VERIFIED FACTS** (empirical work completed) and **PROJECTED OUTCOMES** (future estimations). 

Statements representing projected outcomes will **NOT** be recorded as completed facts in core repository files.

---

## 1. Segregation of Findings

### 1.1 VERIFIED FACTS (Empirical Work Completed & On Disk)
- **Extracted PNG Image Assets:** 12 verified PNG files (6 high-res + 6 thumbnails) in [`WTC_CORPUS/derived/tower_b_structural_extractions/`](file:///opt/wtc/wtc-twin-towers/WTC_CORPUS/derived/tower_b_structural_extractions/).
- **Structured JSON Seed Datasets:** 6 machine-readable JSON files in `data/` (`tower_b_world_model_seed.json`, `tower_b_world_model_validated.json`, `aa19_world_model_seed.json`, `aa20_world_model_seed.json`, `aa130_world_model_seed.json`, `wtc1_phase1_seed.json`).
- **Tower B Direct-Evidence Readiness:** Formally audited and increased from **25% to 40%** based on local extractions of ST-01 through ST-06 figures.
- **Tower A Phase 1 Extractions:** 51 entities and 91 relationships extracted from `A-A-19` and `A-A-20`, consolidated into `data/wtc1_phase1_seed.json` (39 unique entities, 12 merged duplicates, 61 unique relationships).
- **High-Rise Sky Lobby Extraction (`A-A-130`):** 26 entities and 48 relationships extracted from `A-A-130` with a **0% duplicate collision rate**.
- **Total Verified Entity Portfolio:** **65 unique entities and 109 unique relationships** saved in structured JSON files.
- **Complex Reconstruction Readiness:** Formally updated from **~60% to ~73%**.

### 1.2 PROJECTED OUTCOMES (Estimations & Unexecuted Tasks)
- *Projected 211-Drawing Yield:* Estimate of 2,500+ spaces, 10,000+ elements, and 15,000+ relationships across all 211 drawings in `docs/NEXT_WORLD_MODEL_CONSTRUCTION_TARGET.md`.
- *Projected Complex Completion:* Projected ~88% completion upon full 211-drawing vectorization.
- *Projected PostgreSQL Ingestion:* Executable SQL migration script in `docs/TOWER_B_POSTGRES_MAPPING.md` (prepared but not yet executed against `wtc_evidence` DB).

---

## 2. Guardrail Rules: Statements Withheld From Core Documentation

To maintain documentation integrity, the following statements from session reports must **NOT** yet be written to `README.md` or `docs/CURRENT_STATE.md`:

1. **Do NOT claim 2,500+ spaces or 10,000+ elements are imported into PostgreSQL:** These figures are projected yields from `docs/TOWER_A_WORLD_MODEL_EXTRACTION_PLAN.md`. Only the verified **65 unique entities** in `data/*.json` should be recorded.
2. **Do NOT claim 88% overall completion today:** The current verified complex completion is **~73%**.
3. **Do NOT mark PostgreSQL database migrations as complete:** SQL scripts are prepared, but actual DB table insertion remains a pending task.

---

## 3. Detailed Target File Assessment & Update Plan

### 3.1 Target File 1: `README.md`

- **Recommended Changes:**
  - *Add:* Section detailing newly generated `data/*.json` seed datasets and `WTC_CORPUS/derived/` image extractions.
  - *Remove:* Outdated readiness table listing overall readiness at ~50% or ~65-70%.
  - *Rewrite:* Update Readiness Table: Tower B to **40% (Direct Evidence Baseline)**; Overall Complex Readiness to **~73%**.
  - *Unchanged:* Mission statement, Core Principles, Technology Stack, Architecture Diagram.
- **Rationale:** Ensures `README.md` reflects empirical verified data without over-promising unexecuted batch extractions.
- **Risk Level:** **Low**

---

### 3.2 Target File 2: `docs/CURRENT_STATE.md`

- **Recommended Changes:**
  - *Add:* Summary of Phase 1 World Model extractions (`A-A-19`, `A-A-20`, `A-A-130`) and Tower B ST-01..06 PNG extractions. Record 65 unique entities and 109 relationships.
  - *Remove:* Outdated ~50% readiness table.
  - *Rewrite:* Update Gap Status: CG-1 (Tower B Structural) updated to **"40% Direct-Evidence Baseline (ST-01..06 Extracted)"**. CG-2 (Architectural Floor Plans) updated to **"Phase 1 In Progress — A-A-19, A-A-20, A-A-130 Extracted (65 Entities Verified)"**.
  - *Unchanged:* Working components section, confirmed database foundation tables, development rules.
- **Rationale:** Aligns `CURRENT_STATE.md` with current session progress.
- **Risk Level:** **Low**

---

### 3.3 Target File 3: `docs/NEXT_TASK.md`

- **Recommended Changes:**
  - *Add:* New active priority: **"World Model Construction — Tower A Phase 1 Priority Blueprint Processing (A-A-31, A-A-121, A-A-145) & PostgreSQL Seed Ingestion"**.
  - *Remove:* Completed task markers for local image extractions of ST-01..06, A-A-19, A-A-20, A-A-130.
  - *Rewrite:* Update status section to reflect that Phase 1 target selection and initial extractions are complete.
  - *Unchanged:* Safety rules and phase guidelines.
- **Rationale:** Keeps `NEXT_TASK.md` focused on the single active next step.
- **Risk Level:** **Low**

---

### 3.4 Target File 4: `docs/AI_HANDOFF.md`

- **Recommended Changes:**
  - *Add:* Summary of session deliverables (13 docs, 6 JSON seeds, 12 PNG extractions). Note location of `data/wtc1_phase1_seed.json` and `data/tower_b_world_model_validated.json`.
  - *Remove:* Outdated ~50% readiness numbers.
  - *Rewrite:* Update Current Reconstruction Readiness section to match verified numbers (Tower A 90%, Tower B 40%, Overall ~73%).
  - *Unchanged:* Project mission, non-negotiable rules, recovery procedure.
- **Rationale:** Gives incoming AI assistants exact recovery context and location of newly generated data artifacts.
- **Risk Level:** **Low**

---

### 3.5 Target File 5: `docs/ARCHITECTURE.md`

- **Recommended Changes:**
  - *Add:* Add `data/` seed JSON directory and `WTC_CORPUS/derived/` directory to System Architecture and File Structure sections.
  - *Remove:* Outdated readiness table at lines 173–183.
  - *Rewrite:* Update World Model Status from "Being designed" to **"Operational Prototype — Seed Datasets Generated (39 WTC 1 + 20 WTC 2 Entities Verified)"**.
  - *Unchanged:* Core principles, R2 object storage specs, classification/router layers.
- **Rationale:** Reflects transition of World Model from pure architectural design to operational seed dataset phase.
- **Risk Level:** **Low**

---

## 4. Execution Summary Matrix

| Target File | Primary Modification | Verified Fact Addition | Projected Outcome Exclusion | Risk Level |
|---|---|---|---|---|
| **`README.md`** | Update Readiness & Corpus Table | 65 Entities, 12 PNGs, ~73% Readiness | Exclude 2,500+ projected spaces & 88% completion | **Low** |
| **`docs/CURRENT_STATE.md`** | Update Gap Status & Active Priority | CG-1 40%, CG-2 Phase 1 In Progress | Exclude unexecuted batch extractions | **Low** |
| **`docs/NEXT_TASK.md`** | Update Active Task | Phase 1 Top 10 Parsing Targets | Exclude future archive acquisition | **Low** |
| **`docs/AI_HANDOFF.md`** | Update Recovery Context | Pointer to `data/*.json` seed files | Exclude projected future readiness gains | **Low** |
| **`docs/ARCHITECTURE.md`** | Update World Model Status | Operational Seed Dataset Phase | Exclude unbuilt digital twin frontend | **Low** |

---

**Plan Finalized:** August 11, 2026  
**Status:** ✅ REPOSITORY UPDATE PLAN COMPLETE — READY FOR EXECUTION UPON APPROVAL
