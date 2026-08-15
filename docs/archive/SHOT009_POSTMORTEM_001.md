# SHOT009 Postmortem (Vertical Slice V1 & Realism Pass V2)

## Overview
SHOT009 focused on the Radio Row Demolition & Slurry Wall Excavation Era, acting as our first vertical slice to establish realism and environmental pipelines.

## Final Archived Scores
- **Technical**: 9/10
- **Historical**: 9/10
- **Narrative**: 8/10
- **Realism**: 10/10

## What Worked
- **PBR Material Integration**: Replacing flat placeholders with high-quality PBR textures (Concrete 015, Manhattan Schist Bedrock, Mud) drastically improved immersion and visual fidelity.
- **Atmospherics**: Implementing Drei's `<Sky>` component for early morning atmospheric scattering completely transformed the lighting and depth of the scene without requiring complex manual lighting setups.
- **Photorealistic Proxies**: Using 2D photorealistic cutouts (crawler crane, worker) as scale references effectively grounded the massive scale of the 70-ft bathtub excavation.

## What Failed
- **Custom GLSL Chroma Key Shaders**: The initial attempt to use custom chroma-key shaders for 2D proxies caused scale matrix distortion and severe green fringing due to JPEG compression artifacts. This workflow was abandoned.

## Reusable Systems Created
- **Drei `<Billboard>` Workflow**: A scalable, performant system for 2D photorealistic proxies using pre-keyed transparent PNGs, replacing the faulty chroma key pipeline.
- **Modular PBR Walls**: The Slurry Wall implementation can be reused for other foundation shots.
- **Skybox & Lighting Rig**: The August 1966 morning sky lighting setup can be applied to other Day 1 exterior scenes.
