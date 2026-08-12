# Phase 3 Relationship Schema Design Specification

**Document Status:** ✅ AUTHORITATIVE RELATIONSHIP SCHEMA DESIGN SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md), [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md), [`docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md), [`docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md)  
**Target Milestone:** Logical-to-Physical Relationship Graph Mapping Specification Governing PostgreSQL DDL Creation  

---

## Executive Summary

This document establishes the **authoritative physical schema design specification** for relationship graph storage in the World Trade Center Reconstruction Project.

This document defines the physical directed relationship architecture, primary key strategy, $N:M$ graph network cardinalities, evidence citation linkages, confidence score bounds, multi-hop traversal indexing requirements, multi-floor relationship patterns, temporal validity attributes, referential integrity constraints, and governance standards.

Zero SQL DDL scripts, zero `CREATE TABLE` statements, zero database migrations, zero APIs, zero frontend models, and zero web searches were created in this specification.

---

## 1. Directed Relationship Architecture

### Purpose
Defines the schema rules for storing directed property graph edges connecting subject entities to object entities across the approved 10 canonical relationship ENUM types.

### Rationale
Decouples spatial containment trees from complex non-hierarchical engineering networks (MEP power/chilled water distribution), multi-floor penetrations, pedestrian access flows, and visual sightlines.

### Constraints
- All relationships MUST be directed ($\text{Subject Entity} \xrightarrow{\quad\text{Relationship ENUM}\quad} \text{Object Entity}$).
- Relationship ENUM types MUST strictly match the 10 approved canonical ENUMs (`CONTAINS`, `BOUNDED_BY`, `ADJACENT_TO`, `CONNECTS_TO`, `PASSES_THROUGH`, `OVERLOOKS`, `ACCESSES`, `LEADS_TO`, `TRANSFERS_TO`, `POWERED_BY`, `COOLED_BY`, `FEEDS_RISER_TO`, `HOISTS_CAR_FOR`, `SERVES`).

### Traceability to Approved Specifications
Extends Section 9 (*Relationship Graph Model*) of [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md) and Section 11 of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 82 master relationships mapped across 6 vertical anchor elevations (-3.5m to +410.0m).
• ARCHITECTURAL DECISIONS: Dedicated directed graph table storing subject reference, relationship type ENUM, and object reference.
• PHYSICAL SCHEMA REQUIREMENTS: Mandatory subject_id, relationship_type_enum, object_id, confidence_score, evidence_classification.
• FUTURE DDL CONSIDERATIONS: PostgreSQL table creation (`relationships`), ENUM type definitions, composite B-tree indices.
```

---

## 2. Relationship Identity Strategy

### Purpose
Defines the primary key and identity persistence strategy for relationship graph edge records.

### Rationale
Ensures that every relationship edge possesses a unique, deterministic, human-readable or surrogate key for tracking, citation linkage, and lifecycle deprecation.

### Constraints
- Relationship IDs MUST be globally unique and immutable once instantiated.
- Dual edge entries for identical subject, object, and relationship type are STRICTLY FORBIDDEN (unique constraint enforcement).

### Traceability to Approved Specifications
Extends Section 2 (*Entity Identity Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of seed JSON relationships hold deterministic subject-predicate-object tuples.
• ARCHITECTURAL DECISIONS: Immutable canonical string key format (`rel_[subject]_[relationship_type]_[object]`) or surrogate primary key.
• PHYSICAL SCHEMA REQUIREMENTS: Primary key column, subject foreign key reference, object foreign key reference.
• FUTURE DDL CONSIDERATIONS: Primary key constraint (`PRIMARY KEY (relationship_id)`), unique composite constraint (`UNIQUE (subject_entity_id, relationship_type, object_entity_id)`).
```

---

## 3. Relationship Cardinality Requirements

### Purpose
Defines the physical database cardinality and foreign key referential integrity requirements for graph network edges.

### Rationale
Supports arbitrary $N:M$ graph networks where a single entity can be the subject or object of multiple relationships across different functional categories.

### Constraints
- Foreign key references on both `subject_entity_id` and `object_entity_id` MUST reference valid entity records in the `entities` table.
- Deleting an entity MUST be restricted (`ON DELETE RESTRICT`) if active relationship edges reference it.

### Traceability to Approved Specifications
Extends Section 4 (*Logical Cardinality Rules*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Relationship graph forms arbitrary N:M networks across engineering and spatial entities.
• ARCHITECTURAL DECISIONS: Dual foreign key referential integrity constraints referencing primary entity tables.
• PHYSICAL SCHEMA REQUIREMENTS: Non-null subject_entity_id, non-null object_entity_id, ON DELETE RESTRICT cascade.
• FUTURE DDL CONSIDERATIONS: SQL foreign key constraint definitions (`FOREIGN KEY (subject_entity_id) REFERENCES entities(entity_id)`).
```

---

## 4. Relationship Evidence Linkage

### Purpose
Defines the schema requirements for attributing epistemic evidence sources to relationship graph edges.

### Rationale
Ensures that engineering flow links and multi-floor penetrations are backed 100% by primary contract drawings or verified engineering reports (Principle 2: *Cite Sources*).

### Constraints
- Relationship records MUST store `evidence_classification` (`Direct Evidence`, `Supported Inference`, or `Hypothesis`) and `evidence_sources` citations.
- Uncited relationship edges are STRICTLY FORBIDDEN from production storage.

### Traceability to Approved Specifications
Extends Section 7 (*Evidence Linkage Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of seed relationships cite blueprint sheet sources (e.g. A-A-18, A-A-19, A-A-31, A-A-121).
• ARCHITECTURAL DECISIONS: Mandatory epistemic metadata columns on relationship records or junction table citation links.
• PHYSICAL SCHEMA REQUIREMENTS: Non-null evidence_classification_enum, non-null confidence_score, evidence source array.
• FUTURE DDL CONSIDERATIONS: Junction table linking (`relationship_evidence_citations`) or text array column (`evidence_sources TEXT[]`).
```

---

## 5. Relationship Confidence Storage

### Purpose
Defines the schema rules for storing and filtering relationship uncertainty scores.

### Rationale
Enforces Principle 5 (*Quantify Uncertainty*), preventing unverified or speculative relationship edges from corrupting production knowledge graph queries.

### Constraints
- Confidence scores MUST be stored as integers bounded strictly between `0` and `100`.
- Scores `< 80` are STRICTLY FORBIDDEN from production relationship storage.

### Traceability to Approved Specifications
Extends Section 8 (*Confidence Score Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: 100% of verified seed JSON relationships hold confidence scores >= 95%.
• ARCHITECTURAL DECISIONS: Non-null integer confidence score attribute bounded [0, 100].
• PHYSICAL SCHEMA REQUIREMENTS: Numeric range check constraint `CHECK (confidence_score BETWEEN 0 AND 100)`.
• FUTURE DDL CONSIDERATIONS: SQL CHECK constraint, pre-ingestion validation check.
```

---

## 6. Multi-Hop Traversal Requirements

### Purpose
Defines physical database indexing requirements to support high-speed multi-hop graph traversal queries.

### Rationale
Enables instantaneous graph queries tracing continuous 13.8kV electrical distribution loops, chilled water riser lines, or multi-zone elevator transit paths across 110 floor levels.

### Constraints
- Traversal query performance MUST support $O(\log N)$ edge lookup speed for both forward (subject-to-object) and reverse (object-to-subject) graph queries.

### Traceability to Approved Specifications
Extends Section 2 (*Relationship Storage Architecture*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Electrical substation loops and MER chilled water risers span up to 110 stories.
• ARCHITECTURAL DECISIONS: Dual composite indexing strategy on forward and reverse graph edge tuples.
• PHYSICAL SCHEMA REQUIREMENTS: Mandated composite index on (subject_entity_id, relationship_type) and (object_entity_id, relationship_type).
• FUTURE DDL CONSIDERATIONS: PostgreSQL B-tree index creation (`CREATE INDEX idx_rel_forward ON relationships (subject_entity_id, relationship_type)`).
```

---

## 7. Multi-Floor Relationship Handling

### Purpose
Defines physical schema patterns for linking multi-floor vertical elements (Stairs A/B/C, Freight Elevator 50, Core Columns 501–1008) to individual floor datums via graph edges.

### Rationale
Implements Approved Decision B.1, allowing multi-floor elements parented to `Building` to connect dynamically to individual floor levels via `PASSES_THROUGH`, `SERVES`, and `LANDS_AT` graph links.

### Constraints
- Multi-floor relationship links MUST specify exact penetration types and landing flags.

### Traceability to Approved Specifications
Extends Section 6 (*Multi-Floor Entity Handling Rules*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Freight Elevator 50 services all 110 floors plus 5 sub-grade levels.
• ARCHITECTURAL DECISIONS: Combining physical element-floor associations with directed graph traversal links (`PASSES_THROUGH`).
• PHYSICAL SCHEMA REQUIREMENTS: Directed relationship edges connecting Floor entities to Multi-Floor Element entities.
• FUTURE DDL CONSIDERATIONS: Foreign key checks against physical `element_floor_junction` table.
```

---

## 8. Temporal Relationship Handling

### Purpose
Defines schema requirements for storing time-aware historical validity attributes (`valid_from`, `valid_to`) on relationship edges.

### Rationale
Allows modeling physical relationship graph changes over time (e.g. tenant electrical modifications, 1993 post-bombing structural reinforcement).

### Constraints
- Temporal validity attributes represent an Approved Architectural Decision / Logical Model Proposal.
- Historical validity dates MUST NOT be confused with database ingestion record creation dates.

### Traceability to Approved Specifications
Extends Section 10 (*Temporal State Model*) of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: WTC complex physical system configuration evolved between 1966 and 2001.
• ARCHITECTURAL DECISIONS: Optional historical timestamp columns (`valid_from`, `valid_to`) on relationship records.
• PHYSICAL SCHEMA REQUIREMENTS: Optional DATE / TIMESTAMP columns for historical relationship validity.
• FUTURE DDL CONSIDERATIONS: PostgreSQL TIMESTAMP columns, temporal range indices.
```

---

## 9. Integrity Requirements

### Purpose
Defines strict database integrity constraints prohibiting invalid, self-referencing, or circular relationship structures.

### Rationale
Protects graph query engines from infinite loops and data corruption.

### Constraints
- **Self-Referencing Prohibition:** Self-referencing edges ($A \xrightarrow{\quad\text{ENUM}\quad} A$) are STRICTLY FORBIDDEN.
- **Circular Containment Prohibition:** Circular containment chains ($A \xrightarrow{\text{CONTAINS}} B \xrightarrow{\text{CONTAINS}} A$) are STRICTLY FORBIDDEN.

### Traceability to Approved Specifications
Extends Section 10 (*Cardinality and Integrity Requirements*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Spatial containment tree exhibits strict acyclic hierarchy down to Element.
• ARCHITECTURAL DECISIONS: Database-level CHECK constraints and pre-ingestion cycle detection algorithms.
• PHYSICAL SCHEMA REQUIREMENTS: CHECK constraint prohibiting subject = object (`CHECK (subject_entity_id <> object_entity_id)`).
• FUTURE DDL CONSIDERATIONS: SQL CHECK constraint, pre-ingestion Python cycle detection validator.
```

---

## 10. Relationship Governance Requirements

### Purpose
Defines change control, audit logging, idempotency, and write-role governance rules for relationship graph storage.

### Rationale
Ensures that the relationship graph remains an authoritative, evidence-backed knowledge network.

### Constraints
- Relationship updates MUST be idempotent (`ON CONFLICT (subject, relationship_type, object) DO UPDATE`).
- Production write access is restricted exclusively to the `wtc_writer` role.

### Traceability to Approved Specifications
Extends Section 12 (*Schema Governance Requirements*) of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

```text
EVIDENTIARY SEPARATION:
• VERIFIED FACTS: Database write permissions are governed by the `wtc_writer` PostgreSQL role.
• ARCHITECTURAL DECISIONS: Idempotent upsert execution coupled with schema migration version tracking.
• PHYSICAL SCHEMA REQUIREMENTS: Mandated upsert strategy and migration tracking compatibility.
• FUTURE DDL CONSIDERATIONS: Python ingestion script upsert logic (`scripts/ingest_relationships.py`).
```

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 RELATIONSHIP SCHEMA DESIGN SPECIFICATION COMPLETE — READY FOR TASK 3.3 EPISTEMIC EVIDENCE SCHEMA DESIGN
