#!/usr/bin/env python3
"""
World Trade Center 1 Authoritative Digital Twin
Production Ingestion Script for PostgreSQL and Neo4j
"""

import os
import psycopg2
from neo4j import GraphDatabase

PG_HOST = os.getenv("POSTGRES_HOST", "postgres")
PG_PORT = os.getenv("POSTGRES_PORT", "5432")
PG_DB = os.getenv("POSTGRES_DB", "wtc_evidence")
PG_USER = os.getenv("POSTGRES_USER", "wtc_admin")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "ChangeThisToSomethingLongAndRandom")

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://neo4j:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "ChangeThisPassword123")

def seed_database():
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS)
    cursor = conn.cursor()

    # 1. Subsystems
    subsystems = [
        ("structural", "Structural Systems", "Core box columns, perim columns, trusses"),
        ("mechanical", "Mechanical Systems", "Chillers, AHUs, primary pumps, VAV zones"),
        ("electrical", "Electrical Systems", "Switchgear, busducts, xfmrs, panels"),
        ("plumbing", "Plumbing Systems", "Booster pumps, water tanks, sanitary stacks"),
        ("communications", "Communications & IT", "MDF, IDF, fiber frames, patch panels"),
        ("fire_protection", "Fire Protection Systems", "Fire pumps, standpipes, sprinklers"),
        ("security", "Security Systems", "Security SOC, access control, screening"),
        ("life_safety", "Life Safety Systems", "EOC, smoke evac fans, refuge areas"),
        ("vertical_transportation", "Vertical Transportation", "Elevator cabs, banks, motor rooms"),
        ("transit", "Mass Transit", "PATH platforms, ticket hall, concourse"),
        ("circulation", "Pedestrian Circulation", "Skylobbies, concourses, plazas"),
        ("egress", "Means of Egress", "Stairs A, B, C and exit corridors"),
        ("observation", "Observation & Tourism", "Observatory deck, promenade, WOTW"),
        ("operational_support", "Operational Support", "Truck docks, freight receiving"),
        ("facilities_operations", "Facilities Operations", "Engineering office, trades shops"),
        ("building_automation", "Building Automation & BMS", "BMS control center, DDC nodes")
    ]
    for s_id, s_name, s_desc in subsystems:
        cursor.execute(
            "INSERT INTO wtc_evidence.subsystems (subsystem_id, name, description) VALUES (%s, %s, %s) ON CONFLICT (subsystem_id) DO NOTHING;",
            (s_id, s_name, s_desc)
        )

    # 2. Sample Base Drawings
    drawings = [
        ("dwg_s1", "S-1", "Tower A Sub-grade Structural Foundation Plan", "PANYNJ Structural Archive"),
        ("dwg_m7", "M-7", "Tower A Sub-grade MER & Chiller Plant Plan", "PANYNJ Mechanical Archive"),
        ("dwg_e3", "E-3", "Tower A Primary Electrical Switchgear Plan", "PANYNJ Electrical Archive"),
        ("dwg_p4", "P-4", "Tower A Domestic & Sanitary Plumbing Riser Plan", "PANYNJ Plumbing Archive"),
        ("dwg_e20", "E-20", "Tower A Telecommunications Riser & MDF Plan", "PANYNJ Telecom Archive"),
        ("dwg_m26", "M-26", "Tower A Building Automation System Plan", "PANYNJ BMS Archive")
    ]
    for d_id, sheet, title, coll in drawings:
        cursor.execute(
            "INSERT INTO wtc_evidence.drawings (drawing_id, sheet_number, title, corpus_collection) VALUES (%s, %s, %s, %s) ON CONFLICT (drawing_id) DO NOTHING;",
            (d_id, sheet, title, coll)
        )

    # 3. Seed Validated Entities
    entities = [
        ("wtc1_structural_col_501", "Core Box Column 501", "structural", "Sub-grade B6 to Floor 110"),
        ("wtc1_f7_central_chiller_plant", "Floor 7 Central Centrifugal Chiller Plant", "mechanical", "Floor 7"),
        ("wtc1_f7_primary_pumping_station", "Floor 7 Chilled Water Primary Pumping Station", "mechanical", "Floor 7"),
        ("wtc1_chilled_water_riser1", "Chilled Water Vertical Riser Line 1", "mechanical", "Floors 1-110"),
        ("wtc1_fb6_utility_service_entrance_west", "Sub-grade Slurry Wall Utility Entrance West", "electrical", "Level B6"),
        ("wtc1_fb6_coned_utility_intake_vault", "Level B6 ConEd 13.8kV Utility Intake Vault", "electrical", "Level B6"),
        ("wtc1_fb6_high_voltage_distribution_room", "Level B6 High Voltage 13.8kV Distribution Room", "electrical", "Level B6"),
        ("wtc1_f1_master_electrical_switchgear_room", "Floor 1 Master Electrical Switchgear Room", "electrical", "Floor 1"),
        ("wtc1_f1_busduct_riser_east", "Floor 1 Vertical Busduct Riser East 4000A", "electrical", "Floors 1-110"),
        ("wtc1_f41_transformer_vault", "Floor 41 High Voltage Step-Down Transformer Vault", "electrical", "Floor 41"),
        ("wtc1_f41_panelboard_room", "Floor 41 Local Distribution Panelboard Room", "electrical", "Floor 41"),
        ("wtc1_f41_lighting_panel_lp41a", "Floor 41 Branch Lighting Panel LP-41A", "electrical", "Floor 41"),
        ("wtc1_fb1_plumbing_dist_room", "Level B1 Main Water Plumbing Distribution Room", "plumbing", "Level B1"),
        ("wtc1_fb6_water_booster_pump", "Level B6 Domestic Water Booster Pump Room", "plumbing", "Level B6"),
        ("wtc1_f1_water_riser_north", "Floor 1 Domestic Water Vertical Riser North", "plumbing", "Floors 1-110"),
        ("wtc1_f108_water_tank_50k", "Floor 108 Penthouse 50,000 Gallon Water Tank", "plumbing", "Floor 108"),
        ("wtc1_f41_domestic_water_branch_north", "Floor 41 Domestic Water Branch Loop North", "plumbing", "Floor 41"),
        ("wtc1_f1_telecom_mdf_room", "Floor 1 Main Telecommunications MDF Vault", "communications", "Floor 1"),
        ("wtc1_f1_telecom_hub", "Level B1 Telecommunications Distribution Hub", "communications", "Level B1"),
        ("wtc1_f1_telecom_riser_east", "Floor 1 Optical Fiber Vertical Riser East", "communications", "Floors 1-110"),
        ("wtc1_f41_idf_closet", "Floor 41 Local Telecom IDF Closet", "communications", "Floor 41"),
        ("wtc1_f41_fiber_distribution_frame_north", "Floor 41 Optical Fiber Distribution Frame North", "communications", "Floor 41"),
        ("wtc1_f41_communications_cable_tray_network", "Floor 41 Core Overhead Cable Tray Network", "communications", "Floor 41"),
        ("wtc1_fb1_building_automation_control_center", "Level B1 Master BMS Command Control Center", "building_automation", "Level B1"),
        ("wtc1_f41_ddc_control_node_north", "Floor 41 Direct Digital Control DDC Node North", "building_automation", "Floor 41")
    ]
    for e_id, e_name, s_id, level in entities:
        cursor.execute("""
            INSERT INTO wtc_evidence.entities (entity_id, canonical_name, subsystem_id, building_level, validation_status, confidence_score)
            VALUES (%s, %s, %s, %s, 'VALIDATED', 100)
            ON CONFLICT (entity_id) DO NOTHING;
        """, (e_id, e_name, s_id, level))

    # 4. Seed Directed Graph Relationships
    relationships = [
        ("wtc1_fb6_utility_service_entrance_west", "FEEDS", "wtc1_fb6_coned_utility_intake_vault"),
        ("wtc1_fb6_coned_utility_intake_vault", "SUPPLIES", "wtc1_fb6_high_voltage_distribution_room"),
        ("wtc1_fb6_high_voltage_distribution_room", "FEEDS", "wtc1_f1_master_electrical_switchgear_room"),
        ("wtc1_f1_master_electrical_switchgear_room", "FEEDS_RISER_TO", "wtc1_f1_busduct_riser_east"),
        ("wtc1_f1_busduct_riser_east", "DISTRIBUTES_TO", "wtc1_f41_transformer_vault"),
        ("wtc1_f41_transformer_vault", "FEEDS", "wtc1_f41_panelboard_room"),
        ("wtc1_f41_panelboard_room", "BRANCHES_TO", "wtc1_f41_lighting_panel_lp41a"),
        ("wtc1_f7_central_chiller_plant", "COOLED_BY", "wtc1_f7_primary_pumping_station"),
        ("wtc1_f7_primary_pumping_station", "PUMPS_TO", "wtc1_chilled_water_riser1"),
        ("wtc1_fb1_plumbing_dist_room", "SUPPLIES", "wtc1_fb6_water_booster_pump"),
        ("wtc1_fb6_water_booster_pump", "PUMPS_TO", "wtc1_f1_water_riser_north"),
        ("wtc1_f1_water_riser_north", "SUPPLIES", "wtc1_f108_water_tank_50k"),
        ("wtc1_f108_water_tank_50k", "DISTRIBUTES_TO", "wtc1_f41_domestic_water_branch_north"),
        ("wtc1_f1_telecom_mdf_room", "CONNECTS_TO", "wtc1_f1_telecom_hub"),
        ("wtc1_f1_telecom_hub", "ROUTES_TO", "wtc1_f1_telecom_riser_east"),
        ("wtc1_f1_telecom_riser_east", "SERVES", "wtc1_f41_idf_closet"),
        ("wtc1_f41_idf_closet", "BRANCHES_TO", "wtc1_f41_fiber_distribution_frame_north"),
        ("wtc1_f41_fiber_distribution_frame_north", "ROUTES_TO", "wtc1_f41_communications_cable_tray_network"),
        ("wtc1_fb1_building_automation_control_center", "SUPERVISES", "wtc1_f41_ddc_control_node_north")
    ]
    for subj, rel, obj in relationships:
        cursor.execute("""
            INSERT INTO wtc_evidence.relationships (subject_entity_id, relationship_type, object_entity_id, confidence_score)
            VALUES (%s, %s, %s, 100)
            ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO NOTHING;
        """, (subj, rel, obj))

    # 5. Evidence Citations
    evidence = [
        ("ev_col501_s1", "wtc1_structural_col_501", "dwg_s1", 1, "100,100,200,200", "drawing_s1.pdf#page=1&rect=100,100,200,200"),
        ("ev_chiller_m7", "wtc1_f7_central_chiller_plant", "dwg_m7", 1, "150,150,300,300", "drawing_m7.pdf#page=1&rect=150,150,300,300"),
        ("ev_intake_e3", "wtc1_fb6_coned_utility_intake_vault", "dwg_e3", 1, "200,200,400,400", "drawing_e3.pdf#page=1&rect=200,200,400,400")
    ]
    for ev_id, ent_id, dwg_id, pg, rect, uri in evidence:
        cursor.execute("""
            INSERT INTO wtc_evidence.evidence (evidence_id, entity_id, drawing_id, page_number, bounding_box_rect, citation_uri)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (evidence_id) DO NOTHING;
        """, (ev_id, ent_id, dwg_id, pg, rect, uri))

    conn.commit()
    conn.close()
    print("PostgreSQL seed ingestion complete.")

    # 6. Seed Neo4j Graph
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        for e_id, e_name, s_id, level in entities:
            session.run("""
                MERGE (e:Entity {entity_id: $e_id})
                ON CREATE SET e.canonical_name = $e_name, e.subsystem = $s_id, e.level = $level, e.validation_status = 'VALIDATED', e.confidence_score = 100
            """, e_id=e_id, e_name=e_name, s_id=s_id, level=level)
        
        for subj, rel, obj in relationships:
            session.run(f"""
                MATCH (source:Entity {{entity_id: $subj}})
                MATCH (target:Entity {{entity_id: $obj}})
                MERGE (source)-[r:{rel}]->(target)
                ON CREATE SET r.confidence_score = 100
            """, subj=subj, obj=obj)
    
    driver.close()
    print("Neo4j graph seed ingestion complete.")

if __name__ == "__main__":
    seed_database()
