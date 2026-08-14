# Agent Handoff Protocol & Governance
**Reference Document: HANDOFF_PROTOCOL_001**

This document establishes the strict governance rules and operational boundaries for transitioning tasks between specialized agents in the reconstruction pipeline.

## 1. Governance Rules

*   **Rule 1: No Unverified Geometry.** No geometry may be created or added to the engine without an explicit Evidence Reference, a completed Scene Reconstruction, and an approved Shot Target.
*   **Rule 2: No Subjective Success.** No screenshot or implementation may be considered "successful" or "finished" without a defined Shot Target and a formal Validation Review confirming the Success Criterion was met.
*   **Rule 3: No Generic Assets.** No asset may be added to the scene merely because it is a generic construction object (e.g., "we need a truck here"). All assets must structurally support a documented historical scene.

## 2. Handoff Mechanics

To maintain clean architectural boundaries, agents must communicate through formally generated documents rather than ad-hoc conversation.

### A. Evidence to Reconstruction
*   **Trigger:** The `*_EVIDENCE_AUDIT_001.md` is committed.
*   **Handoff:** The Reconstruction Agent consumes the audit to build the `*_SCENE_RECONSTRUCTION_001.md`. It may only use data explicitly passed through the audit.

### B. Reconstruction to Shot Director
*   **Trigger:** The `*_VISUAL_EVIDENCE_BOARD_001.md` is committed.
*   **Handoff:** The Shot Director Agent consumes the evidence board to craft the `HISTORICAL_SHOT_LIST_001.md` and subsequent `SHOT_*_BLOCKING_PLAN_001.md`. It relies on the visual landmarks identified in the reconstruction phase.

### C. Shot Director to Implementation
*   **Trigger:** The `SHOT_*_BLOCKING_PLAN_001.md` is committed.
*   **Handoff:** The Implementation Agent receives authorization to write code. It must configure the engine camera to match the blocking plan *before* tweaking assets or lighting. 

### D. Implementation to Validation
*   **Trigger:** A screenshot (e.g., `SHOT009_V1.png`) is generated.
*   **Handoff:** The Validation Agent consumes the screenshot and the original Blocking Plan to write the `*_GAP_ANALYSIS_001.md`. It must ruthlessly flag any deviation from the plan.

### E. Validation to Implementation (Iteration)
*   **Trigger:** The `*_GAP_ANALYSIS_001.md` is committed.
*   **Handoff:** The Implementation Agent resumes work, explicitly constrained to fixing *only* the specific failures identified in the gap analysis.
