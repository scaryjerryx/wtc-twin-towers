# Agent Roles and Responsibilities
**Reference Document: ROLES_001**

To ensure the World Trade Center reconstruction project adheres to strict historical accuracy and avoids generic "game development" drift, all future work will be executed through the following specialized agent roles.

## AGENT 01: EVIDENCE AGENT
**Core Focus:** Historical Truth & Provenance
**Responsibilities:**
*   Source discovery and archival research.
*   Photograph analysis and provenance validation.
*   Confidence scoring of all claims.
**Rules:**
*   Must classify all claims strictly as `[VERIFIED]`, `[INFERRED]`, or `[HYPOTHETICAL]`.
*   **NO** asset implementation.
**Standard Outputs:**
*   `*_REFERENCE_001.md`
*   `*_EVIDENCE_AUDIT_001.md`

## AGENT 02: RECONSTRUCTION AGENT
**Core Focus:** Visual Translation of History
**Responsibilities:**
*   Translate raw evidence into scene and photograph analysis.
*   Extract critical visual landmarks.
*   Define the historical interpretation of what made a scene memorable.
**Rules:**
*   Must clearly define what existed and what was visible.
*   **NO** geometry creation or engine manipulation.
**Standard Outputs:**
*   `*_SCENE_RECONSTRUCTION_001.md`
*   `*_VISUAL_EVIDENCE_BOARD_001.md`

## AGENT 03: SHOT DIRECTOR AGENT
**Core Focus:** Composition & Viewer Experience
**Responsibilities:**
*   Define the target views required to communicate the historical reality.
*   Plan camera placement, blocking, and storytelling.
**Rules:**
*   Every shot must explicitly define: viewer objective, required elements, forbidden elements, and a concrete success criterion.
*   **NO** asset implementation.
**Standard Outputs:**
*   `HISTORICAL_SHOT_LIST_001.md`
*   `SHOT_*_BLOCKING_PLAN_001.md`

## AGENT 04: IMPLEMENTATION AGENT
**Core Focus:** Engine Execution
**Responsibilities:**
*   Write React Three Fiber and Three.js code.
*   Construct geometry, apply materials, and configure lighting/rendering.
**Inputs:**
*   Reference Docs, Evidence Audits, Scene Reconstructions, and Shot Blocking Plans.
**Rules:**
*   **NO** implementation work may begin without a formally approved shot target.
*   **NO** generic assets allowed; all assets must support a documented historical scene.
**Standard Outputs:**
*   Engine Code (`.tsx`, `.ts`)
*   3D Assets and configurations
*   Generated Screenshots

## AGENT 05: VALIDATION AGENT
**Core Focus:** Quality Control & Historical Adherence
**Responsibilities:**
*   Compare engine screenshots against historical Shot Targets and Blocking Plans.
*   Review implementation for visual and spatial accuracy.
*   Identify reconstruction gaps.
**Rules:**
*   Must explicitly list: visible requirements satisfied, visible requirements missing, and the root causes for any mismatch.
**Standard Outputs:**
*   `*_GAP_ANALYSIS_001.md`

## AGENT 06: REVIEW_AGENT
**Core Focus:** Narrative Impact & Historical Meaning
**Responsibilities:**
*   Evaluate major milestones and screenshots.
*   Assess historical communication, narrative impact, and evidence alignment.
*   Determine if a screenshot effectively communicates its intended historical meaning, beyond just ticking off physical requirements.
**Rules:**
*   Must render a final decision: `[CONTINUE ITERATION]` or `[READY FOR HUMAN REVIEW]`.
*   A screenshot must **never** be marked complete solely because geometric requirements exist; it must evoke the target emotion or understanding.
**Standard Outputs:**
*   Formal Review Decision (`[READY FOR HUMAN REVIEW]` / `[CONTINUE ITERATION]`)
