# V1.1 Technical Prototype 001: R3F Browser Engine Architecture

**Document Status:** 💻 AUTHORITATIVE BROWSER PROTOTYPE SPECIFICATION  
**Date:** August 13, 2026  
**Governing Law:** [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md)  
**Approved Baseline:** [`docs/V1_1_VERTICAL_SLICE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_1_VERTICAL_SLICE_001.md)  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Tech Stack:** React 18, React Three Fiber (R3F), Three.js, TypeScript, Vite  

---

## 1. PROTOTYPE ARCHITECTURE & STACK

The V1.1 Technical Prototype is an uncompromised, zero-install 3D browser experience built using **React 18**, **React Three Fiber (R3F)**, **Three.js**, and **TypeScript**.

It renders 60 FPS interactive WebGL graphics on desktop and mobile devices.

```text
========================================================================================
                 V1.1 BROWSER PROTOTYPE ARCHITECTURE (REACT THREE FIBER)                
========================================================================================
  CLIENT BROWSER (Desktop WASD + Mouse / Mobile Virtual Joystick)
  └── Canvas (React Three Fiber Viewport)
      ├── 1. Temporal Skybox & Atmospheric Lighting (1966 NYC Haze)
      ├── 2. Environment Scene (Spawn, Trailer, Excavation, Slurry Wall)
      ├── 3. Character Controller & Collision Bounds (First-Person Camera)
      └── 4. Interactive Provenance Raycaster (Touch Drawing S-1)
  
  REST BACKEND GATEWAY (Optional Live Telemetry)
  └── FastAPI Server (http://localhost:8000/api/v1/entities)
========================================================================================
```

---

## 2. REPOSITORY FRONTEND STRUCTURE (`frontend/`)

```text
frontend/
├── public/
│   ├── assets/
│   │   ├── textures/ (dirt, cobblestone, timber, blueprint_s1.jpg)
│   │   └── audio/ (diesel_ambient.mp3, coastal_wind.mp3)
├── src/
│   ├── components/
│   │   ├── canvas/
│   │   │   ├── ExperienceCanvas.tsx      # R3F Master Canvas
│   │   │   ├── Day1Environment.tsx       # 1966 Site Geometry
│   │   │   ├── ConstructionTrailer.tsx   # Field Trailer & Screen Door
│   │   │   ├── DrawingRoom.tsx           # Drafting Table & Drawing S-1
│   │   │   └── ExcavationOverlook.tsx    # Bedrock Pit & Slurry Wall Catwalk
│   │   ├── controls/
│   │   │   ├── FirstPersonControls.tsx   # WASD + PointerLock / Mobile Joystick
│   │   │   └── InteractionRaycaster.tsx  # Touch & Raycast Click Listener
│   │   └── ui/
│   │       ├── HUD.tsx                   # 1966 Day 1 Time Indicator
│   │       ├── ProvenanceModal.tsx       # Evidence Inspection Card
│   │       └── MobileJoystick.tsx        # Touchscreen Navigation Overlay
│   ├── hooks/
│   │   └── useInteraction.ts            # Raycast Selection State
│   ├── App.tsx                           # Master React Shell
│   └── main.tsx                          # Vite Entrypoint
├── package.json
└── tsconfig.json
```

---

## 3. PROTOTYPE SCENE LAYOUT (4 CORE LOCATIONS)

The first prototype models **4 focused playable locations** to maintain 60 FPS performance across mobile and desktop browsers:

```text
PROTOTYPE SCENE SPATIAL MAP:
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ [Location A: Spawn Point] (0, 0, 10)                                                 │
│  - Cobblestone ground, wooden hoarding fence, Cortlandt subway exit hood             │
│  - Painted Wooden Sign: "VISITOR PLATFORM & ARCHITECTURAL EXHIBIT ->"                 │
│                                                                                      │
│                          │                                                           │
│                          ▼ (Walk along timber walkway)                               │
│                                                                                      │
│ [Location B: Site Office Trailer] (15, 0, -5)                                        │
│  - Green wooden PA trailer on cinder blocks                                          │
│  - Screen door with collision trigger leading into interior                          │
│                                                                                      │
│                          │                                                           │
│                          ▼ (Step inside)                                             │
│                                                                                      │
│ [Location C: Drawing Room] (15, 0, -12)                                              │
│  - Desk lamp illuminating Drafting Table                                             │
│  - Raycast Target: Drawing S-1 Blueprint (Triggers Provenance Modal)                 │
│                                                                                      │
│                          │                                                           │
│                          ▼ (Exit trailer & walk West)                                │
│                                                                                      │
│ [Location D: Excavation Edge & Catwalk] (-20, 0, -15)                                │
│  - 70ft deep excavated pit in Manhattan schist bedrock                               │
│  - White chalk marks outlining Core Columns 501-508                                  │
│  - Bentonite slurry wall trench along West Street edge                                 │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 4. LIGHTING, AUDIO & ATMOSPHERE

- **Lighting Setup:**
  - `DirectionalLight` (Sunlight): Warm August 1966 morning sun cast at 45° angle with soft shadow maps (`castShadow={true}`).
  - `AmbientLight`: Soft blue sky fill light (`intensity={0.4}`).
  - `PointLight` (Drawing Room): Warm 2700K tungsten lamp spot illuminating Drawing S-1 (`intensity={1.2}`).
- **Atmospheric Fog:** `Three.FogExp2` simulating 1966 NYC industrial atmospheric haze (`color="#e0ded7"`, `density=0.015`).
- **Audio Profile:** Web Audio API soundscape running spatial 3D positional audio:
  - Background: Distant NYC traffic, coastal harbor breeze, tugboat horns (`loop={true}`).
  - Proximity Audio: Diesel engine idle near excavation pit, AC hum inside trailer.

---

## 5. INTERACTION & PROVENANCE MODAL

When a visitor walks up to **Drawing S-1** on the drafting table and clicks or touches it:
1. `InteractionRaycaster.tsx` detects mesh collision.
2. Camera smoothly interpolates to a top-down inspection view (`useFrame` lerp).
3. `ProvenanceModal.tsx` overlay slides up presenting authoritative evidence data:

```text
PROVENANCE EVIDENCE INSPECTION OVERLAY:
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ 📐 DRAWING S-1: FOUNDATION & SLURRY WALL EXCAVATION PLAN                             │
├──────────────────────────────────────────────────────────────────────────────────────┤
│ Contract Ref: NYA-110.001 (Port Authority of NY & NJ Archive)                       │
│ Historical Date: Approved June 1966 | Active Site Execution: August 1966             │
│ Key Evidence: Depicts 3,100ft bentonite slurry wall perimeter trench & bedrock footings│
│ Supported Core Columns: Core Box Columns 501–508 Coordinates                          │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. CONTROLS & COMPATIBILITY MATRIX

- **Desktop Controls:**
  - Movement: WASD or Arrow Keys.
  - Camera Look: Pointer Lock API (Mouse Move).
  - Interact: Left Click or `E` key.
- **Mobile Controls:**
  - Movement: On-screen dual virtual touch joystick (`MobileJoystick.tsx`).
  - Camera Look: Touch drag.
  - Interact: Tap target.

---

## 7. PROTOTYPE SUCCESS CRITERION

Executing `npm run dev` in `frontend/` launches the WebGL canvas in under 2 seconds. A visitor stands in 1966, walks into the site trailer, touches Drawing S-1, and experiences the foundation of the World Trade Center reconstruction.
