# V1.1 Day 1 Asset Catalog 001: 1966 Production Assets

**Document Status:** 🎨 AUTHORITATIVE ASSET PRODUCTION CATALOG  
**Date:** August 13, 2026  
**Governing Law:** [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md)  
**Approved Specifications:** [`docs/V1_1_VERTICAL_SLICE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/V1_1_VERTICAL_SLICE_001.md) & [`docs/TECHNICAL_PROTOTYPE_001.md`](file:///opt/wtc/wtc-twin-towers/docs/TECHNICAL_PROTOTYPE_001.md)  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Target Performance:** React Three Fiber 60 FPS WebGL / Mobile & Desktop Compatible  

---

## 1. 3D ASSET ENUMERATION & CLASSIFICATION

Every 3D mesh asset required for the Day 1 (1966) playable vertical slice is enumerated, classified by historical provenance, and specified for LOD optimization below:

```text
========================================================================================
                      3D ASSET CLASSIFICATION & GEOMETRY MATRIX                        
========================================================================================
┌───┬─────────────────────────────────┬────────────────┬─────────────┬──────┬──────────┐
│ # │ Asset Identifier Name           │ Classification │ Poly Count  │ LODs │ Reuse    │
├───┼─────────────────────────────────┼────────────────┼─────────────┼──────┼──────────┤
│ 1 │ env_radio_row_terrain           │ AUTHORITATIVE  │ 12,000 tris │ LOD2 │ High     │
│ 2 │ env_slurry_wall_trench          │ AUTHORITATIVE  │ 8,500 tris  │ LOD2 │ High     │
│ 3 │ struct_core_column_footing_501  │ AUTHORITATIVE  │ 3,200 tris  │ LOD1 │ Medium   │
│ 4 │ prop_blueprint_table_drawing_s1 │ AUTHORITATIVE  │ 1,800 tris  │ LOD0 │ Unique   │
│ 5 │ prop_pa_site_trailer            │ AUTHORITATIVE  │ 4,500 tris  │ LOD2 │ High     │
│ 6 │ struct_timber_catwalk_overlook  │ EVIDENCE-BACKED│ 2,400 tris  │ LOD1 │ High     │
│ 7 │ env_radio_row_demolished_façade │ EVIDENCE-BACKED│ 6,200 tris  │ LOD2 │ Medium   │
│ 8 │ veh_bucyrus_erie_crane_1966     │ EVIDENCE-BACKED│ 14,000 tris │ LOD3 │ High     │
│ 9 │ veh_mack_dump_truck_1966        │ EVIDENCE-BACKED│ 9,500 tris  │ LOD3 │ High     │
│ 10│ prop_surveyor_transit_tripod    │ EVIDENCE-BACKED│ 2,100 tris  │ LOD1 │ Medium   │
│ 11│ prop_bentonite_slurry_grabber   │ EVIDENCE-BACKED│ 5,800 tris  │ LOD2 │ High     │
│ 12│ prop_cortlandt_subway_exit_hood │ INTERPRETIVE   │ 1,600 tris  │ LOD1 │ Unique   │
│ 13│ env_timber_hoarding_fence       │ INTERPRETIVE   │ 800 tris    │ LOD1 │ Modular  │
│ 14│ prop_pa_painted_visitor_sign    │ INTERPRETIVE   │ 450 tris    │ LOD0 │ Unique   │
│ 15│ prop_trailer_desk_lamp          │ INTERPRETIVE   │ 650 tris    │ LOD0 │ Unique   │
└───┴─────────────────────────────────┴────────────────┴─────────────┴──────┴──────────┘
```

---

## 2. AUDIO ASSET REQUIREMENTS

The soundscape uses spatial 3D audio positional nodes via the Web Audio API:

1. **Site Ambience (`audio_site_ambient_1966.mp3`):**  
   - *Composition:* Distant NYC street traffic, Hudson River tugboat whistles, coastal gulls, wind through scaffolding.  
   - *Type:* 2D Stereo Loop.
2. **Machinery & Excavation (`audio_diesel_excavator_idle.mp3`):**  
   - *Composition:* Bucyrus-Erie steam shovel engine idle, gravel dumping clatter, bentonite slurry pump chugging.  
   - *Type:* 3D Spatial Positional Audio Node centered at Excavation Pit `(-20, 0, -15)`.
3. **Office & Drawing Room (`audio_office_trailer_ac_hum.mp3`):**  
   - *Composition:* Window air conditioner unit hum, soft desk clock ticking, blueprint paper rustling.  
   - *Type:* 3D Spatial Positional Audio Node inside Trailer `(15, 0, -12)`.
4. **Voices & Work Calls (`audio_worker_callouts.wav`):**  
   - *Composition:* Ambient 1960s construction foreman depth callouts and vehicle backup horns.  
   - *Type:* Random Trigger Spatial Audio.

---

## 3. INTERACTABLE OBJECT DEFINITIONS

| Interactable Asset | Interaction Trigger | Provenance Data / Action |
| :--- | :--- | :--- |
| **`prop_pa_painted_visitor_sign`** | Look + Click / Tap | Displays historical context card: *"Radio Row Demolition & Site Groundbreaking (August 5, 1966)"*. |
| **`prop_surveyor_transit_tripod`** | Look + Click / Tap | Highlights white chalk outlines of Core Columns 501–508 on exposed bedrock. |
| **`prop_trailer_screen_door`** | Approach (<2m) / Click | Triggers door swing animation and switches camera bounds into Trailer Interior. |
| **`prop_blueprint_table_drawing_s1`** | Click / Tap Target | Opens **Drawing S-1 Provenance Inspection Overlay** (Contract NYA-110.001 evidence metadata). |
| **`struct_timber_catwalk_overlook`** | Walk onto boundary | Triggers audio shift to open pit wind and presents 70ft depth callout modal. |

---

## 4. MVP MINIMUM ASSET SET

The **MVP Minimum Asset Set** contains only the essential 7 assets required to launch the 60 FPS prototype:

```text
========================================================================================
                          MVP MINIMUM ASSET SET (7 ASSETS)                             
========================================================================================
 1. env_radio_row_terrain           ├── Base ground geometry & dirt/cobblestone texture
 2. env_timber_hoarding_fence       ├── Modular perimeter fence defining play area
 3. prop_pa_site_trailer            ├── Green field office trailer (exterior/interior)
 4. prop_blueprint_table_drawing_s1 ├── Oak drafting table with Drawing S-1 blueprint
 5. struct_core_column_footing_501  ├── Core column 501-508 bedrock footing markers
 6. env_slurry_wall_trench          ├── 70ft excavation pit & bentonite slurry trench
 7. prop_pa_painted_visitor_sign    └── Wooden directional entrance sign
========================================================================================
```

---

## 5. PRODUCTION READY SUMMARY

This asset catalog provides the complete enumeration, poly-budget, audio specification, and interactable map required to begin 3D modeling and R3F component assembly for the Day 1 (1966) playable experience.
