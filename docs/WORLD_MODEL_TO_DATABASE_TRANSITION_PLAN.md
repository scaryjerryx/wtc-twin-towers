# World Model to Database Transition Plan

**Document Status:** ✅ APPROVED TRANSITION PLAN  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1, 3, 5, 8, 10, 13, 14)  
**Basis Datasets:** [`data/wtc1_world_model_v1.json`](file:///opt/wtc/wtc-twin-towers/data/wtc1_world_model_v1.json), [`data/tower_b_world_model_validated.json`](file:///opt/wtc/wtc-twin-towers/data/tower_b_world_model_validated.json)  
**Target Milestone:** Transition from **World Model Construction Phase** to **Database Design Preparation Phase**.

---

## Executive Summary

This plan defines the exact criteria, remaining extraction sequence, and threshold metrics required to formally complete the **World Model Construction Phase** and initiate **Database Design Preparation**.

Zero SQL DDL scripts, zero database migrations, zero database schemas, and zero web searches were created in this document.

The project currently holds **134 verified unique entities** (114 WTC 1 + 20 WTC 2) across 5 vertical elevations. To establish the complete **Minimum Viable World Model (MVWM)** baseline, the project requires **one final blueprint extraction: Blueprint A-A-18 (Sub-Level 1 Concourse Master Plan)**. 

Extracting `A-A-18` will bring the total portfolio to **155+ verified entities**, closing the sub-grade retail and transit gap and triggering the formal stop criteria for pure extraction.

---

## 1. Remaining Highest-Value Extractions

### 1.1 Tower A (WTC 1) Priority Extractions
1. **`A-A-18` (Sub-Level 1 Concourse Master Plan & PATH Access) — `CRITICAL #1 TARGET`:**  
   - *Value:* Fills the sub-grade retail concourse, shopping mall, subway access, and PATH station entrance gap (+20–25 new spaces).  
   - *Location:* [`WTC_CORPUS/floor-plans/911research-blueprints/original/A-A-18_0.png`](file:///opt/wtc/wtc-twin-towers/original/A-A-18_0.png).
2. **`A-A-30` (Floor 6 Plaza Lobby Tree Transfer & Mezzanine Plan):**  
   - *Value:* Fills the plaza lobby mezzanine level and lower tree column transfer structural connections.
3. **`A-A-149` (Floor 108 Upper MER & Roof Hat Truss Plan):**  
   - *Value:* Captures the roof hat truss framing, elevator machine rooms, and mechanical cooling towers.

### 1.2 Tower B (WTC 2) Priority Extractions
1. **ST-01 through ST-06 Structural Extractions (`COMPLETED`):**  
   - 20 verified entities cataloged in `data/tower_b_world_model_validated.json` (Core box columns 501–1008, floor trusses C32/C36, lobby tree transfers, outrigger belt trusses, hat truss).
2. **NCSTAR 1-1 / 1-2 WTC 2 Sky Lobby & Observation Deck Figures:**  
   - *Value:* Secondary validation of WTC 2 78th Floor Sky Lobby and Outdoor Observation Deck Promenade.

---

## 2. Missing Entity & Relationship Categories

### 2.1 Missing Entity Categories
- **Sub-Grade Retail & Transit Spaces (`retail_space`, `transit_station`):** Shopping mall stores, PATH train platforms, subway turnstile concourses (resolved by parsing `A-A-18`).
- **Roof Antenna Structure Elements (`antenna_element`):** Television broadcast antenna mast structural framing on Floor 110/Roof (resolved by parsing `A-A-149`).

### 2.2 Missing Relationship Categories
- **Structural Load Path Links (`SUPPORTS`, `BEARS_ON`):** Explicit load transfer links connecting floor deck slabs to core box columns and perimeter spandrel girders.
- **Fluid & Airflow Piping/Duct Networks (`FLOWS_TO`, `CIRCULATES_WITH`):** Hydraulic fluid and airflow routing links connecting Floor 7 primary chillers to Floor 75 booster chillers.

---

## 3. Definition of Minimum Viable World Model (MVWM)

The **Minimum Viable World Model (MVWM)** represents the minimum data completeness required before database DDL design should begin:

```text
MINIMUM VIABLE WORLD MODEL (MVWM) BASELINE:
┌────────────────────────────────────────────────────────────────────────┐
│ • Total Verified Unique Entities : 150+ Entities (Currently 134)       │
│ • Total Master Relationships     : 75+ Relational Links (Currently 57) │
│ • Vertical Anchor Datums Covered : 6 Datums (Sub-Grade B1 to Floor 107)│
│ • Schema Category Stability      : 15 Canonical Entity Categories      │
│ • Epistemic Classification       : 100% Direct Blueprint Evidence     │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Phase Transition Criteria

```text
WORLD MODEL CONSTRUCTION               DATABASE DESIGN PREPARATION
(Blueprint Parsing Phase)               (PostGIS & DDL Design Phase)
┌────────────────────────┐              ┌────────────────────────┐
│ Current State: 134 Ent │ ───────────► │ Target Baseline: 155   │
│ Target: +21 Ent (A-A-18)│   TRIGGER    │ Verified Entities      │
└────────────────────────┘  STOP CRITERIA└────────────────────────┘
```

### 4.1 Stop Criteria for Extraction Phase
The extraction-only phase will stop when:
1. Blueprint `A-A-18` (Sub-Level 1 Concourse Plan) extraction is complete.
2. Master dataset `wtc1_world_model_v2.json` is generated containing **135+ unique WTC 1 entities**.
3. Combined portfolio across WTC 1 and WTC 2 reaches **155+ verified entities** (135 WTC 1 + 20 WTC 2).
4. All 6 vertical key anchor elevations (Sub-grade B1, Floor 1, Floor 7, Floor 75, Floor 78, Floor 107) are represented with **0% duplicate collision rates**.

### 4.2 Start Criteria for Database Design Preparation Phase
The Database Design Preparation phase will start immediately upon meeting the stop criteria, authorizing engineers to:
1. Formulate PostgreSQL PostGIS table DDL structures (`complexes`, `sites`, `buildings`, `towers`, `floors`, `zones`, `spaces`, `elements`, `evidence_references`, `confidence_scores`).
2. Define custom PostgreSQL enum types for `entity_type`, `evidence_classification`, and `relationship_type`.
3. Build automated Python test suites to validate `wtc1_world_model_v2.json` loading into local PostgreSQL database `wtc_evidence`.

---

## 5. Recommended Execution Sequence

```text
STEP 1: Parse Blueprint A-A-18 (Sub-Level 1 Concourse Plan)
        └─► Generate data/aa18_world_model_seed.json (+20-25 Entities)

STEP 2: Consolidate Master Seed Dataset wtc1_world_model_v2.json
        └─► Reaches 135+ WTC 1 Entities (155+ Combined Complex Entities)

STEP 3: Trigger Stop Criteria for Pure Extraction Phase
        └─► Transition project mode to PREPARE FOR DATABASE DESIGN

STEP 4: Initiate Database Design Preparation
        └─► PostGIS spatial schema DDL, Enum types, and DB ingestion pipeline
```

---

**Plan Completed:** August 12, 2026  
**Status:** ✅ WORLD MODEL TO DATABASE TRANSITION PLAN APPROVED — READY FOR A-A-18 EXTRACTION
