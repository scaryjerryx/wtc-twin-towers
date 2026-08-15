# PRODUCTION ROLES

## Autonomous Agent Governance Structure

The project has transitioned to an autonomous, multi-agent production system to ensure rapid, historically accurate, and high-quality 3D simulation development.

### Team A: Implementation
- **Role**: 3D Engineering & Rendering
- **Responsibilities**:
  - Implement basic blockout geometry in React Three Fiber.
  - Apply final PBR textures (Concrete, Metal, Wood) and atmospherics (fog, lighting) in the Realism Pass.
  - Produce authoritative milestone screenshots for review.
- **Ownership**: `/frontend/src/` and `TEAM_A_STATUS_001.md`.

### Team B: Research & Assets
- **Role**: Historical Context & Authenticity
- **Responsibilities**:
  - Research physical conditions, authentic materials, and architectural blueprints for a given shot.
  - Deliver reference material to guide implementation.
- **Ownership**: `/docs/research/` and `TEAM_B_STATUS_001.md`.

### Team C: Production Manager
- **Role**: Workflow Coordination & Repository Governance
- **Responsibilities**:
  - Execute Project Director directives.
  - Maintain the Production Board and ensure tickets are routed correctly.
  - Escalate only completed milestones or Technical Blockers.
  - Archive completed shot postmortems and organize files.
- **Ownership**: `DAY1_PRODUCTION_BOARD_001.md`, `/docs/archive/`.

### Team D: Critic
- **Role**: Quality Assurance & Calibration
- **Responsibilities**:
  - Establish specific evaluation criteria for each shot.
  - Evaluate rendered screenshots across four axes: Technical, Historical, Narrative, and Realism.
  - Prevent milestone escalation if scores fall below acceptable thresholds.
- **Ownership**: `/docs/shots/` and `TEAM_D_REVIEW_001.md`.

### Project Director
- **Role**: Vision & Direction
- **Responsibilities**:
  - Define high-level roadmap and shot objectives.
  - Review and approve/reject escalated milestones.
  - Declare sprints (e.g., Governance, Stabilization).
