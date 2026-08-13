-- Authoritative Database Persistence Script: Baseline 002 Synchronization
-- Target Database: wtc_evidence (PostgreSQL 16.14 + PostGIS 3.6.4)
-- Date: August 13, 2026

BEGIN;

-- 2. Upsert All 56 VALIDATED Entities
INSERT INTO entities (entity_id, entity_category, building_id, confidence_score, lifecycle_state)
VALUES
  -- Baseline 001 Structural Core Columns 501-503
  ('wtc1_structural_col_501', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_502', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_503', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Baseline 002 Structural Core Columns 504-508 & 601-604
  ('wtc1_structural_col_504', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_505', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_506', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_507', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_508', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_601', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_602', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_603', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_structural_col_604', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Perimeter Column Trees F44 & F78
  ('wtc1_f44_col_tree_1', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_col_tree_2', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_col_tree_3', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f78_col_tree_1', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f78_col_tree_2', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f78_col_tree_3', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Express & Local Elevator Banks
  ('wtc1_f78_elevator_bank_c', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_elevator_bank_b1', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_local_elevator_bank_1', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_local_elevator_bank_2', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_local_elevator_bank_3', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_local_elevator_bank_4', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_elevator_bank_b2', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f107_observation_express_bank', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_service_shaft_49', 'elevator', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_heavy_freight_shaft_50', 'elevator', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Core Egress Stairs & Corridors
  ('wtc1_f1_stair_a_enclosure', 'stair', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_stair_b_enclosure', 'stair', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_stair_c_enclosure', 'stair', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_stair_a_exit_corridor', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_stair_b_exit_corridor', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_stair_c_exit_corridor', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f78_skylobby_stair_transfer_landing', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_plaza_lobby_stair_exit_vestibule', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Public Circulation, Transit & Retail
  ('wtc1_fb1_path_concourse_zone', 'transit_station', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_fb1_shopping_concourse_retail', 'retail_space', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_fb1_cortlandt_street_subway_connector', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_fb1_path_commuter_ticket_hall', 'space', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_skylobby_zone', 'zone', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_express_elevator_landing', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f44_local_elevator_bank_2', 'elevator_bank', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f78_skylobby_zone', 'zone', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_north_elevator_hall', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_south_elevator_hall', 'corridor', 'wtc1_tower_a', 100, 'VALIDATED'),
  -- Mechanical & Electrical Infrastructure
  ('wtc1_f7_central_chiller_plant', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f7_north_ahu_supply_room', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f7_south_ahu_return_room', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f7_primary_pumping_station', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_chilled_water_riser1', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_chilled_water_riser2', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_chilled_water_riser3', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_main_electrical_vault', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_fb1_b1_electrical_distribution_substation', 'mechanical_area', 'wtc1_tower_a', 100, 'VALIDATED'),
  ('wtc1_f1_fan_room_101', 'service_area', 'wtc1_tower_a', 100, 'VALIDATED')
ON CONFLICT (entity_id) DO UPDATE SET
  confidence_score = EXCLUDED.confidence_score,
  lifecycle_state = EXCLUDED.lifecycle_state;

-- 3. Upsert Physical Elements & Geometries
INSERT INTO elements (element_id, name, element_category, building_id, confidence_score, lifecycle_state, geometry_2d, z_min, z_max)
VALUES
  ('wtc1_structural_col_504', 'Core Box Column 504', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983210 196410, 983214 196410, 983214 196414, 983210 196414, 983210 196410))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_505', 'Core Box Column 505', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983220 196410, 983224 196410, 983224 196414, 983220 196414, 983220 196410))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_506', 'Core Box Column 506', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983230 196410, 983234 196410, 983234 196414, 983230 196414, 983230 196410))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_507', 'Core Box Column 507', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983240 196410, 983244 196410, 983244 196414, 983240 196414, 983240 196410))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_508', 'Core Box Column 508', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983250 196410, 983254 196410, 983254 196414, 983250 196414, 983250 196410))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_601', 'Core Box Column 601', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983210 196450, 983214 196450, 983214 196454, 983210 196454, 983210 196450))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_602', 'Core Box Column 602', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983220 196450, 983224 196450, 983224 196454, 983220 196454, 983220 196450))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_603', 'Core Box Column 603', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983230 196450, 983234 196450, 983234 196454, 983230 196454, 983230 196450))', 2263), 31.0, 1360.0),
  ('wtc1_structural_col_604', 'Core Box Column 604', 'structural_element', 'wtc1_tower_a', 100, 'VALIDATED', ST_GeomFromText('POLYGON((983240 196450, 983244 196450, 983244 196454, 983240 196454, 983240 196450))', 2263), 31.0, 1360.0)
ON CONFLICT (element_id) DO UPDATE SET
  name = EXCLUDED.name,
  element_category = EXCLUDED.element_category,
  confidence_score = EXCLUDED.confidence_score,
  lifecycle_state = EXCLUDED.lifecycle_state,
  geometry_2d = EXCLUDED.geometry_2d,
  z_min = EXCLUDED.z_min,
  z_max = EXCLUDED.z_max;

-- 4. Insert Directed Property Graph Relationships (36 Baseline Edges)
INSERT INTO relationships (relationship_id, subject_entity_id, relationship_type, object_entity_id, confidence_score)
VALUES
  ('rel_b002_1', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_504', 100),
  ('rel_b002_2', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_505', 100),
  ('rel_b002_3', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_506', 100),
  ('rel_b002_4', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_507', 100),
  ('rel_b002_5', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_508', 100),
  ('rel_b002_6', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_601', 100),
  ('rel_b002_7', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_602', 100),
  ('rel_b002_8', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_603', 100),
  ('rel_b002_9', 'wtc1_tower_a', 'CONTAINS', 'wtc1_structural_col_604', 100),
  ('rel_b002_10', 'wtc1_f44_col_tree_1', 'BOUNDED_BY', 'wtc1_f44_skylobby_zone', 100),
  ('rel_b002_11', 'wtc1_f44_col_tree_2', 'BOUNDED_BY', 'wtc1_f44_skylobby_zone', 100),
  ('rel_b002_12', 'wtc1_f44_col_tree_3', 'BOUNDED_BY', 'wtc1_f44_skylobby_zone', 100),
  ('rel_b002_13', 'wtc1_f78_col_tree_1', 'BOUNDED_BY', 'wtc1_f78_skylobby_zone', 100),
  ('rel_b002_14', 'wtc1_f78_col_tree_2', 'BOUNDED_BY', 'wtc1_f78_skylobby_zone', 100),
  ('rel_b002_15', 'wtc1_f78_col_tree_3', 'BOUNDED_BY', 'wtc1_f78_skylobby_zone', 100),
  ('rel_b002_16', 'wtc1_tower_a', 'CONTAINS', 'wtc1_f44_elevator_bank_b2', 100),
  ('rel_b002_17', 'wtc1_f44_elevator_bank_b2', 'CONNECTS_TO', 'wtc1_tower_a', 100),
  ('rel_b002_18', 'wtc1_f107_observation_express_bank', 'CONNECTS_TO', 'wtc1_tower_a', 100),
  ('rel_b002_19', 'wtc1_f44_express_elevator_landing', 'TRANSFERS_TO', 'wtc1_f44_skylobby_zone', 100),
  ('rel_b002_20', 'wtc1_f44_skylobby_zone', 'ACCESSES', 'wtc1_f44_local_elevator_bank_2', 100),
  ('rel_b002_21', 'wtc1_f1_stair_a_enclosure', 'CONNECTS_TO', 'wtc1_tower_a', 100),
  ('rel_b002_22', 'wtc1_f1_stair_b_enclosure', 'CONNECTS_TO', 'wtc1_tower_a', 100),
  ('rel_b002_23', 'wtc1_f1_stair_c_enclosure', 'CONNECTS_TO', 'wtc1_tower_a', 100),
  ('rel_b002_24', 'wtc1_f1_stair_a_enclosure', 'LEADS_TO', 'wtc1_f1_stair_a_exit_corridor', 100),
  ('rel_b002_25', 'wtc1_f1_stair_b_enclosure', 'LEADS_TO', 'wtc1_f1_stair_b_exit_corridor', 100),
  ('rel_b002_26', 'wtc1_f1_stair_c_enclosure', 'LEADS_TO', 'wtc1_f1_stair_c_exit_corridor', 100),
  ('rel_b002_27', 'wtc1_f1_stair_a_enclosure', 'LEADS_TO', 'wtc1_f1_plaza_lobby_stair_exit_vestibule', 100),
  ('rel_b002_28', 'wtc1_fb1_path_concourse_zone', 'TRANSFERS_TO', 'wtc1_fb1_cortlandt_street_subway_connector', 100),
  ('rel_b002_29', 'wtc1_fb1_shopping_concourse_retail', 'CONNECTS_TO', 'wtc1_fb1_path_concourse_zone', 100),
  ('rel_b002_30', 'wtc1_f7_central_chiller_plant', 'FEEDS_RISER_TO', 'wtc1_chilled_water_riser1', 100),
  ('rel_b002_31', 'wtc1_f7_north_ahu_supply_room', 'SERVES', 'wtc1_tower_a', 100),
  ('rel_b002_32', 'wtc1_f7_south_ahu_return_room', 'SERVES', 'wtc1_tower_a', 100),
  ('rel_b002_33', 'wtc1_chilled_water_riser2', 'FEEDS_RISER_TO', 'wtc1_tower_a', 100),
  ('rel_b002_34', 'wtc1_chilled_water_riser3', 'FEEDS_RISER_TO', 'wtc1_tower_a', 100),
  ('rel_b002_35', 'wtc1_f1_main_electrical_vault', 'SERVES', 'wtc1_tower_a', 100),
  ('rel_b002_36', 'wtc1_fb1_b1_electrical_distribution_substation', 'SERVES', 'wtc1_tower_a', 100)
ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO NOTHING;

COMMIT;
