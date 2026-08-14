# Asset Specification: Suspended PATH Tubes
**Reference Document: PATH_TUBE_ASSET_SPEC_001**

## 1. Geometry

**Element: Dual Parallel Tubes**
*   **Claim:** The Hudson & Manhattan crossing consisted of two parallel cast-iron tubes.
*   **Classification:** [VERIFIED]
*   **Source:** HAER NY-142; PANYNJ Engineering Archives.
*   **Confidence:** High
*   **Implementation guidance:** Model two distinct cylindrical meshes separated by a fixed track-width gap. Do not use a single large mass.

**Element: Outer Diameter**
*   **Claim:** The outer diameter of each tube was approximately 15 to 17 feet.
*   **Classification:** [VERIFIED]
*   **Source:** Standard 1909 H&M shield-driven tunnel specifications.
*   **Confidence:** High
*   **Implementation guidance:** Set cylinder radius to ~2.5 meters.

**Element: Flange Segmentation (Ribbing)**
*   **Claim:** The tubes were composed of bolted cast-iron rings creating heavy exterior ribbing.
*   **Classification:** [VERIFIED]
*   **Source:** HAER NY-142 close-up photography.
*   **Confidence:** High
*   **Implementation guidance:** Add protruding circular flanges (`radius + 0.2m`) at regular intervals (approx. 1 to 1.5 meters) along the entire length of the tube geometry.

## 2. Materials

**Element: Primary Material**
*   **Claim:** The primary material of the tubes was cast iron.
*   **Classification:** [VERIFIED]
*   **Source:** Historic American Engineering Record / 1909 construction records.
*   **Confidence:** High
*   **Implementation guidance:** Apply a metallic shader. Do not use flat matte shaders.

**Element: Support Material**
*   **Claim:** The support trusses were made of heavy-duty industrial steel.
*   **Classification:** [VERIFIED]
*   **Source:** *City in the Sky* (Glanz & Lipton); ENR 1968.
*   **Confidence:** High
*   **Implementation guidance:** Apply a standard steel/iron material with moderate reflectivity, distinct from the cast iron of the tubes.

## 3. Colors

**Element: Tube Color**
*   **Claim:** The tubes were a dark, oxidized rust-black/brown.
*   **Classification:** [INFERRED]
*   **Source:** Standard oxidation profiles of 60-year-old buried cast iron.
*   **Confidence:** High
*   **Implementation guidance:** Base color should be a very dark grey/black (`#1a1816`) mixed with deep brown rust undertones.

**Element: Safety Markings**
*   **Claim:** The bases of the support columns were painted with high-visibility safety stripes.
*   **Classification:** [INFERRED]
*   **Source:** Standard 1960s OSHA/PANYNJ heavy construction site safety protocols; B&W photo banding.
*   **Confidence:** Moderate
*   **Implementation guidance:** Add alternating bright orange (`#ea580c`) and white bands to the bottom 1 meter of the structural columns.

## 4. Weathering

**Element: Texture Surface**
*   **Claim:** The cast iron was heavily pitted and scarred from being buried in landfill since 1909.
*   **Classification:** [INFERRED]
*   **Source:** Metallurgical degradation of historic infrastructure.
*   **Confidence:** High
*   **Implementation guidance:** Apply high roughness (`0.95`) to the metallic shader. The surface should not look smooth or newly manufactured.

**Element: Bentonite/Mud Streaking**
*   **Claim:** The tubes were streaked with pale grey/tan mud and slurry dust.
*   **Classification:** [INFERRED]
*   **Source:** Proximity to the active slurry wall trenching operations.
*   **Confidence:** Moderate
*   **Implementation guidance:** Future texture passes should blend pale grey dirt maps onto the lower half of the tubes and support cradles.

## 5. Structural Supports

**Element: X-Braced Trusses**
*   **Claim:** The tubes were supported by vertical steel I-beam towers featuring dense X-bracing.
*   **Classification:** [VERIFIED]
*   **Source:** HAER NY-142 photography.
*   **Confidence:** High
*   **Implementation guidance:** Create complex truss geometry. Do not use simple solid boxes or fragile single poles. The supports must look capable of holding hundreds of tons of active train weight.

**Element: Bedrock Footings**
*   **Claim:** The trusses sat on thick concrete pads poured directly onto the bedrock floor.
*   **Classification:** [VERIFIED]
*   **Source:** *Engineering News-Record* (1968) diagrams of temporary tiebacks and underpinning.
*   **Confidence:** High
*   **Implementation guidance:** Anchor the steel columns into flat, wide concrete box geometries at `Y = -10` (pit floor).

**Element: Shared Cradles**
*   **Claim:** The two parallel tubes rested in shared, heavy steel saddle cradles atop the columns.
*   **Classification:** [VERIFIED]
*   **Source:** HAER NY-142 photography.
*   **Confidence:** High
*   **Implementation guidance:** Model a wide horizontal cross-beam directly under both tubes that transfers the load to the vertical columns.

## 6. Placement

**Element: Diagonal Crossing**
*   **Claim:** The tubes crossed the rectangular excavation pit diagonally.
*   **Classification:** [VERIFIED]
*   **Source:** PANYNJ site engineering plans; HAER aerial/wide photography.
*   **Confidence:** High
*   **Implementation guidance:** Apply a `Math.PI / 4` (45-degree) or similar Y-axis rotation to the entire tube group so it slices across the orthogonal grid of the slurry walls.

**Element: Suspension Height**
*   **Claim:** The tubes were suspended mid-air, with the pit floor excavated completely beneath them down to bedrock.
*   **Classification:** [VERIFIED]
*   **Source:** HAER NY-142; Darton, *Divided We Stand*.
*   **Confidence:** High
*   **Implementation guidance:** The tubes must be positioned at approximately `Y = -2`, while the pit floor is at `Y = -10`, leaving 8 scale meters of empty space beneath the tubes supported by the columns.
