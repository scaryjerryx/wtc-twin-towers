#!/usr/bin/env python3
"""
World Trade Center 1 Authoritative Digital Twin
Production Full Dataset Ingestion Script (185 Entities & 175 Relationships)
Loads directly from data/wtc1_entities.json and data/wtc1_relationships.json
"""

import os
import json
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

DATA_DIR = os.getenv("DATA_DIR", "/app/data")

def load_full_model():
    entities_path = os.path.join(DATA_DIR, "wtc1_entities.json")
    relationships_path = os.path.join(DATA_DIR, "wtc1_relationships.json")

    if not os.path.exists(entities_path) or not os.path.exists(relationships_path):
        # Fallback to local repo path if running outside container context
        entities_path = "/opt/wtc/wtc-twin-towers/data/wtc1_entities.json"
        relationships_path = "/opt/wtc/wtc-twin-towers/data/wtc1_relationships.json"

    with open(entities_path, "r") as f:
        entities = json.load(f)

    with open(relationships_path, "r") as f:
        relationships = json.load(f)

    print(f"Loaded {len(entities)} Entities and {len(relationships)} Relationships from JSON datasets.")

    # 1. PostgreSQL Ingestion
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS)
    cursor = conn.cursor()

    # Subsystems reference
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

    # Ingest 185 Entities into PostgreSQL
    for e in entities:
        cursor.execute("""
            INSERT INTO wtc_evidence.entities (entity_id, canonical_name, subsystem_id, building_level, validation_status, confidence_score)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (entity_id) DO NOTHING;
        """, (e["entity_id"], e["canonical_name"], e["subsystem"], e["level"], e["validation_status"], e["confidence_score"]))

    # Ingest 175 Relationships into PostgreSQL
    for r in relationships:
        cursor.execute("""
            INSERT INTO wtc_evidence.relationships (subject_entity_id, relationship_type, object_entity_id, confidence_score)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO NOTHING;
        """, (r["subject_entity_id"], r["relationship_type"], r["object_entity_id"], r["confidence_score"]))

    conn.commit()
    conn.close()
    print("PostgreSQL 185-entity dataset ingestion complete.")

    # 2. Neo4j Ingestion
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        for e in entities:
            session.run("""
                MERGE (node:Entity {entity_id: $e_id})
                ON CREATE SET node.canonical_name = $name, node.subsystem = $sub, node.level = $lvl, node.validation_status = $status, node.confidence_score = $score
            """, e_id=e["entity_id"], name=e["canonical_name"], sub=e["subsystem"], lvl=e["level"], status=e["validation_status"], score=e["confidence_score"])

        for r in relationships:
            rel_type = r["relationship_type"]
            session.run(f"""
                MATCH (source:Entity {{entity_id: $subj}})
                MATCH (target:Entity {{entity_id: $obj}})
                MERGE (source)-[rel:{rel_type}]->(target)
                ON CREATE SET rel.confidence_score = $score
            """, subj=r["subject_entity_id"], obj=r["object_entity_id"], score=r["confidence_score"])

    driver.close()
    print("Neo4j 175-edge graph dataset ingestion complete.")

if __name__ == "__main__":
    load_full_model()
