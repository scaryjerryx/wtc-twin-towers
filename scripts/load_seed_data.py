#!/usr/bin/env python3
"""
World Trade Center 1 Authoritative Digital Twin
Seed Data Ingestion Script
"""

import os
import psycopg2
from neo4j import GraphDatabase

PG_HOST = os.getenv("POSTGRES_HOST", "localhost")
PG_PORT = os.getenv("POSTGRES_PORT", "5432")
PG_DB = os.getenv("POSTGRES_DB", "wtc_evidence")
PG_USER = os.getenv("POSTGRES_USER", "wtc_admin")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "ChangeThisToSomethingLongAndRandom")

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "ChangeThisPassword123")

def seed_subsystems(cursor):
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
            "INSERT INTO wtc_evidence.subsystems (subsystem_id, name, description) VALUES (%s, %s, %s) ON CONFLICT (subsystem_id) DO NOTHING",
            (s_id, s_name, s_desc)
        )

def seed_sample_data():
    print("Initializing PostgreSQL seed data...")
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS)
    cursor = conn.cursor()
    
    seed_subsystems(cursor)
    
    # 1. Sample Drawing
    cursor.execute("""
        INSERT INTO wtc_evidence.drawings (drawing_id, sheet_number, title, corpus_collection)
        VALUES ('dwg_s1', 'S-1', 'Tower A Sub-grade Structural Foundation Plan', 'PANYNJ Structural Archive')
        ON CONFLICT (drawing_id) DO NOTHING;
    """)
    
    # 2. Sample Entities
    entities = [
        ("wtc1_structural_col_501", "Core Box Column 501", "structural", "Floor B6 to 110"),
        ("wtc1_f7_central_chiller_plant", "Floor 7 Central Centrifugal Chiller Plant", "mechanical", "Floor 7"),
        ("wtc1_fb6_coned_utility_intake_vault", "Level B6 ConEd 13.8kV Utility Intake Vault", "electrical", "Level B6"),
        ("wtc1_fb6_water_booster_pump", "Level B6 Domestic Water Booster Pump Room", "plumbing", "Level B6"),
        ("wtc1_f1_telecom_mdf_room", "Floor 1 Main Telecommunications MDF Vault", "communications", "Floor 1")
    ]
    for e_id, e_name, s_id, level in entities:
        cursor.execute("""
            INSERT INTO wtc_evidence.entities (entity_id, canonical_name, subsystem_id, building_level, validation_status, confidence_score)
            VALUES (%s, %s, %s, %s, 'VALIDATED', 100)
            ON CONFLICT (entity_id) DO NOTHING;
        """, (e_id, e_name, s_id, level))
        
    conn.commit()
    conn.close()
    print("PostgreSQL seed data successfully initialized.")

if __name__ == "__main__":
    seed_sample_data()
