# Phase 3 Entity Schema Design Specification

**Document Status:** ✅ AUTHORITATIVE ENTITY SCHEMA DESIGN SPECIFICATION  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md), [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md), [`docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_POSTGRESQL_SCHEMA_ROADMAP.md)  
**Target Milestone:** Logical-to-Physical Entity Mapping Specification Governing PostgreSQL DDL Creation  

---

## Executive Summary

This document establishes the **authoritative physical schema design specification** for the core World Model entities across the approved 6-Tier Spatial Containment Hierarchy (`Site` ──► `Building` ──► `Floor` ──► `Zone` ──► `Space` ──► `Element`).

This document defines the logical-to-physical mapping, primary keys, required attributes, parent ownership, integrity constraints, inheritance strategies, and multi-floor handling implications for each entity class.

Zero SQL DDL scripts, zero `CREATE TABLE` statements, zero database migrations, zero APIs, zero frontend models, and zero web searches were created in this specification.

---

## 1. Logical-to-Physical Mapping Overview

```text
6-TIER SPATIAL CONTAINMENT TREE MAPPING:
┌───────────────────┬─────────────────────────┬──────────────────────────────────┬────────────────────────────┐
│ Hierarchy Tier    │ Logical Entity Class    │ Physical Target Name             │ Primary Key Strategy       │
├───────────────────┼─────────────────────────┼──────────────────────────────────┼────────────────────────────┤
│ Tier 1: Site      │ Site                    │ sites                            │ Canonical String (site_id) │
│ Tier 2: Building  │ Building                │ buildings                        │ Canonical String (bldg_id) │
│ Tier 3: Floor     │ Floor                   │ floors                           │ Canonical String (flr_id)  │
│ Tier 4: Zone      │ Zone                    │ zones                            │ Canonical String (zone_id) │
│ Tier 5: Space     │ Space (Subtypes)        │ spaces                           │ Canonical String (spc_id)  │
│ Tier 6: Element   │ Element (Subtypes)      │ elements                         │ Canonical String (elm_id)  │
└───────────────────┴─────────────────────────┴──────────────────────────────────┴────────────────────────────┘
```

---

## 2. Physical Schema Design: `Site` (Tier 1 Root Anchor)

### 2.1 Entity Purpose & Definition
Represents the top-level 16-acre World Trade Center superblock site boundary, serving as the root parent anchor for all buildings, plaza spaces, and infrastructure networks.

### 2.2 Attribute Specifications
- **`site_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc_complex`).
- **`name` (Required):** Human-readable site title (`World Trade Center Complex`).
- **`description` (Optional):** Historical narrative or site boundary description.
- **`geometry_2d` (Required):** PostGIS 2D polygon footprint boundary in NAD83 / NYC State Plane Feet (`EPSG:2263`).
- **`z_min` (Required):** Minimum vertical elevation bound in feet relative to Port Authority Zero Datum (+310.0 ft PA). Default: `-70.0` (sub-grade B6 foundation bed).
- **`z_max` (Required):** Maximum vertical elevation bound in feet relative to Port Authority Zero Datum. Default: `+1370.0` (North Tower antenna tip).
- **`confidence_score` (Required):** Integer uncertainty score (`100`).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 2.3 Parent Ownership & Constraints
- **Parent Ownership:** Root node (no parent reference).
- **Constraints:** Primary key immutable; confidence score bounded strictly between `0` and `100`.

---

## 3. Physical Schema Design: `Building` (Tier 2 Structure Level)

### 3.1 Entity Purpose & Definition
Represents discrete primary building structures across the site, capturing high-rise towers, low-rise hotel slabs, concourses, and utility substations.

### 3.2 Attribute Specifications
- **`building_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc1_tower_a`, `wtc2_tower_b`, `wtc3_hotel`, `wtc7_building`).
- **`site_id` (Foreign Key / Required):** Foreign key reference to `sites.site_id`.
- **`name` (Required):** Official building title (`One World Trade Center - North Tower`).
- **`structure_type_enum` (Required):** ENUM attribute (`high_rise_tower`, `podium_building`, `hotel_slab`, `substation_base`, `transit_terminal`).
- **`geometry_2d` (Required):** PostGIS 2D polygon building footprint (`EPSG:2263`).
- **`z_min` / `z_max` (Required):** Building elevation range in PA Datum feet (e.g., `-70.0` to `+1368.0` for WTC 1).
- **`confidence_score` (Required):** Integer uncertainty score ($\ge 80$).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 3.3 Parent Ownership & Constraints
- **Parent Ownership:** Parented directly to `sites.site_id`.
- **Constraints:** Non-null `site_id` reference with `ON DELETE RESTRICT` cascade; non-null `structure_type_enum`.

---

## 4. Physical Schema Design: `Floor` (Tier 3 Vertical Datums)

### 4.1 Entity Purpose & Definition
Represents horizontal floor slab levels, sub-grade basements, and roof decks within a building structure.

### 4.2 Attribute Specifications
- **`floor_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc1_f1`, `wtc1_f7`, `wtc1_f75`, `wtc1_f78`, `wtc1_f107`, `wtc1_b1`).
- **`building_id` (Foreign Key / Required):** Foreign key reference to `buildings.building_id`.
- **`floor_number` (Required):** Integer floor index (`-1` for B1, `1` for Floor 1, `107` for Floor 107).
- **`floor_name` (Required):** Descriptive name (`78th Floor Sky Lobby Concourse`).
- **`elevation_pa_feet` (Required):** Datum elevation of finished floor slab in PA Datum feet relative to +310.0 ft PA zero datum (e.g. `0.0` for Floor 1, `+932.0` for Floor 78, `+1310.0` for Floor 107).
- **`height_feet` (Required):** Slab-to-slab floor height in feet (e.g. `12.0` ft for standard office floor, `36.0` ft for Sky Lobby).
- **`geometry_2d` (Required):** PostGIS 2D polygon floor footprint (`EPSG:2263`).
- **`z_min` / `z_max` (Required):** Floor slab vertical range (`elevation_pa_feet` to `elevation_pa_feet + height_feet`).
- **`confidence_score` (Required):** Integer uncertainty score ($\ge 80$).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 4.3 Parent Ownership & Constraints
- **Parent Ownership:** Parented directly to `buildings.building_id`.
- **Constraints:** Non-null `building_id` reference; non-null `elevation_pa_feet`.

---

## 5. Physical Schema Design: `Zone` (Tier 4 Functional Subdivisions)

### 4.1 Entity Purpose & Definition
Represents major functional subdivisions within a floor slab, such as elevator core zones, tenant areas, mechanical plants, service corridors, and glazing perimeters.

### 5.2 Attribute Specifications
- **`zone_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc1_f7_lower_mer_zone`, `wtc1_f78_sky_lobby_concourse_zone`).
- **`floor_id` (Foreign Key / Required):** Foreign key reference to `floors.floor_id`.
- **`building_id` (Foreign Key / Required):** Foreign key reference to `buildings.building_id`.
- **`name` (Required):** Zone name (`Floor 7 Lower Mechanical Plant Zone`).
- **`zone_type_enum` (Required):** ENUM attribute (`core_zone`, `tenant_zone`, `mechanical_zone`, `service_zone`, `concourse_zone`, `glazing_zone`).
- **`geometry_2d` (Required):** PostGIS 2D polygon zone boundary footprint (`EPSG:2263`).
- **`z_min` / `z_max` (Required):** Zone vertical elevation bounds in PA Datum feet.
- **`confidence_score` (Required):** Integer uncertainty score ($\ge 80$).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 5.3 Parent Ownership & Constraints
- **Parent Ownership:** Parented to `floors.floor_id` (or `buildings.building_id` for multi-floor zones).
- **Constraints:** Non-null parent reference; valid `zone_type_enum`.

---

## 6. Physical Schema Design: `Space` (Tier 5 Enclosed Room Volumes)

### 6.1 Entity Purpose & Definition
Represents discrete enclosed rooms, retail shops, transit concourses, kitchens, service areas, corridors, and restrooms.

### 6.2 Attribute Specifications
- **`space_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc1_f107_windows_on_the_world_main_dining_room`, `wtc1_f78_sky_lobby_west_concourse`).
- **`zone_id` (Foreign Key / Optional):** Foreign key reference to `zones.zone_id`.
- **`floor_id` (Foreign Key / Required):** Foreign key reference to `floors.floor_id`.
- **`name` (Required):** Official room/space title (`Windows on the World Main Dining Room`).
- **`space_category_enum` (Required):** ENUM attribute (`general_space`, `retail_space`, `transit_station`, `kitchen_area`, `service_area`, `corridor`).
- **`room_number` (Optional):** Architectural room code or number (e.g. `107-101`).
- **`geometry_2d` (Required):** PostGIS 2D polygon space footprint (`EPSG:2263`).
- **`z_min` / `z_max` (Required):** Space vertical elevation bounds in PA Datum feet.
- **`confidence_score` (Required):** Integer uncertainty score ($\ge 80$).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 6.3 Parent Ownership & Constraints
- **Parent Ownership:** Parented to `zones.zone_id` or `floors.floor_id`.
- **Constraints:** Non-null `floor_id` reference; valid `space_category_enum`.

---

## 7. Physical Schema Design: `Element` (Tier 6 Physical Components)

### 7.1 Entity Purpose & Definition
Represents physical structural columns, chillers, air handling units, elevators, escalators, stairwells, and window wall spandrels.

### 7.2 Attribute Specifications
- **`element_id` (Primary Key):** Canonical immutable string identifier (e.g. `wtc1_f7_chiller_1`, `wtc1_stair_a`, `wtc1_elevator_car_50`, `wtc1_col_501`).
- **`space_id` (Foreign Key / Optional):** Foreign key reference to `spaces.space_id` (for single-room elements).
- **`zone_id` (Foreign Key / Optional):** Foreign key reference to `zones.zone_id`.
- **`floor_id` (Foreign Key / Optional):** Foreign key reference to `floors.floor_id` (for single-floor elements).
- **`building_id` (Foreign Key / Required):** Foreign key reference to `buildings.building_id`.
- **`name` (Required):** Element title (`Core Box Column 501`, `Centrifugal Chiller 1`).
- **`element_category_enum` (Required):** ENUM attribute (`structural_element`, `mechanical_area`, `mechanical_element`, `architectural_element`, `elevator_bank`, `elevator`, `stair`, `escalator`).
- **`is_multi_floor` (Required):** Boolean flag indicating whether the element penetrates multiple floor slabs (`true` for Stairs, Elevators, Core Columns).
- **`geometry_2d` (Required):** PostGIS 2D polygon or point geometry (`EPSG:2263`).
- **`z_min` / `z_max` (Required):** Element vertical elevation range in PA Datum feet.
- **`confidence_score` (Required):** Integer uncertainty score ($\ge 80$).
- **`created_at` / `updated_at` (Required):** System timestamps.

### 7.3 Inheritance & Multi-Floor Handling Strategy
- **Inheritance Strategy:** Single-floor elements inherit parent spatial container keys (`space_id` / `floor_id`). Multi-floor elements set `space_id` and `floor_id` to NULL and parent directly to `building_id`.
- **Multi-Floor Handling Implications:** Elements with `is_multi_floor = true` link to physical `element_floor_junction` physical association records (`element_id`, `floor_id`, `penetration_type`, `has_landing`, `has_machine_room`), providing $O(1)$ SQL queries for floor-filtered element lookups.

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 ENTITY SCHEMA DESIGN SPECIFICATION COMPLETE — READY FOR TASK 3.3 JUNCTION & GRAPH SCHEMA DESIGN
