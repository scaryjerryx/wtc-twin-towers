# REPOSITORY MAP

## Folder Structure

```
/opt/wtc/wtc-twin-towers/
│
├── docs/                      # Project Documentation Root
│   ├── production/            # Active Production Board, Status Reports, Sprint Docs
│   ├── research/              # Team B Historical Research and Asset References
│   ├── shots/                 # Team D Evaluation Criteria
│   ├── archive/               # Completed Postmortems and outdated documentation
│   └── assets/                # Asset Pipeline rules and documentation
│
├── frontend/                  # React Application Root
│   ├── public/                # Static assets
│   │   └── textures/          # PBR texture maps (concrete, metal, etc.)
│   └── src/
│       ├── components/        # React Components
│       │   ├── canvas/        # R3F 3D Scene Components (Day1World, Bathtub, etc.)
│       │   ├── controls/      # FirstPersonControls
│       │   ├── ui/            # Overlay interfaces (HUD, ProvenanceModal)
│       │   └── audio/         # Procedural Audio (SiteAudio)
│       └── App.tsx            # Application entry point
│
├── media/                     # Media Storage
│   └── screenshots/           # Milestone Renders
│       ├── shot002/           # SHOT002 (Suspended PATH Tubes)
│       ├── shot003/           # SHOT003 (Icanda Slurry Wall Operation)
│       ├── shot004/           # SHOT004 (Radio Row Demolition Edge)
│       ├── shot005/           # SHOT005 (Public Observation Deck)
│       ├── shot009/           # SHOT009 (Vertical Slice / Overlook)
│       └── archive/           # Duplicates and intermediate screenshot renders
```

## Document Ownership
- **Project Director**: Drives high-level objectives, approves milestones, sets policy.
- **Team A (Implementation)**: Owns `/frontend/src/` (Codebase) and `TEAM_A_STATUS_001.md`.
- **Team B (Research)**: Owns `/docs/research/` (Reference docs) and `TEAM_B_STATUS_001.md`.
- **Team C (Production Manager)**: Owns `DAY1_PRODUCTION_BOARD_001.md`, coordinates teams, archives milestones.
- **Team D (Critic)**: Owns `/docs/shots/` (Criteria) and `TEAM_D_REVIEW_001.md`.

## Workflow Paths
1. **Objective Initialization**: Project Director defines target (e.g., SHOT006). Team C updates Production Board.
2. **Research & Criteria**: Team B produces `SHOTXXX_REFERENCE.md`. Team D produces `SHOTXXX_EVALUATION_CRITERIA.md`.
3. **Blockout Pass**: Team A implements basic geometry in `/frontend/src/components/canvas/`. Generates `SHOTXXX_BLOCKOUT_V1.png`. Team D evaluates.
4. **Realism Pass**: Team A integrates final PBR textures and lighting. Generates `SHOTXXX_REALISM_V1.png`. Team D evaluates.
5. **Milestone Review**: Team C escalates to Project Director.
6. **Archive**: Upon approval, Team C creates `SHOTXXX_POSTMORTEM_001.md` and moves to next target.

## Screenshot Locations
All active, canonical milestone screenshots are stored in their respective shot subdirectories in `/media/screenshots/shotXXX/`. Intermediate drafts are housed in `/media/screenshots/archive/`.
