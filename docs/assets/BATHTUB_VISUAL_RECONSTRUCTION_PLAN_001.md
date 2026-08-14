# Visual Reconstruction Plan: The Bathtub Retaining Wall
**Reference Document: BATHTUB_VISUAL_RECONSTRUCTION_PLAN_001**

## Objective
To close the gap between mathematical accuracy and historical visual identity for the Bathtub Retaining Wall, shifting the scene from a "flat geometric model" to an oppressive, brutalist engineering marvel that matches 1968 archival photography. (Geometry dimensions are assumed correct and excluded from this plan).

---

## Ranked Interventions (By Visual Impact)

### 1. High-Contrast Directional Lighting (Max Impact)
**The Problem:** The current diffuse lighting flattens the sheer concrete face and hides the depth of the tie-back anchors, destroying the drama of the scene.
**The Intervention:**
*   Implement strong, high-contrast directional sunlight (representing late morning or early afternoon).
*   Ensure shadow casting is enabled on all tie-back caps to throw harsh, repetitive diagonal shadows down the vertical concrete face.
*   This single change establishes the "brutalist grid" effect that defines the historical photographs.

### 2. Implementation of Scale References (High Impact)
**The Problem:** A 70-foot drop means nothing without recognizable objects to force the viewer's brain to process the scale.
**The Intervention:**
*   **Floor Level:** Reintroduce a period-accurate crawler crane (mustard yellow or faded red) resting on the bedrock floor to establish the massive vertical height of the wall.
*   **Street Level:** Add continuous timber perimeter hoarding along the `Y=0` rim. Seeing a tiny human-scaled fence hanging precariously at the top edge of the crater immediately triggers an understanding of depth.

### 3. Material Fidelity: Rough Concrete (High Impact)
**The Problem:** The slurry wall currently reads as smooth, flat grey plastic.
**The Intervention:**
*   Replace standard solid-color shaders with physically based rendering (PBR) concrete materials.
*   The material must have high roughness and utilize normal maps to simulate concrete that was cast directly against raw, irregular earth. The surface should catch the new directional lighting with heavy micro-shadowing.

### 4. Textural Weathering: Moisture & Slurry Stains (Moderate Impact)
**The Problem:** The current walls look sterile, ignoring the reality of holding back the Hudson River.
**The Intervention:**
*   Apply dark, vertical streaking textures along the panel seams (`Y=0` down to `Y=-70`).
*   Incorporate rust streaks descending from the iron tie-back anchor caps.
*   Add pale grey dusting (dried bentonite slurry) to the lower third of the wall.

### 5. Photographic Composition (Moderate Impact)
**The Problem:** Arbitrary camera angles fail to capture the architectural intent of the historical HAER surveys.
**The Intervention:**
*   **Floor Camera (`BATHTUB_FLOOR`):** Lock the camera low to the bedrock, tilting sharply upward, placing a crawler crane in the immediate foreground while the sheer wall dominates the remaining 80% of the frame.
*   **Wide Camera (`BATHTUB_WIDE`):** Frame the shot from the street-level rim, ensuring the camera captures both the timber hoarding in the foreground and the 70-foot drop to the bedrock in the same shot, forcing perspective.

### 6. Material Fidelity: Blasted Bedrock (Moderate Impact)
**The Problem:** The pit floor looks like scattered children's blocks.
**The Intervention:**
*   Apply jagged, uneven normal/displacement maps to the bedrock floor geometry to read as solid Manhattan schist.
*   Upgrade groundwater puddles from flat black circles to highly reflective, low-roughness materials that catch the bright sky reflection, creating contrast against the dark rock.
