# Entity Identity & Referential Integrity Review

**Document Status:** ✅ AUTHORITATIVE REFERENTIAL INTEGRITY ARCHITECTURE SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Audited Documents:**  
1. [`database/migrations/V1_0__create_world_model_schema.sql`](file:///opt/wtc/wtc-twin-towers/database/migrations/V1_0__create_world_model_schema.sql)  
2. [`docs/V1_0_MIGRATION_REMEDIATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_0_MIGRATION_REMEDIATION_REVIEW.md)  
3. [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md)  
4. [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md)  
5. [`docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_ENTITY_SCHEMA_DESIGN.md)  
6. [`docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md)  

---

## Executive Summary

This document establishes the **authoritative referential integrity architecture** resolving how the World Trade Center Reconstruction Project will enforce database-level referential integrity across:

1. `entity_evidence_citations.entity_id`
2. `entity_aliases.entity_id`
3. `relationships.subject_entity_id` and `relationships.object_entity_id`

while entities remain physically structured across the 6-tier spatial containment tree (`sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`).

Zero SQL migration rewrites, zero DDL execution, and zero web searches were performed in this review.

---

## 1. Evaluation of Candidate Referential Integrity Strategies

```text
STRATEGY EVALUATION MATRIX:
┌────────────────────────────────────────────────────────────────────────┬────────────────────────────────┐
│ Candidate Strategy                                                     │ Architectural Classification   │
├────────────────────────────────────────────────────────────────────────┼────────────────────────────────┤
│ Option 1: Master Entity Registry Table (`entities`) + Tier Tables     │ ✅ APPROVED (Recommended)      │
│ Option 2: Pre-Ingestion Software Validation + Procedural PL/pgSQL Triggers│ ❌ REJECTED                    │
│ Option 3: Polymorphic Nullable Foreign Keys (6 FK columns per table)   │ ❌ REJECTED                    │
└────────────────────────────────────────────────────────────────────────┴────────────────────────────────┘
```

---

### Option 1: Master Entity Registry Table (`entities`) + Tier Tables (APPROVED)

#### Purpose
Instantiate a lightweight master entity reference table (`entities`) storing canonical ID, category ENUM, primary building parent, confidence score, and lifecycle state. Tier tables (`sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`) reference `entities(entity_id)` as their primary key anchor.

#### Advantages
- **Declarative Foreign Keys:** Enables native PostgreSQL `FOREIGN KEY (entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` across `entity_evidence_citations`, `entity_aliases`, and `relationships` (`subject_entity_id`, `object_entity_id`).
- **Zero Orphan Guarantee:** Guarantees 100% database-enforced referential integrity.
- **Repository Alignment:** Fully aligns with Section 2.1 of [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) and Section 1 of [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md).

#### Disadvantages
- Requires inserting a record into `entities` prior to inserting into physical tier tables (`sites`, `buildings`, etc.).

#### Repository Compliance & Complexity
- **Repository Compliance:** 100% Compliant.
- **Implementation Complexity:** Low.
- **Impact on Migration:** Adds 1 master entity table (`entities`) to Step 3 of DDL migration.

#### Classification: **`APPROVED`**

---

### Option 2: Pre-Ingestion Software Validation + PL/pgSQL Triggers (REJECTED)

#### Purpose
Omit database-level foreign key constraints. Rely on Python pre-ingestion scripts (`scripts/validate_seeds.py`) and PostgreSQL `BEFORE INSERT OR UPDATE` PL/pgSQL procedural triggers to verify entity existence across 6 physical tier tables.

#### Disadvantages
- Bypasses native PostgreSQL declarative referential integrity.
- Procedural triggers add CPU overhead during bulk ingestion.
- Increases system fragility if raw SQL updates bypass Python ingestion scripts.

#### Classification: **`REJECTED`**

---

### Option 3: Polymorphic Nullable Foreign Keys (REJECTED)

#### Purpose
Replace `entity_id` with 6 optional foreign keys (`site_id`, `building_id`, `floor_id`, `zone_id`, `space_id`, `element_id`) in `entity_evidence_citations`, `entity_aliases`, and `relationships`.

#### Disadvantages
- Bloats citation, alias, and relationship tables with 6 to 12 nullable foreign key columns per row.
- Violates Approved Decision C.1 and destroys query simplicity.

#### Classification: **`REJECTED`**

---

## 2. Mandatory Referential Integrity Architecture Resolution

### A. How `entity_evidence_citations.entity_id` will enforce integrity:
`entity_evidence_citations.entity_id` will enforce a declarative foreign key constraint referencing `entities(entity_id)` with `ON DELETE RESTRICT`.

### B. How `entity_aliases.entity_id` will enforce integrity:
`entity_aliases.entity_id` will enforce a declarative foreign key constraint referencing `entities(entity_id)` with `ON DELETE RESTRICT`.

### C. How `relationships` subject and object endpoints will enforce integrity:
`relationships.subject_entity_id` and `relationships.object_entity_id` will enforce declarative foreign key constraints referencing `entities(entity_id)` with `ON DELETE RESTRICT`.

---

## 3. Approved Physical DDL Modification Blueprint

When migration revision `V1_1__remediate_world_model_schema.sql` is authored:

1. **Add Master `entities` Table (Step 3):**
   Instantiate `entities (entity_id VARCHAR(128) PRIMARY KEY, entity_category entity_category_enum NOT NULL, building_id VARCHAR(128), confidence_score INTEGER NOT NULL, lifecycle_state lifecycle_state_enum NOT NULL, created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP)`.
2. **Link Tier Tables to Master `entities`:**
   Configure `sites`, `buildings`, `floors`, `zones`, `spaces`, and `elements` to reference `entities(entity_id) ON DELETE RESTRICT`.
3. **Add Foreign Key Constraints to Junction & Graph Tables:**
   Add `FOREIGN KEY (entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` to `entity_evidence_citations` and `entity_aliases`. Add `FOREIGN KEY (subject_entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` and `FOREIGN KEY (object_entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` to `relationships`.
4. **Refine Single-Parent CHECK Constraints:**
   Update `check_zones_parent`, `check_spaces_parent`, and `check_elements_parent` to mandate `((column IS NOT NULL)::int + ...) = 1`.
5. **Add Temporal Era Attributes:**
   Add `temporal_era temporal_era_enum` column to `relationships` and `elements`.

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ ENTITY IDENTITY INTEGRITY REVIEW COMPLETE — ARCHITECTURAL STRATEGY APPROVED FOR DDL REMEDIATION MIGRATION
