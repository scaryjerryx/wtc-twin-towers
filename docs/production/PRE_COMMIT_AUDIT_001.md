# PRE-COMMIT AUDIT 001

## Executive Summary
This audit reviews all untracked files in the repository prior to the Day 1 Preview commit. The goal is to ensure the repository remains clean, performant, and aligned with the new Autonomous Production System architecture. No files have been deleted; this is an audit only.

## File Classification

### 1. `frontend/capture*.mjs`
**Classification: REMOVE / EXCLUDE**
- **Reasoning**: There are over 15 intermediate Puppeteer capture scripts (`capture2.mjs`, `capture_shot009_v2.mjs`, etc.) generated during the iterative realism passes. These clutter the codebase and are no longer necessary. They should be added to `.gitignore` or deleted.

### 2. `media/screenshots/archive/`
**Classification: EXCLUDE**
- **Reasoning**: This directory contains 15+ intermediate and duplicate high-resolution PNGs (e.g., `BATHTUB_LIGHTING_BEFORE.png`, `verification_spawn_...png`). Committing these will heavily bloat the Git history. They should be `.gitignore`d.

### 3. `docs/archive/`
**Classification: KEEP**
- **Reasoning**: Text-based postmortems (e.g., `SHOT002_POSTMORTEM_001.md`) are lightweight and provide valuable historical context on lessons learned. They should be tracked.

### 4. `media/screenshots/shotXXX/`
**Classification: KEEP**
- **Reasoning**: These are the final, canonical milestone renders (e.g., `SHOT004_REALISM_V1.png`) necessary for release notes and documentation.

### 5. `docs/production/`, `docs/research/`, `docs/shots/`
**Classification: KEEP**
- **Reasoning**: Core governance and workflow documents essential to the new autonomous system.

### 6. `frontend/public/textures/` and `frontend/public/models/`
**Classification: KEEP**
- **Reasoning**: Final PBR material dependencies required for the Day 1 Realism passes to render correctly.

## Recommended Commit Contents
- `docs/production/*`
- `docs/research/*`
- `docs/shots/*`
- `docs/archive/*`
- `frontend/src/*`
- `frontend/public/*`
- `media/screenshots/shotXXX/*`
- `media/videos/*`
- Root markdown files (`README.md`, `docs/PROJECT_VISION_2026.md`)

## Recommended Exclusions (.gitignore updates)
```text
# Exclude intermediate capture scripts
frontend/capture*.mjs
frontend/debug_console.mjs

# Exclude archival media to prevent repo bloat
media/screenshots/archive/*
```

## Expected Repository Impact
- **Without Exclusions**: Committing all untracked archival screenshots and scripts will bloat the repository by ~15-20MB of unnecessary binary data.
- **With Exclusions**: The commit will cleanly capture the Day 1 state, preserving only the canonical screenshots and text-based governance documents, resulting in a lean, professional history.
