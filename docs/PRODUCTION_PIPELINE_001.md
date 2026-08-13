# V1.1 Production Pipeline 001: 1966 Asset Creation Workflow

**Document Status:** 🛠 AUTHORITATIVE PRODUCTION PIPELINE SPECIFICATION  
**Date:** August 13, 2026  
**Governing Law:** [`docs/VISION_CONSTITUTION_001.md`](file:///opt/wtc/wtc-twin-towers/docs/VISION_CONSTITUTION_001.md)  
**Approved Assets:** [`docs/DAY1_ASSET_CATALOG_001.md`](file:///opt/wtc/wtc-twin-towers/docs/DAY1_ASSET_CATALOG_001.md)  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Target Output Format:** WebGL GLTF/GLB Binary + R3F Component JSX Wrappers  

---

## 1. CREATION METHODOLOGY & SOURCE PIPELINE MATRIX

Every 3D asset in [`docs/DAY1_ASSET_CATALOG_001.md`](file:///opt/wtc/wtc-twin-towers/docs/DAY1_ASSET_CATALOG_001.md) is mapped to its exact historical source archive, creation technique, and validation rule below:

```text
========================================================================================
                     ASSET CREATION METHODOLOGY & SOURCE MATRIX                         
========================================================================================
┌───┬─────────────────────────────────┬─────────────────────┬──────────────────────────┬──────────────────────────────────────┐
│ # │ Asset Identifier Name           │ Creation Method     │ Source Archive           │ Validation Method                    │
├───┼─────────────────────────────────┼─────────────────────┼──────────────────────────┼──────────────────────────────────────┤
│ 1 │ env_radio_row_terrain           │ Archival Derived    │ PANYNJ Site Grid Plan    │ PostGIS EPSG:2263 spatial overlay    │
│ 2 │ env_slurry_wall_trench          │ Archival Derived    │ Icanda Ltd. Wall Plans   │ Cross-section depth validation (70ft)│
│ 3 │ struct_core_column_footing_501  │ Hand Modelled       │ Drawing S-1 Column Specs │ Dimension check against PANYNJ S-1   │
│ 4 │ prop_blueprint_table_drawing_s1 │ Archival Derived    │ Contract NYA-110.001     │ High-res 4K scan texture alignment   │
│ 5 │ prop_pa_site_trailer            │ Hand Modelled       │ 1966 Field Office Photos │ Scale check against standard trailer │
│ 6 │ struct_timber_catwalk_overlook  │ Procedural          │ Site Scaffolding Specs   │ Structural timber span check         │
│ 7 │ env_radio_row_demolished_façade │ Photogrammetry / AI │ 1966 Archival Photos     │ Architectural brick bond alignment   │
│ 8 │ veh_bucyrus_erie_crane_1966     │ Hand Modelled       │ 1966 Crane Spec Manual   │ Scale check against manufacturer spec│
│ 9 │ veh_mack_dump_truck_1966        │ Hand Modelled       │ 1966 Mack Truck Schem.   │ Wheelbase & bed volume verification  │
│ 10│ prop_surveyor_transit_tripod    │ Hand Modelled       │ 1960s K&E Transit Spec   │ Height & optical scale check         │
│ 11│ prop_bentonite_slurry_grabber   │ Hand Modelled       │ Excavation Equipment Doc │ Clamshell bucket capacity check      │
│ 12│ prop_cortlandt_subway_exit_hood │ Hand Modelled       │ IRT Station Drawings     │ Hood geometry match to subway plans  │
│ 13│ env_timber_hoarding_fence       │ Procedural          │ Construction Wall Photos │ Tileable 8ft modular fence check     │
│ 14│ prop_pa_painted_visitor_sign    │ Hand Modelled       │ 1966 Site Entrance Photo │ Typography match to historical sign  │
│ 15│ prop_trailer_desk_lamp          │ Hand Modelled       │ 1960s Desk Lamp Catalog  │ Tungsten spot focal cone test        │
└───┴─────────────────────────────────┴─────────────────────┴──────────────────────────┴──────────────────────────────────────┘
```

---

## 2. PRODUCTION TOOLCHAIN & EXPORT PIPELINE

```text
========================================================================================
                     PRODUCTION TOOLCHAIN & CONVERSION WORKFLOW                         
========================================================================================
 ARCHIVAL SOURCES  ──►  3D MODELING & TEXTURING  ──► OPTIMIZATION ──► R3F INTEGRATION
 (PANYNJ Plans /      (Blender 4.2 /               (Draco /         (gltfjsx / 
  Sanborn Maps /       Substance 3D Painter)        KTX2)            React Components)
  Archival Scans)
========================================================================================
```

1. **Modeling & UV Layout:** Blender 4.2 LTS (Low-poly modeling, PBR UV unwrapping).
2. **Surfacing & Texturing:** Substance 3D Painter (PBR Metallic-Roughness workflow: Albedo, Normal, Roughness at 2K resolution).
3. **Geometry Compression:** Draco Mesh Compression & KTX2 / Basis Universal Texture Compression (Reduces 50MB scene to <8MB).
4. **React Three Fiber Conversion:** `@gltfjsx/cli` converts compressed `.glb` files directly into type-safe TypeScript React components (`<TrailerMesh />`).

---

## 3. MVP PRODUCTION ORDER & DEPENDENCY PHASING

```text
MVP PRODUCTION SEQUENCE (BUILD ORDER):
┌───────────────────────────────┬────────────────────────────────────────────────────────┐
│ Phasing Order                 │ Asset Set Included in Phase                            │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ PHASE 1: Core Ground (Day 1)  │ 1. `env_radio_row_terrain`                             │
│                               │ 2. `env_slurry_wall_trench`                            │
│                               │ 3. `struct_core_column_footing_501`                    │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ PHASE 2: Interactive Interior │ 4. `prop_pa_site_trailer`                              │
│                               │ 5. `prop_blueprint_table_drawing_s1`                   │
│                               │ 6. `prop_pa_painted_visitor_sign`                      │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ PHASE 3: Overlook & Details   │ 7. `struct_timber_catwalk_overlook`                    │
│                               │ 8. `prop_surveyor_transit_tripod`                      │
│                               │ 9. `env_timber_hoarding_fence`                         │
├───────────────────────────────┼────────────────────────────────────────────────────────┤
│ PHASE 4: Background Polish    │ 10. `veh_bucyrus_erie_crane_1966`                      │
│ (Post-MVP)                    │ 11. `veh_mack_dump_truck_1966`                         │
└───────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 4. ESTIMATED PRODUCTION EFFORT FOR DAY 1 MVP

- **Phase 1 (Terrain & Footings):** 2 Days (Blender ground mesh & PostGIS EPSG:2263 scale alignment).
- **Phase 2 (Trailer & Drawing S-1):** 3 Days (Trailer mesh modeling, high-res blueprint scan texture, Raycast trigger logic).
- **Phase 3 (Catwalk & Fencing):** 2 Days (Timber catwalk, modular fence instance, R3F lighting setup).
- **Phase 4 (R3F Assembly & Testing):** 2 Days (Draco GLTF export, `@gltfjsx` conversion, 60 FPS performance testing).
- **Total Estimated Effort:** **9 Engineering Days** to a fully playable 60 FPS Day 1 (1966) browser prototype.

---

## 5. DEVELOPER QUICKSTART: COMMENCING ASSET PRODUCTION

```bash
# 1. Install R3F GLTF Conversion CLI
npm install -g gltfjsx

# 2. Export Blender scene as compressed GLB to frontend/public/assets/
# 3. Generate TypeScript React Component from GLB
npx gltfjsx public/assets/models/day1_scene.glb --transform --types -o src/components/canvas/Day1Scene.tsx
```

The production pipeline is complete and ready for 3D modeling and R3F component generation.
