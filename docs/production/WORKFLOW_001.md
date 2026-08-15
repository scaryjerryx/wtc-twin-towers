# WORKFLOW ARCHITECTURE

## The Autonomous Cycle

1. **Directive Initialization**
   - Project Director sets a new Target Objective (e.g., "SHOT006").
   - Team C updates the Production Board.

2. **Research & Criteria Formulation**
   - Team B analyzes the historical requirements and produces `SHOTXXX_REFERENCE_001.md`.
   - Team D generates the specific grading rubric in `SHOTXXX_EVALUATION_CRITERIA_001.md`.

3. **Blockout V1**
   - Team A creates the initial untextured geometry focusing purely on composition and scale.
   - Team A renders `SHOTXXX_BLOCKOUT_V1.png`.
   - Team D reviews the blockout against criteria. If acceptable, it escalates to the Project Director.

4. **Realism Pass V1**
   - Upon Blockout approval, Team A applies PBR materials, atmospherics, and detailed assets.
   - Team A renders `SHOTXXX_REALISM_V1.png`.
   - Team D reviews. If acceptable, it escalates to the Project Director.

5. **Approval & Archival**
   - Upon Realism Pass approval, Team C creates a `SHOTXXX_POSTMORTEM_001.md`.
   - Team C archives the milestone, updates the board, and awaits the next target.

## Escalation Policy
To maintain high velocity, the autonomous system **only** halts to escalate to the human Project Director in two scenarios:
1. A visual milestone is ready for authoritative review.
2. An insurmountable Technical Blocker occurs (e.g., rendering API quota exhaustion).
