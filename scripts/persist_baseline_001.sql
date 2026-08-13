-- ============================================================================
-- WORLD TRADE CENTER RECONSTRUCTION PROJECT: BASELINE 001 DATABASE PERSISTENCE
-- File: scripts/persist_baseline_001.sql
-- Description: Transactional PostgreSQL/PostGIS Ingestion of World Model Baseline 001
-- Governing Document: docs/PHASE_5_WORLD_MODEL_BASELINE_001.md
-- ============================================================================

BEGIN;

-- ----------------------------------------------------------------------------
-- STEP 1: PRE-INGESTION SANITY CHECK & AUXILIARY PARENT ENTITY INGESTION
-- ----------------------------------------------------------------------------

-- Ingest auxiliary entity if not exists: wtc1_f1_core_shear_wall
INSERT INTO entities (entity_id, entity_category, building_id, confidence_score, lifecycle_state)
VALUES ('wtc1_f1_core_shear_wall', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED')
ON CONFLICT (entity_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

INSERT INTO elements (element_id, space_id, zone_id, floor_id, building_id, name, element_category, is_multi_floor, geometry_2d, z_min, z_max, confidence_score, lifecycle_state)
VALUES ('wtc1_f1_core_shear_wall', NULL, NULL, 'wtc1_floor_1', NULL, 'Tower A Sub-grade Core Shear Wall', 'structural_element', FALSE, ST_SetSRID(ST_GeomFromText('POLYGON((979250 197350, 979300 197350, 979300 197360, 979250 197360, 979250 197350))'), 2263), -20.0, 10.0, 100, 'VALIDATED')
ON CONFLICT (element_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

-- ----------------------------------------------------------------------------
-- STEP 2: INGEST MASTER ENTITY REGISTRY RECORDS (entities table)
-- ----------------------------------------------------------------------------

INSERT INTO entities (entity_id, entity_category, building_id, confidence_score, lifecycle_state)
VALUES 
    ('wtc1_structural_col_501', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_f78_elevator_bank_c', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_structural_col_502', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_f1_elevator_bank_b1', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_f78_col_tree_1', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_structural_col_503', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_f78_skylobby_zone', 'zone', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_chilled_water_riser1', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
    ('wtc1_f1_fan_room_101', 'service_area', 'wtc1_tower_a', 100, 'VALIDATED')
ON CONFLICT (entity_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

-- ----------------------------------------------------------------------------
-- STEP 3: INGEST PHYSICAL TIER DETAILS (elements, spaces, zones)
-- ----------------------------------------------------------------------------

-- Elements (6 Physical Component Elements)
INSERT INTO elements (element_id, space_id, zone_id, floor_id, building_id, name, element_category, is_multi_floor, geometry_2d, z_min, z_max, confidence_score, lifecycle_state)
VALUES 
    ('wtc1_structural_col_501', NULL, NULL, NULL, 'wtc1_tower_a', 'Tower A Structural Core Box Column 501', 'structural_element', TRUE, ST_SetSRID(ST_GeomFromText('POINT(979310.0 197410.0)'), 2263), -70.00, 1370.00, 100, 'VALIDATED'),
    ('wtc1_f78_elevator_bank_c', NULL, NULL, NULL, 'wtc1_tower_a', 'Tower A Express Elevator Bank C (Shafts 41-48)', 'elevator_bank', TRUE, ST_SetSRID(ST_GeomFromText('POLYGON((979300 197400, 979350 197400, 979350 197450, 979300 197450, 979300 197400))'), 2263), 940.00, 1370.00, 100, 'VALIDATED'),
    ('wtc1_structural_col_502', NULL, NULL, NULL, 'wtc1_tower_a', 'Tower A Structural Core Box Column 502', 'structural_element', TRUE, ST_SetSRID(ST_GeomFromText('POINT(979320.0 197410.0)'), 2263), -70.00, 1370.00, 100, 'VALIDATED'),
    ('wtc1_f1_elevator_bank_b1', NULL, NULL, NULL, 'wtc1_tower_a', 'Sub-grade Elevator Bank B1 (Shafts 1-6)', 'elevator_bank', TRUE, ST_SetSRID(ST_GeomFromText('POLYGON((979280 197380, 979320 197380, 979320 197420, 979280 197420, 979280 197380))'), 2263), -40.00, 10.00, 100, 'VALIDATED'),
    ('wtc1_f78_col_tree_1', NULL, NULL, 'wtc1_floor_78', NULL, 'Floor 78 Perimeter Column Tree Assembly 1', 'structural_element', FALSE, ST_SetSRID(ST_GeomFromText('POLYGON((979200 197500, 979210 197500, 979210 197530, 979200 197530, 979200 197500))'), 2263), 930.00, 970.00, 100, 'VALIDATED'),
    ('wtc1_structural_col_503', NULL, NULL, NULL, 'wtc1_tower_a', 'Tower A Structural Core Box Column 503', 'structural_element', TRUE, ST_SetSRID(ST_GeomFromText('POINT(979330.0 197410.0)'), 2263), -70.00, 1370.00, 100, 'VALIDATED'),
    ('wtc1_chilled_water_riser1', NULL, NULL, NULL, 'wtc1_tower_a', 'Sub-grade Chilled Water Riser 1', 'mechanical_area', TRUE, ST_SetSRID(ST_GeomFromText('POINT(979290.0 197430.0)'), 2263), -70.00, 1370.00, 100, 'VALIDATED')
ON CONFLICT (element_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

-- Zones (1 Functional Floor Zone)
INSERT INTO zones (zone_id, floor_id, building_id, site_id, name, zone_type, geometry_2d, z_min, z_max, confidence_score, lifecycle_state)
VALUES 
    ('wtc1_f78_skylobby_zone', 'wtc1_floor_78', NULL, NULL, 'Floor 78 Skylobby Passenger Transfer Concourse Zone', 'zone', ST_SetSRID(ST_GeomFromText('POLYGON((979250 197350, 979400 197350, 979400 197500, 979250 197500, 979250 197350))'), 2263), 940.00, 955.00, 100, 'VALIDATED')
ON CONFLICT (zone_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

-- Spaces (1 Enclosed Service Space)
INSERT INTO spaces (space_id, zone_id, floor_id, name, space_category, room_number, geometry_2d, z_min, z_max, confidence_score, lifecycle_state)
VALUES 
    ('wtc1_f1_fan_room_101', NULL, 'wtc1_floor_1', 'Sub-grade Fan Room 101', 'service_area', '101', ST_SetSRID(ST_GeomFromText('POLYGON((979260 197360, 979290 197360, 979290 197390, 979260 197390, 979260 197360))'), 2263), -20.00, 10.00, 100, 'VALIDATED')
ON CONFLICT (space_id) DO UPDATE SET 
    confidence_score = 100,
    lifecycle_state = 'VALIDATED',
    updated_at = CURRENT_TIMESTAMP;

-- ----------------------------------------------------------------------------
-- STEP 4: INGEST EVIDENCE CITATIONS (entity_evidence_citations table)
-- ----------------------------------------------------------------------------

INSERT INTO entity_evidence_citations (citation_id, entity_id, source_id, sheet_code, evidence_classification, confidence_score)
VALUES 
    -- Column 501 (5 Sheets)
    ('cite_col501_aa121', 'wtc1_structural_col_501', 'src_yamasaki_drawings', 'A-A-121', 'Direct Evidence', 100),
    ('cite_col501_aa18',  'wtc1_structural_col_501', 'src_yamasaki_drawings', 'A-A-18',  'Direct Evidence', 100),
    ('cite_col501_aa101', 'wtc1_structural_col_501', 'src_yamasaki_drawings', 'A-A-101', 'Direct Evidence', 100),
    ('cite_col501_s1',    'wtc1_structural_col_501', 'src_yamasaki_drawings', 'S-1',     'Direct Evidence', 100),
    ('cite_col501_aa20',  'wtc1_structural_col_501', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),
    
    -- Express Elevator Bank C (4 Sheets)
    ('cite_bankc_aa121', 'wtc1_f78_elevator_bank_c', 'src_yamasaki_drawings', 'A-A-121', 'Direct Evidence', 100),
    ('cite_bankc_aa101', 'wtc1_f78_elevator_bank_c', 'src_yamasaki_drawings', 'A-A-101', 'Direct Evidence', 100),
    ('cite_bankc_aa19',  'wtc1_f78_elevator_bank_c', 'src_yamasaki_drawings', 'A-A-19',  'Direct Evidence', 100),
    ('cite_bankc_aa20',  'wtc1_f78_elevator_bank_c', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Column 502 (4 Sheets)
    ('cite_col502_aa101', 'wtc1_structural_col_502', 'src_yamasaki_drawings', 'A-A-101', 'Direct Evidence', 100),
    ('cite_col502_s1',    'wtc1_structural_col_502', 'src_yamasaki_drawings', 'S-1',     'Direct Evidence', 100),
    ('cite_col502_aa130', 'wtc1_structural_col_502', 'src_yamasaki_drawings', 'A-A-130', 'Direct Evidence', 100),
    ('cite_col502_aa20',  'wtc1_structural_col_502', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Sub-grade Elevator Bank B1 (4 Sheets)
    ('cite_bankb1_aa121', 'wtc1_f1_elevator_bank_b1', 'src_yamasaki_drawings', 'A-A-121', 'Direct Evidence', 100),
    ('cite_bankb1_aa18',  'wtc1_f1_elevator_bank_b1', 'src_yamasaki_drawings', 'A-A-18',  'Direct Evidence', 100),
    ('cite_bankb1_aa130', 'wtc1_f1_elevator_bank_b1', 'src_yamasaki_drawings', 'A-A-130', 'Direct Evidence', 100),
    ('cite_bankb1_aa20',  'wtc1_f1_elevator_bank_b1', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Column Tree 1 (3 Sheets)
    ('cite_tree1_s1',    'wtc1_f78_col_tree_1', 'src_yamasaki_drawings', 'S-1',     'Direct Evidence', 100),
    ('cite_tree1_aa19',  'wtc1_f78_col_tree_1', 'src_yamasaki_drawings', 'A-A-19',  'Direct Evidence', 100),
    ('cite_tree1_aa130', 'wtc1_f78_col_tree_1', 'src_yamasaki_drawings', 'A-A-130', 'Direct Evidence', 100),

    -- Column 503 (3 Sheets)
    ('cite_col503_s1',    'wtc1_structural_col_503', 'src_yamasaki_drawings', 'S-1',     'Direct Evidence', 100),
    ('cite_col503_aa130', 'wtc1_structural_col_503', 'src_yamasaki_drawings', 'A-A-130', 'Direct Evidence', 100),
    ('cite_col503_aa20',  'wtc1_structural_col_503', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Skylobby Zone (3 Sheets)
    ('cite_skylobby_aa19',  'wtc1_f78_skylobby_zone', 'src_yamasaki_drawings', 'A-A-19',  'Direct Evidence', 100),
    ('cite_skylobby_aa130', 'wtc1_f78_skylobby_zone', 'src_yamasaki_drawings', 'A-A-130', 'Direct Evidence', 100),
    ('cite_skylobby_aa20',  'wtc1_f78_skylobby_zone', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Chilled Water Riser 1 (3 Sheets)
    ('cite_cwriser_aa101', 'wtc1_chilled_water_riser1', 'src_yamasaki_drawings', 'A-A-101', 'Direct Evidence', 100),
    ('cite_cwriser_m7',    'wtc1_chilled_water_riser1', 'src_yamasaki_drawings', 'M-7',     'Direct Evidence', 100),
    ('cite_cwriser_aa20',  'wtc1_chilled_water_riser1', 'src_yamasaki_drawings', 'A-A-20',  'Direct Evidence', 100),

    -- Fan Room 101 (3 Sheets)
    ('cite_fanroom_aa18', 'wtc1_f1_fan_room_101', 'src_yamasaki_drawings', 'A-A-18', 'Direct Evidence', 100),
    ('cite_fanroom_m7',   'wtc1_f1_fan_room_101', 'src_yamasaki_drawings', 'M-7',    'Direct Evidence', 100),
    ('cite_fanroom_aa31', 'wtc1_f1_fan_room_101', 'src_yamasaki_drawings', 'A-A-31', 'Direct Evidence', 100)
ON CONFLICT (entity_id, source_id, sheet_code) DO UPDATE SET 
    confidence_score = EXCLUDED.confidence_score;

-- ----------------------------------------------------------------------------
-- STEP 5: INGEST DIRECTED PROPERTY GRAPH RELATIONSHIPS (relationships table)
-- ----------------------------------------------------------------------------

INSERT INTO relationships (relationship_id, subject_entity_id, relationship_type, object_entity_id, confidence_score, evidence_classification)
VALUES 
    ('rel_baseline001_1', 'wtc1_tower_a',              'CONTAINS',       'wtc1_structural_col_501',  100, 'Direct Evidence'),
    ('rel_baseline001_2', 'wtc1_tower_a',              'CONTAINS',       'wtc1_f78_elevator_bank_c', 100, 'Direct Evidence'),
    ('rel_baseline001_3', 'wtc1_f78_elevator_bank_c',  'CONNECTS_TO',    'wtc1_f78_skylobby_zone',   100, 'Direct Evidence'),
    ('rel_baseline001_4', 'wtc1_tower_a',              'CONTAINS',       'wtc1_f1_elevator_bank_b1', 100, 'Direct Evidence'),
    ('rel_baseline001_5', 'wtc1_structural_col_501',   'CONNECTS_TO',    'wtc1_structural_col_502',  100, 'Direct Evidence'),
    ('rel_baseline001_6', 'wtc1_f78_col_tree_1',       'BOUNDED_BY',     'wtc1_f78_skylobby_zone',   100, 'Direct Evidence'),
    ('rel_baseline001_7', 'wtc1_f1_core_shear_wall',   'BOUNDED_BY',     'wtc1_f1_fan_room_101',     100, 'Direct Evidence'),
    ('rel_baseline001_8', 'wtc1_f1_fan_room_101',       'SERVES',         'wtc1_tower_a',             100, 'Direct Evidence'),
    ('rel_baseline001_9', 'wtc1_chilled_water_riser1', 'FEEDS_RISER_TO', 'wtc1_tower_a',             100, 'Direct Evidence')
ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO UPDATE SET 
    confidence_score = 100;

COMMIT;
