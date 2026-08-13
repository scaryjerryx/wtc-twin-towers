"""
World Trade Center 1 Authoritative Digital Twin REST API Gateway
FastAPI Application Backend
"""

import os
from fastapi import FastAPI, HTTPException, Query
from typing import List, Optional
import psycopg2
from psycopg2.extras import RealDictCursor
from neo4j import GraphDatabase

app = FastAPI(
    title="World Trade Center 1 Authoritative Digital Twin REST API",
    description="Production REST API server mapping WTC 1 entities, directed graph relationships, evidence citations, and flow paths.",
    version="1.0.0"
)

# Database Configurations
PG_HOST = os.getenv("POSTGRES_HOST", "localhost")
PG_PORT = os.getenv("POSTGRES_PORT", "5432")
PG_DB = os.getenv("POSTGRES_DB", "wtc_evidence")
PG_USER = os.getenv("POSTGRES_USER", "wtc_admin")
PG_PASS = os.getenv("POSTGRES_PASSWORD", "ChangeThisToSomethingLongAndRandom")

NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASS = os.getenv("NEO4J_PASSWORD", "ChangeThisPassword123")

def get_pg_connection():
    return psycopg2.connect(
        host=PG_HOST, port=PG_PORT, dbname=PG_DB, user=PG_USER, password=PG_PASS
    )

def get_neo4j_driver():
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASS))

@app.get("/api/v1/health")
def health_check():
    return {"status": "ONLINE", "model_status": "AUTHORITATIVE DIGITAL TWIN", "version": "1.0.0"}

@app.get("/api/v1/entities")
def list_entities(
    subsystem: Optional[str] = Query(None, description="Subsystem ID filter"),
    level: Optional[str] = Query(None, description="Building floor level filter")
):
    conn = get_pg_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT entity_id, canonical_name, subsystem_id, building, building_level, validation_status, confidence_score FROM wtc_evidence.entities WHERE 1=1"
    params = []
    if subsystem:
        query += " AND subsystem_id = %s"
        params.append(subsystem)
    if level:
        query += " AND building_level = %s"
        params.append(level)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/api/v1/entities/{id}")
def get_entity_by_id(id: str):
    conn = get_pg_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM wtc_evidence.entities WHERE entity_id = %s", (id,))
    entity = cursor.fetchone()
    if not entity:
        conn.close()
        raise HTTPException(status_code=404, detail="Entity not found")
    
    cursor.execute("SELECT drawing_id, page_number, bounding_box_rect, citation_uri FROM wtc_evidence.evidence WHERE entity_id = %s", (id,))
    evidence = cursor.fetchall()
    entity["evidence_citations"] = evidence
    conn.close()
    return entity

@app.get("/api/v1/relationships")
def list_relationships(
    subject_id: Optional[str] = Query(None),
    type: Optional[str] = Query(None)
):
    conn = get_pg_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    query = "SELECT * FROM wtc_evidence.v_directed_graph_edges WHERE 1=1"
    params = []
    if subject_id:
        query += " AND subject_entity_id = %s"
        params.append(subject_id)
    if type:
        query += " AND relationship_type = %s"
        params.append(type)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows

@app.get("/api/v1/trace")
def trace_path(start_entity_id: str):
    driver = get_neo4j_driver()
    with driver.session() as session:
        cypher = """
        MATCH path = (src:Entity {entity_id: $start_id})-[r*1..10]->(dst:Entity)
        RETURN [n in nodes(path) | n.entity_id] as node_path, [rel in relationships(path) | type(rel)] as rel_path
        """
        result = session.run(cypher, start_id=start_entity_id)
        paths = [record.data() for record in result]
    driver.close()
    return {"start_entity_id": start_entity_id, "traversal_paths": paths}
