# V1.1 Vertical Slice 001: Day 1 (1966) Playable Experience

**Document Status:** 🎮 AUTHORITATIVE VERTICAL SLICE SPECIFICATION  
**Date:** August 13, 2026  
**Governing Law:** [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md)  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Scope:** 10-Minute Playable Experience — Day 1 (August 1966)  

---

## 1. VERTICAL SLICE OVERVIEW

The goal of Version 1.1 Vertical Slice 001 is **not to build the full 35-year complex**, but to deliver the smallest possible, fully playable 10-minute experience that proves the core vision of [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md).

```text
========================================================================================
                 VERTICAL SLICE 001: 7 PLAYABLE ENVIRONMENT LOCATIONS                 
========================================================================================
 [1] Visitor Spawn ──► [2] Demolition Zone ──► [3] Excavation Overlook
 (Church & Cortlandt)  (Radio Row Storefronts) (Bedrock & White Core Lines)
                                                        │
                                                        ▼
 [7] Slurry Wall Catwalk ◄── [6] Drawing Room ◄── [5] Trailer Interior ◄── [4] Trailer Exterior
 (West St / Slurry Trench)   (Drawing S-1 Table)   (Ammonia & Blueprints)  (PA Site Office)
========================================================================================
```

---

## 2. Playable Location Specifications

### Location 1: Visitor Spawn Location (Church & Cortlandt Street)
- **Geometry:** Cobblestone street intersection bounded by timber pedestrian hoarding fencing and the historic Cortlandt Street subway station exit stair hood.
- **Atmosphere:** Warm August morning sunlight filtering through NYC haze; dust motes floating near timber fencing.
- **Sounds:** City traffic, distant harbor tugboats, steam shovels, footsteps on timber decking.
- **Interactable Objects:** Wooden perimeter fence gap, painted direction sign (**"VISITOR PLATFORM & ARCHITECTURAL EXHIBIT ->"**).
- **Provenance Interaction:** Touching the wooden direction sign displays its historical site origin.
- **Evidence Overlay:** `Drawing A-A-18 (Site Boundary & Street Grid Plan, 1966)`.

---

### Location 2: Radio Row Demolition Zone
- **Geometry:** 19th-century brick commercial building facades in active dismantling state, heavy timber crane mats laid over dirt pathways.
- **Atmosphere:** Hazy brick dust, diesel fumes, smell of old pine timbers.
- **Sounds:** Cranking crane cables, brick masonry tumbling into steel dump hoppers, bulldozers idling.
- **Interactable Objects:** Demolished brick wall pile, surveyor transit tripod.
- **Provenance Interaction:** Inspecting surveyor transit reveals chalk-marked core column coordinates.
- **Evidence Overlay:** `Archival Site Survey Photo #NYA-1966-0805`.

---

### Location 3: Excavation Overlook Platform
- **Geometry:** Elevated 10x20ft timber viewing deck equipped with a wooden handrail, overlooking a 70ft deep excavated pit.
- **Atmosphere:** Open sky overhead, wind sweeping across the open pit, deep earth shadows.
- **Sounds:** Steam shovel buckets biting into bedrock, workers shouting depth callouts.
- **Interactable Objects:** Brass coin-operated viewing binoculars.
- **Provenance Interaction:** Looking through binoculars highlights the white chalk outlines of Core Box Columns 501–508 on exposed bedrock.
- **Evidence Overlay:** `Drawing S-1 (Bedrock Excavation & Foundation Footing Plan)`.

---

### Location 4: Construction Trailer Exterior
- **Geometry:** Green-painted wooden Port Authority field trailer raised on concrete cinder blocks with a 3-step wooden entry stair.
- **Atmosphere:** Shaded trailer wall, mud puddles around cinder blocks.
- **Sounds:** Hum of a window air conditioner unit, screen door spring squeak.
- **Interactable Objects:** Trailer wooden screen door handle, brass wall mailbox marked **"PANYNJ CHIEF FIELD ENGINEER"**.
- **Provenance Interaction:** Touching screen door handle triggers door open animation and interior transition.
- **Evidence Overlay:** `Contract Spec NYA-110.001 (Field Supervision Offices)`.

---

### Location 5: Construction Trailer Interior
- **Geometry:** 12x24ft narrow wooden trailer room with linoleum floor, pinboards, filing cabinets, and a central drafting table.
- **Atmosphere:** Cool air-conditioned air, strong smell of blueprint ammonia, pencil lead, and brewed coffee.
- **Sounds:** Window AC hum, paper rustling, wall clock ticking.
- **Interactable Objects:** Filing cabinet drawers, coffee pot, central drafting table.
- **Provenance Interaction:** Opening filing cabinet reveals historical site memos.
- **Evidence Overlay:** `PANYNJ Field Office Record Log #1966-01`.

---

### Location 6: Drawing Room (Drafting Table)
- **Geometry:** Heavy oak drafting table with brass desk lamp illuminating an unrolled blueprint sheet.
- **Atmosphere:** Warm focal desk lamp spot surrounded by dim ambient room lighting.
- **Sounds:** Ticking desk clock, soft pencil scratching ambient audio.
- **Interactable Objects:** **Drawing S-1 (Foundation & Slurry Wall Plan)** blueprint sheet.
- **Provenance Interaction:** Touching Drawing S-1 opens an interactive blueprint inspection mode.
- **Evidence Overlay:** `Drawing S-1 (Contract NYA-110.001) -- Slurry Wall Trench Detail & Core Column Footings`.

---

### Location 7: Slurry Wall Trench Catwalk (West Street / Hudson River Edge)
- **Geometry:** Narrow 4ft wide timber catwalk cantilevered over a 3,100ft continuous trench running along West Street.
- **Atmosphere:** Salty Hudson River breeze, gray bentonite slurry splash, bright riverfront sunlight.
- **Sounds:** Slurry pump chugging, clamshell bucket dropping into bentonite fluid, tugboat horns.
- **Interactable Objects:** Catwalk safety cable, bentonite slurry sampling bucket.
- **Provenance Interaction:** Touching safety cable highlights tieback anchor rods drilled into Hudson schist.
- **Evidence Overlay:** `Drawing S-2 (Slurry Wall Tieback Anchor Detail)`.

---

## 3. EVIDENCE & ASSET CLASSIFICATION MATRIX

```text
ASSET CLASSIFICATION MATRIX:
┌──────────────────────────────────────────────┬─────────────────────────┬────────────────────────────────────────┐
│ Asset / Environment Element                  │ Classification          │ Historical Evidence Basis              │
├──────────────────────────────────────────────┼─────────────────────────┼────────────────────────────────────────┤
│ Core Column Footing Coordinates (501-508)    │ AUTHORITATIVE           │ Drawing S-1 & S-2 Foundation Plans     │
│ Slurry Wall Trench Bounds & Tiebacks         │ AUTHORITATIVE           │ Icanda Ltd. Slurry Wall Contract Plans │
│ PANYNJ Site Office Trailer & Drawing S-1     │ AUTHORITATIVE           │ Drawing A-A-18 & Contract NYA-110.001  │
│ Radio Row Building Footprints                │ EVIDENCE-BACKED         │ 1966 Sanborn Fire Insurance Maps       │
│ Demolition Equipment & Steam Shovels         │ EVIDENCE-BACKED         │ 1966 PANYNJ Construction Photographs   │
│ Pedestrian Wooden Hoarding Fences & Signage  │ EVIDENCE-BACKED         │ Archival Press Photographs (Aug 1966)  │
│ Background Ambient Traffic & Tugboat Sounds  │ INTERPRETIVE            │ 1960s Lower Manhattan Acoustic Profile │
└──────────────────────────────────────────────┴─────────────────────────┴────────────────────────────────────────┘
```

---

## 4. SUCCESS CRITERION & PLAYABLE PROOF

By completing this 10-minute vertical slice, a visitor immediately understands:
1. This is a **living historical world** set on Day 1 (1966).
2. The core experience is **walking the site, entering drawing rooms, and touching historical evidence**.
3. Returning on future days will allow them to watch the towers rise through 2001.
