#!/usr/bin/env python3
"""
World Trade Center 1 Authoritative Runtime Dataset Reconciliation Script
Reconciles live PostgreSQL and Neo4j runtime databases to match the exact 185 Authoritative Entities and 175 Relationships.
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

def reconcile():
    entities_path = os.path.join(DATA_DIR, "wtc1_entities.json")
    relationships_path = os.path.join(DATA_DIR, "wtc1_relationships.json")

    if not os.path.exists(entities_path) or not os.path.exists(relationships_path):
        entities_path = "/opt/wtc/wtc-twin-towers/data/wtc1_entities.json"
        relationships_path = "/opt/wtc/wtc-twin-towers/data/wtc1_relationships.json"

    with open(entities_path, "r") as f:
        auth_entities = json.load(f)
    auth_entity_ids = set(e["entity_id"] for e in auth_entities)

    with open(relationships_path, "r") as f:
        auth_relationships = json.load(f)
    auth_rel_tuples = set((r["subject_entity_id"], r["relationship_type"], r["object_entity_id"]) for r in auth_relationships)

    print(f"Loaded {len(auth_entity_ids)} Authoritative Entity IDs and {len(auth_rel_tuples)} Authoritative Relationship Tuples.")

    # 1. Connect PostgreSQL
    conn = psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS)
    cursor = conn.cursor()

    cursor.execute("SELECT entity_id, canonical_name FROM wtc_evidence.entities;")
    pg_entities = cursor.fetchall()
    pg_entity_map = {row[0]: row[1] for row in pg_entities}
    
    sample_entities = {eid: name for eid, name in pg_entity_map.items() if eid not in auth_entity_ids}
    print(f"Identified {len(sample_entities)} SAMPLE/NON-AUTHORITATIVE entities in PostgreSQL:")
    for eid, name in sample_entities.items():
        print(f"  - {eid}: {name}")

    cursor.execute("SELECT relationship_id, subject_entity_id, relationship_type, object_entity_id FROM wtc_evidence.relationships;")
    pg_rels = cursor.fetchall()
    
    sample_rels = []
    for rel_id, subj, rtype, obj in pg_rels:
        if (subj, rtype, obj) not in auth_rel_tuples:
            sample_rels.append((rel_id, subj, rtype, obj))

    print(f"Identified {len(sample_rels)} SAMPLE/NON-AUTHORITATIVE relationships in PostgreSQL:")
    for rel_id, subj, rtype, obj in sample_rels:
        print(f"  - [{rel_id}] {subj} --({rtype})--> {obj}")

    # Reconcile PostgreSQL
    # Delete non-authoritative relationships first
    for rel_id, subj, rtype, obj in sample_rels:
        cursor.execute("DELETE FROM wtc_evidence.relationships WHERE relationship_id = %s;", (rel_id,))
    
    # Delete non-authoritative evidence citations if any
    for eid in sample_entities:
        cursor.execute("DELETE FROM wtc_evidence.evidence WHERE entity_id = %s;", (eid,))
        cursor.execute("DELETE FROM wtc_evidence.validations WHERE entity_id = %s;", (eid,))
        cursor.execute("DELETE FROM wtc_evidence.entities WHERE entity_id = %s;", (eid,))

    conn.commit()
    conn.close()
    print("PostgreSQL database reconciliation complete.")

    # 2. Connect Neo4j
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))
    with driver.session() as session:
        # Delete non-authoritative nodes and relationships
        for eid in sample_entities:
            session.run("MATCH (n:Entity {entity_id: $eid}) DETACH DELETE n;", eid=eid)
            
        for rel_id, subj, rtype, obj in sample_rels:
            session.run(f"MATCH (s:Entity {{entity_id: $subj}})-[r:{rtype}]->(o:Entity {{entity_id: $obj}}) DELETE r;", subj=subj, obj=obj)

    driver.close()
    print("Neo4j graph database reconciliation complete.")

if __name__ == "__main__":
    reconcile()
