# Reconstruction Pipeline Workflow
**Reference Document: WORKFLOW_001**

To prevent random asset creation and enforce a historically defensible reconstruction, all future development cycles must strictly adhere to this linear pipeline. Skipping phases is prohibited.

## The Linear Pipeline

1.  **Evidence Collection**
    *   *Actor:* Evidence Agent
    *   *Action:* Gather raw historical data, architectural plans, and archival photographs.
2.  **Evidence Audit**
    *   *Actor:* Evidence Agent
    *   *Action:* Classify every claim (`[VERIFIED]`, `[INFERRED]`, `[HYPOTHETICAL]`) based on the collected evidence.
3.  **Scene Reconstruction Analysis**
    *   *Actor:* Reconstruction Agent
    *   *Action:* Analyze the audited evidence to describe the physical layout, environment, and visual atmosphere of the historical moment.
4.  **Visual Evidence Board**
    *   *Actor:* Reconstruction Agent
    *   *Action:* Isolate key archival photographs that best represent the scene, extracting scale, depth, and complexity cues.
5.  **Historical Shot Definition**
    *   *Actor:* Shot Director Agent
    *   *Action:* Define the exact camera views required to recreate the scene's emotional and physical impact in the engine.
6.  **Shot Blocking Plan**
    *   *Actor:* Shot Director Agent
    *   *Action:* Break down the chosen shot into strict geometric relationships (Foreground, Midground, Background) before textures/lighting are considered.
7.  **Implementation**
    *   *Actor:* Implementation Agent
    *   *Action:* Write R3F/Three.js code to execute the blocking plan and scene requirements.
8.  **Screenshot Generation**
    *   *Actor:* Implementation Agent
    *   *Action:* Capture the rendered output directly from the engine camera.
9.  **Gap Analysis**
    *   *Actor:* Validation Agent
    *   *Action:* Compare the engine screenshot against the Shot Blocking Plan and Scene Reconstruction. Identify failures.
10. **Iteration**
    *   *Action:* Return to Step 7 (Implementation) to correct the identified gaps until the Validation Agent confirms the Success Criterion is met.
