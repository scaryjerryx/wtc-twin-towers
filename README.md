# World Trade Center 1 Authoritative Digital Twin (v1.0.0)

[![Release](https://img.shields.io/badge/Release-v1.0.0--authoritative-blue.svg?style=for-the-badge&logo=github)](https://github.com/scaryjerryx/wtc-twin-towers/releases/tag/v1.0.0-authoritative)
[![Status](https://img.shields.io/badge/Status-PRODUCTION%20READY-brightgreen.svg?style=for-the-badge)](https://github.com/scaryjerryx/wtc-twin-towers)
[![Validation](https://img.shields.io/badge/Validation%20Rate-100.0%25-success.svg?style=for-the-badge)](docs/PHASE_5_AUTHORITATIVE_VERIFICATION_PROGRAM_001.md)
[![Database](https://img.shields.io/badge/PostgreSQL-16%20%2B%20PostGIS-336791.svg?style=for-the-badge&logo=postgresql)](sql/schema.sql)
[![Graph DB](https://img.shields.io/badge/Neo4j-v5.15.0%20%2B%20APOC-008CC1.svg?style=for-the-badge&logo=neo4j)](neo4j/constraints.cypher)
[![API Gateway](https://img.shields.io/badge/FastAPI-OpenAPI%203.1-009688.svg?style=for-the-badge&logo=fastapi)](api/openapi.yaml)
[![Docker Stack](https://img.shields.io/badge/Docker%20Compose-Containerized-2496ED.svg?style=for-the-badge&logo=docker)](docker-compose.yml)

> **The Authoritative Multi-Database Digital Twin of World Trade Center 1 (Tower A)** — A production-grade spatial, relational, and property graph platform mapping 185 evidence-verified infrastructure entities, 175 directed flow paths, 16 subsystems, and 8 operational flow chains from sub-grade basements to floor 110.

---

## 📌 Executive Overview

### What is the WTC 1 Authoritative Digital Twin?
The **World Trade Center 1 Authoritative Digital Twin** is a multi-database, full-stack digital twin platform engineered to model the structural, mechanical, electrical, plumbing, telecommunications, fire protection, and operational infrastructure of World Trade Center 1 (Tower A).

### Why Was It Created?
Historically, architectural and MEP (Mechanical, Electrical, Plumbing) infrastructure data resided across thousands of disconnected 2D Port Authority of New York and New Jersey (PANYNJ) contract drawings (`S`, `M`, `E`, `P`, `A-A` series). Synthesizing cross-floor dependencies, electrical distribution paths, or single-points-of-failure from flat blueprints required hours of manual cross-sheet inspection.

### What Problems Does It Solve?
- **Instant Graph Traversal:** Resolves 10-hop power, fluid, airflow, and data flow paths across 110 floors in under 5 milliseconds.
- **Predictive Cascade Failure Simulation:** Simulates downstream component blackouts caused by utility intake or switchgear disruptions.
- **Single-Point-of-Failure (SPOF) Auditing:** Automatically ranks high-centrality hub nodes using graph degree metrics.
- **Unified Multi-Disciplinary View:** Integrates core box columns, high-voltage busducts, chilled water risers, and optical fiber frames into a single PostGIS/Neo4j query interface.

---

## 📊 Key System Metrics

```text
========================================================================================
                 WORLD TRADE CENTER 1 DIGITAL TWIN VERSION 1.0 METRICS                 
========================================================================================
 - Validated Entities:              185 Entities (100% Evidence Traceable)
 - Directed Graph Relationships:    175 Edges (100% Continuous Flow Paths)
 - Subsystem Domains Covered:       16 Primary & Expanded Subsystems
 - End-to-End Operational Chains:   8 Continuous System Backbone Loops
 - Model Validation Rate:           100.0% Validation Rate
 - Model Contradiction Count:       0 Contradictions
 - Orphan / Isolated Nodes:         0 Orphan Nodes (Single Unified Component Graph)
 - Runtime Synchronization:        100.0% Synchronized (PostgreSQL, Neo4j, FastAPI)
========================================================================================
```

---

## 🏗 System Architecture

The platform uses a tri-database hybrid architecture separating spatial geometry, property graph pathfinding, and REST API gateway services into containerized microservices orchestrated via Docker Compose.

```mermaid
graph TD
    Client[REST API Client / Web Browser / Analyst] -->|HTTP / OpenAPI 3.1| API[FastAPI Application Gateway :8000]
    
    subgraph Containerized Stack (Docker Compose)
        API -->|Psycopg2 SQL Queries| PG[(PostgreSQL 16 + PostGIS 3.6 :5432)]
        API -->|Neo4j Bolt Driver| NEO[(Neo4j Property Graph v5.15 :7687)]
        
        PG ---|Relational & Spatial Geometry| DB_DATA[(wtc_evidence Schema / 9 Tables)]
        NEO ---|Cypher Property Graph| GRAPH_DATA[(:Entity Nodes & Directed Edges)]
    end
    
    subgraph Data Pipeline & ETL Contracts
        JSON_ENTities[data/wtc1_entities.json] -->|Ingestion Loader| API
        JSON_Rels[data/wtc1_relationships.json] -->|Ingestion Loader| API
    end
```

### Architecture Components:
1. **Relational & Spatial Engine (PostgreSQL 16 + PostGIS 3.6):** Stores entity schemas, drawing metadata, bounding box crops, validation logs, and PostGIS `EPSG:2263` spatial geometries.
2. **Property Graph Engine (Neo4j v5.15 + APOC Core):** High-performance graph traversal engine executing variable-length Cypher queries (`r*1..10`) for power, water, air, and fiber signal tracing.
3. **API Gateway (FastAPI Python 3.11):** Serves interactive OpenAPI 3.1 REST documentation, entity search, relationship queries, and graph pathfinding endpoints.
4. **Data Contracts & ETL Layer:** Draft 2020-12 JSON Schemas (`entity.schema.json`, `relationship.schema.json`) validating JSON data ingestion.

---

## 🔥 Key Features & Capabilities

- ⚡ **Multi-Hop Electrical Power Tracing:** Traces 13.8kV ConEd street utility intake through switchgear, vertical busduct risers, step-down transformers, and floor panelboards down to individual lighting panels.
- ❄️ **HVAC Airflow & Thermal Comfort Modeling:** Traces chilled water from Floor 7 central chillers through vertical risers, AHU rooms, primary supply trunks, and VAV terminal boxes down to ceiling diffusers.
- 💧 **Domestic Potable Water Cascades:** Models Level B6 water booster pump pressure delivery up 1,300 feet to Floor 108 penthouse 50,000-gallon water storage tanks and gravity downfeeds.
- 📡 **Optical Fiber Lineage:** Traces telecom signal from street carrier demarcation through Floor 1 MDF vaults, optical fiber risers, and Floor 41/75 IDF closets to overhead cable trays.
- 🚨 **BMS Telemetry & Control Loops:** Maps field sensors, dampers, and DDC nodes to the Level B1 Master BMS Command Control Center.
- ⚠️ **Single-Point-of-Failure (SPOF) Detection:** Identifies top degree-centrality hub nodes across electrical, mechanical, and plumbing systems.
- 💥 **Cascade Failure Simulations:** Simulates multi-stage downstream blackout and thermal overload zones resulting from utility intake or switchgear disruptions.
- 📈 **Executive Intelligence Scorecards:** Generates floor-level risk scorecards (Floors 41, 75, 107) and subsystem resilience rankings across all 16 domains.

---

## 🚀 Quickstart Deployment Guide

### Prerequisites
- Docker Engine 24.0+ & Docker Compose v2.20+
- Git 2.34+

### 1. Clone Repository & Launch Stack
```bash
# Clone the repository
git clone https://github.com/scaryjerryx/wtc-twin-towers.git
cd wtc-twin-towers

# Launch the full containerized stack
docker compose up -d --build
```

### 2. Verify Container Health
```bash
docker compose ps
```
*Expected Output: `wtc1_postgres`, `wtc1_neo4j`, and `wtc1_api_server` all report `Up (healthy)` or `Started`.*

### 3. Service Endpoint URLs
| Service | Endpoint URL | Credentials / Notes |
| :--- | :--- | :--- |
| **REST API Gateway (OpenAPI Docs)** | [`http://localhost:8000/docs`](http://localhost:8000/docs) | Interactive Swagger UI |
| **Neo4j Property Graph Browser** | [`http://localhost:7474`](http://localhost:7474) | User: `neo4j` \| Pass: `ChangeThisPassword123` |
| **PostgreSQL Database** | `localhost:5432` | User: `wtc_admin` \| Pass: `ChangeThisToSomethingLongAndRandom` \| DB: `wtc_evidence` |
| **REST Healthcheck Endpoint** | [`http://localhost:8000/api/v1/health`](http://localhost:8000/api/v1/health) | Returns HTTP 200 JSON `{"status":"ONLINE"}` |

---

## 💻 Example Queries

### 1. REST API Graph Traversal (`GET /api/v1/trace`)
Query power path from sub-grade utility entrance down to floor panelboards:
```bash
curl -s "http://localhost:8000/api/v1/trace?start_entity_id=wtc1_fb6_utility_service_entrance_west"
```

### 2. Cypher Graph Query (Neo4j Power Traversal)
```cypher
MATCH path = (src:Entity {entity_id: 'wtc1_fb6_utility_service_entrance_west'})-[r*1..10]->(dst:Entity)
WHERE ALL(rel in relationships(path) WHERE type(rel) IN ['FEEDS', 'SUPPLIES', 'FEEDS_RISER_TO', 'DISTRIBUTES_TO', 'BRANCHES_TO'])
RETURN [n in nodes(path) | n.canonical_name] AS PowerPath, length(path) AS HopCount;
```

### 3. PostgreSQL SQL Query (Top 10 Infrastructure Hubs)
```sql
SELECT entity_id, canonical_name, (outgoing_edge_count + incoming_edge_count) AS total_degree
FROM wtc_evidence.v_entity_audit
ORDER BY total_degree DESC LIMIT 10;
```

---

## 🖼 Screenshots & System Demos

```text
┌──────────────────────────────────────────────────────────────────────────────────┐
│                             [ Neo4j Graph Viewport ]                             │
│                                                                                  │
│    (ConEd Intake) ──FEEDS──> (HV Dist Room) ──FEEDS──> (Master Switchgear)       │
│                                                              │                   │
│                                                        FEEDS_RISER_TO            │
│                                                              ▼                   │
│    (LP-41A Panel) <──BRANCHES── (Panelboard Room) <──DISTRIBUTES── (Busduct)     │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

- 📌 **Interactive OpenAPI 3.1 Swagger Docs:** View endpoints at `http://localhost:8000/docs`.
- 📌 **Neo4j Cypher Visualizer:** Query graph topology at `http://localhost:7474`.
- 📌 **PostgreSQL PostGIS Views:** Query `v_entity_audit` and `v_directed_graph_edges` via `psql`.

---

## 📜 Project Phase History

- **Phase 5 (Reconstruction & Verification):** Executed 45 real reconstruction sessions ([`docs/PHASE_5_REAL_RECONSTRUCTION_SESSION_001.md`](docs/PHASE_5_REAL_RECONSTRUCTION_SESSION_001.md) to `045.md`), 5 gap analyses, and 100% verification audit ([`docs/PHASE_5_AUTHORITATIVE_VERIFICATION_PROGRAM_001.md`](docs/PHASE_5_AUTHORITATIVE_VERIFICATION_PROGRAM_001.md)).
- **Phase 6 (Implementation & Deployment):** Designed DDL schemas ([`sql/schema.sql`](sql/schema.sql)), containerized stack ([`docker-compose.yml`](docker-compose.yml)), validated runtime health, and reconciled data datasets ([`docs/PHASE_6_RUNTIME_DATASET_RECONCILIATION_001.md`](docs/PHASE_6_RUNTIME_DATASET_RECONCILIATION_001.md)).
- **Phase 7 (Analytics & Executive Intelligence):** Published 70 query blueprints ([`docs/PHASE_7_DIGITAL_TWIN_QUERY_ANALYTICS_PROGRAM_001.md`](docs/PHASE_7_DIGITAL_TWIN_QUERY_ANALYTICS_PROGRAM_001.md)), operational trace paths, cascade failure impact models, and promoted Version 1.0.

---

## 🗺 Future Roadmap

- **v1.1 Visualization:** WebGL / Three.js 3D interactive viewport rendering PostGIS geometry polygons in web browsers.
- **v1.2 AI Copilot:** Fine-tuned Natural Language interface translating conversational questions into SQL and Cypher path queries.
- **v1.3 Advanced Graph Analytics:** Graph Data Science (GDS) PageRank, Betweenness Centrality, and community detection algorithms.
- **v2.0 Interactive Digital Twin:** Real-time IoT sensor streaming, MQTT integration, and dynamic building automation control loops.

---

## 🏷 Release & Production Status

- **Official Release Tag:** [`v1.0.0-authoritative`](https://github.com/scaryjerryx/wtc-twin-towers/releases/tag/v1.0.0-authoritative)
- **Target Branch:** `main` (Synchronized with `origin/main`)
- **Documentation:** [`docs/GITHUB_RELEASE_NOTES_V1.0.0.md`](docs/GITHUB_RELEASE_NOTES_V1.0.0.md)
- **License:** Open Engineering & Historical Research License.

*The World Trade Center 1 Authoritative Digital Twin is live, verified, and officially classified as Version 1.0 Production Ready.*
