# CAPTURE SCRIPT AUDIT 001

## Overview
An audit of the `/frontend/*.mjs` Puppeteer capture scripts was conducted to identify active production workflows and prune superseded intermediate iterations, particularly focusing on the rapid `capture_shot009_v2-v7.mjs` generation cycle.

## Classification

### Recommended Production Scripts (KEEP)
These scripts represent the canonical, stable rendering pipelines for our major completed milestones.
- **`capture_bathtub.mjs`**: Generates the definitive `BATHTUB_WIDE` and `BATHTUB_FLOOR` perspectives.
- **`capture_path_tubes.mjs`**: Generates the definitive `PATH_TUBE_WIDE` perspective.
- **`capture_shot009.mjs`**: The canonical script for generating the Slurry Wall Vertical Slice (`SHOT009_FINAL.png`).
- **`debug_console.mjs`**: Core utility for headless browser log inspection.
- **`download_textures.mjs`**: Core asset pipeline script.

### Recommended Archive Scripts (ARCHIVE)
These scripts represent valuable configuration experiments (e.g., specific camera angles or lighting setups) that are not currently in the active build pipeline but hold historical reference value for Team A.
- **`capture_lighting.mjs`**: Contains specific R3F lighting coordinate tests.
- **`capture_scale.mjs`**: Contains specific FOV and scale-comparison camera tests.

### Recommended Removal Scripts (REMOVE / MERGE)
These scripts are superseded intermediate versions, exact duplicates, or early pipeline tests that clutter the repository.
- **`capture_shot009_v2.mjs` through `capture_shot009_v7.mjs`**: (REMOVE). These were rapid iterative tests adjusting camera pitch and yaw. `capture_shot009.mjs` is the merged, finalized version.
- **`capture.mjs` through `capture6.mjs`**: (REMOVE). Early pipeline tests that hardcoded absolute output paths to temporary `.gemini/brain/` directories rather than the canonical `/media/` folder.
- **`capture_screenshot.mjs`**: (REMOVE). Duplicate of early tests.
- **`capture_verification.mjs`**: (REMOVE). Superseded by specific `shotXXX` capture scripts.

## Action Plan
- Do not modify files. This audit serves as a guide for the next repository clean-up phase.
