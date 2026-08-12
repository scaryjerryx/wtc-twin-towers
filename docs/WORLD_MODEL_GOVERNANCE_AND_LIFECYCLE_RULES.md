# World Model Governance & Entity/Relationship Lifecycle Rules

**Document Status:** ✅ APPROVED PHASE 2 SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specification:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md)  
**Target Phase:** **Phase 2 — Database Design Preparation**  

---

## Executive Summary

This document establishes the governing **Entity & Relationship Lifecycle Rules, Evidence Linkage Protocols, Confidence Scoring Criteria, Data Management Standards, and Architecture Validation Framework** for the World Trade Center Reconstruction Project.

Zero SQL DDL scripts, zero database migrations, zero database tables, and zero web searches were created in this specification.

This specification governs how World Model seed data (`data/*.json`) is managed, updated, validated, and prepared for future PostgreSQL database ingestion, ensuring 100% compliance with epistemic governance standards.

---

## 1. Entity Lifecycle Rules

Every entity in the World Model (`site`, `building`, `floor`, `zone`, `space`, `element`) follows a strict 5-stage lifecycle:

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  DRAFT SEED  │ ──► │ CORROBORATED │ ──► │  VALIDATED   │ ──► │  DEPRECATED  │ ──► │   ARCHIVED   │
│  (Extraction)│     │ (Multi-Sheet)│     │  (Consol.)   │     │ (Superseded) │     │ (Historical) │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### 1.1 Lifecycle States:
1. **DRAFT SEED:** Entity extracted from a single blueprint sheet (e.g. `A-A-19`). Initialized with `corroboration_count: 1` and `confidence_score: 95`.
2. **CORROBORATED:** Entity identified on 2 or more distinct blueprint sheets (e.g. `A-A-19` + `A-A-20` + `A-A-31`). `evidence_sources` array appended; `corroboration_count` incremented.
3. **VALIDATED:** Entity verified against structural vector extractions or cross-checked across vertical anchor elevations. Approved for database ingestion.
4. **DEPRECATED:** Entity superseded by a higher-resolution drawing or canonical ID merge. Retained in historical logs with `deprecated: true` flag.
5. **ARCHIVED:** Read-only historical record retained for audit trails.

### 1.2 Entity Immutability Rules:
- **Canonical ID Permanence:** Once an `entity_id` is assigned (e.g. `wtc1_f107_windows_on_the_world_main_dining_room`), it MUST remain immutable. Entity IDs may never be renamed or reassigned.
- **Single Parent Rule:** In the strict 6-tier spatial tree (`Site` ──► `Building` ──► `Floor` ──► `Zone` ──► `Space` ──► `Element`), an entity MUST have exactly ONE primary tree parent (`parent_entity`). Multi-floor vertical entities set `building_id` as their primary parent.

---

## 2. Relationship Lifecycle Rules

Relationships between entities (`CONTAINS`, `BOUNDED_BY`, `ADJACENT_TO`, `CONNECTS_TO`, `PASSES_THROUGH`, `OVERLOOKS`, `ACCESSES`, `LEADS_TO`, `TRANSFERS_TO`, `POWERED_BY`, `COOLED_BY`, `FEEDS_RISER_TO`, `HOISTS_CAR_FOR`, `SERVES`) govern the directed property graph:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ RELATIONSHIP LIFECYCLE CONSTRAINTS                                     │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Endpoint Integrity: Both subject_id and object_id MUST exist.      │
│ 2. Directional Strictness: All relationships are directed (A ──► B).   │
│ 3. Category Validation: ENUM type MUST match approved taxonomy.        │
│ 4. No Orphan Links: Deleting/deprecating an entity removes its links.  │
└────────────────────────────────────────────────────────────────────────┘
```

### 2.1 Graph Traversal & Penetration Rules:
- **Vertical Multi-Floor Penetrations:** Multi-floor elements (Stairs A/B/C, Freight Elevator 50, Core Columns) connect to individual floor datums via `PASSES_THROUGH`, `SERVES`, or `LANDS_AT` graph links.
- **System Dependency Chains:** Engineering systems follow directed flow chains (e.g., `13.8kV Substation ──(POWERED_BY)──► Centrifugal Chiller ──(COOLED_BY)──► AHU Fan ──(FEEDS_RISER_TO)──► Sky Lobby`).

---

## 3. Evidence Linkage Rules

In compliance with **Principle 2 (*Cite Sources*)** and **Principle 3 (*Separate Evidence From Inference*)**:

1. **Mandatory Citation Array:** Every entity and relationship record MUST include:
   - `evidence_sources`: JSON array of all source blueprint codes (e.g., `["A-A-18", "A-A-19", "A-A-20"]`).
   - `evidence_classification`: Epistemic classification (`Direct Evidence`, `Supported Inference`, `Hypothesis`).
2. **Direct Evidence Requirement:** Entities derived directly from Yamasaki contract drawings or Emery Roth plans MUST be classified as `Direct Evidence`.
3. **Inference Scoping:** Geometrically or engineering-deduced structures must be explicitly marked as `Supported Inference` with a documented rationale.

---

## 4. Confidence Scoring Rules

In compliance with **Principle 5 (*Quantify Uncertainty*)**:

```text
CONFIDENCE SCORE SCALE (0 to 100 Integer):
┌────────────────────────────────────────────────────────────────────────┐
│ 95 - 100 : DIRECT EVIDENCE (Yamasaki / Emery Roth Contract Blueprints)  │
│ 80 - 94  : SUPPORTED INFERENCE (Engineering Deduction / Structural)    │
│  0 - 79  : UNVERIFIED HYPOTHESIS (STRICTLY FORBIDDEN FROM DB INGESTION)│
└────────────────────────────────────────────────────────────────────────┘
```

- **Production Threshold:** Only entities and relationships with `confidence_score >= 80` are eligible for production seed consolidation and database ingestion.
- **Automatic Corroboration Boost:** Entities corroborated across 3 or more independent blueprint sheets achieve maximum confidence (`95-100%`).

---

## 5. Data Management Rules

1. **Deterministic JSON Formatting:** Seed JSON files (`data/*.json`) MUST be formatted with 2-space indentation, deterministic key ordering, and sorted by `entity_id`.
2. **Idempotent Consolidation Pipelines:** Consolidation scripts (`wtc1_world_model_v1.json`) MUST be 100% idempotent. Re-running consolidation on seed files must yield byte-for-byte identical output.
3. **Zero-Invention Guarantee (Principle 1):** No AI agent or developer may invent speculative rooms, fictional room numbers, or unverified dimensions.

---

## 6. Architecture Validation Framework

All seed datasets MUST validate against the **Approved 6-Tier Spatial Containment Hierarchy**:

```text
VALIDATION CHECKLIST:
[X] Tier 1: Site Level Validated (wtc_complex)
[X] Tier 2: Building Level Validated (wtc1_tower_a, wtc2_tower_b; attribute: structure_type)
[X] Tier 3: Floor Level Validated (6 Anchor Elevations: -3.5m to +410.0m)
[X] Tier 4: Zone Level Validated (20 Core, Concourse, MER, Louver, Glazing Zones)
[X] Tier 5: Space Level Validated (General Rooms, Retail, Transit, Kitchens, Service, Corridors)
[X] Tier 6: Element Level Validated (Columns, Chillers, Elevators, Stairs, Louvers, Window Walls)
```

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 2 GOVERNANCE & LIFECYCLE RULES COMPLETE — READY FOR DATABASE SCHEMA SPECIFICATION
