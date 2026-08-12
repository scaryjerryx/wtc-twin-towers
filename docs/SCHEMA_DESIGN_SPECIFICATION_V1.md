# Schema Design Specification v1.0

**Document Status:** ✅ AUTHORITATIVE SCHEMA DESIGN SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md), [`docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md)  
**Target Milestone:** Authoritative Schema Blueprint Governing Future PostgreSQL DDL Creation  

---

## Executive Summary

This document establishes the **authoritative Schema Design Specification v1.0** for the World Trade Center Reconstruction Project.

This document is strictly a schema design blueprint and DOES NOT contain physical database implementation code. Zero SQL scripts, zero `CREATE TABLE` DDL statements, zero database migrations, zero indexes, zero triggers, zero stored procedures, zero views, zero API contracts, zero frontend designs, and zero web searches were created in this specification.

This document translates the approved architecture from [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) into exact, non-negotiable schema design rules, key strategies, integrity constraints, ingestion validation rules, and governance requirements that **all future PostgreSQL DDL schema authors MUST implement in Phase 3**.

---

## 1. Entity Storage Architecture

### Purpose
Defines the schema rules for storing physical and spatial entities across the approved 6-Tier Spatial Containment Hierarchy (`Site` ──► `Building` ──► `Floor` ──► `Zone` ──► `Space` ──► `Element`).

### Rationale
Ensures that all 15 canonical entity category ENUM types are represented consistently, avoiding table-depth redundancy while preserving structural and spatial classification.

### Constraints
- Every entity table MUST enforce single-parent containment referencing its immediate spatial parent.
- No entity record may exist without a validated entity category ENUM.

### Dependency on Approved Logical Data Model
Extends Section 1 (*Core Entity Families*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 164 verified unique entities cataloged across 6 anchor elevations (-3.5m to +410.0m).
• SCHEMA DESIGN PRINCIPLES: Single physical entity table vs category-specific tables; immutable string primary keys.
• SCHEMA DESIGN REQUIREMENTS: Primary key must be canonical string ID; parent reference must be non-null (except Site); category ENUM required.
• FUTURE DDL CONSIDERATIONS: PostgreSQL table creation (`entities`), ENUM type definitions, foreign key index creation.
```

---

## 2. Relationship Storage Architecture

### Purpose
Defines the schema rules for storing directed property graph relationships between entities.

### Rationale
Decouples physical tree containment (`CONTAINS`) from complex engineering flow networks (`POWERED_BY`, `COOLED_BY`), multi-floor traversals (`PASSES_THROUGH`), and pedestrian access (`TRANSFERS_TO`).

### Constraints
- All relationships MUST be directed ($\text{Subject} \xrightarrow{\text{ENUM}} \text{Object}$).
- Relationship ENUM types MUST strictly match the 10 approved canonical ENUMs.

### Dependency on Approved Logical Data Model
Extends Section 11 (*Relationship Graph Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 82 master relationships mapped across 6 vertical anchor elevations.
• SCHEMA DESIGN PRINCIPLES: Directed graph stored in a dedicated relationship link table.
• SCHEMA DESIGN REQUIREMENTS: Subject reference, relationship type ENUM, object reference, confidence score, and evidence classification.
• FUTURE DDL CONSIDERATIONS: PostgreSQL table creation (`relationships`), composite B-tree indices on (subject_id, relationship_type).
```

---

## 3. Evidence Storage Architecture

### Purpose
Defines the schema rules for linking entity records to corroborating primary historical evidence sources.

### Rationale
Implements Approved Decision C.1, establishing a normalized epistemic junction model (`entity_evidence_citations`) to guarantee 100% citation traceability (Principle 2: *Cite Sources*).

### Constraints
- Direct array storage of citations on entity tables is STRICTLY FORBIDDEN.
- Citation records MUST reference a validated master evidence source record.

### Dependency on Approved Logical Data Model
Extends Section 7 (*Evidence Linkage Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of extracted entities are cited against Yamasaki contract drawings (A-A series) or Emery Roth plans.
• SCHEMA DESIGN PRINCIPLES: Epistemic separation between raw evidence sources and entity extraction citations.
• SCHEMA DESIGN REQUIREMENTS: Junction table linking entity reference to source reference, sheet code, classification ENUM, and confidence score.
• FUTURE DDL CONSIDERATIONS: PostgreSQL tables (`sources`, `entity_evidence_citations`), foreign key cascades, sheet code indexes.
```

---

## 4. Confidence Storage Architecture

### Purpose
Defines the schema rules for storing, enforcing, and querying epistemic uncertainty ratings across entities and relationships.

### Rationale
Enforces Principle 5 (*Quantify Uncertainty*), ensuring that unverified hypotheses are automatically rejected prior to production ingestion.

### Constraints
- Confidence scores MUST be stored as integers bounded strictly between `0` and `100`.
- Scores `< 80` are STRICTLY FORBIDDEN from production entity storage.

### Dependency on Approved Logical Data Model
Extends Section 8 (*Confidence Score Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of seed JSON entities hold confidence scores >= 95%.
• SCHEMA DESIGN PRINCIPLES: Non-null confidence scoring mandatory on all entity, relationship, and citation records.
• SCHEMA DESIGN REQUIREMENTS: Numeric range check constraint (0 to 100); ingestion check rejecting score < 80.
• FUTURE DDL CONSIDERATIONS: SQL CHECK constraints (`CHECK (confidence_score BETWEEN 0 AND 100)`), pre-ingestion validation triggers.
```

---

## 5. Lifecycle Storage Architecture

### Purpose
Defines the schema rules for tracking entity governance lifecycle transitions across 5 approved states.

### Rationale
Ensures historical entities superseded by higher-resolution blueprint extractions are safely deprecated without breaking referential integrity or historical audit trails.

### Constraints
- Lifecycle state MUST be one of the 5 approved ENUMs (`DRAFT_SEED`, `CORROBORATED`, `VALIDATED`, `DEPRECATED`, `ARCHIVED`).
- Deprecated entity records MUST retain their original canonical identifier permanently.

### Dependency on Approved Logical Data Model
Extends Section 9 (*Lifecycle State Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Master seed dataset consolidates 114 WTC 1 entities and 48 merged cross-floor duplicates.
• SCHEMA DESIGN PRINCIPLES: Lifecycle state tracking with non-destructive entity deprecation flags.
• SCHEMA DESIGN REQUIREMENTS: Lifecycle state ENUM column, deprecation boolean flag, deprecation timestamp, and superseding entity reference.
• FUTURE DDL CONSIDERATIONS: Lifecycle state ENUM type, deprecation audit table, partial index on active entities (`WHERE NOT deprecated`).
```

---

## 6. Temporal Storage Architecture

### Purpose
Defines the schema rules for storing time-aware historical validity attributes (`valid_from`, `valid_to`) and historical era classifications.

### Rationale
Supports the long-term vision of a living historical digital twin capable of representing the WTC complex across its 35-year physical history (1966 to 2001).

### Constraints
- Temporal era classifications represent an Approved Architectural Decision / Logical Model Proposal.
- Temporal timestamps MUST represent actual historical calendar dates, NOT database ingestion timestamps.

### Dependency on Approved Logical Data Model
Extends Section 10 (*Temporal State Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: WTC complex physical timeline spans 1966 (groundbreaking) to 2001 (destruction).
• SCHEMA DESIGN PRINCIPLES: Decoupling historical event validity dates from database record creation dates.
• SCHEMA DESIGN REQUIREMENTS: Optional `valid_from` and `valid_to` date attributes; optional historical era ENUM attribute.
• FUTURE DDL CONSIDERATIONS: PostgreSQL DATE / TIMESTAMP columns, temporal range overlapping indices (`GIST (daterange)`).
```

---

## 7. Multi-Floor Entity Storage Architecture

### Purpose
Defines the schema rules for storing and querying multi-floor vertical elements (Stairs A/B/C, Freight Elevator 50, Core Box Columns 501–1008) across floor slabs.

### Rationale
Implements Approved Decision B.1, utilizing a hybrid tree-junction storage model to deliver $O(1)$ SQL queries for floor-filtered element lookups without violating single-parent tree containment.

### Constraints
- Multi-floor entities MUST set `Building` or `Site` as their primary containment parent.
- Floor-by-floor penetrations MUST be stored in a dedicated physical junction table.

### Dependency on Approved Logical Data Model
Extends Section 6 (*Multi-Floor Entity Handling Rules*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Core Columns 501–1008 and Stairs A/B/C penetrate up to 110 continuous floor slabs.
• SCHEMA DESIGN PRINCIPLES: Primary building parenting paired with physical floor penetration association tables.
• SCHEMA DESIGN REQUIREMENTS: Dedicated element-floor association table storing element reference, floor reference, penetration type ENUM, landing flag, and machine room flag.
• FUTURE DDL CONSIDERATIONS: PostgreSQL table creation (`element_floor_junction`), composite primary key (element_id, floor_id), floor-lookup index.
```

---

## 8. Spatial Storage Architecture

### Purpose
Defines the schema rules for spatial coordinate storage, 2D footprint geometry, numeric elevation bounds, and spatial reference system alignment.

### Rationale
Implements Approved Decisions A.1 and A.2, storing 2D polygon footprints paired with explicit numeric elevation bounds (`z_min`, `z_max` in PA Datum feet) for ultra-fast spatial indexing and seamless 3D WebGL extrusion.

### Constraints
- Native 3D volumetric mesh storage (`POLYGONZ`) is STRICTLY FORBIDDEN for standard floor plan spaces.
- Spatial coordinates MUST be stored using NAD83 / NYC State Plane Feet (`EPSG:2263`) with local Port Authority Zero Datum (+310.0 ft PA) offsets.

### Dependency on Approved Logical Data Model
Extends Section 3 (*Spatial Representation Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Port Authority zero datum (+310.0 ft PA) defines 0.0 ft elevation across all original contract drawings.
• SCHEMA DESIGN PRINCIPLES: 2D PostGIS polygon footprints + numeric elevation bounds (`z_min`, `z_max`).
• SCHEMA DESIGN REQUIREMENTS: PostGIS 2D geometry column (SRID 2263 / 4326), numeric `z_min` and `z_max` elevation columns in feet.
• FUTURE DDL CONSIDERATIONS: PostGIS extension (`CREATE EXTENSION postgis`), 2D GiST spatial index (`USING GIST (geometry_2d)`), Z-range check constraint.
```

---

## 9. Identity and Key Strategy

### Purpose
Defines the schema requirements for primary key generation, canonical string formatting, entity foreign key references, and alias resolution.

### Rationale
Guarantees global uniqueness, human readability, and immutable identity persistence across all database tables and subsystem queries.

### Constraints
- Surrogate auto-incrementing integer IDs (`SERIAL` / `BIGSERIAL`) MUST NOT be used as public canonical entity identifiers.
- Primary key strings MUST be permanent and immutable.

### Dependency on Approved Logical Data Model
Extends Section 2 (*Entity Identity Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of seed JSON records utilize canonical string IDs (e.g., `wtc1_f107_windows_on_the_world_main_dining_room`).
• SCHEMA DESIGN PRINCIPLES: Human-readable, immutable canonical string keys as primary entity identifiers.
• SCHEMA DESIGN REQUIREMENTS: Primary key string column (`entity_id`), non-null foreign key parent string column (`parent_entity_id`), alias mapping table.
• FUTURE DDL CONSIDERATIONS: Primary key constraints (`PRIMARY KEY (entity_id)`), foreign key constraints (`FOREIGN KEY (parent_entity_id) REFERENCES entities`), alias lookup table creation.
```

---

## 10. Cardinality and Integrity Requirements

### Purpose
Defines the schema rules for enforcing logical containment ratios and relational integrity across entity tables.

### Rationale
Translates logical cardinality rules into non-negotiable database integrity requirements, preventing orphan records or invalid spatial hierarchies.

### Constraints
- Orphan child entities (entities without valid parent references) MUST be rejected by foreign key constraints.
- Circular containment chains ($A \text{ contains } B \text{ contains } A$) MUST be strictly prohibited.

### Dependency on Approved Logical Data Model
Extends Section 4 (*Logical Cardinality Rules*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Spatial containment tree exhibits strict $1:N$ hierarchy from Site down to Element.
• SCHEMA DESIGN PRINCIPLES: Strict foreign key referential integrity with ON DELETE RESTRICT cascades.
• SCHEMA DESIGN REQUIREMENTS: Foreign key referential constraints on parent IDs, mandatory junction foreign keys, non-null check constraints.
• FUTURE DDL CONSIDERATIONS: SQL foreign key constraint definitions, referential integrity indexes.
```

---

## 11. Ingestion Validation Requirements

### Purpose
Defines pre-ingestion validation rules that seed datasets (`data/*.json`) MUST satisfy prior to database insertion.

### Rationale
Guarantees Principle 1 (*Evidence Over Assumptions*) and Principle 5 (*Quantify Uncertainty*), preventing corrupt or unverified data from contaminating production tables.

### Constraints
- Automated Python seed validation scripts MUST validate 100% of seed records against schema constraints before DDL execution.
- Any seed record with `confidence_score < 80` or missing `evidence_sources` MUST trigger ingestion failure.

### Dependency on Approved Logical Data Model
Extends Section 7 (*Evidence Linkage Model*) and Section 8 (*Confidence Score Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Pre-ingestion Python validation script verified 164 seed entities across 7 JSON files.
• SCHEMA DESIGN PRINCIPLES: Pre-database software validation layer coupled with database-level check constraints.
• SCHEMA DESIGN REQUIREMENTS: Mandated Python validation pipeline checking canonical ID formatting, parent existence, ENUM validity, spatial bounds, and confidence thresholds.
• FUTURE DDL CONSIDERATIONS: Stored validation functions, staging table ingestion routines.
```

---

## 12. Schema Governance Requirements

### Purpose
Defines change control, versioning, audit logging, and schema migration governance standards for all future PostgreSQL DDL modifications.

### Rationale
Ensures that the PostgreSQL database remains an authoritative, tamper-proof, evidence-backed World Model repository.

### Constraints
- Schema changes MUST be executed via idempotent, version-controlled SQL migration scripts.
- Uncited manual data edits in the production database are STRICTLY FORBIDDEN.

### Dependency on Approved Logical Data Model
Extends Section 12 (*Data Ownership Boundaries*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Phase 1 database migration pipeline deployed 5 idempotent migrations under `database/`.
• SCHEMA DESIGN PRINCIPLES: Strictly versioned, idempotent, migration-driven schema governance.
• SCHEMA DESIGN REQUIREMENTS: Schema version tracking table, migration audit log, restricted write roles (`wtc_writer`), read-only public roles.
• FUTURE DDL CONSIDERATIONS: Migration tracking table (`schema_migrations`), DDL migration script naming conventions (`V1_0__create_world_model_tables.sql`).
```

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ SCHEMA DESIGN SPECIFICATION V1.0 FINALIZED — AUTHORITATIVE BLUEPRINT FOR PHASE 3 POSTGRESQL DDL CREATION
