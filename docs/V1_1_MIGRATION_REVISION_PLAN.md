# Phase 3 Migration Revision Plan v1.1

**Document Status:** ✅ AUTHORITATIVE MIGRATION REVISION PLAN  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Target Migration File to Revise:** `database/migrations/V1_0__create_world_model_schema.sql` (to be updated to `V1_1__remediate_world_model_schema.sql`)  
**Audited Parent Specifications:**  
1. [`docs/V1_0_MIGRATION_REMEDIATION_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_0_MIGRATION_REMEDIATION_REVIEW.md)  
2. [`docs/ENTITY_IDENTITY_INTEGRITY_REVIEW.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_IDENTITY_INTEGRITY_REVIEW.md)  
3. [`docs/ENTITY_REGISTRY_IMPACT_ASSESSMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ENTITY_REGISTRY_IMPACT_ASSESSMENT.md)  
4. [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md)  
5. [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md)  

**FINAL MIGRATION PLAN RECOMMENDATION:** **`[X] Migration Requires Minor Revision`**  

---

## Executive Summary

This document establishes the **authoritative Migration Revision Plan v1.1** defining the exact DDL modifications required before the World Model migration script can be executed against PostgreSQL `wtc_evidence`.

Zero SQL scripts, zero database migration rewrites, zero physical table executions, and zero web searches were created in this revision plan.

This plan details 5 specific DDL revisions addressing all verified integrity findings, single-parent `CHECK` constraint ambiguities, and temporal attribute omissions.

The single selected recommendation is **`[X] Migration Requires Minor Revision`**.

---

## 1. Verified Issues Scorecard

```text
REVISION PLAN SCORECARD:
┌────────────────────────────────────────────────────────────────────────┬──────────────────┐
│ Verified Issue                                                         │ Classification   │
├────────────────────────────────────────────────────────────────────────┼──────────────────┤
│ 1. Missing Entity Referential Integrity (Citations -> Entities)        │ IMPORTANT        │
│ 2. Missing Relationship Endpoint Integrity (Subject/Object -> Entities)│ IMPORTANT        │
│ 3. Missing Entity Alias Integrity (Aliases -> Entities)                │ MINOR            │
│ 4. Ambiguous Single-Parent CHECK Constraints (Zones, Spaces, Elements) │ IMPORTANT        │
│ 5. Unused `temporal_era_enum` Definition (Missing Columns)              │ MINOR            │
└────────────────────────────────────────────────────────────────────────┴──────────────────┘
```

---

## 2. Detailed Required Revisions (5 Items)

### 2.1 Revision 1: Master Entity Registry Table (`entities`) & Citation Foreign Key
- **Current Implementation:** `entity_evidence_citations.entity_id VARCHAR(128) NOT NULL` (unconstrained string, no FK).
- **Required Revision:** Instantiate `entities` master reference table in Step 3. Add `FOREIGN KEY (entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` to `entity_evidence_citations`. Add `FOREIGN KEY (site_id, bldg_id, etc.) REFERENCES entities(entity_id)` to physical tier tables.
- **Repository Justification:** [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md) Section 3 & [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) Section 7.
- **Impact on Migration:** Moderate (instantiates master `entities` table in Step 3 before tier tables).
- **Risk Level:** Low.
- **Classification:** **`IMPORTANT`**.

---

### 2.2 Revision 2: Relationship Endpoint Foreign Keys
- **Current Implementation:** `subject_entity_id` and `object_entity_id` in `relationships` are unconstrained strings without FKs.
- **Required Revision:** Add `FOREIGN KEY (subject_entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` and `FOREIGN KEY (object_entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` to `relationships`.
- **Repository Justification:** [`docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_RELATIONSHIP_SCHEMA_DESIGN.md) Section 3.
- **Impact on Migration:** Moderate.
- **Risk Level:** Low.
- **Classification:** **`IMPORTANT`**.

---

### 2.3 Revision 3: Entity Alias Foreign Key
- **Current Implementation:** `entity_aliases.entity_id` is an unconstrained string without a foreign key.
- **Required Revision:** Add `FOREIGN KEY (entity_id) REFERENCES entities(entity_id) ON DELETE RESTRICT` to `entity_aliases`.
- **Repository Justification:** [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) Section 2.3.
- **Impact on Migration:** Minor.
- **Risk Level:** Low.
- **Classification:** **`MINOR`**.

---

### 2.4 Revision 4: Strict Single-Parent CHECK Constraints (`zones`, `spaces`, `elements`)
- **Current Implementation:** `CHECK (col1 IS NOT NULL OR col2 IS NOT NULL OR ...)` permits multiple simultaneous non-null parent references on the same record.
- **Required Revision:** Replace `OR` clauses with exact integer sum equality:
  - `zones`: `CHECK (((floor_id IS NOT NULL)::int + (building_id IS NOT NULL)::int + (site_id IS NOT NULL)::int) = 1)`
  - `spaces`: `CHECK (((zone_id IS NOT NULL)::int + (floor_id IS NOT NULL)::int) = 1)`
  - `elements`: `CHECK (((space_id IS NOT NULL)::int + (zone_id IS NOT NULL)::int + (floor_id IS NOT NULL)::int + (building_id IS NOT NULL)::int) = 1)`
- **Repository Justification:** [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) Section 5 (*Single-Parent Rule*).
- **Impact on Migration:** Minor string update in DDL CHECK constraints.
- **Risk Level:** Low.
- **Classification:** **`IMPORTANT`**.

---

### 2.5 Revision 5: `temporal_era_enum` Column Addition
- **Current Implementation:** `CREATE TYPE temporal_era_enum AS ENUM (...)` defined in Step 2 but unreferenced by any table column.
- **Required Revision:** Add `temporal_era temporal_era_enum` optional column to `relationships` and `elements` tables.
- **Repository Justification:** [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md) Section 6 & [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md) Section 10.
- **Impact on Migration:** Minor column addition.
- **Risk Level:** Low.
- **Classification:** **`MINOR`**.

---

## 3. Entity Registry Design Impact & DDL Modification Scope

Updating the migration DDL requires 6 precise, non-breaking modifications:

```text
DDL MODIFICATION EXECUTION STEPS:
1. Step 3: Insert `entities` master table DDL.
2. Step 3: Add `REFERENCES entities(entity_id)` to `sites`, `buildings`, `floors`, `zones`, `spaces`, `elements`.
3. Step 3: Replace `OR` clauses in `zones`, `spaces`, `elements` with `((col IS NOT NULL)::int + ...) = 1`.
4. Step 4: Add `REFERENCES entities(entity_id)` to `entity_evidence_citations` and `entity_aliases`.
5. Step 5: Add `REFERENCES entities(entity_id)` to `relationships` (`subject_entity_id` and `object_entity_id`).
6. Step 5: Add `temporal_era temporal_era_enum` optional column to `relationships` and `elements`.
```

---

## 4. Migration Risk Assessment

- **Dependency Ordering Risk:** Managed by creating `entities` master table in Step 3 before tier tables or junction tables are defined.
- **Foreign Key Cascade Risk:** `ON DELETE RESTRICT` prevents accidental deletion of parent entities.
- **Ingestion Failure Risk:** Managed via automated Python pre-ingestion validation suite (`scripts/validate_seeds.py`).

---

## 5. Final Recommendation

```text
FINAL MIGRATION PLAN RECOMMENDATION SELECTION:
[ ] Migration Revision Not Required
[X] Migration Requires Minor Revision ◄── SOLE SELECTED RECOMMENDATION
[ ] Migration Requires Major Revision
```

### Detailed Justification:
The migration file requires 5 discrete, minor DDL refinements to achieve 100% repository-strict correctness and declarative referential integrity. The recommendation is **`[X] Migration Requires Minor Revision`**.
