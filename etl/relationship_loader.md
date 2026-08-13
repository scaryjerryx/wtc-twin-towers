# ETL Relationship Ingestion Pipeline Specification

## Pipeline Overview
The Relationship Ingestion Pipeline extracts property graph edges, validates them against `schemas/relationship.schema.json`, enforces foreign key integrity against `wtc_evidence.entities`, and inserts directed edges into PostgreSQL (`wtc_evidence.relationships`) and Neo4j (`-[:REL_TYPE]->`).

```text
Session Relationship Blocks ──► Foreign Key Validation ──► PostgreSQL Graph Table ──► Neo4j Native Relationships
```

## Pipeline Execution Stages
1. **Extraction:** Parses directed edge tuples `(subject_id, relationship_type, object_id)`.
2. **Foreign Key Integrity Check:** Verifies both subject and object exist in `wtc_evidence.entities`.
3. **Relational Load:** Inserts edge into `wtc_evidence.relationships` with UNIQUE constraint enforcement (`unique_directed_edge`).
4. **Graph Synchronization:** Executes Neo4j Cypher APOC relationship creation.
