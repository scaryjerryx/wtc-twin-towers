# V1.1 Implementation Backlog 001: Day 1 (1966) Playable Experience

**Document Status:** 📋 AUTHORITATIVE IMPLEMENTATION BACKLOG  
**Date:** August 13, 2026  
**Governing Law:** [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md)  
**Parent Specifications:**  
1. [`docs/V1_1_OPEN_WORLD_FOUNDATION.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_1_OPEN_WORLD_FOUNDATION.md)  
2. [`docs/VISITOR_ARRIVAL_EXPERIENCE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISITOR_ARRIVAL_EXPERIENCE_001.md)  
3. [`docs/V1_1_VERTICAL_SLICE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_1_VERTICAL_SLICE_001.md)  
4. [`docs/TECHNICAL_PROTOTYPE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/TECHNICAL_PROTOTYPE_001.md)  
5. [`docs/DAY1_ASSET_CATALOG_001.md`](file:///opt/wtc/wtc-twin-towers/docs/DAY1_ASSET_CATALOG_001.md)  
6. [`docs/PRODUCTION_PIPELINE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/PRODUCTION_PIPELINE_001.md)  

---

## 1. IMPLEMENTATION EPICS OVERVIEW

```text
========================================================================================
                 V1.1 DAY 1 PLAYABLE EXPERIENCE IMPLEMENTATION EPICS                   
========================================================================================
 [Epic A] Project Bootstrap          ├── Vite + React 18 + R3F + Three.js + TS Setup
 [Epic B] Terrain & World Geometry   ├── 1966 Ground Mesh, Excavation Pit & Slurry Trench
 [Epic C] Radio Row Environment      ├── Fences, Cortlandt Exit Hood & Direction Signs
 [Epic D] Construction Trailer       ├── PA Site Trailer Exterior, Screen Door & Interior
 [Epic E] Drawing Room               ├── Oak Drafting Table & Drawing S-1 Blueprint Mesh
 [Epic F] Provenance System          ├── Raycaster Click/Touch Listener & Evidence Modal
 [Epic G] Desktop Controls           ├── WASD Keyboard + Mouse PointerLock Controller
 [Epic H] Mobile Controls            └── Dual Touch Virtual Joystick & Tap Overlay
========================================================================================
```

---

## 2. FIRST 30 DEVELOPMENT TASKS (EXECUTION ORDER)

The first 30 concrete, testable tasks are ordered in exact execution sequence:

```text
FIRST 30 DEVELOPMENT TASKS (ORDERED EXECUTION SEQUENCE):
┌───┬────────┬────┬──────────────────────────────────────────┬──────────────────────────────────────────┐
│ # │ Epic   │ Pri│ Task Name                                │ Acceptance Test & Verification           │
├───┼────────┼────┼──────────────────────────────────────────┼──────────────────────────────────────────┤
│ 1 │ Epic A │ P0 │ Initialize `frontend/` Vite React TS app │ `npm run dev` starts local server on 5173│
│ 2 │ Epic A │ P0 │ Install R3F (`@react-three/fiber`, three)│ R3F Canvas renders a blue test cube      │
│ 3 │ Epic A │ P0 │ Configure R3F Canvas & Responsive Resize │ Canvas resizes smoothly on window drag   │
│ 4 │ Epic G │ P0 │ Implement Basic Keyboard WASD Hook       │ Console logs keypress state changes      │
│ 5 │ Epic G │ P0 │ Add PointerLock Camera Controller        │ Mouse drag rotates camera 360 degrees    │
│ 6 │ Epic B │ P0 │ Create `env_radio_row_terrain` Plane     │ Plane renders at Y=0 with dirt texture   │
│ 7 │ Epic B │ P0 │ Model 70ft Excavation Pit Depressions    │ Pit drops from Y=0 down to Y=-21m        │
│ 8 │ Epic B │ P0 │ Render White Chalk Core Column Lines     │ Core Box Columns 501-508 outlines visible│
│ 9 │ Epic B │ P0 │ Add Bentonite Slurry Trench Along West St│ Slurry trench mesh renders along pit edge│
│ 10│ Epic C │ P0 │ Model Modular Timber Hoarding Fence Mesh │ Fence encloses site boundary at Y=0      │
│ 11│ Epic C │ P0 │ Place Visitor Entrance Direction Sign    │ Painted "VISITOR PLATFORM ->" sign stands│
│ 12│ Epic D │ P0 │ Model `prop_pa_site_trailer` Box Mesh    │ Green PA Trailer renders at (15, 0, -5)  │
│ 13│ Epic D │ P0 │ Add Screen Door Mesh with Pivot Anchor   │ Door swings open when camera approaches  │
│ 14│ Epic D │ P0 │ Build Trailer Interior Linoleum Floor    │ Interior room bounds accessible at Y=0   │
│ 15│ Epic E │ P0 │ Model Oak Drafting Table Mesh            │ Drafting Table sits in center of Trailer │
│ 16│ Epic E │ P0 │ Apply `Drawing S-1` 4K Blueprint Texture │ Drawing S-1 details legible on table mesh│
│ 17│ Epic E │ P0 │ Add Tungsten PointLight Spot over Desk   │ Warm 2700K spot illuminates Drawing S-1  │
│ 18│ Epic F │ P0 │ Implement Raycaster Hover Target Listener│ Cursor changes style when hovering S-1   │
│ 19│ Epic F │ P0 │ Create `ProvenanceModal.tsx` React Overlay│ Modal opens on clicking Drawing S-1 mesh │
│ 20│ Epic F │ P0 │ Populate NYA-110.001 Provenance Metadata │ Modal displays verified S-1 evidence card│
│ 21│ Epic G │ P1 │ Add Bounding Box Player Collision Bounds │ Player cannot walk through trailer walls │
│ 22│ Epic C │ P1 │ Place Cortlandt Subway Hood Model        │ Cortlandt exit hood renders at Spawn     │
│ 23│ Epic B │ P1 │ Build Timber Overlook Viewing Platform   │ Viewing deck extends over excavation pit │
│ 24│ Epic B │ P1 │ Add Surveyor Transit Tripod Prop         │ Tripod stands on overlook deck          │
│ 25│ Epic H │ P1 │ Add Touch Virtual Joystick Overlay       │ Mobile touch drag moves player camera    │
│ 26│ Epic H │ P1 │ Add Tap-to-Interact Mobile Handler       │ Tapping Drawing S-1 opens modal on phone  │
│ 27│ Epic A │ P1 │ Add `Three.FogExp2` 1966 NYC Atmospheric │ Atmospheric fog blends distant horizon   │
│ 28│ Epic A │ P1 │ Configure Web Audio Ambient Soundscape   │ Background traffic audio plays on spawn  │
│ 29│ Epic A │ P1 │ Add Draco GLTF Asset Pipeline Script     │ Assets compressed to <8MB bundle size    │
│ 30│ Epic F │ P2 │ Build 10-Minute Day 1 Time Indicator HUD │ HUD displays "Day 1 (1966)" time badge   │
└───┴────────┴────┴──────────────────────────────────────────┴──────────────────────────────────────────┘
```

---

## 3. MVP DEFINITION & ACCEPTANCE CRITERIA

The **V1.1 Day 1 MVP** is complete when:
1. A user opens the URL in a browser on desktop or mobile.
2. The user spawns at Church & Cortlandt in 1966.
3. The user walks into the Port Authority site trailer.
4. The user approaches the drafting table and clicks **Drawing S-1**.
5. The **NYA-110.001 Provenance Modal** opens, displaying verified blueprint evidence.

Development is ready to begin on Task #1.
