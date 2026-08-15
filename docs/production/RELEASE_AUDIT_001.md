# RELEASE AUDIT 001

## 1. Files Approved for Release (RELEASE)
These files represent the canonical Day 1 state and should be committed:
- **Root**: `README.md`, `.gitignore`
- **Documentation**: `/docs/production/*`, `/docs/research/*`, `/docs/shots/*`, `/docs/assets/*`, `/docs/PROJECT_VISION_2026.md`
- **Source Code**: `/frontend/src/*` (React components, R3F hooks, Day1World.tsx, etc.)
- **Production Scripts**: `/frontend/capture_*.mjs`, `/frontend/download_textures.mjs`, `/frontend/debug_console.mjs`
- **Public Assets (Web-Ready)**: `.jpg`, `.png`, and `.gltf` files in `/frontend/public/`
- **Media**: Final canonical screenshots (`SHOT002_REALISM_V1.png`, `SHOT009_FINAL.png`, etc.) and walkthrough videos.

## 2. Files that Should be Archived (ARCHIVE)
These files provide historical context but do not need to be in the active production root.
- **Documentation**: `/docs/archive/*` (Completed Postmortems)
- **Scripts**: `/frontend/scripts/archive/*` (Already relocated during previous sprint)

## 3. Files that Should be Excluded (EXCLUDE)
These files were identified during the audit as repository bloat and should be either deleted or added to `.gitignore` prior to commit:
- **Intermediate Media**: The `/media/screenshots/shot009/` directory contains numerous intermediate renders (`SHOT009_V2.png` through `V7.png`, `_BEFORE.png`, `_AFTER.png`, etc.). These should be excluded or moved to the ignored `/media/screenshots/archive/` folder.
- **Raw 3D Source Files**: `/frontend/public/textures/` contains large raw source files like `.blend`, `.usdc`, `.mtlx`, and `.tres`. These are not served by Vite to the web client and heavily bloat the Git history. Only the baked `.jpg`/`.png` textures should be tracked.

## 4. Repository Risks
- **Git History Bloat**: If the `.blend` files and intermediate `SHOT009_V*.png` files are committed, it will permanently bloat the Git history by over 50MB. A cleanup of these specific files is highly recommended before the `git add .` command.
- **Quota Blocker**: SHOT005 remains in "Blockout" status because the Realism Pass is blocked by API quotas. The release must clearly state this is a Day 1 Preview, not a finalized Day 1.

## 5. Recommended Git Commit Plan
Assuming the exclusions above are handled:
1. `git add README.md docs/ .gitignore`
2. `git commit -m "docs: finalize governance and production architecture"`
3. `git add frontend/` (after excluding .blend files)
4. `git commit -m "feat(day1): implement Day 1 Radio Row demolition and Bathtub excavation"`
5. `git add media/` (after moving intermediate shot009 pngs to archive)
6. `git commit -m "chore(media): add canonical milestone renders and videos"`

## 6. Recommended Git Tag
- **Tag**: `v0.1.0-day1-preview`
- **Annotation**: "Day 1 Preview: August 1966 - Slurry Wall & Radio Row"

## 7. Recommended GitHub Release Description
**Title**: Day 1 Preview: Groundbreaking (August 1966)
**Description**: 
This release establishes the World Trade Center Historical Simulation's autonomous production pipeline. It includes the first batch of verified historical reconstructions:
- **SHOT002**: Suspended PATH Tubes
- **SHOT003**: Icanda Slurry Wall Operation
- **SHOT004**: Radio Row Demolition Edge
- **SHOT009**: Slurry Wall Vertical Slice

Built entirely on verified Port Authority evidence. *Note: SHOT005 (Observation Deck) is included as a structural blockout; realism pass pending API quota reset.*
