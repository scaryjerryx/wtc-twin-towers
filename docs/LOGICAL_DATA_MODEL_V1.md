# Logical Data Model v1.0

**Document Status:** ✅ AUTHORITATIVE LOGICAL DATA MODEL  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_GOVERNANCE_AND_LIFECYCLE_RULES.md), [`docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_2_CRITICAL_ARCHITECTURE_DECISIONS.md)  
**Target Milestone:** Authoritative Logical Data Model Bridging World Model Specification and Future PostgreSQL Schema Design  

---

## Executive Summary

This document establishes the **authoritative Logical Data Model v1.0** for the World Trade Center Reconstruction Project.

This document is strictly conceptual, implementation-independent, and database-independent. Zero SQL DDL scripts, zero PostgreSQL schema definitions, zero physical table creations, zero foreign key constraints, zero database indexes, zero API designs, zero frontend models, and zero web searches were created in this specification.

This Logical Data Model defines the conceptual entities, entity families, identity models, spatial representation models, logical cardinality rules, multi-floor handling models, evidence citation structures, confidence scoring mechanisms, lifecycle states, temporal state models, directed graph relationships, and data ownership boundaries that **all future PostgreSQL DDL schema designs MUST implement**.

---

## Partitioning of Facts, Decisions, and Future Considerations

```text
┌────────────────────────────────────────────────────────────────────────┐
│ VERIFIED FACTS (Physical Data Saved on Disk in data/*.json & docs/*.md)│
├────────────────────────────────────────────────────────────────────────┤
│ • 164 Verified Unique Entities & 82 Master Relationships cataloged     │
│ • Approved 6-Tier Spatial Containment Hierarchy                       │
│ • Approved Specification v1.0 & Governance Rules                       │
│ • 4 Critical Architecture Decisions (A.1, A.2, B.1, C.1) Approved      │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ ARCHITECTURAL DECISIONS (Approved Logical Model Abstractions)          │
├────────────────────────────────────────────────────────────────────────┤
│ • 5 Core Entity Families & 15 ENUM Types                               │
│ • 2D Plan Footprint + Numeric Z-Elevation Bounds (Option A.1.2)        │
│ • Dual EPSG:2263 NYC State Plane + PA Datum Grid (Option A.2.2)        │
│ • Hybrid Tree-Junction Multi-Floor Model (Option B.1.2)                │
│ • Normalized Epistemic Junction Model (Option C.1.2)                   │
│ • Historical Era Classifications (Construction, Operational, Repair)   │
└────────────────────────────────────────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│ FUTURE IMPLEMENTATION CONSIDERATIONS (Phase 3 DDL Deliverables)        │
├────────────────────────────────────────────────────────────────────────┤
│ • Physical PostgreSQL PostGIS DDL table creation DDL (`CREATE TABLE`)   │
│ • Foreign key constraint indices and SQL trigger formulations          │
│ • Automated Python seed data loading and upsert execution              │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Core Entity Families

The Logical Data Model organizes all 15 canonical entity types into 5 functional Entity Families:

```text
┌────────────────────────────────────────────────────────────────────────┐
│ FAMILY 1: ROOT & STRUCTURE FAMILY  (Site, Building)                    │
├────────────────────────────────────────────────────────────────────────┤
│ FAMILY 2: SPATIAL HIERARCHY FAMILY (Floor, Zone, Space, Subtypes)      │
├────────────────────────────────────────────────────────────────────────┤
│ FAMILY 3: PHYSICAL ELEMENT FAMILY  (Structural, MEP, Escalator, etc.)  │
├────────────────────────────────────────────────────────────────────────┤
│ FAMILY 4: EPISTEMIC & CITATION FAMILY (Source, EvidenceCitation)       │
├────────────────────────────────────────────────────────────────────────┤
│ FAMILY 5: RELATIONAL GRAPH FAMILY  (RelationshipLink)                  │
└────────────────────────────────────────────────────────────────────────┘
```

### 1.1 Entity Family Definitions:

1. **Root & Structure Family:**  
   - *Entities:* `Site`, `Building` (with `structure_type` attribute: `high_rise_tower`, `podium_building`, `hotel_slab`, `substation_base`, `transit_terminal`).
   - *Purpose:* Anchors the top two physical levels of the spatial tree.
   - *Rationale:* Consolidates `Building` and `Tower` into a single entity class, eliminating depth redundancy while preserving structural classification.
   - *Constraints:* Must exist before any child floor, zone, or element can be instantiated.

2. **Spatial Hierarchy Family:**  
   - *Entities:* `Floor`, `Zone`, `Space` (subtypes: `general_space`, `retail_space`, `transit_station`, `kitchen_area`, `service_area`, `corridor`).
   - *Purpose:* Defines horizontal floor levels, functional floor subdivisions, and enclosed room volumes.
   - *Rationale:* Captures the architectural layout of lobbies, tenant offices, shopping concourses, and observation decks.
   - *Constraints:* Every space must be parented to exactly one `Zone` or `Floor`.

3. **Physical Element Family:**  
   - *Entities:* `Element` (subtypes: `structural_element`, `mechanical_area`, `mechanical_element`, `architectural_element`, `elevator_bank`, `elevator`, `stair`, `escalator`).
   - *Purpose:* Represents physical structural, mechanical, electrical, and transport components.
   - *Rationale:* Provides discrete physical objects for structural analysis, HVAC systems, and vertical circulation.
   - *Constraints:* Single-floor elements parent to `Zone`/`Floor`; multi-floor elements parent to `Building`.

4. **Epistemic & Citation Family:**  
   - *Entities:* `EvidenceSource`, `EvidenceCitation`.
   - *Purpose:* Stores source drawing metadata and links entities to supporting historical evidence.
   - *Rationale:* Guarantees 100% traceability for every entity (Principle 2: *Cite Sources*).
   - *Constraints:* Non-null citation required for every production entity (`confidence_score >= 80`).

5. **Relational Graph Family:**  
   - *Entities:* `RelationshipLink`.
   - *Purpose:* Stores directed graph edges between entities (`CONTAINS`, `POWERED_BY`, `TRANSFERS_TO`, etc.).
   - *Rationale:* Separates non-tree engineering dependencies and visual sightlines from spatial containment.
   - *Constraints:* Both subject and object entities must exist; link must be directed.

---

## 2. Entity Identity Model

### 2.1 Canonical Entity Identity & Naming Conventions
- **Human-Readable Canonical Identifiers:** Every entity in the World Model MUST possess a globally unique, human-readable canonical identifier (e.g. `wtc1_f107_windows_on_the_world_main_dining_room`, `wtc1_f7_chiller_1`).
- **Hierarchical Identity Formatting:** Entity IDs follow deterministic structural prefixes:
  - Complex Root: `wtc_complex`
  - Buildings: `wtc1_tower_a`, `wtc2_tower_b`, `wtc3_hotel`, `wtc7_building`
  - Floors: `wtc1_f1`, `wtc1_f7`, `wtc1_f75`, `wtc1_f78`, `wtc1_f107`, `wtc1_b1`
  - Spaces/Elements: `wtc1_f107_[space_name]`, `wtc1_f7_[element_name]`

### 2.2 Immutability & Persistence Principles
- **Identifier Permanence:** Once assigned, an entity identifier is immutable and MUST NOT be renamed, reassigned, or recycled across the entity's entire lifecycle.
- **Cross-State Persistence:** An entity retains its identical canonical key as it transitions across lifecycle states (`DRAFT_SEED` ──► `CORROBORATED` ──► `VALIDATED` ──► `DEPRECATED` ──► `ARCHIVED`).

### 2.3 Alias Handling Principles
- **Alias Mapping Concept:** Historical blueprints, engineering reports, and tenant directories often refer to the same physical entity by different names (e.g. "Elevator Shaft 50" vs "Car 50" vs "Freight Elevator 50").
- **Resolution Boundary:** The Logical Data Model decouples raw historical names from canonical IDs via a conceptual entity alias mapping model, ensuring alternative names resolve deterministically to a single canonical entity.

### 2.4 Identity Ownership Rules
- **World Model Ownership:** Canonical entity IDs are generated and owned exclusively by the World Model core asset tier.
- **Subsystem Immutability:** External producers (Evidence Engine) and consumers (Reconstruction Platform) MUST reference canonical entity IDs without mutating identity definitions.

---

## 3. Spatial Representation Model

### 3.1 Approved 2D Footprint & Height Bounds Strategy (Decision A.1)
- **Conceptual Strategy:** Horizontally, spatial volumes (zones, spaces, elements) are represented as 2D polygonal footprints, paired with explicit numeric vertical elevation bounds (`z_min`, `z_max`).
- **Elevation Datum Baseline:** Vertical bounds `z_min` and `z_max` are measured in feet relative to the Port Authority zero datum (+310.0 ft PA = 0.0 ft elevation).
- **Extrusion Model:** 3D volumetric enclosures are derived logically by extruding the 2D polygon footprint vertically from `z_min` to `z_max`.

### 3.2 Approved Coordinate Reference Systems (Decision A.2)
- **Dual-Grid Alignment Standard:**
  1. **Regional GIS Standard:** Primary real-world coordinates align with NAD83 / New York Long Island State Plane Feet (`EPSG:2263`) for regional positioning.
  2. **Local Site Grid Standard:** Local spatial coordinates align to the Port Authority Site Grid (Origin (0,0) set to North Tower Centerpoint, 0.0 ft elevation set to +310.0 ft PA datum).

### 3.3 Spatial Ownership & Containment Boundaries
- **Parent Polygon Enclosure:** Every child spatial footprint MUST be logically enclosed within the 2D polygonal footprint boundary of its parent spatial container.
- **Multi-Floor Spatial Representation:** Multi-floor vertical entities (Stairs A/B/C, Elevator Shafts, Core Box Columns) span a continuous Z-elevation range $[z_{\text{min\_base}}, z_{\text{max\_apex}}]$, maintaining spatial boundary intersection across every intermediate floor slab elevation.

---

## 4. Logical Cardinality Rules

The Logical Data Model defines conceptual cardinality expectations between entity families without specifying physical database constraints or foreign key mechanisms:

```text
LOGICAL CARDINALITY EXPECTATIONS:
┌───────────────────────────────────────┬────────────────────────────────┐
│ Relationship Type                     │ Conceptual Cardinality Ratio   │
├───────────────────────────────────────┼────────────────────────────────┤
│ Site ──► Buildings                    │ One-to-Many  (1 : N)           │
│ Building ──► Floors                   │ One-to-Many  (1 : N)           │
│ Floor ──► Zones                       │ One-to-Many  (1 : N)           │
│ Zone ──► Spaces                       │ One-to-Many  (1 : N)           │
│ Space ──► Elements                    │ One-to-Many  (1 : N)           │
│ Entity ──► Evidence Citations         │ One-to-Many  (1 : N)           │
│ Evidence Source ──► Evidence Citations│ One-to-Many  (1 : N)           │
│ Entity ──► Directed Graph Links       │ Many-to-Many (N : M)           │
│ Multi-Floor Element ──► Floor Slabs   │ One-to-Many  (1 : N)           │
└───────────────────────────────────────┴────────────────────────────────┘
```

1. **Tree Containment Cardinalities:**  
   - A `Site` contains one or more `Buildings` ($1 : N$).
   - A `Building` contains one or more `Floors` ($1 : N$).
   - A `Floor` contains one or more `Zones` ($1 : N$).
   - A `Zone` contains zero, one, or many `Spaces` ($1 : N$).
   - A `Space` contains zero, one, or many `Elements` ($1 : N$).
2. **Epistemic Citation Cardinalities:**  
   - An `Entity` can be supported by one or many `EvidenceCitations` ($1 : N$).
   - An `EvidenceSource` can provide citations for one or many `Entities` ($1 : N$).
3. **Graph Link & Multi-Floor Cardinalities:**  
   - Entities form arbitrary directed graph networks ($N : M$).
   - A multi-floor element penetrates one or many intermediate floor slabs ($1 : N$).

---

## 5. Parent-Child Containment Rules

- **Single-Parent Rule:** In the strict 6-tier spatial tree (`Site` ──► `Building` ──► `Floor` ──► `Zone` ──► `Space` ──► `Element`), an entity MUST have exactly ONE primary tree parent identifier.
- **Bounding Enclosure Constraint:** Every child spatial entity MUST be geometrically contained within the 2D footprint bounding polygon of its parent entity.
- **Root Escalation Rule:** Entities that naturally exist outside a building envelope (e.g. Austin J. Tobin Plaza concourses) escalation-parent directly to `Site`.

---

## 6. Multi-Floor Entity Handling Rules

In accordance with Approved Decision B.1:

```text
PRIMARY PHYSICAL PARENT : Building (wtc1_tower_a)
PHYSICAL JUNCTION MODEL : Element-Floor Penetration Association (Element + Floor + Penetration Type)
DIRECTED GRAPH LINKS    : Floor 75 ──(PASSES_THROUGH)──► wtc1_stair_a
```

1. **Primary Tree Parenting:** Multi-floor vertical entities (Stairs A/B/C, Freight Elevator 50, Core Box Columns 501–1008, Perimeter Box Columns, Slurry Wall Foundation) set `Building` or `Site` as their primary tree parent.
2. **Physical Floor Association:** Floor-by-floor penetrations maintain a logical element-floor penetration association capturing element identity, floor identity, penetration type, door landings, and machine room locations.
3. **Graph Dependency Links:** Vertical floor traversals, door landings, and riser connections connect to individual floor records via `PASSES_THROUGH`, `SERVES`, or `LANDS_AT` graph links.
4. **Immutable Identity:** Multi-floor entities maintain permanent, cross-floor canonical string keys (e.g. `wtc1_stair_a`).

---

## 7. Evidence Linkage Model

In accordance with Approved Decision C.1:

```text
ENTITY (wtc1_f107_main_dining_room)
   └── EVIDENCE CITATION RECORD (Epistemic Association)
          ├── Source Identifier : source_yamasaki_blueprints
          ├── Drawing Sheet Code: A-A-145
          ├── Classification    : Direct Evidence
          └── Confidence Rating : 95% Verified
```

1. **Normalized Citation Model:** Evidence citations are modeled via a dedicated `EvidenceCitation` entity family linking `Entity` to `EvidenceSource`.
2. **Mandatory Epistemic Attributes:** Every citation record MUST store entity reference, source reference, drawing sheet code (e.g. `A-A-145`), evidence classification (`Direct Evidence`, `Supported Inference`, or `Hypothesis`), and confidence score (0 to 100).
3. **Multi-Source Corroboration:** Entities supported by multiple drawings link to multiple `EvidenceCitation` records, generating an automated corroboration count.

---

## 8. Confidence Score Model

In compliance with **Principle 5 (*Quantify Uncertainty*)**:

- **Numerical Integer Scale:** `0` to `100`.
- **`95–100%` (Direct Evidence):** Derived directly from primary contract blueprints (Yamasaki & Associates / Emery Roth & Sons).
- **`80–94%` (Supported Inference):** Structurally or engineering-deduced elements backed by code standards or adjacent sheet corroboration.
- **`<80%` (Unverified Hypothesis):** **STRICTLY FORBIDDEN from production seed consolidation and database ingestion**.

---

## 9. Lifecycle State Model

Entities transition through 5 governance states:

```text
DRAFT_SEED ──► CORROBORATED ──► VALIDATED ──► DEPRECATED ──► ARCHIVED
```

1. **`DRAFT_SEED`:** Initial extraction from a single blueprint sheet (corroboration count = 1, confidence score = 95).
2. **`CORROBORATED`:** Entity verified across 2+ distinct blueprint sheets (corroboration count >= 2).
3. **`VALIDATED`:** Cross-checked against structural vectors or vertical anchor elevations. Approved for production.
4. **`DEPRECATED`:** Superseded by a higher-resolution drawing or merged canonical ID. Retained with deprecated flag.
5. **`ARCHIVED`:** Read-only historical record retained for audit trails.

---

## 10. Temporal State Model

> **ARCHITECTURAL DECISION / LOGICAL MODEL PROPOSAL:**  
> The temporal state model and historical era classifications defined below represent an approved Phase 2 logical model proposal designed to support future time-aware digital twin capabilities.

To support the long-term vision of a **living, time-aware historical reconstruction** (1966 construction to 2001 operational):

1. **Temporal Validity Bounds:** All entities and relationships support optional temporal attributes:
   - `valid_from`: Historical timestamp when the physical element was constructed/installed (e.g., `1972-04-01`).
   - `valid_to`: Historical timestamp when the physical element was altered, replaced, or destroyed (e.g., `2001-09-11`).
2. **Historical Era Classifications (ARCHITECTURAL DECISION):**
   - `CONSTRUCTION_ERA` (1966–1973): Steel erection, slurry wall excavation, facade installation.
   - `OPERATIONAL_ERA` (1973–2001): Completed twin towers, tenant fit-outs, Windows on the World, Observatory.
   - `POST_1993_REPAIR_ERA` (1993–2001): Sub-grade repairs and security upgrades following 1993 bombing.

---

## 11. Relationship Graph Model

Relationships are modeled as a directed property graph:

$$\text{Subject Entity} \xrightarrow{\quad\text{Relationship ENUM}\quad} \text{Object Entity}$$

- **10 Approved Relationship ENUMs:** `CONTAINS`, `BOUNDED_BY`, `ADJACENT_TO`, `CONNECTS_TO`, `PASSES_THROUGH`, `OVERLOOKS`, `ACCESSES`, `LEADS_TO`, `TRANSFERS_TO`, `POWERED_BY`, `COOLED_BY`, `FEEDS_RISER_TO`, `HOISTS_CAR_FOR`, `SERVES`.
- **Graph Traversal Constraints:** Graph traversals MUST support multi-hop path queries for MEP engineering systems and vertical elevator/stairwell circulation.

---

## 12. Data Ownership Boundaries

```text
┌────────────────────────┐       ┌────────────────────────┐       ┌────────────────────────┐
│    EVIDENCE ENGINE     │ ───►  │      WORLD MODEL       │ ───►  │ RECONSTRUCTION PLATFORM│
│  (Producer Subsystem)  │       │ (Core Asset Container) │       │  (Consumer Subsystem)  │
└────────────────────────┘       └────────────────────────┘       └────────────────────────┘
```

1. **Evidence Engine (Producer):** Discovers, acquires, hashes, OCRs, and extracts evidence. Does NOT own the World Model ontology.
2. **World Model (Core Asset Container):** Owns the authoritative spatial containment tree, canonical entity IDs, entity families, confidence scores, and relationship graph.
3. **Reconstruction Platform (Consumer):** Reads World Model data via API for browser-based WebGL 3D rendering and historical walkthroughs. Does NOT mutate World Model state.

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ LOGICAL DATA MODEL V1.0 REVISED & FINALIZED — AUTHORITATIVE CONCEPTUAL SPECIFICATION FOR PHASE 3 DDL DESIGN
