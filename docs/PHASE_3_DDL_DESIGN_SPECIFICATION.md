# Phase 3 DDL Design Specification v1.0

**Document Status:** ✅ AUTHORITATIVE DDL DESIGN SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md), [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md), [`docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md), [`docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md), [`docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md)  
**Target Milestone:** Authoritative DDL Blueprint Governing Future Executable SQL Migration File Authoring  

---

## Executive Summary

This document establishes the **authoritative DDL Design Specification v1.0** for the World Trade Center Reconstruction Project.

This document is strictly a DDL design blueprint and DOES NOT contain executable SQL code. Zero SQL migration files, zero `CREATE TABLE` DDL statements, zero `ALTER TABLE` statements, zero executable scripts, zero triggers, zero stored procedures, and zero web searches were created in this specification.

This DDL Design Specification translates all approved logical schemas and physical specifications into exact, non-negotiable DDL design requirements, object inventories, ENUM taxonomies, table structures, key strategies, constraint enforcement rules, spatial indexing rules, multi-floor association rules, and migration ordering requirements that **future migration authors MUST follow when writing executable SQL files**.

---

## 1. Database Object Inventory

### Purpose
Defines the complete inventory of physical database objects required to implement the World Model in PostgreSQL.

### Rationale
Provides an exhaustive blueprint of extensions, schemas, ENUM types, tables, constraints, and indices required before executable migration authoring begins.

### Constraints
- No database object outside this approved inventory may be instantiated without prior architectural approval.

### Dependency on Approved Specifications
Extends Section 1 (*Entity Storage Architecture*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 164 verified unique entities and 82 master relationships cataloged on disk in data/*.json.
• DDL DESIGN REQUIREMENTS: 1 Extension (postgis), 6 ENUM types, 11 primary tables, 15 foreign key constraints, 8 spatial/composite indices.
• IMPLEMENTATION RISKS: Object creation dependency errors if table DDL is executed out of sequence.
• FUTURE MIGRATION CONSIDERATIONS: Idempotent migration authoring under `database/migrations/V1.0__create_world_model_schema.sql`.
```

---

## 2. ENUM Inventory

### Purpose
Defines the required PostgreSQL ENUM types representing approved canonical taxonomies.

### Rationale
Enforces database-level type safety for building structure types, entity categories, relationship categories, evidence classifications, lifecycle states, and historical eras.

### Constraints
- ENUM values MUST strictly match approved canonical taxonomies in [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md).

### Dependency on Approved Specifications
Extends Section 1 (*Core Entity Families*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 15 entity category ENUMs, 10 relationship ENUMs, and 5 building structure type ENUMs approved.
• DDL DESIGN REQUIREMENTS: 6 ENUM types (structure_type_enum, entity_category_enum, relationship_type_enum, evidence_classification_enum, lifecycle_state_enum, temporal_era_enum).
• IMPLEMENTATION RISKS: Adding unapproved ENUM values breaks seed dataset validation scripts.
• FUTURE MIGRATION CONSIDERATIONS: SQL `CREATE TYPE` DDL execution prior to table creation.
```

#### Approved ENUM Value Taxonomies:
1. **`structure_type_enum`:** `high_rise_tower`, `podium_building`, `hotel_slab`, `substation_base`, `transit_terminal`.
2. **`entity_category_enum`:** `site`, `building`, `floor`, `zone`, `space`, `general_space`, `retail_space`, `transit_station`, `kitchen_area`, `service_area`, `corridor`, `structural_element`, `mechanical_area`, `mechanical_element`, `architectural_element`, `elevator_bank`, `elevator`, `stair`, `escalator`.
3. **`relationship_type_enum`:** `CONTAINS`, `BOUNDED_BY`, `ADJACENT_TO`, `CONNECTS_TO`, `PASSES_THROUGH`, `OVERLOOKS`, `ACCESSES`, `LEADS_TO`, `TRANSFERS_TO`, `POWERED_BY`, `COOLED_BY`, `FEEDS_RISER_TO`, `HOISTS_CAR_FOR`, `SERVES`.
4. **`evidence_classification_enum`:** `Direct Evidence`, `Supported Inference`, `Hypothesis`.
5. **`lifecycle_state_enum`:** `DRAFT_SEED`, `CORROBORATED`, `VALIDATED`, `DEPRECATED`, `ARCHIVED`.
6. **`temporal_era_enum`:** `CONSTRUCTION_ERA`, `OPERATIONAL_ERA`, `POST_1993_REPAIR_ERA`.

---

## 3. Table Inventory

### Purpose
Defines the required 11 primary target tables constituting the physical World Model schema.

### Rationale
Translates the 6-tier spatial containment tree, multi-floor junction models, epistemic citation models, and property graphs into discrete, normalized database tables.

### Constraints
- Every table MUST possess a primary key and non-null audit timestamps (`created_at`, `updated_at`).

### Dependency on Approved Specifications
Extends [`docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md) and [`docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Master seed datasets consolidate 164 verified entities across 6 vertical anchor elevations.
• DDL DESIGN REQUIREMENTS: 11 Primary Target Tables (`sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`, `sources`, `entity_evidence_citations`, `element_floor_junction`, `relationships`, `entity_aliases`).
• IMPLEMENTATION RISKS: Foreign key circular dependencies if table creation order is violated.
• FUTURE MIGRATION CONSIDERATIONS: Top-down table DDL execution matching 6-tier containment hierarchy.
```

---

## 4. Key Strategy

### Purpose
Defines primary key requirements, canonical string formatting, and key immutability rules.

### Rationale
Guarantees global uniqueness and human readability without relying on surrogate auto-incrementing integer serials (`SERIAL`/`BIGSERIAL`) as public keys.

### Constraints
- Canonical string primary keys MUST be permanent and immutable once assigned.

### Dependency on Approved Specifications
Extends Section 2 (*Entity Identity Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of seed JSON records use canonical string keys (e.g. `wtc1_f107_windows_on_the_world_main_dining_room`).
• DDL DESIGN REQUIREMENTS: Mandatory primary key constraint on `entity_id` string column across all entity tables.
• IMPLEMENTATION RISKS: String primary keys require explicit foreign key CASCADE updates if entity IDs are merged.
• FUTURE MIGRATION CONSIDERATIONS: SQL `PRIMARY KEY (entity_id)` constraint authoring.
```

---

## 5. Foreign Key Strategy

### Purpose
Defines foreign key referential integrity constraints governing parent-child spatial containment and citation links.

### Rationale
Prevents orphan child entities, broken graph links, or unanchored evidence citations.

### Constraints
- All parent foreign key references MUST enforce `ON DELETE RESTRICT` cascades to prevent accidental parent container deletion.

### Dependency on Approved Specifications
Extends Section 10 (*Cardinality and Integrity Requirements*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Containment hierarchy exhibits strict $1:N$ parent-child tree structure down to Element.
• DDL DESIGN REQUIREMENTS: Mandatory foreign key constraints on parent IDs (`site_id`, `building_id`, `floor_id`, `zone_id`, `space_id`, `source_id`).
• IMPLEMENTATION RISKS: Foreign key validation locks during bulk ingestion.
• FUTURE MIGRATION CONSIDERATIONS: SQL `FOREIGN KEY (parent_id) REFERENCES parent_table(id) ON DELETE RESTRICT`.
```

---

## 6. Constraint Strategy

### Purpose
Defines inline and table-level `CHECK`, `NOT NULL`, and `UNIQUE` constraints protecting data integrity.

### Rationale
Enforces database-level protection against invalid confidence scores, corrupted spatial bounds, or self-referencing relationship loops.

### Constraints
- Confidence scores MUST be bounded strictly: `CHECK (confidence_score BETWEEN 0 AND 100)`.
- Minimum elevation MUST NOT exceed maximum elevation: `CHECK (z_min <= z_max)`.
- Relationships MUST NOT self-reference: `CHECK (subject_entity_id <> object_entity_id)`.

### Traceability to Approved Specifications
Extends Section 6 (*Constraint Strategy*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Principle 5 requires quantifying uncertainty; Principle 1 prohibits unverified hypotheses.
• DDL DESIGN REQUIREMENTS: Mandatory `CHECK` constraints on confidence scores, elevation bounds, and graph edge non-reflexivity.
• IMPLEMENTATION RISKS: Seed data ingestion failure if seed JSON records violate CHECK constraints.
• FUTURE MIGRATION CONSIDERATIONS: SQL `CONSTRAINT check_confidence CHECK (confidence_score BETWEEN 0 AND 100)` authoring.
```

---

## 7. Spatial Storage Strategy

### Purpose
Defines PostGIS extension configuration, 2D polygon footprint geometry columns, numeric elevation attributes, and spatial indexing requirements.

### Rationale
Implements Approved Decisions A.1 and A.2, storing 2D polygon footprints (`EPSG:2263` State Plane Feet) paired with explicit numeric elevation bounds (`z_min`, `z_max` in PA Datum feet) for $O(\log N)$ spatial indexing and seamless WebGL 3D extrusion.

### Constraints
- Native 3D volumetric mesh storage (`POLYGONZ`) is STRICTLY FORBIDDEN for standard floor plan spaces.

### Dependency on Approved Specifications
Extends Section 3 (*Spatial Representation Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Port Authority zero datum (+310.0 ft PA) defines 0.0 ft elevation across all original drawings.
• DDL DESIGN REQUIREMENTS: PostGIS 2D polygon geometry column (`EPSG:2263`), numeric `z_min` and `z_max` columns, 2D GiST spatial index.
• IMPLEMENTATION RISKS: Missing PostGIS extension initialization before spatial column creation.
• FUTURE MIGRATION CONSIDERATIONS: SQL `CREATE EXTENSION IF NOT EXISTS postgis;` and `CREATE INDEX idx_spatial ON table USING GIST (geometry_2d);`.
```

---

## 8. Multi-Floor Storage Strategy

### Purpose
Defines DDL requirements for storing multi-floor vertical elements (Stairs A/B/C, Freight Elevator 50, Core Box Columns 501–1008) across floor slabs.

### Rationale
Implements Approved Decision B.1, utilizing a physical `element_floor_junction` table to deliver $O(1)$ SQL queries for floor-filtered element lookups without violating single-parent tree containment.

### Constraints
- Multi-floor elements MUST set `Building` or `Site` as their primary containment parent.

### Dependency on Approved Specifications
Extends Section 6 (*Multi-Floor Entity Handling Rules*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Freight Elevator 50 services all 110 floors plus 5 sub-grade levels.
• DDL DESIGN REQUIREMENTS: Dedicated `element_floor_junction` physical association table (`element_id`, `floor_id`, `penetration_type_enum`, `has_landing`, `has_machine_room`).
• IMPLEMENTATION RISKS: Element-floor junction records out of sync with graph `PASSES_THROUGH` links.
• FUTURE MIGRATION CONSIDERATIONS: Primary key on `(element_id, floor_id)` composite tuple in `element_floor_junction`.
```

---

## 9. Evidence Citation Storage Strategy

### Purpose
Defines DDL requirements for linking entity records to corroborating primary historical evidence sources.

### Rationale
Implements Approved Decision C.1, establishing a normalized epistemic junction table (`entity_evidence_citations`) to guarantee 100% citation traceability (Principle 2: *Cite Sources*).

### Constraints
- Storing evidence citations as direct array columns on entity tables is STRICTLY FORBIDDEN.

### Dependency on Approved Specifications
Extends Section 7 (*Evidence Linkage Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of extracted entities cite Yamasaki blueprints (A-A series) or Emery Roth plans.
• DDL DESIGN REQUIREMENTS: Dedicated `entity_evidence_citations` junction table (`id`, `entity_id`, `source_id`, `sheet_code`, `evidence_classification_enum`, `confidence_score`).
• IMPLEMENTATION RISKS: Orphan citation records if source IDs are deleted.
• FUTURE MIGRATION CONSIDERATIONS: Composite B-tree index on `(entity_id, source_id)` in `entity_evidence_citations`.
```

---

## 10. Relationship Graph Storage Strategy

### Purpose
Defines DDL requirements for directed property graph relationship storage and multi-hop traversal indexing.

### Rationale
Decouples spatial containment trees from complex non-hierarchical engineering networks (MEP power/chilled water distribution), multi-floor penetrations, and pedestrian access flows.

### Constraints
- All relationships MUST be directed ($\text{Subject Entity} \xrightarrow{\quad\text{ENUM}\quad} \text{Object Entity}$).

### Dependency on Approved Specifications
Extends [`docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 82 master relationships mapped across 6 vertical anchor elevations.
• DDL DESIGN REQUIREMENTS: `relationships` property graph table (`relationship_id`, `subject_entity_id`, `relationship_type_enum`, `object_entity_id`, `confidence_score`).
• IMPLEMENTATION RISKS: Slow multi-hop graph queries without forward and reverse composite indices.
• FUTURE MIGRATION CONSIDERATIONS: Dual composite indices `USING btree (subject_entity_id, relationship_type_enum)` and `USING btree (object_entity_id, relationship_type_enum)`.
```

---

## 11. Temporal Storage Strategy

### Purpose
Defines DDL requirements for storing time-aware historical validity attributes (`valid_from`, `valid_to`) and historical era classifications.

### Rationale
Supports the long-term vision of a living historical digital twin capable of representing the WTC complex across its 35-year physical history (1966 to 2001).

### Constraints
- Temporal era classifications represent an Approved Architectural Decision / Logical Model Proposal.

### Dependency on Approved Specifications
Extends Section 10 (*Temporal State Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: WTC complex physical timeline spans 1966 (groundbreaking) to 2001 (destruction).
• DDL DESIGN REQUIREMENTS: Optional `valid_from` and `valid_to` DATE/TIMESTAMP columns and `temporal_era_enum` column on entity and relationship tables.
• IMPLEMENTATION RISKS: Confusing historical validity dates with database record creation timestamps.
• FUTURE MIGRATION CONSIDERATIONS: SQL `DATE` or `TIMESTAMP WITH TIME ZONE` column authoring.
```

---

## 12. Migration Ordering Requirements

### Purpose
Defines the strict 5-step sequential migration execution order for Phase 3 SQL DDL file authoring.

### Rationale
Prevents dependency resolution errors, broken foreign key constraints, or missing PostGIS extension errors during migration runner execution.

### Constraints
- Executable SQL migration files MUST be written as idempotent, version-controlled scripts under `database/migrations/`.

### Dependency on Approved Specifications
Extends Section 10 (*Migration Strategy*) of [`docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Phase 1 database migration pipeline deployed 5 idempotent migrations under `database/`.
• DDL DESIGN REQUIREMENTS: 5-step sequential migration execution order.
• IMPLEMENTATION RISKS: Migration script failure if table creation sequence violates spatial tree depth.
• FUTURE MIGRATION CONSIDERATIONS: Authoring idempotent SQL file `database/migrations/V1.0__create_world_model_schema.sql`.
```

#### Sequential Migration DDL Execution Order:
```text
STEP 1: Initialize PostGIS Extension & Define 6 ENUM Types
STEP 2: Create Core Spatial Containment Tree Tables (sites ──► buildings ──► floors ──► zones ──► spaces ──► elements)
STEP 3: Create Auxiliary Junction Tables (sources ──► entity_evidence_citations ──► element_floor_junction ──► entity_aliases)
STEP 4: Create Directed Property Graph Table (relationships)
STEP 5: Apply Foreign Key Constraints, CHECK Constraints, and GiST Spatial Indices
```

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 DDL DESIGN SPECIFICATION V1.0 FINALIZED — AUTHORITATIVE BLUEPRINT FOR EXECUTABLE MIGRATION CREATION
