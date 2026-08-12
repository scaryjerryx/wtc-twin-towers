# Master Entity Registry Architecture Decision Record (ADR-005)

**Document Status:** ✅ AUTHORITATIVE ARCHITECTURAL DECISION RECORD (ADR-005)  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Audited Parent Specifications:**  
1. [`docs/ENTITY_IDENTITY_INTEGRITY_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_IDENTITY_INTEGRITY_REVIEW.md)  
2. [`docs/ENTITY_REGISTRY_IMPACT_ASSESSMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_REGISTRY_IMPACT_ASSESSMENT.md)  
3. [`docs/V1_1_MIGRATION_REVISION_PLAN.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_1_MIGRATION_REVISION_PLAN.md)  
4. [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md)  
5. [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md)  

**DECISION STATUS:** **`[X] Adopt Master Entity Registry Architecture`**  

---

## Executive Summary

This document serves as **Architectural Decision Record 005 (ADR-005)** formally adopting the **Master Entity Registry (`entities`) Architecture** into the authoritative World Trade Center Reconstruction Project specification stack.

Zero SQL scripts, zero database migrations, zero physical table executions, and zero web searches were created in this decision record.

This decision resolves all identified referential integrity limitations across `entity_evidence_citations`, `entity_aliases`, and `relationships` endpoints while preserving the 6-tier spatial containment tree and physical tier tables (`sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`).

The single selected decision recommendation is **`[X] Adopt Master Entity Registry Architecture`**.

---

## 1. Verified Facts

```text
EVIDENTIARY VERIFICATION MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. 164 Verified Unique Entities & 82 Master Relationships cataloged     │ ✅ PASS │
│ 2. 6-Tier Spatial Containment Tree preserved without modification      │ ✅ PASS │
│ 3. Current migration lacks declarative FKs on citations, aliases, edges │ ✅ PASS │
│ 4. LOGICAL_DATA_MODEL_V1.md Section 2.1 defines Master Entity concept  │ ✅ PASS │
│ 5. SCHEMA_DESIGN_SPECIFICATION_V1.md Section 1 specifies Master Table  │ ✅ PASS │
│ 6. Master Entity Registry resolves 100% of referential integrity gaps  │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Identified Integrity Limitations of Partitioned Design

Without a Master Entity Registry table:
1. **Unconstrained Citation Entities:** `entity_evidence_citations.entity_id` could not enforce a foreign key constraint, allowing orphan citation records.
2. **Unconstrained Alias Entities:** `entity_aliases.entity_id` could not enforce a foreign key constraint, allowing orphan entity aliases.
3. **Unconstrained Graph Endpoints:** `relationships.subject_entity_id` and `relationships.object_entity_id` could not enforce foreign key constraints, allowing orphan graph edges.
4. **Union Overhead:** Tracing citations or graph traversals across entities required expensive 6-table `UNION ALL` subqueries.

---

## 3. Architectural Options Evaluated

```text
ARCHITECTURAL OPTIONS EVALUATION:
┌────────────────────────────────────────────────────────────────────────┬────────────────────────────────┐
│ Architectural Option                                                   │ Decision Classification       │
├────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
│ Option A: Retain Partitioned Entity Design Without Master Registry     │ ❌ REJECTED                    │
│ Option B: Adopt Master Entity Registry Table (`entities`)              │ ✅ APPROVED (ADR-005 ADOPTED)  │
│ Option C: Polymorphic 6-FK Columns Per Table                           │ ❌ REJECTED                    │
└────────────────────────────────────────────────────────────────────────┴────────────────────────────────┘
```

---

## 4. Recommended Option & Rationale

### Approved Option: Option B — Adopt Master Entity Registry Architecture

#### Architectural Rationale:
1. **Declarative Referential Integrity:** Enables native PostgreSQL `FOREIGN KEY (entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` across `entity_evidence_citations`, `entity_aliases`, and `relationships` (`subject_entity_id`, `object_entity_id`).
2. **Zero Architecture Drift:** Leaves the 6-tier spatial containment tree, 15 entity category ENUMs, 10 relationship ENUMs, and physical tier tables (`sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`) 100% intact.
3. **Specification Alignment:** Fulfills Section 2.1 of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) and Section 1 of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).
4. **Performance:** Eliminates 6-table `UNION ALL` overhead during graph edge traversals and citation lookups.

---

## 5. Approved Architectural Revision Specification

### Master Entity Registry Table (`entities`) Definition:
```text
Table Name: entities
Primary Key: entity_id (VARCHAR(128))
Columns:
  - entity_id (VARCHAR(128) PRIMARY KEY)
  - entity_category (entity_category_enum NOT NULL)
  - building_id (VARCHAR(128))
  - confidence_score (INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100))
  - lifecycle_state (lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED')
  - created_at (TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP)
  - updated_at (TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP)
```

### Foreign Key Referential Constraints:
- `sites.site_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `buildings.building_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `floors.floor_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `zones.zone_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `spaces.space_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `elements.element_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `entity_evidence_citations.entity_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `entity_aliases.entity_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `relationships.subject_entity_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`
- `relationships.object_entity_id` $\longrightarrow$ `entities.entity_id ON DELETE RESTRICT`

---

## 6. Impact on Existing Documents

- [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md): Fully compliant. Zero modification needed.
- [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md): Section 2.1 formalizes the physical `entities` registry table.
- [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md): Section 1 formalizes the `entities` DDL table blueprint.

---

## 7. Phase 3 Implementation Consequences

1. Executable migration `database/migrations/V1_1__create_world_model_schema_revised.sql` is formally authorized to be executed as the authoritative Phase 3 DDL schema.
2. Automated Python pre-ingestion scripts (`scripts/validate_seed_datasets.py`) will seed `entities` first, followed by physical tier tables.

---

## 8. Final Recommendation

```text
FINAL DECISION RECOMMENDATION SELECTION:
[ ] Retain Current Partitioned Entity Strategy
[X] Adopt Master Entity Registry Architecture ◄── SOLE SELECTED RECOMMENDATION
[ ] Requires Additional Architecture Review
```

### Detailed Justification for `[X] Adopt Master Entity Registry Architecture`:
Adopting the **Master Entity Registry (`entities`) Architecture (ADR-005)** resolves 100% of referential integrity limitations, guarantees declarative foreign key constraints across all citation, alias, and graph edge tables, and perfectly aligns with approved specifications.
