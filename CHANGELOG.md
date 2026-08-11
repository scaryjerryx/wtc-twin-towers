# Changelog



All notable changes to this project will be documented in this file.

---

## [Unreleased]

### August 10, 2026 — Reconstruction Corpus & Planning Session

#### Acquisitions

- Gerrycan collections (4 ZIPs, 546MB): AA20a1, floor-96-A, floor-75-B, structural database
- Tower B exterior wall schedules (floors 1-9) — matching Tower A XLS
- Tower B exterior panel schedule (B2, 25MB) — comprehensive
- Upper floor exterior wall AB2/AB3 XLS (floors 107-110, both towers)
- Floor 75-B structural database (SDB + $2k files)
- WTC2 documentation (readme files, DJVU metadata, OCR text)

#### Gaps Closed

- CG-4 (Tower A Upper Wall Schedules) — CLOSED
- CG-1 (Tower B Structural) — Partially addressed

#### Readiness

- Overall: ~40% → ~50% (+10%)
- Tower B: 45% → 60% (+15%)
- Tower A: 60% → 65% (+5%)

#### Documents Produced

- `docs/GERRYCAN_COLLECTION_ASSESSMENT.md`
- `docs/READINESS_50_TO_80_REPLAN.md`
- `docs/ARCHITECTURAL_ACQUISITION_CAMPAIGN.md`
- `docs/SESSION_SUMMARY_2026_08_10.md`

#### Repository Documentation Sync

- `README.md` — Added reconstruction vision, living reconstruction concept, two timeline model, corpus status, readiness table, Prototype 0.1
- `docs/CURRENT_STATE.md` — Added reconstruction readiness, evidence corpus, gap status, current phase rules
- `docs/NEXT_TASK.md` — Updated to Architectural Evidence Acquisition Campaign
- `docs/AI_HANDOFF.md` — Added reconstruction vision, readiness, corpus, gap status, current phase rules
- `docs/ARCHITECTURE.md` — Added reconstruction layer (spatial hierarchy, two timeline model, living reconstruction, readiness)
- `CHANGELOG.md` — This update
- `.gitignore` — Added `WTC_CORPUS/` exclusion

### Completed

- M6 – Source Seeding Repair
- M7 – Search Request Generation
- M8 – Controlled Source Search
- M9 – Human Review & Manual Promotion
- M10 – Discovery Queue Repair
- M11 – Downloader Schema Additions
- M12 – Asset Registration & Provenance
- M13 – Downloader Repair & R2 Integration
- M14 – Controlled End-to-End Test
- M15 – Orchestrator Repair
- M16 – Knowledge Platform Import Repair
- M17 – Acquisition → Knowledge Pipeline Integration
- M18 – Citation Provenance Integration
- M19 – AI-Assisted Metadata Processing
- M20 – Asset Classification & Routing
- M21 – Photo Processing
- M22 – Independent-Source Verification
- M23 – Timeline Event Model

---

## [0.5.0] - 2026-08-08

### Completed Milestones

- M0 – Backup Verification
- M1 – Architecture Decisions
- M2 – Source Registry Reconciliation
- M3 – Limited Writer Role
- M4 – First Schema Migration
- M5 – Package / Import Repair
- M6 – Source Seeding Repair

### Added

- Discovery queue retry fields
- Discovery-to-queue foreign key
- Search candidate uniqueness controls
- Search candidate record type support
- Source governance metadata
- Package-safe discovery entry point

### Database

- Discovery queue migration completed
- Search candidate migration completed
- Writer role created and documented

### Documentation

- Architecture updates
- Session logging
- Milestone tracking
- AI handoff updates
- Current state tracking

### Fixes

- Discovery package import issue resolved
- M5 regression (unqualified import) discovered and repaired during M6
- Source seeding now supports URL upserts with accurate per-row status reporting