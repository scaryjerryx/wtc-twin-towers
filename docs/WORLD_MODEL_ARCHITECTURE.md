# World Model Architecture

## Date: August 11, 2026

## Purpose

This document defines the World Model — the structured, time-aware, evidence-backed representation of the World Trade Center complex that serves as the core asset of the Reconstruction Platform.

---

## 1. What Is the World Model?

The World Model is the structured digital representation of the World Trade Center complex. It is:

- **Spatial** — Every element has a position in 3D space
- **Hierarchical** — Elements are organized from site down to individual objects
- **Time-aware** — Elements have historical states that change over time
- **Evidence-backed** — Every element references supporting historical evidence
- **Confidence-scored** — Every element carries a reconstruction confidence level
- **Queryable** — The model can be queried by location, time, type, and evidence

The World Model is NOT:

- The 3D renderer (that's React Three Fiber)
- The evidence database (that's the Evidence Engine)
- The user interface (that's the Reconstruction Platform)

The World Model is the **data** that powers everything else.

---

## 2. Spatial Hierarchy

### 2.1 Top-Level Structure

```
World Trade Center Complex
 └── Site (16-acre superblock)
      ├── Building
      │    ├── WTC 1 (North Tower)
      │    ├── WTC 2 (South Tower)
      │    ├── WTC 3 (Marriott Hotel)
      │    ├── WTC 4 (South Plaza Building)
      │    ├── WTC 5 (North Plaza Building)
      │    ├── WTC 6 (U.S. Customs House)
      │    └── WTC 7 (47-story office building)
      ├── Plaza (Austin J. Tobin Plaza)
      ├── Concourse (Underground mall and transit)
      └── Infrastructure
           ├── PATH Station
           ├── Subway Connections
           ├── Parking
           ├── Loading Docks
           └── Utilities
```

### 2.2 Tower Hierarchy

```
Tower (WTC 1 or WTC 2)
 └── Floor (1-110, plus sub-levels and mechanical)
      ├── Zone
      │    ├── Core Zone
      │    │    ├── Elevator Bank A
      │    │    ├── Elevator Bank B
      │    │    ├── Elevator Bank C
      │    │    ├── Elevator Bank D
      │    │    ├── Stairwell 1
      │    │    ├── Stairwell 2
      │    │    ├── Stairwell 3
      │    │    ├── Mechanical Shaft
      │    │    ├── Electrical Closet
      │    │    ├── Telephone Closet
      │    │    └── Restrooms
      │    ├── Tenant Zone
      │    │    ├── Office Space
      │    │    ├── Conference Room
      │    │    ├── Reception Area
      │    │    ├── Kitchen/Break Room
      │    │    └── Storage
      │    ├── Mechanical Zone
      │    │    ├── HVAC Equipment
      │    │    ├── Electrical Equipment
      │    │    ├── Plumbing Equipment
      │    │    └── Fire Protection Equipment
      │    └── Service Zone
      │         ├── Freight Elevator
      │         ├── Service Corridor
      │         └── Janitorial Closet
      └── Structural Elements
           ├── Perimeter Columns
           ├── Core Columns
           ├── Floor Trusses
           ├── Spandrel Beams
           ├── Core Walls
           └── Floor Slabs
```

### 2.3 Special Spaces

```
Special Spaces
 ├── Lobbies
 │    ├── Tower A Lobby (1st Floor)
 │    └── Tower B Lobby (1st Floor)
 ├── Sky Lobbies
 │    ├── Sky Lobby 44 (44th Floor, Tower A)
 │    └── Sky Lobby 78 (78th Floor, Tower A)
 ├── Observation Deck (107th Floor, Tower A)
 │    ├── Indoor Viewing Area
 │    ├── Outdoor Rooftop Deck
 │    └── Gift Shop
 ├── Windows on the World (107th Floor, Tower A)
 │    ├── Main Dining Room
 │    ├── Bar
 │    ├── Kitchen
 │    ├── Private Dining Rooms
 │    └── Reception Area
 ├── Mechanical Floors
 │    ├── 7th-8th Floors (Lower Mechanical)
 │    ├── 41st-42nd Floors (Mid Mechanical)
 │    ├── 75th-76th Floors (Upper Mechanical)
 │    └── 108th-109th Floors (Top Mechanical)
 └── Roof (110th Floor, Tower A)
      ├── Bulkhead
      ├── TV Mast Base
      └── Antenna Structure
```

---

## 3. Data Model

### 3.1 Core Entities

| Entity | Description | Key Attributes |
|--------|-------------|----------------|
| **Complex** | The entire WTC complex | name, location, boundary |
| **Site** | The 16-acre superblock | boundary, elevation, coordinates |
| **Building** | A structure on the site | name, type, footprint, height |
| **Tower** | A tower within a building | tower_id (A/B), floor_count |
| **Floor** | A single floor level | floor_number, elevation, slab_thickness |
| **Zone** | A functional zone on a floor | zone_type (core/tenant/mechanical/service) |
| **Space** | A defined room or area | space_type, area, dimensions |
| **Element** | A structural or architectural component | element_type, material, dimensions |
| **System** | A building system | system_type (HVAC/electrical/plumbing/elevator) |

### 3.2 Evidence Entities

| Entity | Description | Key Attributes |
|--------|-------------|----------------|
| **EvidenceReference** | Link between element and evidence | element_id, evidence_id, relevance |
| **EvidenceSource** | The original source material | source_type, url, file_hash, acquisition_date |
| **Confidence** | Reconstruction confidence level | score (0-100), level (verified/supported/etc.) |
| **Provenance** | Evidence acquisition history | source_organization, retrieval_date, rights |

### 3.3 Time Entities

| Entity | Description | Key Attributes |
|--------|-------------|----------------|
| **HistoricalState** | State of an element at a point in time | element_id, year, state_data |
| **ConstructionEvent** | A construction milestone | date, description, affected_elements |
| **ChangeEvent** | A modification to an element | date, description, before_state, after_state |
| **TimePeriod** | A named historical period | name, start_year, end_year |

### 3.4 Spatial Entities

| Entity | Description | Key Attributes |
|--------|-------------|----------------|
| **Position** | 3D position of an element | x, y, z coordinates |
| **BoundingBox** | 3D bounding volume | min_x, min_y, min_z, max_x, max_y, max_z |
| **Orientation** | Rotation of an element | rotation_x, rotation_y, rotation_z |
| **Dimensions** | Physical dimensions | width, depth, height |

---

## 4. PostgreSQL Schema Design

### 4.1 Spatial Hierarchy Tables

```sql
-- Complex
CREATE TABLE complexes (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Sites
CREATE TABLE sites (
    id SERIAL PRIMARY KEY,
    complex_id INTEGER REFERENCES complexes(id),
    name TEXT NOT NULL,
    boundary GEOMETRY(POLYGON, 4326),
    ground_elevation NUMERIC,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Buildings
CREATE TABLE buildings (
    id SERIAL PRIMARY KEY,
    site_id INTEGER REFERENCES sites(id),
    name TEXT NOT NULL,
    building_code TEXT,  -- WTC1, WTC2, etc.
    building_type TEXT,  -- tower, low-rise, plaza
    footprint GEOMETRY(POLYGON, 4326),
    height_m NUMERIC,
    floor_count INTEGER,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Towers
CREATE TABLE towers (
    id SERIAL PRIMARY KEY,
    building_id INTEGER REFERENCES buildings(id),
    tower_designation TEXT,  -- A, B
    structural_system TEXT,
    core_type TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Floors
CREATE TABLE floors (
    id SERIAL PRIMARY KEY,
    tower_id INTEGER REFERENCES towers(id),
    floor_number INTEGER NOT NULL,
    floor_name TEXT,  -- "1st Floor", "Sky Lobby 44", etc.
    floor_type TEXT,  -- office, mechanical, lobby, observation, restaurant, roof
    elevation_m NUMERIC,
    slab_thickness_m NUMERIC,
    floor_height_m NUMERIC,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Zones
CREATE TABLE zones (
    id SERIAL PRIMARY KEY,
    floor_id INTEGER REFERENCES floors(id),
    zone_type TEXT NOT NULL,  -- core, tenant, mechanical, service
    zone_name TEXT,
    area_sq_m NUMERIC,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Spaces
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    zone_id INTEGER REFERENCES zones(id),
    space_type TEXT NOT NULL,  -- office, corridor, elevator, stairwell, lobby, restroom, etc.
    space_name TEXT,
    area_sq_m NUMERIC,
    dimensions JSONB,  -- {width, depth, height}
    created_at TIMESTAMP DEFAULT NOW()
);

-- Elements
CREATE TABLE elements (
    id SERIAL PRIMARY KEY,
    space_id INTEGER REFERENCES spaces(id),
    floor_id INTEGER REFERENCES floors(id),
    element_type TEXT NOT NULL,  -- wall, column, beam, truss, door, window, etc.
    element_name TEXT,
    material TEXT,
    position JSONB,  -- {x, y, z}
    bounding_box JSONB,  -- {min_x, min_y, min_z, max_x, max_y, max_z}
    dimensions JSONB,  -- {width, depth, height}
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 4.2 Evidence Tables

```sql
-- Evidence References
CREATE TABLE evidence_references (
    id SERIAL PRIMARY KEY,
    element_id INTEGER REFERENCES elements(id),
    space_id INTEGER REFERENCES spaces(id),
    floor_id INTEGER REFERENCES floors(id),
    evidence_type TEXT NOT NULL,  -- blueprint, photo, report, drawing
    evidence_source TEXT NOT NULL,  -- 911research, ncstar, wtci, etc.
    evidence_identifier TEXT,  -- A-A-165, NCSTAR 1-1 p42, etc.
    evidence_url TEXT,
    evidence_file_path TEXT,
    relevance TEXT,  -- primary, secondary, contextual
    created_at TIMESTAMP DEFAULT NOW()
);

-- Confidence Scores
CREATE TABLE confidence_scores (
    id SERIAL PRIMARY KEY,
    element_id INTEGER REFERENCES elements(id),
    space_id INTEGER REFERENCES spaces(id),
    floor_id INTEGER REFERENCES floors(id),
    confidence_level TEXT NOT NULL,  -- verified, well_supported, supported, provisional, inferred, unknown
    confidence_score INTEGER CHECK (confidence_score BETWEEN 0 AND 100),
    source_count INTEGER,
    independent_source_count INTEGER,
    assessment_date TIMESTAMP DEFAULT NOW(),
    assessed_by TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### 4.3 Time Tables

```sql
-- Historical States
CREATE TABLE historical_states (
    id SERIAL PRIMARY KEY,
    element_id INTEGER REFERENCES elements(id),
    space_id INTEGER REFERENCES spaces(id),
    floor_id INTEGER REFERENCES floors(id),
    year INTEGER NOT NULL,
    state_data JSONB,  -- element-specific state at this year
    is_constructed BOOLEAN DEFAULT FALSE,
    is_operational BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Construction Events
CREATE TABLE construction_events (
    id SERIAL PRIMARY KEY,
    year INTEGER NOT NULL,
    month INTEGER,
    day INTEGER,
    event_type TEXT NOT NULL,  -- steel_erection, concrete_pour, facade_install, etc.
    description TEXT,
    affected_floors JSONB,  -- [1, 2, 3] or {"from": 1, "to": 10}
    affected_elements JSONB,  -- [element_ids]
    evidence_references JSONB,  -- [evidence_reference_ids]
    created_at TIMESTAMP DEFAULT NOW()
);

-- Time Periods
CREATE TABLE time_periods (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,  -- "Construction Era", "Operational Era", etc.
    start_year INTEGER NOT NULL,
    end_year INTEGER,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 5. Time-Awareness

### 5.1 Historical States

Every element in the World Model can have multiple historical states:

```
Element: Tower A 107th Floor East Wall
  State 1967: Not constructed
  State 1968: Under construction
  State 1970: Completed (original configuration)
  State 1976: Modified (Windows on the World opened)
  State 1993: Unchanged (bombing did not affect 107th floor)
  State 2001: Final state
```

### 5.2 State Transitions

Elements transition between states based on construction events:

```
Not Constructed → Under Construction → Completed → Modified → Final
```

### 5.3 Query by Time

The World Model supports temporal queries:

- "Show me Tower A as it was in 1973"
- "What did the 107th Floor look like in 1976 vs 1993?"
- "When was the 44th Floor Sky Lobby completed?"
- "What changed between 1968 and 1970?"

---

## 6. Evidence Integration

### 6.1 Evidence Linking

Every element in the World Model links to its supporting evidence:

```
Element: Tower A 107th Floor Restaurant East Wall
  → Evidence: A-A-165_0.png (107th Floor Plan - Restaurant Level)
    → Source: 911Research.net Blueprint Collection
      → Provenance: Whistleblower release, March 2007
        → Confidence: Verified (95%)
```

### 6.2 Evidence Types

| Evidence Type | What It Supports |
|---------------|-----------------|
| Architectural Blueprint | Wall positions, room layouts, door locations |
| Structural Drawing | Column positions, beam sizes, truss configurations |
| Construction Photo | Visual verification of as-built conditions |
| Engineering Report | Material specifications, structural analysis |
| Site Plan | Building positions, plaza layout, infrastructure |
| NCSTAR Report | Post-construction analysis and documentation |

### 6.3 Confidence Calculation

Confidence is calculated based on:

1. **Source count** — How many sources support this element
2. **Source independence** — Are sources independent or derivative
3. **Source quality** — Original drawings vs. secondary references
4. **Source relevance** — Direct evidence vs. contextual evidence
5. **Human review** — Has the evidence been reviewed

---

## 7. API Design

### 7.1 REST Endpoints

```
GET  /api/world/complex          — Get complex overview
GET  /api/world/site             — Get site data
GET  /api/world/buildings        — List all buildings
GET  /api/world/buildings/:id    — Get building details
GET  /api/world/towers/:id       — Get tower details
GET  /api/world/floors/:id       — Get floor details
GET  /api/world/floors?tower=:id — List floors in a tower
GET  /api/world/spaces/:id       — Get space details
GET  /api/world/spaces?floor=:id — List spaces on a floor
GET  /api/world/elements/:id     — Get element details
GET  /api/world/elements?space=:id — List elements in a space
```

### 7.2 Time-Aware Endpoints

```
GET  /api/world/state?year=1973           — Get world state at a year
GET  /api/world/floors/:id/state?year=1973 — Get floor state at a year
GET  /api/world/timeline                   — Get construction timeline
GET  /api/world/events?year=1968           — Get events for a year
```

### 7.3 Evidence Endpoints

```
GET  /api/evidence/element/:id       — Get evidence for an element
GET  /api/evidence/space/:id         — Get evidence for a space
GET  /api/evidence/floor/:id         — Get evidence for a floor
GET  /api/evidence/source/:id        — Get source details
GET  /api/evidence/confidence/:id    — Get confidence for an element
```

---

## 8. World Model Population

### 8.1 Current Evidence Available

| World Model Layer | Evidence Available | Status |
|-------------------|-------------------|--------|
| Site | Site plans, foundation drawings | Partial |
| Buildings | Building footprints, heights | Partial |
| Tower A Structural | AA20a1 structural sheets | Ready |
| Tower A Architectural | 211 blueprint drawings | Ready |
| Tower A Floors | Floor plans for all 110 floors | Ready |
| Tower A Core | Core plans for most floors | Ready |
| Tower A Elevators | 26 elevator drawings | Ready |
| Tower A Mechanical | 10 mechanical floor plans | Ready |
| Tower A Special Spaces | Windows on the World, Observation Deck, Sky Lobby 44 | Ready |
| Tower B | Limited structural data | Partial |
| Concourse | Sub-level plans | Partial |
| Plaza | Limited evidence | Minimal |

### 8.2 Population Priority

1. **Tower A** — Most complete evidence, start here
2. **Tower A Special Spaces** — High public interest
3. **Site and Plaza** — Context for towers
4. **Concourse** — Below-grade connections
5. **Tower B** — As evidence becomes available
6. **WTC 3-7** — Lower priority

---

## 9. Relationship to Other Systems

### 9.1 Evidence Engine → World Model

The Evidence Engine populates the World Model:

```
Evidence Engine                    World Model
─────────────                      ───────────
Discovery → Acquisition            (not directly connected)
Processing → Knowledge Extraction  → Elements, Spaces, Floors
Citations → Provenance             → Evidence References
Verification → Confidence          → Confidence Scores
Timeline → Events                  → Historical States
```

### 9.2 World Model → Reconstruction Platform

The World Model powers the Reconstruction Platform:

```
World Model                        Reconstruction Platform
───────────                        ──────────────────────
Spatial Hierarchy                  → 3D Scene Graph
Element Positions                  → 3D Geometry Placement
Historical States                  → Time Travel System
Evidence References                → Citation Panel
Confidence Scores                  → Visual Confidence Display
```

---

## 10. Success Criteria

The World Model is successful when:

1. Every floor of Tower A is represented with spatial data
2. Every major space has defined boundaries and type
3. Every element links to supporting evidence
4. Every element has a confidence score
5. Historical states exist for key time periods
6. The API serves world data efficiently
7. The model can be queried by location, time, and evidence

---

**Document prepared:** August 11, 2026  
**Status:** ✅ ARCHITECTURE DOCUMENT