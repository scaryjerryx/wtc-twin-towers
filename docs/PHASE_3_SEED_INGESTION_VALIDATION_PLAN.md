# Phase 3 Seed Ingestion Validation Plan

**Document Status:** ✅ AUTHORITATIVE SEED INGESTION VALIDATION PLAN  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Audited Parent Specifications:**  
1. [`docs/PHASE_3_EXECUTION_EVIDENCE_REPORT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_EXECUTION_EVIDENCE_REPORT.md)  
2. [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md)  
3. [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md)  
4. [`database/migrations/V1_1__create_world_model_schema_revised.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_1__create_world_model_schema_revised.sql)  

**TARGET DATA BASELINE:** **164 Verified Unique Entities & 82 Master Relationships across 11 Seed Datasets**  

---

## Executive Summary

This document establishes the **authoritative Seed Ingestion Validation Plan** governing the ingestion and database-level validation of all approved seed datasets (`data/*.json`) into the live PostgreSQL PostGIS schema (`wtc_evidence`).

Zero schema modifications, zero DDL changes, zero architecture revisions, and zero web searches were introduced in this validation plan.

This plan details the 10 required validation procedures, entity ingestion ordering, relationship ingestion pipeline, epistemic citation linking, confidence score bounds, lifecycle state rules, multi-floor penetration checks, PostGIS spatial footprint checks, and acceptance criteria required to complete Phase 3 database population.

---

## 1. Evidentiary & Data Inventory Overview

```text
SEED DATASET INVENTORY (11 Files in data/*.json):
┌──────────────────────────────────────┬─────────────────────────┬──────────────────────────────────┐
│ Seed Dataset File Name               │ Primary System Domain   │ Target Entity Tier Range         │
├──────────────────────────────────────┼─────────────────────────┼──────────────────────────────────┤
│ 1. wtc1_world_model_v1.json          │ WTC 1 North Tower       │ Site ──► Floor 107 Elements      │
│ 2. wtc1_phase1_seed.json             │ Core Infrastructure     │ Subgrade ──► Mechanical Plants   │
│ 3. tower_b_world_model_validated.json│ WTC 2 South Tower       │ Building ──► Observation Deck    │
│ 4. tower_b_world_model_seed.json     │ WTC 2 Foundation        │ Sub-grade B6 ──► Plaza Level     │
│ 5. aa18_world_model_seed.json        │ Drawing A-A-18          │ Sub-grade B1 ──► B6 Concourse    │
│ 6. aa19_world_model_seed.json        │ Drawing A-A-19          │ Concourse Pedestrian Network     │
│ 7. aa20_world_model_seed.json        │ Drawing A-A-20          │ Main Lobby ──► Express Elevator  │
│ 8. aa31_world_model_seed.json        │ Drawing A-A-31          │ Floor 7 Mechanical Room (MER)    │
│ 9. aa121_world_model_seed.json       │ Drawing A-A-121         │ Floor 107 Windows on the World   │
│ 10. aa130_world_model_seed.json      │ Drawing A-A-130         │ Floor 107 Observation Deck       │
│ 11. aa145_world_model_seed.json      │ Drawing A-A-145         │ Core Columns 501–1008            │
└──────────────────────────────────────┴─────────────────────────┴──────────────────────────────────┘
```

---

## 2. Ingestion & Validation Plan Across 10 Required Areas

### 2.1 Seed File Inventory & Pipeline Setup
- **Purpose:** Verify presence, valid JSON syntax, and cryptographic integrity of all 11 seed JSON files.
- **Validation Method:** Execute Python pre-ingestion scanner (`python scripts/validate_seeds.py`).
- **Expected Result:** All 11 files present; 100% valid JSON syntax; 164 entities and 82 relationships parsed.
- **Failure Conditions:** Missing JSON file, syntax error, or unparseable payload.

### 2.2 Entity Ingestion Sequence
- **Purpose:** Respect foreign key dependencies by ingesting entities in strict top-down spatial containment hierarchy order.
- **Validation Method:** Ingest master entity records into `entities` first, followed sequentially by `sites` ──► `buildings` ──► `floors` ──► `zones` ──► `spaces` ──► `elements`.
- **Expected Result:** 164 primary entity records inserted into `entities` and physical tier tables with zero foreign key violations.
- **Failure Conditions:** `foreign_key_violation` during tier table insertion.

### 2.3 Relationship Ingestion Sequence
- **Purpose:** Ingest directed property graph edge links after all subject and object entity records are instantiated.
- **Validation Method:** Ingest 82 master relationship edge tuples into `relationships`.
- **Expected Result:** 82 directed edge records created with valid `subject_entity_id` and `object_entity_id` foreign keys.
- **Failure Conditions:** `foreign_key_violation`, self-loop `check_violation`, or unique edge duplicate.

### 2.4 Evidence Ingestion Sequence
- **Purpose:** Populate master evidence sources and epistemic citation links (Principle 2: *Cite Sources*).
- **Validation Method:** Populate `sources` table with Yamasaki/Emery Roth drawing titles, followed by `entity_evidence_citations` linking `entity_id` and `source_id`.
- **Expected Result:** All 164 entities linked to at least 1 valid source record with sheet code (`A-A-18`, `A-A-121`, etc.).
- **Failure Conditions:** Orphan citation or missing source reference.

### 2.5 Referential Integrity Validation
- **Purpose:** Confirm 100% declarative foreign key referential integrity across the populated database.
- **Validation Method:** Query database for orphan entity IDs, unlinked citations, or unanchored graph edges.
- **Expected Result:** Exactly 0 orphan records across all 11 database tables.
- **Failure Conditions:** Any orphan record detected in system catalog query.

### 2.6 Confidence Score Validation
- **Purpose:** Enforce Principle 5 (*Quantify Uncertainty*), verifying that all stored scores strictly conform to $[0, 100]$ bounds and exceed the production threshold ($\ge 80$).
- **Validation Method:** Query database for confidence scores outside range: `SELECT * FROM entities WHERE confidence_score < 80 OR confidence_score > 100;`.
- **Expected Result:** 0 records returned.
- **Failure Conditions:** Any entity or relationship record with `confidence_score < 80` or $> 100$.

### 2.7 Lifecycle State Validation
- **Purpose:** Ensure all ingested seed entities possess valid lifecycle state classifications (`DRAFT_SEED`, `CORROBORATED`, `VALIDATED`, `DEPRECATED`, `ARCHIVED`).
- **Validation Method:** Query `entities` for lifecycle state distribution: `SELECT lifecycle_state, count(*) FROM entities GROUP BY lifecycle_state;`.
- **Expected Result:** 100% of seed entities classified as `CORROBORATED` or `VALIDATED`.
- **Failure Conditions:** Null lifecycle state or invalid ENUM value.

### 2.8 Multi-Floor Entity Validation
- **Purpose:** Verify Approved Decision B.1 for multi-floor vertical elements (Stairs A/B/C, Freight Elevator 50, Core Box Columns).
- **Validation Method:** Query `elements WHERE is_multi_floor = true` and verify corresponding entries in `element_floor_junction` and `PASSES_THROUGH` relationship edges.
- **Expected Result:** Every multi-floor element has primary parent `building_id` and $\ge 2$ physical floor junction entries in `element_floor_junction`.
- **Failure Conditions:** Multi-floor element lacking floor junction records.

### 2.9 Spatial Validation
- **Purpose:** Verify PostGIS 2D polygon footprint validity and elevation Z-bounds ($z_{\text{min}} \le z_{\text{max}}$).
- **Validation Method:** Execute PostGIS geometry checks (`SELECT ST_IsValid(geometry_2d), ST_SRID(geometry_2d) FROM elements;`).
- **Expected Result:** 100% of 2D polygon geometries return `ST_IsValid = true` and `ST_SRID = 2263`. `z_min <= z_max` holds for all records.
- **Failure Conditions:** Invalid spatial polygon, wrong SRID, or $z_{\text{min}} > z_{\text{max}}$.

### 2.10 Ingestion Acceptance Criteria
- **Purpose:** Define non-negotiable quantitative metrics for Phase 3 ingestion completion.
- **Validation Method:** Run automated post-ingestion audit script (`scripts/audit_ingestion.py`).
- **Expected Result:**
  - Exactly **164 unique entities** present in `entities` and physical tier tables.
  - Exactly **82 master relationships** present in `relationships`.
  - 0 orphan citations, 0 orphan aliases, 0 invalid geometries.
- **Failure Conditions:** Entity count $< 164$ or relationship count $< 82$.

---

## 3. Post-Ingestion Validation Workflow

```text
POST-INGESTION VALIDATION PIPELINE:
┌────────────────────────────────────────────────────────────────────────┐
│ STEP 1: Execute Python Ingestion Script (`python scripts/ingest.py`)    │
├────────────────────────────────────────────────────────────────────────┤
│ STEP 2: Execute Catalog Count Audit (164 Entities, 82 Relationships)   │
├────────────────────────────────────────────────────────────────────────┤
│ STEP 3: Execute PostGIS Geometry Audit (ST_IsValid = true, SRID = 2263)│
├────────────────────────────────────────────────────────────────────────┤
│ STEP 4: Execute Referential Integrity Audit (0 Orphan Records)         │
├────────────────────────────────────────────────────────────────────────┤
│ STEP 5: Confirm Phase 3 Completion ──► AUTHORIZE PHASE 4 OPENING        │
└────────────────────────────────────────────────────────────────────────┘
```

---

**Plan Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 SEED INGESTION VALIDATION PLAN COMPLETE — READY FOR DATASET INGESTION EXECUTION
