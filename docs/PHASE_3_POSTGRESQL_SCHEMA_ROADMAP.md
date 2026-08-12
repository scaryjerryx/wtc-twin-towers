# Phase 3 PostgreSQL Schema Execution Roadmap

**Document Status:** ✅ AUTHORITATIVE PHASE 3 EXECUTION ROADMAP  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md), [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md), [`docs/PHASE_2_COMPLETION_AND_PHASE_3_AUTHORIZATION.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_COMPLETION_AND_PHASE_3_AUTHORIZATION.md)  
**Target Milestone:** Authoritative Implementation Roadmap Governing PostgreSQL PostGIS DDL Creation & Seed Data Ingestion  

---

## Executive Summary

This document establishes the **authoritative execution roadmap for Phase 3: Schema Design & PostgreSQL PostGIS DDL Execution**.

This document is strictly an implementation roadmap and DOES NOT contain physical SQL code or DDL scripts. Zero SQL scripts, zero `CREATE TABLE` DDL statements, zero database migrations, zero indexes, zero triggers, zero views, zero API contracts, zero frontend models, and zero web searches were created in this roadmap.

This roadmap defines the precise 6-task execution sequence, entity creation order, relationship creation order, evidence schema order, spatial PostGIS configuration, multi-floor junction order, constraint enforcement rules, validation strategies, migration strategies, and success criteria required to execute Phase 3 cleanly.

---

## 1. Evidentiary & Implementation Partitioning

```text
┌────────────────────────────────────────────────────────────────────────┐
│ VERIFIED FACTS (Physical Baseline Saved on Disk in data/*.json)        │
├────────────────────────────────────────────────────────────────────────┤
│ • Phase 2 Database Design Preparation OFFICIALLY CLOSED                │
│ • Phase 3 PostgreSQL Schema Design OFFICIALLY AUTHORIZED              │
│ • 164 Verified Unique Entities & 82 Master Relationships cataloged     │
│ • Approved 6-Tier Spatial Containment Hierarchy & 4 Critical Decisions │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION REQUIREMENTS (Non-Negotiable Phase 3 Tasks)              │
├────────────────────────────────────────────────────────────────────────┤
│ • Task 3.1: PostgreSQL PostGIS Extensions & ENUM Type Definitions     │
│ • Task 3.2: 6-Tier Spatial Tree Entity Table DDL Formulation           │
│ • Task 3.3: Epistemic Evidence & Multi-Floor Junction Table DDL        │
│ • Task 3.4: Directed Relational Graph Table DDL Formulation            │
│ • Task 3.5: Foreign Key Constraints & PostGIS GiST Index Tuning        │
│ • Task 3.6: Automated Python Pre-Ingestion Seed Validation Test Suite  │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ IMPLEMENTATION RISKS (Operational Controls & Pre-Ingestion Rules)      │
├────────────────────────────────────────────────────────────────────────┤
│ • Foreign key dependency ordering errors during table creation         │
│ • PostGIS 2D polygon footprint extrusion height bounds validation      │
│ • Element-floor junction association sync via pre-ingestion scripts    │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ FUTURE DDL TASKS (Upcoming Phase 3 Code Creation Pipeline)             │
├────────────────────────────────────────────────────────────────────────┤
│ • Idempotent SQL migration files under `database/migrations/`          │
│ • Python seed data loading and upsert execution (`scripts/ingest.py`)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Schema Design Execution Sequence

Phase 3 execution will proceed across 6 strictly ordered implementation tasks:

```text
TASK 3.1: Extensions & Base ENUMs (PostGIS, Structure Types, Category & Relationship ENUMs)
          │
          ▼
TASK 3.2: Core Spatial Containment Tree DDL (sites ──► buildings ──► floors ──► zones ──► spaces ──► elements)
          │
          ▼
TASK 3.3: Epistemic Evidence & Multi-Floor Junction DDL (sources, entity_evidence_citations, element_floor_junction)
          │
          ▼
TASK 3.4: Directed Relational Graph DDL (relationships table)
          │
          ▼
TASK 3.5: Foreign Key Constraints & PostGIS GiST Index Tuning (CHECK constraints & 2D spatial indices)
          │
          ▼
TASK 3.6: Automated Python Pre-Ingestion Seed Test Suite & Ingestion Execution (data/*.json ingestion)
```

---

## 3. Entity Schema Creation Order

To respect SQL foreign key dependencies, primary entity tables MUST be instantiated top-down following the approved 6-Tier Spatial Containment Hierarchy:

1. `sites` (Root entity table)
2. `buildings` (References `sites`)
3. `floors` (References `buildings`)
4. `zones` (References `floors` or `buildings`)
5. `spaces` (References `zones` or `floors`)
6. `elements` (References `spaces`, `zones`, `floors`, or `buildings`)

---

## 4. Relationship Schema Creation Order

The directed property graph table MUST be created after all primary entity tables are instantiated:

1. `relationships` table instantiated.
2. Foreign key references configured: `subject_entity_id REFERENCES entities`, `object_entity_id REFERENCES entities`.
3. Relationship type ENUM constraint applied (10 canonical ENUMs).

---

## 5. Evidence Schema Creation Order

Epistemic citation tables MUST be created in the following order:

1. `sources` master evidence table instantiated (storing drawing titles, authors, creation dates, archive repositories).
2. `entity_evidence_citations` junction table instantiated (referencing `entity_id` and `source_id`).
3. Evidence classification ENUM and confidence score range CHECK constraints applied.

---

## 6. Spatial Schema Creation Order

PostGIS spatial geometry integration MUST follow a 3-step configuration:

1. **Extension Initialization:** Enable PostGIS extension (`postgis`).
2. **Spatial Attribute Configuration:** Add 2D polygon footprint geometry columns (`EPSG:2263` State Plane Feet) and numeric `z_min` / `z_max` elevation columns (feet relative to +310.0 ft PA datum) to `spaces`, `zones`, and `elements` tables.
3. **Spatial Index Tuning:** Configure 2D GiST spatial bounding box indices (`USING GIST (geometry_2d)`).

---

## 7. Multi-Floor Schema Implementation Order

Multi-floor vertical element associations MUST be configured following the hybrid tree-junction architecture:

1. Instantiate `elements` table with primary building parent references (`building_id`).
2. Instantiate `element_floor_junction` physical association table (`element_id REFERENCES elements`, `floor_id REFERENCES floors`).
3. Add penetration attributes (`penetration_type_enum`, `has_landing`, `has_machine_room`).

---

## 8. Constraint Implementation Order

Database integrity constraints MUST be applied in two distinct stages:

### Stage 1: Inline Table Constraints
- `NOT NULL` constraints on canonical string primary keys, parent IDs, category ENUMs, and confidence scores.
- `CHECK` constraints on confidence scores: `CHECK (confidence_score BETWEEN 0 AND 100)`.

### Stage 2: Alter Table Referential Constraints
- Foreign key constraints with `ON DELETE RESTRICT` cascades to prevent accidental deletion of parent containers or evidence sources.

---

## 9. Ingestion Validation Strategy

Prior to executing SQL ingestion on production tables:

1. **Automated Python Seed Test Suite:** Build a Python validation script (`scripts/validate_seeds.py`) that parses all 164 verified entities across 7 seed JSON files (`data/*.json`).
2. **Validation Checklist:**
   - [X] Canonical ID formatting compliance.
   - [X] Parent entity existence in containment tree.
   - [X] ENUM validity against approved taxonomies.
   - [X] Elevation range validity ($z_{\text{min}} \le z_{\text{max}}$).
   - [X] Confidence score threshold ($\ge 80$).
   - [X] Non-null evidence citation presence.

---

## 10. Migration Strategy

1. **Idempotent SQL Scripts:** All DDL creation scripts MUST be written as version-controlled, idempotent migration files under `database/migrations/` (e.g. `V1.0__create_world_model_schema.sql`).
2. **Migration Runner:** Execute migrations via the existing repository database runner (`database/migrate.py`).
3. **Rollback Safety:** Include explicit transactional rollback blocks (`BEGIN; ... COMMIT;`).

---

## 11. Phase 3 Success Criteria

Phase 3 will be deemed **100% SUCCESSFUL** when:

1. All PostgreSQL PostGIS DDL tables, ENUM types, constraints, and indices execute with zero errors.
2. Automated Python pre-ingestion validation test suite passes 100% across all 164 seed entities in `data/*.json`.
3. All 164 verified unique entities and 82 master relationships are ingested cleanly into PostgreSQL `wtc_evidence`.
4. Zero orphan records or invalid spatial parent references exist in the database.
5. Spatial 2D PostGIS intersection queries and Z-range elevation queries return accurate results.

---

**Roadmap Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 IMPLEMENTATION ROADMAP FINALIZED — READY FOR TASK 3.1 DDL CREATION
