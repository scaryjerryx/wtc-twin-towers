-- ============================================================================
-- WORLD TRADE CENTER RECONSTRUCTION PROJECT: POSTGRESQL POSTGIS MIGRATION V1.1
-- Migration File: database/migrations/V1_1__create_world_model_schema_revised.sql
-- Description: Revised executable DDL incorporating Master Entity Registry (entities),
--              declarative foreign keys, refined single-parent CHECK constraints, and temporal_era attributes.
-- Author: Research Lead
-- Date: August 12, 2026
-- Governing Specification: docs/V1_1_MIGRATION_REVISION_PLAN.md
-- ============================================================================

BEGIN;

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

-- STEP 3: CREATE MASTER ENTITY REGISTRY TABLE

CREATE TABLE entities (
    entity_id VARCHAR(128) PRIMARY KEY,
    entity_category entity_category_enum NOT NULL,
    building_id VARCHAR(128),
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    lifecycle_state lifecycle_state_enum NOT NULL DEFAULT 'VALIDATED',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- STEP 4: CREATE CORE SPATIAL CONTAINMENT TREE TABLES

-- 1. TIER 1: SITES (Root Spatial Anchor)
CREATE TABLE sites (
    site_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    building_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    floor_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    zone_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    CONSTRAINT check_zones_single_parent CHECK (
        ((floor_id IS NOT NULL)::int + (building_id IS NOT NULL)::int + (site_id IS NOT NULL)::int) = 1
    ),
    CONSTRAINT check_zones_z_bounds CHECK (z_min <= z_max)
);

-- 5. TIER 5: SPACES (Enclosed Room Volumes)
CREATE TABLE spaces (
    space_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    CONSTRAINT check_spaces_single_parent CHECK (
        ((zone_id IS NOT NULL)::int + (floor_id IS NOT NULL)::int) = 1
    ),
    CONSTRAINT check_spaces_z_bounds CHECK (z_min <= z_max)
);

-- 6. TIER 6: ELEMENTS (Physical Components)
CREATE TABLE elements (
    element_id VARCHAR(128) PRIMARY KEY REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    temporal_era temporal_era_enum DEFAULT 'OPERATIONAL_ERA',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_elements_single_parent CHECK (
        ((space_id IS NOT NULL)::int + (zone_id IS NOT NULL)::int + (floor_id IS NOT NULL)::int + (building_id IS NOT NULL)::int) = 1
    ),
    CONSTRAINT check_elements_z_bounds CHECK (z_min <= z_max)
);

-- STEP 5: CREATE AUXILIARY JUNCTION & EPISTEMIC TABLES

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
    entity_id VARCHAR(128) NOT NULL REFERENCES entities(entity_id) ON DELETE RESTRICT,
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
    entity_id VARCHAR(128) NOT NULL REFERENCES entities(entity_id) ON DELETE RESTRICT,
    raw_alias VARCHAR(255) NOT NULL,
    source_context VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_alias_entity UNIQUE (entity_id, raw_alias)
);

-- STEP 6: CREATE DIRECTED PROPERTY GRAPH TABLE

-- 11. DIRECTED RELATIONSHIPS GRAPH TABLE
CREATE TABLE relationships (
    relationship_id VARCHAR(128) PRIMARY KEY,
    subject_entity_id VARCHAR(128) NOT NULL REFERENCES entities(entity_id) ON DELETE RESTRICT,
    relationship_type relationship_type_enum NOT NULL,
    object_entity_id VARCHAR(128) NOT NULL REFERENCES entities(entity_id) ON DELETE RESTRICT,
    confidence_score INTEGER NOT NULL CHECK (confidence_score BETWEEN 0 AND 100),
    evidence_classification evidence_classification_enum NOT NULL DEFAULT 'Direct Evidence',
    temporal_era temporal_era_enum DEFAULT 'OPERATIONAL_ERA',
    valid_from DATE,
    valid_to DATE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT check_no_self_loops CHECK (subject_entity_id <> object_entity_id),
    CONSTRAINT unique_directed_edge UNIQUE (subject_entity_id, relationship_type, object_entity_id)
);

-- STEP 7: CREATE SPATIAL AND GRAPH INDICES

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

COMMIT;
