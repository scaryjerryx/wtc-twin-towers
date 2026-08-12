# Phase 3 PostgreSQL PostGIS DDL Draft v1.0

**Document Status:** ✅ AUTHORITATIVE DDL DRAFT FOR REVIEW  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent Specifications:** [`docs/WORLD_MODEL_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/WORLD_MODEL_SPECIFICATION_V1.md), [`docs/LOGICAL_DATA_MODEL_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/LOGICAL_DATA_MODEL_V1.md), [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md), [`docs/PHASE_3_DDL_DESIGN_SPECIFICATION.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_DDL_DESIGN_SPECIFICATION.md), [`docs/PHASE_3_DDL_PRE_DRAFTING_AUDIT.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_DDL_PRE_DRAFTING_AUDIT.md)  
**Target Milestone:** PostgreSQL PostGIS DDL Draft Governing Executable SQL Migration File Authoring  

---

## Executive Summary

This document establishes the **authoritative PostgreSQL PostGIS DDL Draft v1.0** for the World Trade Center Reconstruction Project.

This is the first document in the project repository permitted to contain `CREATE TYPE`, `CREATE TABLE`, `ALTER TABLE`, foreign key constraint, CHECK constraint, and PostGIS geometry DDL statements.

This DDL draft implements 100% approved architecture from [`docs/SCHEMA_DESIGN_SPECIFICATION_V1.md`](file:///opt/wtc/wtc-twin-towers/docs/SCHEMA_DESIGN_SPECIFICATION_V1.md) and [`docs/PHASE_3_DDL_DESIGN_SPECIFICATION.md`](file:///opt/wtc/wtc-twin-towers/docs/PHASE_3_DDL_DESIGN_SPECIFICATION.md). Zero new entity types, zero new relationship types, zero new hierarchy exceptions, and zero web searches were created in this draft.

---

## 1. Verified Architecture Basis

```text
VERIFIED ARCHITECTURE BASIS:
• 6-Tier Spatial Containment Hierarchy: Site ──► Building ──► Floor ──► Zone ──► Space ──► Element.
• 15 Canonical Entity Category ENUMs & 10 Relationship ENUMs approved.
• 4 Critical Architecture Decisions:
  - Decision A.1: 2D Footprint (GEOMETRY(POLYGON, 2263)) + Numeric z_min/z_max Bounds (PA Datum feet).
  - Decision A.2: Dual EPSG:2263 NYC State Plane Feet + Local PA Datum Zero Grid (+310.0 ft PA).
  - Decision B.1: Hybrid Tree-Junction Multi-Floor Model (element_floor_junction).
  - Decision C.1: Normalized Epistemic Junction Table Model (entity_evidence_citations).
• 164 Verified Unique Entities & 82 Master Relationships cataloged on disk in data/*.json.
```

---

## 2. Complete DDL Implementation Specification

```sql
-- ============================================================================
-- WORLD TRADE CENTER RECONSTRUCTION PROJECT: POSTGRESQL POSTGIS DDL SCHEMA V1.0
-- ============================================================================

-- STEP 1: INITIALIZE POSTGIS SPATIAL EXTENSION
CREATE EXTENSION IF NOT EXISTS postgis;

-- STEP 2: CREATE CANONICAL ENUM TYPES

CREATE TYPE structure_type_enum AS ENUM (
    'high_rise_tower',
    'podium_building',
    'hotel_slab',
    'substation_base',
    'transit_terminal'
);

CREATE TYPE entity_category_enum AS ENUM (
    'site',
    'building',
    'floor',
    'zone',
    'space',
    'general_space',
    'retail_space',
    'transit_station',
    'kitchen_area',
    'service_area',
    'corridor',
    'structural_element',
    'mechanical_area',
    'mechanical_element',
    'architectural_element',
    'elevator_bank',
    'elevator',
    'stair',
    'escalator'
);

CREATE TYPE relationship_type_enum AS ENUM (
    'CONTAINS',
    'BOUNDED_BY',
    'ADJACENT_TO',
    'CONNECTS_TO',
    'PASSES_THROUGH',
    'OVERLOOKS',
    'ACCESSES',
    'LEADS_TO',
    'TRANSFERS_TO',
    'POWERED_BY',
    'COOLED_BY',
    'FEEDS_RISER_TO',
    'HOISTS_CAR_FOR',
    'SERVES'
);

CREATE TYPE evidence_classification_enum AS ENUM (
    'Direct Evidence',
    'Supported Inference',
    'Hypothesis'
);

CREATE TYPE lifecycle_state_enum AS ENUM (
    'DRAFT_SEED',
    'CORROBORATED',
    'VALIDATED',
    'DEPRECATED',
    'ARCHIVED'
);

CREATE TYPE temporal_era_enum AS ENUM (
    'CONSTRUCTION_ERA',
    'OPERATIONAL_ERA',
    'POST_1993_REPAIR_ERA'
);

-- STEP 3: CREATE CORE SPATIAL CONTAINMENT TREE TABLES

-- 1. TIER 1: SITES (Root Spatial Anchor)
CREATE TABLE sites (
    site_id VARCHAR(128) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    geometry_2d GEOMETRY(POLYGON, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL DEFAULT -70.00,
    z_max NUMERIC(8, 2) NOT NULL DEFAULT 1370.00,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_sites_z_bounds CHECK (z_min <= z_max)
);

-- 2. TIER 2: BUILDINGS (Structure Level)
CREATE TABLE buildings (
    building_id VARCHAR(128) PRIMARY KEY,
    site_id VARCHAR(128) NOT NULL REFERENCES sites(site_id) ON DELETE RESTRICT,
    name VARCHAR(255) NOT NULL,
    structure_type structure_type_enum NOT NULL,
    geometry_2d GEOMETRY(POLYGON, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL,
    z_max NUMERIC(8, 2) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_buildings_z_bounds CHECK (z_min <= z_max)
);

-- 3. TIER 3: FLOORS (Vertical Datums)
CREATE TABLE floors (
    floor_id VARCHAR(128) PRIMARY KEY,
    building_id VARCHAR(128) NOT NULL REFERENCES buildings(building_id) ON DELETE RESTRICT,
    floor_number INTEGER NOT NULL,
    floor_name VARCHAR(255) NOT NULL,
    elevation_pa_feet NUMERIC(8, 2) NOT NULL,
    height_feet NUMERIC(8, 2) NOT NULL DEFAULT 12.00,
    geometry_2d GEOMETRY(POLYGON, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL,
    z_max NUMERIC(8, 2) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_floors_z_bounds CHECK (z_min <= z_max)
);

-- 4. TIER 4: ZONES (Functional Floor Subdivisions)
CREATE TABLE zones (
    zone_id VARCHAR(128) PRIMARY KEY,
    floor_id VARCHAR(128) REFERENCES floors(floor_id) ON DELETE RESTRICT,
    building_id VARCHAR(128) REFERENCES buildings(building_id) ON DELETE RESTRICT,
    site_id VARCHAR(128) REFERENCES sites(site_id) ON DELETE RESTRICT,
    name VARCHAR(255) NOT NULL,
    zone_type entity_category_enum NOT NULL,
    geometry_2d GEOMETRY(POLYGON, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL,
    z_max NUMERIC(8, 2) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_zones_parent CHECK (floor_id IS NOT NULL OR building_id IS NOT NULL OR site_id IS NOT NULL),
    CONSTRAINT check_zones_z_bounds CHECK (z_min <= z_max)
);

-- 5. TIER 5: SPACES (Enclosed Room Volumes)
CREATE TABLE spaces (
    space_id VARCHAR(128) PRIMARY KEY,
    zone_id VARCHAR(128) REFERENCES zones(zone_id) ON DELETE RESTRICT,
    floor_id VARCHAR(128) REFERENCES floors(floor_id) ON DELETE RESTRICT,
    name VARCHAR(255) NOT NULL,
    space_category entity_category_enum NOT NULL,
    room_number VARCHAR(64),
    geometry_2d GEOMETRY(POLYGON, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL,
    z_max NUMERIC(8, 2) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_spaces_parent CHECK (zone_id IS NOT NULL OR floor_id IS NOT NULL),
    CONSTRAINT check_spaces_z_bounds CHECK (z_min <= z_max)
);

-- 6. TIER 6: ELEMENTS (Physical Components)
CREATE TABLE elements (
    element_id VARCHAR(128) PRIMARY KEY,
    space_id VARCHAR(128) REFERENCES spaces(space_id) ON DELETE RESTRICT,
    zone_id VARCHAR(128) REFERENCES zones(zone_id) ON DELETE RESTRICT,
    floor_id VARCHAR(128) REFERENCES floors(floor_id) ON DELETE RESTRICT,
    building_id VARCHAR(128) REFERENCES buildings(building_id) ON DELETE RESTRICT,
    name VARCHAR(255) NOT NULL,
    element_category entity_category_enum NOT NULL,
    is_multi_floor BOOLEAN NOT NULL DEFAULT FALSE,
    geometry_2d GEOMETRY(GEOMETRY, 2263) NOT NULL,
    z_min NUMERIC(8, 2) NOT NULL,
    z_max NUMERIC(8, 2) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_elements_parent CHECK (space_id IS NOT NULL OR zone_id IS NOT NULL OR floor_id IS NOT NULL OR building_id IS NOT NULL),
    CONSTRAINT check_elements_z_bounds CHECK (z_min <= z_max)
);

-- STEP 4: CREATE AUXILIARY JUNCTION & EPISTEMIC TABLES

-- 7. MASTER EVIDENCE SOURCES
CREATE TABLE sources (
    source_id VARCHAR(128) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_organization VARCHAR(255),
    publication_year INTEGER,
    archive_repository VARCHAR(255),
    file_path VARCHAR(512),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 8. EPISTEMIC EVIDENCE CITATIONS JUNCTION TABLE
CREATE TABLE entity_evidence_citations (
    citation_id VARCHAR(128) PRIMARY KEY,
    entity_id VARCHAR(128) NOT NULL,
    source_id VARCHAR(128) NOT NULL REFERENCES sources(source_id) ON DELETE RESTRICT,
    sheet_code VARCHAR(64) NOT NULL,
    evidence_classification evidence_classification_enum NOT NULL DEFAULT 'Direct Evidence',
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_entity_source_sheet UNIQUE (entity_id, source_id, sheet_code)
);

-- 9. MULTI-FLOOR PENETRATION JUNCTION TABLE
CREATE TABLE element_floor_junction (
    element_id VARCHAR(128) NOT NULL REFERENCES elements(element_id) ON DELETE RESTRICT,
    floor_id VARCHAR(128) NOT NULL REFERENCES floors(floor_id) ON DELETE RESTRICT,
    penetration_type VARCHAR(64) NOT NULL DEFAULT 'PASSES_THROUGH',
    has_landing BOOLEAN NOT NULL DEFAULT FALSE,
    has_machine_room BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (element_id, floor_id)
);

-- 10. CANONICAL ENTITY ALIAS MAPPING TABLE
CREATE TABLE entity_aliases (
    alias_id VARCHAR(128) PRIMARY KEY,
    entity_id VARCHAR(128) NOT NULL,
    raw_alias VARCHAR(255) NOT NULL,
    source_context VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_alias_entity UNIQUE (entity_id, raw_alias)
);

-- STEP 5: CREATE DIRECTED PROPERTY GRAPH TABLE

-- 11. DIRECTED RELATIONSHIPS GRAPH TABLE
CREATE TABLE relationships (
    relationship_id VARCHAR(128) PRIMARY KEY,
    subject_entity_id VARCHAR(128) NOT NULL,
    relationship_type relationship_type_enum NOT NULL,
    object_entity_id VARCHAR(128) NOT NULL,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    evidence_classification evidence_classification_enum NOT NULL DEFAULT 'Direct Evidence',
    valid_from DATE,
    valid_to DATE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_no_self_loops CHECK (subject_entity_id <> object_entity_id),
    CONSTRAINT unique_directed_edge UNIQUE (subject_entity_id, relationship_type, object_entity_id)
);

-- STEP 6: CREATE SPATIAL AND GRAPH INDICES

-- PostGIS 2D GiST Spatial Indices
CREATE INDEX idx_sites_spatial ON sites USING GIST (geometry_2d);
CREATE INDEX idx_buildings_spatial ON buildings USING GIST (geometry_2d);
CREATE INDEX idx_floors_spatial ON floors USING GIST (geometry_2d);
CREATE INDEX idx_zones_spatial ON zones USING GIST (geometry_2d);
CREATE INDEX idx_spaces_spatial ON spaces USING GIST (geometry_2d);
CREATE INDEX idx_elements_spatial ON elements USING GIST (geometry_2d);

-- Property Graph Forward & Reverse Composite Indices
CREATE INDEX idx_rel_forward ON relationships (subject_entity_id, relationship_type);
CREATE INDEX idx_rel_reverse ON relationships (object_entity_id, relationship_type);
```

---

## 3. Implementation Assumptions

1. **Database Platform Target:** PostgreSQL 14+ with PostGIS 3.0+ extension enabled.
2. **Coordinate Reference System:** All 2D geometries stored in NAD83 / New York Long Island State Plane Feet (`EPSG:2263`).
3. **Database Write Role:** Write permissions restricted to `wtc_writer` PostgreSQL role; public role set to `SELECT` read-only.
4. **Idempotency Strategy:** Future SQL migration runner will execute DDL inside explicit transactional blocks (`BEGIN; ... COMMIT;`).

---

## 4. Open Implementation Risks & Mitigation Controls

1. **Foreign Key Cascade Locking:**  
   - *Risk:* `ON DELETE RESTRICT` cascades on primary entity tables may lock large subtrees during bulk schema updates.
   - *Control:* Bulk ingestion will occur strictly top-down in `sites` ──► `elements` sequence.
2. **Spatial Projection Conversion Overhead:**  
   - *Risk:* Transforming `EPSG:2263` State Plane coordinates to `EPSG:4326` Lat/Long for browser mapping incur CPU overhead.
   - *Control:* WebGL API endpoints will serve pre-transformed local site grid coordinates centered at (0,0).

---

**Specification Approved:** August 12, 2026  
**Status:** ✅ PHASE 3 DDL DRAFT V1.0 FINALIZED — READY FOR REPOSITORY AUDIT & REVIEW
