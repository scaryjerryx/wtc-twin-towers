# ETL Entity Ingestion Pipeline Specification

## Pipeline Overview
The Entity Ingestion Pipeline parses markdown session reports (`docs/PHASE_5_REAL_RECONSTRUCTION_SESSION_*.md`), validates entities against `schemas/entity.schema.json`, and loads validated records into PostgreSQL (`wtc_evidence.entities`) and Neo4j (`:Entity` nodes).

```text
Markdown Session Reports ──► JSON Serialization ──► JSON Schema Validation ──► PostgreSQL / PostGIS ──► Neo4j Graph
```

## Pipeline Execution Stages
1. **Extraction:** Parser extracts entity metadata blocks (`entity_id`, `canonical_name`, `subsystem_id`, `building_level`, `confidence_score`).
2. **Schema Enforcement:** Schema validator validates JSON payloads against `schemas/entity.schema.json`.
3. **Relational Load:** Executes SQL UPSERT into `wtc_evidence.entities`.
4. **Graph Synchronization:** Executes Cypher MERGE into Neo4j graph database.
