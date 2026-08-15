# DAY 1 MATERIAL ASSET LIBRARY 001

**FOCUS:** Actual asset acquisition for SHOT009 integration (Web-friendly, CC0 Priority)

## 1. Mud / Excavation Materials
* **Exact Source URL:** https://polyhaven.com/a/brown_mud_02
* **Exact Asset Name:** Brown Mud 02
* **License:** CC0 (Public Domain)
* **Texture Resolution:** 2K (Optimal for WebGL)
* **Download Instructions:** 
  1. Navigate to the URL.
  2. Select `2K` resolution.
  3. Ensure format is set to `ZIP` (or select `WebP` for manual map download).
  4. Extract the Diffuse/Color, Normal, Roughness, and Displacement maps into your project's `public/textures/mud/` directory.
* **R3F Integration Notes:** Load the maps array using `@react-three/drei`'s `useTexture` hook. Pass the maps directly into a `<meshStandardMaterial>`. If using the displacement map, ensure your floor `<planeGeometry>` has sufficient `args={[width, height, widthSegments, heightSegments]}` to subdivide the mesh, and tune `displacementScale` to avoid extreme artifacting.

## 2. Concrete Wall Materials (Slurry Wall)
* **Exact Source URL:** https://ambientcg.com/view?id=Concrete015
* **Exact Asset Name:** Concrete 015
* **License:** CC0 (Public Domain)
* **Texture Resolution:** 2K (JPG)
* **Download Instructions:**
  1. Navigate to the URL.
  2. Click the `2K-JPG` download button.
  3. Extract the Color, Normal, and Roughness maps into `public/textures/concrete/`.
* **R3F Integration Notes:** Load via `useTexture`. Because the slurry wall covers a massive area, you must tile the material. Iterate over the loaded texture maps and set `map.wrapS = THREE.RepeatWrapping` and `map.wrapT = THREE.RepeatWrapping`. Adjust the `repeat={[x, y]}` prop on the textures to maintain scale based on the wall dimensions. Skip displacement entirely to save performance.

## 3. Bedrock Materials (Manhattan Schist Base)
* **Exact Source URL:** https://polyhaven.com/a/layered_rock
* **Exact Asset Name:** Layered Rock
* **License:** CC0 (Public Domain)
* **Texture Resolution:** 2K (WebP)
* **Download Instructions:**
  1. Navigate to the URL.
  2. Select `2K` resolution.
  3. Extract maps to `public/textures/bedrock/`.
* **R3F Integration Notes:** Load with `useTexture`. Apply to your rock models or procedural rock geometries situated at the base of the excavation. For scattering bedrock chunks, apply this material to the template geometry used inside a `<InstancedMesh>` or R3F's `<Instances>` component to ensure a single draw call.

## 4. Tie-backs (Rusty Steel/Metal)
* **Exact Source URL:** https://ambientcg.com/view?id=Metal035
* **Exact Asset Name:** Metal 035
* **License:** CC0 (Public Domain)
* **Texture Resolution:** 1K or 2K (JPG)
* **Download Instructions:**
  1. Navigate to the URL.
  2. Click the `1K-JPG` or `2K-JPG` download button (1K is recommended for thin rods to save memory).
  3. Extract Color, Normal, Roughness, and Metalness maps to `public/textures/metal/`.
* **R3F Integration Notes:** Load via `useTexture`. Apply to `<cylinderGeometry>` representing the tie-back rods anchoring the slurry wall. Pass the metalness map to `<meshStandardMaterial metalnessMap={metalMap} />` and ensure the base `metalness` value is set to `1.0`. Use the roughness map to break up reflections and give an authentic weathered, industrial look.
