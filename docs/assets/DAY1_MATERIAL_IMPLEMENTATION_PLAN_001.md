# DAY 1 MATERIAL IMPLEMENTATION PLAN 001

**OBJECTIVE:** Implement the highest-impact Day 1 realism upgrades to immediately improve SHOT009 for the current Vite + React Three Fiber (R3F) build.

## 1. Mud / Excavation Materials

* **Source:** PolyHaven / ambientCG
* **Download Location:** polyhaven.com/textures (Search: `Brown Mud`, `Mud Track`) or ambientCG.com
* **License:** CC0 (Public Domain) - Free for commercial use, no attribution required.
* **Three.js Implementation Approach:** Load textures via `THREE.TextureLoader`. Apply to a `MeshStandardMaterial`. To achieve the deep track marks without heavy geometry, utilize parallax mapping or a `displacementMap` applied to a `PlaneGeometry` with appropriately subdivided segments.
* **R3F Implementation Approach:** Use the `useTexture` hook from `@react-three/drei` to load the PBR maps array. Apply them inside a `<meshStandardMaterial>` component attached to a `<mesh>` with `<planeGeometry>`.
* **Texture Map Requirements:** Color/Diffuse, Normal (GL format), Roughness, Displacement/Height, Ambient Occlusion (AO). Recommended 2K resolution, highly compressed WebP format to reduce bundle size.
* **Expected Performance Impact:** Moderate to High. If utilizing a `displacementMap`, the underlying geometry requires high vertex density, which can impact rendering times on lower-end devices. Fallback to normal maps only for lower quality settings.

## 2. Concrete Wall Materials (Slurry Wall)

* **Source:** ambientCG / PolyHaven
* **Download Location:** ambientCG.com (Search: `Concrete 015`, `Poured Concrete`)
* **License:** CC0 (Public Domain)
* **Three.js Implementation Approach:** Load textures via `THREE.TextureLoader`. Since the slurry wall is massive, texture tiling is critical. Set `texture.wrapS = THREE.RepeatWrapping` and `texture.wrapT = THREE.RepeatWrapping`, adjusting the `repeat` vector based on the world-scale dimensions of the wall meshes.
* **R3F Implementation Approach:** Load via `useTexture`. Iterate over the loaded maps to set wrap properties, or apply the `repeat={[x, y]}` prop directly if configuring texture objects. Bind to `<meshStandardMaterial>` on the wall geometries.
* **Texture Map Requirements:** Color/Diffuse, Normal, Roughness, AO. Displacement is unnecessary and should be avoided to save performance. Use repeating seamless textures.
* **Expected Performance Impact:** Low. The walls are relatively simple planar geometries. Standard PBR rendering without displacement keeps the vertex count low and GPU impact minimal.

## 3. Bedrock Materials (Manhattan Schist)

* **Source:** PolyHaven (Surfaces) / Sketchfab (3D Rock Assets)
* **Download Location:** polyhaven.com (Search: `Cliff Face`, `Layered Rock`) / sketchfab.com (Search: `CC0 Schist`, `Bedrock`)
* **License:** CC0 (Public Domain) or CC-BY (requires attribution in UI).
* **Three.js Implementation Approach:** For surfaces, apply PBR maps similarly to the concrete walls. For 3D scattered bedrock chunks, load the geometries via `THREE.GLTFLoader` and utilize `THREE.InstancedMesh` to render hundreds of rock variations in a single draw call.
* **R3F Implementation Approach:** Use `useGLTF` from `@react-three/drei` to load rock models. Use the `<Instances>` and `<Instance>` components from `drei` to efficiently scatter the bedrock meshes across the lowest points of the excavation site.
* **Texture Map Requirements:** Color/Diffuse, Normal, Roughness. For 3D models, textures should be heavily optimized. Utilize KTX2/Basis Universal texture compression for GLTF models to drastically reduce GPU memory footprint.
* **Expected Performance Impact:** High (if not optimized). Scattered 3D meshes can quickly bottleneck the CPU via draw calls if not instanced properly. Relying strictly on R3F `<Instances>` and KTX2 compressed textures will keep performance stable.
