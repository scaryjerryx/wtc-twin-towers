# World Model Specification v1.0

**Document Status:** ✅ APPROVED AUTHORITATIVE SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Evaluated Datasets:** [`data/wtc1_world_model_v1.json`](file:///opt/wtc/wtc-twin-towers/data/wtc1_world_model_v1.json), [`data/tower_b_world_model_validated.json`](file:///opt/wtc/wtc-twin-towers/data/tower_b_world_model_validated.json), [`data/aa18_world_model_seed.json`](file:///opt/wtc/wtc-twin-towers/data/aa18_world_model_seed.json)  

---

## Executive Summary

This document establishes the **authoritative World Model Specification v1.0** for the World Trade Center Reconstruction Project.

Zero SQL DDL scripts, zero database migrations, zero table creation statements, and zero web searches were created in this specification.

This document defines the formal ontology, canonical 6-tier spatial containment tree, 15 entity category types, 10 relationship types, multi-floor entity handling rules, evidence linkage protocols, confidence scoring constraints, and architectural rules that **all future PostgreSQL database schema designs and data ingestion pipelines MUST follow**.

---

## 1. Canonical Entity Hierarchy (The 6-Tier Spatial Containment Tree)

The World Model physical containment structure is defined by a strict 6-tier hierarchical tree:

```text
Tier 1: Site (WTC Complex / Plaza Area)
  └── Tier 2: Building (WTC 1, WTC 2, WTC 3-7, PATH Terminal)
       └── Tier 3: Floor (Sub-Grade B6 to Floor 110 / Roof)
            └── Tier 4: Zone (Core, Concourse, MER, Louver, Glazing Envelope)
                 └── Tier 5: Space (Enclosed Rooms, Retail Stores, Transit Halls)
                      └── Tier 6: Element (Columns, Chillers, Elevators, Stairs)
```

### Hierarchy Level Specifications:

1. **`Site` (Tier 1):** The root spatial container representing the entire 16-acre World Trade Center complex property (`wtc_complex`).
2. **`Building` (Tier 2):** Primary physical structure containers (WTC 1 North Tower, WTC 2 South Tower, WTC 3 Marriott Hotel, WTC 4–7, Sub-grade PATH Terminal). Includes attribute `structure_type` (`high_rise_tower`, `podium_building`, `hotel_slab`, `substation_base`, `transit_terminal`).
3. **`Floor` (Tier 3):** Horizontal elevation datums (Sub-Levels B1–B6, Floor 1, Floor 7 MER, Floor 75 MER, Floor 78 Sky Lobby, Floor 107 Apex Suite).
4. **`Zone` (Tier 4):** Functional subdivisions of a floor level (Core Zone, Concourse Zone, Chiller Zone, AHU Fan Zone, Facade Glazing Envelope Zone, Slurry Wall Envelope Zone).
5. **`Space` (Tier 5):** Discrete enclosed room volumes, retail arcades, transit platform halls, dining rooms, kitchens, service areas, and corridors.
6. **`Element` (Tier 6):** Discrete physical structural columns, centrifugal chillers, 13.8kV electrical transformers, stairwells, elevator cars/shafts, escalators, window walls, and mechanical air louvers.

---

## 2. Canonical Entity Categories (The 15 Entity Type ENUMs)

All entities in the World Model MUST be classified into one of the following 15 canonical category types:

| Category ENUM | Hierarchy Level | Functional Description | Example Entities |
|---|---|---|---|
| **`site`** | Tier 1 | Entire 16-acre WTC Complex property | `wtc_complex` |
| **`building`** | Tier 2 | Major building structure container | `wtc1_tower_a`, `wtc2_tower_b` |
| **`floor`** | Tier 3 | Horizontal vertical elevation level | `wtc1_floor_b1`, `wtc1_floor_1`, `wtc1_floor_107` |
| **`zone`** | Tier 4 | Functional floor subdivision | `wtc1_f7_primary_hvac_chiller_zone` |
| **`space`** | Tier 5 | General public or operational room volume | `wtc1_f107_windows_on_the_world_main_dining_room` |
| **`retail_space`** | Tier 5 | Sub-grade concourse retail store / bank | `wtc1_fb1_north_retail_arcade_galleria` |
| **`transit_station`** | Tier 5 | Commuter rail platform / subway connector | `wtc1_fb1_path_terminal_turnstile_concourse` |
| **`kitchen_area`** | Tier 5 | Commercial culinary kitchen / bakery suite | `wtc1_f107_main_commercial_kitchen_complex` |
| **`service_area`** | Tier 5 | Operations room, SCADA office, loading dock | `wtc1_fb1_truck_loading_ramp_and_dock` |
| **`corridor`** | Tier 5 | Passenger concourse hall or catwalk chase | `wtc1_f78_sky_lobby_passenger_transit_lounge` |
| **`structural_element`** | Tier 6 | Columns, trusses, spandrels, decks | `wtc1_core_box_columns_501_1008`, `wtc1_perimeter_box_columns` |
| **`mechanical_area`** | Tier 6 | Chiller vaults, 13.8kV substations, EMRs | `wtc1_f7_central_chiller_plant_room` |
| **`mechanical_element`** | Tier 6 | Facade mechanical air louvers | `wtc1_f7_perimeter_mechanical_louver_grilles` |
| **`architectural_element`** | Tier 6 | Panoramic facade glass window wall | `wtc1_f107_floor_to_ceiling_window_wall_glazing` |
| **`elevator_bank`** | Tier 6 | Elevator shaft bank group (Express / Local) | `wtc1_express_shuttle_bank_78` |
| **`elevator`** | Tier 6 | Heavy freight & primary service cars | `wtc1_heavy_freight_elevator_50`, `wtc1_service_elevator_49` |
| **`stair`** | Tier 6 | Emergency egress stairwells A/B/C | `wtc1_stair_a`, `wtc1_stair_b`, `wtc1_stair_c` |
| **`escalator`** | Tier 6 | Monumental escalators & PATH escalators | `wtc1_f78_sky_lobby_monumental_escalators` |

---

## 3. Canonical Relationship Categories (The 10 Relationship Type ENUMs)

Relationships between entities MUST be classified into one of 10 canonical relationship ENUMs:

### 3.1 Spatial Containment & Adjacency Relationships
- **`CONTAINS`**: Parent-to-child physical spatial inclusion (e.g., `Floor CONTAINS Zone`, `Zone CONTAINS Space`).
- **`BOUNDED_BY`**: Space or zone bounded by perimeter structural walls or glazing envelopes.
- **`ADJACENT_TO`**: Horizontal spatial adjacency on the same floor elevation.
- **`CONNECTS_TO`**: Horizontal door or passage connectivity between spaces.
- **`PASSES_THROUGH`**: Multi-floor vertical column, elevator shaft, or stairwell penetration across floor slabs.

### 3.2 Visual & Pedestrian Flow Relationships
- **`OVERLOOKS`**: Visual sightline from a space/dining room to an architectural window wall or plaza.
- **`ACCESSES`**: Pedestrian access path from an elevator reception foyer to rooms/concourses.
- **`LEADS_TO`**: Direct passage flow connecting pedestrian tunnels to turnstiles and store arcades.
- **`TRANSFERS_TO`**: Passenger transfer connection between express shuttle elevators, escalators, and local elevator banks.

### 3.3 Engineering System Dependency Relationships
- **`POWERED_BY`**: Electrical substation or transformer vault powering chillers, AHU fans, water pumps, or elevator hoists.
- **`COOLED_BY`**: Chilled water plant or facade louvers supplying cooling to AHU supply fans.
- **`FEEDS_RISER_TO`**: MER plant feeding chilled water or air supply risers to upper floors and sky lobbies.
- **`HOISTS_CAR_FOR`**: Elevator machine room traction hoist machinery powering specific elevator cars.
- **`SERVES`**: Utility area, kitchen, or equipment serving a building, floor, or specific space.

---

## 4. Multi-Floor Entity Handling Rules

To prevent breaking single-parent tree constraints in database designs:

```text
MULTIPLE-FLOOR VERTICAL SYSTEM ENTITY RULE:
Primary Physical Parent: Building (wtc1_tower_a)
Secondary Graph Links  : Floor 1  ──(PASSES_THROUGH)──► Vertical Entity (wtc1_stair_a)
                         Floor 7  ──(PASSES_THROUGH)──► Vertical Entity (wtc1_stair_a)
                         Floor 75 ──(PASSES_THROUGH)──► Vertical Entity (wtc1_stair_a)
                         Floor 78 ──(PASSES_THROUGH)──► Vertical Entity (wtc1_stair_a)
                         Floor 107──(PASSES_THROUGH)──► Vertical Entity (wtc1_stair_a)
```

1. **Primary Physical Parent:** Multi-floor vertical entities (Stairs A/B/C, Freight Elevator 50, Service Elevator 49, Core Box Columns 501–1008, Perimeter Box Columns, Slurry Wall Foundation) MUST set `building_id` or `site_id` as their primary tree parent.
2. **Relational Graph Penetrations:** Floor-by-floor door landings, shaft penetrations, or column nodes MUST connect to specific `floor_id` records via `PASSES_THROUGH`, `SERVES`, or `LANDS_AT` graph links.
3. **Immutable Canonical IDs:** Multi-floor entities MUST assign stable, cross-floor canonical IDs (e.g. `wtc1_stair_a`, `wtc1_heavy_freight_elevator_50`, `wtc1_core_box_columns_501_1008`).

---

## 5. Evidence Linkage Requirements

In compliance with **Principle 2 (*Cite Sources*)** and **Principle 3 (*Separate Evidence From Inference*)**:

1. **Mandatory Evidence Citation:** Every entity and relationship record MUST store:
   - `evidence_source`: Specific blueprint drawing sheet code (e.g., `A-A-19`, `A-A-20`, `ST-01`).
   - `evidence_classification`: Epistemic classification (`Direct Evidence`, `Supported Inference`, `Hypothesis`).
2. **Corroboration Tracking:** Entities supported by multiple blueprint drawings MUST store an array of source sheets (`evidence_sources`: `["A-A-19", "A-A-20", "A-A-31"]`) and a `corroboration_count` integer.

---

## 6. Confidence Score Requirements

In compliance with **Principle 5 (*Quantify Uncertainty*)**:

1. **Confidence Scale:** Numerical integer score from `0` to `100`.
2. **`95–100%` (Direct Evidence):** Explicitly drawn, labeled, and dimensioned on primary Yamasaki contract drawings or Emery Roth architectural plans.
3. **`80–94%` (Supported Inference):** Structurally or engineering-deduced elements backed by code standards or adjacent sheet corroboration.
4. **`<80%` (Unverified Hypothesis):** Requires mandatory disclaimer; **STRICTLY FORBIDDEN from automated database table ingestion**.

---

## 7. Mandatory Constraints for Database Design

Future PostgreSQL database DDL formulations and ingestion scripts MUST enforce:

1. **Immutable Primary Keys:** Entity IDs MUST be human-readable, deterministic string keys (e.g., `wtc1_f107_windows_on_the_world_main_dining_room`).
2. **Strict Foreign Key Integrity:** All parent-child tree links MUST enforce referential integrity (`parent_entity_id REFERENCES entities(entity_id)`).
3. **Non-Null Epistemic Metadata:** No entity or relationship record may be inserted with NULL values for `evidence_classification`, `confidence_score`, or `evidence_sources`.
4. **No Invention of Evidence (Principle 1):** Unproven speculative room geometry or non-blueprint entities must never be inserted into production tables.
5. **No Unverified Symmetry Assumptions (Principle 7):** Tower B (WTC 2) entities must never be copied from Tower A (WTC 1) without explicit Tower B blueprint evidence.

---

**Specification Finalized:** August 12, 2026  
**Status:** ✅ AUTHORITATIVE WORLD MODEL SPECIFICATION V1.0 APPROVED — READY FOR POSTGRESQL DESIGN
