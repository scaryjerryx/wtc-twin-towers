# Reconstruction Platform Vision

## Date: August 11, 2026

## Purpose

This document defines the Reconstruction Platform — the browser-based, interactive, evidence-backed experience that is the product of the World Trade Center Reconstruction Project.

---

## 1. Platform Definition

The Reconstruction Platform is:

**A browser-based, interactive, time-aware 3D reconstruction of the World Trade Center complex where every element is traceable to supporting historical evidence.**

It is NOT:

- A static 3D model
- A video game
- A VR-only experience
- An AI-powered simulation
- A downloadable application

It IS:

- A web application accessible from any browser
- A historically accurate spatial reconstruction
- An evidence-citation system
- A time-travel experience
- A public historical resource

---

## 2. Core Experience

### 2.1 Spatial Navigation

Users navigate the WTC complex in 3D:

- Walk through the Austin J. Tobin Plaza
- Descend into the underground concourse
- Enter Tower A and Tower B lobbies
- Ride elevators to any floor
- Explore office floors
- Visit the Observation Deck (107th Floor)
- Dine at Windows on the World (107th Floor)
- Inspect mechanical floors
- Walk through sky lobbies (44th and 78th Floors)
- Explore the roof and TV mast

### 2.2 Time Travel

Users travel through the complex's history:

- **1966:** Site preparation, foundation excavation
- **1967:** Steel erection begins, Tower A rising
- **1968-1970:** Towers climbing, facade installation
- **1971-1973:** Completion, topping out, opening
- **1973-1993:** Operational era, tenant occupancy
- **1993:** Post-bombing repairs
- **1993-2001:** Modified operational era
- **2001:** Final state

### 2.3 Evidence Inspection

Users inspect the evidence behind any element:

- Click a wall → See the blueprint that defines it
- Click a column → See the structural drawing
- Click the restaurant → See the architectural plans
- Click the observation deck → See the evidence references

### 2.4 Confidence Display

Every element shows its reconstruction confidence:

- **Verified (95%):** Multiple independent sources
- **Well Supported (85%):** Two independent sources
- **Supported (70%):** One source
- **Provisional (50%):** Claim without direct evidence
- **Inferred:** Reconstructed from context
- **Unknown:** No evidence available

---

## 3. Technical Architecture

### 3.1 Stack

```
PostgreSQL World Database
        ↓
API Layer (REST/GraphQL)
        ↓
Next.js Application Shell
        ↓
React Three Fiber 3D Renderer
        ↓
Evidence Citation Overlay
        ↓
Browser (Desktop, Tablet, Mobile)
```

### 3.2 Component Responsibilities

| Component | Responsibility |
|-----------|---------------|
| **PostgreSQL** | Store World Model: buildings, floors, spaces, elements, evidence references, confidence scores, historical states |
| **API Layer** | Serve world data, evidence citations, and historical states to the frontend |
| **Next.js** | Application shell, routing, state management, UI components |
| **React Three Fiber** | 3D rendering, spatial navigation, time-travel transitions |
| **Evidence Overlay** | Citation display, confidence indicators, provenance information |

### 3.3 Browser Requirements

- WebGL 2.0 support (standard in all modern browsers)
- No plugins required
- No installation required
- Responsive design for all screen sizes

---

## 4. Evidence Citation System

### 4.1 Citation Chain

Every reconstruction element maintains a citation chain:

```
Element (e.g., "107th Floor East Wall")
  → Evidence Reference (e.g., "A-A-165, Sheet 1")
    → Source (e.g., "911Research.net Blueprint Collection")
      → Provenance (e.g., "Whistleblower release, March 2007")
        → Confidence (e.g., "Verified - 95%")
```

### 4.2 User Flow

1. User hovers over or clicks a reconstruction element
2. An evidence panel appears showing:
   - What the element is
   - What evidence supports it
   - Where the evidence came from
   - When the evidence was acquired
   - How confident the reconstruction is
3. User can expand to see:
   - Original source material (blueprint, photo, report)
   - Related evidence
   - Alternative interpretations
   - Open questions

### 4.3 Evidence Types Displayed

| Evidence Type | Display Format |
|---------------|---------------|
| Architectural Blueprint | PNG viewer with sheet reference |
| Structural Drawing | PNG viewer with drawing number |
| Engineering Report | PDF excerpt with page reference |
| Construction Photo | Image viewer with date and location |
| Site Plan | SVG/PNG with annotations |
| NCSTAR Report | PDF excerpt with section reference |

---

## 5. Historical Timeline System

### 5.1 Release Model

The public experiences the WTC as a **construction journey** released over time:

| Release Day | Historical Year | What's New |
|-------------|----------------|------------|
| Day 1 | 1966 | Site preparation, foundation |
| Day 2 | 1967 | Steel erection, Tower A base |
| Day 3 | 1968 | Tower A rising, Tower B foundation |
| ... | ... | ... |
| Day 35 | 2001 | Full operational complex |

### 5.2 Timeline Rules

- Users can travel backward to any previously released year
- Users can compare two historical states side by side
- Users cannot access unreleased future states
- After Day 35 (2001), the full timeline unlocks as a permanent archive

### 5.3 Construction Visualization

Long-term vision for construction-era visualization:

- Active crane models at appropriate positions
- Partially completed steel frames
- Concrete placement sequences
- Facade installation progress
- Construction staging areas with materials
- Temporary construction elevators
- Worker presence (stylized, not individual)

---

## 6. Spatial Navigation Design

### 6.1 Movement Modes

| Mode | Description |
|------|-------------|
| **Free Walk** | First-person walking through spaces |
| **Floor Jump** | Instant teleport to any floor |
| **Elevator Ride** | Animated elevator transition between floors |
| **Orbit View** | External orbit around buildings |
| **Section Cut** | Cross-section view of tower interior |

### 6.2 Navigation Landmarks

Key locations accessible from navigation:

- Austin J. Tobin Plaza (ground level)
- Tower A Lobby (1st Floor)
- Tower B Lobby (1st Floor)
- Concourse Level (below grade)
- Sky Lobby 44 (44th Floor)
- Sky Lobby 78 (78th Floor)
- Windows on the World (107th Floor)
- Observation Deck (107th Floor)
- Mechanical Floors (7-8, 41-42, 75-76, 108-109)
- Roof (110th Floor)

---

## 7. Visual Design Principles

### 7.1 Reconstruction Aesthetic

The visual style should communicate:

- **Historical accuracy** — Based on evidence, not artistic interpretation
- **Clarity** — Clean, readable, understandable
- **Honesty** — Uncertainty is visible, not hidden
- **Respect** — Appropriate tone for a historical reconstruction

### 7.2 Confidence Visualization

| Confidence Level | Visual Treatment |
|-----------------|------------------|
| Verified (95%) | Full detail, solid materials |
| Well Supported (85%) | Full detail, subtle transparency |
| Supported (70%) | Reduced detail, visible transparency |
| Provisional (50%) | Wireframe or outline |
| Inferred | Dashed outline, labeled |
| Unknown | Gray placeholder |

### 7.3 Time Visualization

- Current year displayed prominently
- Timeline scrubber for year selection
- Visual transitions between years
- Construction progress indicators

---

## 8. Platform Accessibility

### 8.1 Device Support

| Device | Minimum Requirements |
|--------|---------------------|
| Desktop | WebGL 2.0, 4GB RAM |
| Laptop | WebGL 2.0, 4GB RAM |
| Tablet | WebGL 2.0, 2GB RAM |
| Mobile | WebGL 2.0, 2GB RAM |

### 8.2 Performance Targets

| Metric | Target |
|--------|--------|
| Initial load | < 5 seconds |
| Floor transition | < 1 second |
| Year transition | < 2 seconds |
| Evidence panel open | < 500ms |
| Frame rate | 30+ FPS |

### 8.3 Fallback Experience

For devices that cannot run WebGL:

- 2D floor plan viewer
- Evidence browser
- Timeline explorer
- Photo gallery

---

## 9. Development Phases

### Phase A: World Model Foundation
- PostgreSQL schema for spatial hierarchy
- API endpoints for world data
- Basic 3D rendering of Tower A structural skeleton

### Phase B: Architectural Integration
- Floor plans integrated into 3D model
- Core and elevator systems
- Mechanical floors
- Special spaces (Windows on the World, Observation Deck, Sky Lobby 44)

### Phase C: Evidence Citation
- Click-to-cite system
- Evidence panel UI
- Confidence visualization
- Provenance display

### Phase D: Time Travel
- Historical state system
- Timeline scrubber
- Year transitions
- Construction visualization

### Phase E: Public Release
- Deployment
- Performance optimization
- Accessibility
- Documentation

---

## 10. Success Criteria

The Reconstruction Platform is successful when:

1. A user can open any modern browser and access the experience
2. The user can navigate the WTC complex in 3D
3. The user can travel through time (1966-2001)
4. The user can click any element and see its evidence
5. The user can understand reconstruction confidence
6. The experience works on desktop, tablet, and mobile
7. No installation, plugin, or app store is required

---

**Document prepared:** August 11, 2026  
**Status:** ✅ STRATEGIC VISION DOCUMENT