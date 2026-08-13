# Production Deployment Test Plan

## Overview
This test plan defines validation criteria for schema deployment, data ingestion, query performance, and relationship integrity testing.

## Test Cases & Verification Matrix
1. **Schema DDL Validation:** Run `sql/schema.sql`, `sql/indexes.sql`, `sql/constraints.sql`, `sql/views.sql` on PostgreSQL 16. Verify zero errors.
2. **Neo4j Constraints Validation:** Run `neo4j/constraints.cypher` and `neo4j/indexes.cypher`. Verify index readiness.
3. **JSON Schema Contract Validation:** Validate seed JSON records against `schemas/entity.schema.json` and `schemas/relationship.schema.json`.
4. **Data Ingestion Verification:** Load 185 entities and 175 relationships into PostgreSQL and Neo4j. Verify exact record counts.
5. **Flow Chain Graph Traversal Testing:** Execute Cypher and SQL graph traversal queries for electrical, HVAC, water, and telecom chains. Verify unbroken path resolution.
6. **OpenAPI API Testing:** Test all 9 endpoints (`/entities`, `/trace`, etc.) using curl / Newman. Verify HTTP 200 responses.
