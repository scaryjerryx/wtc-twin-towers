# DAY 1 ASSET LIBRARY 001

**FOCUS:** Day 1 Excavation Scene - 3D Models & Assets (Web-friendly, CC0 Priority)

## 1. Historical Crawler Cranes
* **Exact URL:** https://sketchfab.com/search?q=crawler+crane+vintage&type=models&features=downloadable (Specific CC0 model recommendation: *Vintage Crawler Crane Low Poly* or similar free-to-download generic crawler)
* **License:** CC0 (Public Domain) or CC-BY (Attribution required)
* **glTF Availability:** Yes (Direct download as `.gltf` / `.glb`)
* **File Size:** ~4MB to 8MB (depending on texture resolution)
* **Three.js Compatibility:** Excellent. Standard PBR workflow. For R3F, load using `@react-three/drei`'s `useGLTF`. If rigged, utilize `useAnimations` to drive the boom/cables.

## 2. Construction Workers
* **Exact URL:** https://sketchfab.com/search?q=construction+worker+low+poly&type=models&features=downloadable
* **License:** CC-BY (Requires attribution)
* **glTF Availability:** Yes (.glb)
* **File Size:** ~2MB to 5MB (Keep vertex count low for scattering)
* **Three.js Compatibility:** Good. Ensure models are low-poly if instancing or placing multiple workers. Skinned meshes require care in Three.js; use `useAnimations` for idle/working loops.

## 3. Excavation Equipment (Bulldozers / Loaders)
* **Exact URL:** https://sketchfab.com/search?q=excavator+low+poly&type=models&features=downloadable
* **License:** CC0 or CC-BY
* **glTF Availability:** Yes (.glb)
* **File Size:** ~3MB to 6MB
* **Three.js Compatibility:** Excellent. Easily loaded as static props in the background of SHOT009 to provide scale and context to the massive excavation site.

## 4. Groundwater Puddles
* **Exact URL:** https://polyhaven.com/a/mud_cracked_puddles (or similar wet mud surface)
* **License:** CC0 (Public Domain)
* **glTF Availability:** N/A (Texture maps to be applied to planes or decals)
* **File Size:** ~5MB (for 2K WebP textures)
* **Three.js Compatibility:** High. Can be implemented using a simple plane overlapping the main mud geometry. Use `MeshStandardMaterial` or `MeshPhysicalMaterial` manipulating the roughness map (black for puddles) to achieve high reflectivity for standing water.

## 5. Bedrock Meshes (Schist Boulders/Chunks)
* **Exact URL:** https://polyhaven.com/search?t=models&q=rock
* **License:** CC0 (Public Domain)
* **glTF Availability:** Yes (PolyHaven supports direct `.glb` downloads for 3D assets)
* **File Size:** ~4MB to 10MB (Highly recommend downloading the 1K or 2K texture variant for web)
* **Three.js Compatibility:** Excellent. Ideal candidates for `THREE.InstancedMesh` or R3F's `<Instances>`. This will allow the Implementation Team to scatter hundreds of bedrock chunks at the base of the slurry wall with only a single draw call.
