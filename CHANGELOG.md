# Changelog

All notable changes to this project will be documented in this file.

---

## [Unreleased]

### Completed

- M6 – Source Seeding Repair

### Planned

- M7 – Search Request Generation
- M8 – Controlled Source Search
- M9 – Human Review & Promotion
- M10 – Discovery Queue Repair
- M11 – Downloader Schema Additions
- M12 – Asset Registration & Provenance
- M13 – Downloader Repair & R2 Integration
- M14 – Controlled End-to-End Test
- M15 – Orchestrator Repair

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
