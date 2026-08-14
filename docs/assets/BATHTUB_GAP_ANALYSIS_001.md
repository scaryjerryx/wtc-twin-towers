# Reconstruction Gap Analysis: Bathtub Retaining Wall
**Reference Document: BATHTUB_GAP_ANALYSIS_001**

## Comparison Assessment

This analysis compares the current in-engine implementation against the historical requirements defined in `BATHTUB_SCENE_RECONSTRUCTION_001.md`.

### 1. Wall Height & Scale
*   **Requirement:** 70-foot deep sheer vertical cliff. Oppressive scale.
*   **Status:** Partially Visible.
*   **Analysis:** The strict numerical height (`Y=20` engine units) is correct. However, without street-level context (perimeter hoarding) or floor-level context (crawler cranes/workers), the human eye cannot resolve the scale. The pit feels like a small box rather than a massive 16-acre crater.

### 2. Wall Verticality
*   **Requirement:** Sheer vertical retaining wall.
*   **Status:** Currently Visible.
*   **Analysis:** The wall geometry is strictly vertical. However, the flat grey material (`#64748b`) lacks the rough, unfinished concrete texture cast against raw earth, causing it to read as smooth plastic rather than brutalist concrete.

### 3. Tie-Back Anchors
*   **Requirement:** Protruding angled steel caps arranged in precise horizontal grids.
*   **Status:** Partially Visible.
*   **Analysis:** The geometry (cylinders) and grid math exist. However, they read as small, abstract pegs rather than heavy steel anchor caps. They lack the bulky wedge/plate details that visually communicate "holding back thousands of tons of river pressure." The lighting does not cast the required sharp shadows to emphasize their depth.

### 4. Panel Seams
*   **Requirement:** Distinct vertical lines separating each 22-foot slurry pour.
*   **Status:** Partially Visible.
*   **Analysis:** The seams exist as distinct geometry (darker inset boxes). However, they look overly manufactured and artificial. Real slurry wall seams are rough, stained with mud/seepage, and slightly irregular where the concrete met the earth, not perfectly sharp right angles.

### 5. Bedrock Floor
*   **Requirement:** Rough, uneven, blasted Manhattan schist bedrock with groundwater puddles.
*   **Status:** Missing (Effectively).
*   **Analysis:** While geometry exists, it currently renders as a flat plane covered in scattered, abstract rotating cubes. It fails entirely to communicate the continuous, jagged organic texture of blasted solid bedrock. The "puddles" read as flat black circles rather than reflective water.

### 6. Visual Impact & Lighting
*   **Requirement:** Strong directional sunlight casting sharp, repetitive shadows from the tie-backs across the flat concrete.
*   **Status:** Missing.
*   **Analysis:** The flat, diffuse lighting of the scene prevents the brutalist grid of the tie-backs from popping. The scene lacks the high-contrast drama necessary to immediately communicate "massive engineered excavation."

## Summary of Gaps

The engine implementation successfully hit the *mathematical* requirements (22-foot panels, 70-foot depth, 4 rows of tie-backs), but failed the *visual identity* requirements. 

**Why the current implementation fails to match:**
1.  **Context-less Scale:** Massive structures require small recognizable structures (hoarding, cranes) to force perspective.
2.  **Texture vs. Geometry:** We relied on raw geometry to do the work of textures. Bedrock and concrete seams require high-fidelity bump/normal mapping, not just overlapping solid-color boxes.
3.  **Lighting Failure:** The drama of the Bathtub is defined by shadows cast across its sheer face, which the current lighting model does not support.
