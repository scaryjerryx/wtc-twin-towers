# AI Working Principles & Project Governance Charter

**Document Status:** ✅ PERMANENT OPERATING CHARTER  
**Effective Date:** August 11, 2026  
**Target Audience:** All AI Agents, Subagents, Human Contributors, and System Engineers  

---

# Mission

The objective of the project is to build a **historically accurate, evidence-backed, browser-based reconstruction of the World Trade Center**.

- **The Reconstruction Platform is the product.** It is the browser-based, interactive 3D historical experience delivered to the public.
- **The Evidence Engine is a supporting system.** It is the automated discovery, acquisition, processing, knowledge extraction, and citation scaffolding that populates the World Model.

---

# Core Principles

### 1. Evidence First
No reconstruction claim may be treated as fact unless supported by evidence. Unsubstantiated claims or visual guesses must never be presented as established historical truth.

### 2. Never Invent Evidence
AI systems must never fabricate drawings, dimensions, photographs, dates, occupants, layouts, structural details, or architectural features. If evidence does not exist in the corpus, the system must not hallucinate mock data or fake citations.

### 3. Separate Evidence From Inference
Every conclusion, assertion, or model element must explicitly identify its epistemic classification:
- **Direct Evidence:** Supported directly by primary historical documents (e.g., Yamasaki blueprints, AA20a1 structural sheets).
- **Supported Inference:** Logically deduced from adjacent primary evidence (e.g., symmetrical core framing supported by perimeter schedules).
- **Hypothesis:** Plausible architectural configuration lacking direct corroborations.
- **Unknown:** Area where no evidence or reliable inference currently exists.

### 4. Preserve Uncertainty
Missing information should remain explicitly marked as unknown until direct evidence is acquired. Gaps in the historical record must be preserved and rendered transparently rather than hidden under aesthetic guesswork.

### 5. Provenance Required
Every major reconstruction element should be traceable back to original sources, including source organization, acquisition date, URL, file hash, and drawing sheet reference.

### 6. Confidence Scoring
Use transparent, standardized confidence levels across all World Model elements and assertions:
- **95% Verified:** Corroborated by multiple independent primary sources.
- **85% Well Supported:** Supported by two independent sources or high-quality primary drawing set.
- **70% Supported:** Supported by a single direct source.
- **50% Provisional:** Claim or element supported by indirect context without direct drawing evidence.
- **25% Speculative:** Inferred from context, structural patterns, or building codes without specific evidence.

### 7. No Symmetry Assumptions
Tower B (WTC 2) must not be assumed to match Tower A (WTC 1) unless supported by explicit evidence. While the towers shared major structural concepts, differences existed in mechanical floors, Sky Lobby configurations, exterior wall details, tenant fit-outs, TV antenna structures, and height.

### 8. The World Model Is The Core Asset
The World Model (the structured, time-aware PostgreSQL spatial representation of the complex) is the core asset of the project. Temporary processing scripts, scrapers, or ephemeral pipeline tools are secondary scaffolding built solely to serve and populate the World Model.

### 9. Browser First
Target platform:
- **Desktop Browser** (Chrome, Firefox, Safari, Edge)
- **Tablet Browser** (iPadOS, Android)
- **Mobile Browser** (iOS, Android)

No installation required. No plugins. No downloadable client. No app-store dependency. Powered by native WebGL 2.0.

### 10. AI Is A Development Tool
AI systems assist with:
- Research and source discovery
- Document and blueprint analysis
- Software architecture design
- Code generation, verification, and testing

AI is **NOT** a runtime dependency. The final Reconstruction Platform must function independently without requiring live AI API queries or active LLM runtime models.

### 11. Traceable Reconstruction
Users should ultimately be able to click or inspect any reconstructed object (wall, column, room, window, elevator) and view the supporting evidence, blueprint snippet, confidence level, and provenance chain behind it.

### 12. Historical Integrity
Where evidence sources conflict (e.g., design drawing vs. as-built photograph vs. post-event report), preserve the conflict, document the disagreement, and present the competing evidence transparently rather than silently resolving the discrepancy.

### 13. Reconstruction Before Enhancement
Priority must always be given to reconstructing verified physical geometry before adding enrichment features.

Examples:
- Building geometry before furnishings
- Structural accuracy before aesthetics
- Evidence-backed layouts before decorative content
- Reconstruction scope before commemorative features

Additional historical, memorial, tenant, and storytelling layers are important but must not delay completion of the core reconstruction.

### 14. Preserve Buildability
When evaluating evidence acquisitions, prioritize evidence that directly increases World Model completeness.

Evidence should be ranked by:
1. Reconstruction impact
2. World Model value
3. Citation value
4. Historical interest

Research work should maximize reconstruction readiness.

---

# Research Prioritization Framework

All research, evidence acquisition, and processing tasks must adhere to the following priority hierarchy:

- **Priority 1: Critical Reconstruction Blockers**  
  Primary structural and architectural drawing collections without which fundamental 3D geometry cannot be established (e.g., Tower B structural sheets, missing sky lobby architectural plans, site-level civil plans).
- **Priority 2: Major Architectural Gaps**  
  Secondary building documentation, overall site boundary plans, concourse layouts, upper exterior wall schedules, and building envelope details (e.g., WTC 3–7 documentation, MEP risers).
- **Priority 3: Interior Detail**  
  Interior layout plans, lobby finishes, core tenant layouts, elevator/escalator schedules, and floor-specific fit-outs.
- **Priority 4: Enhancement and Enrichment**  
  Construction progress photographs, interior lifestyle photography, historical tenant directories, audio/video recordings, and ambient environmental data.

---

# Current Major Evidence Gaps

*Derived from repository evidence (`EVIDENCE_GAP_REPORT.md`, `README.md`, `CORPUS_INVENTORY.md`):*

### Critical Gaps (Priority 1)
- **CG-1: Tower B (South Tower) Structural Drawings** — Structural engineering sheets equivalent to AA20a1 for WTC 2 are missing from the corpus.
- **CG-2: Tower B Architectural Floor Plans & Upper Sky Lobbies** — While Tower A floor plans are ~85% complete (211 blueprints acquired), Tower B interior layouts and upper vertical circulation (Sky Lobby 78 drawings) remain incomplete.
- **CG-3: Site Plan & Austin J. Tobin Plaza Documentation** — Site-level civil and landscape plans showing the exact spatial relationship between buildings, Tobin Plaza, concourse entrances, and surrounding street infrastructure are currently minimal (Plaza readiness at 25%, Site at 40%).
- **CG-4: Tower A Exterior Wall Schedules (Floors 10–110)** — Current exterior wall XLS schedules cover only floors 1–9. Upper floor wall panel and spandrel transitions require data for floors 10–110.

### Important Gaps (Priority 2 & 3)
- **IG-1: Construction Photographs (1966–1973)** — Needed to verify as-built structural sequencing and support the 35-day historical construction journey mode.
- **IG-2: Interior Photographs** — Missing visual verification for completed lobbies, Sky Lobbies, Windows on the World, Observation Deck, and office interiors.
- **IG-3: Buildings 3–7 Documentation** — WTC 3 (Marriott Hotel), WTC 4, WTC 5, and WTC 6 have 0% architectural/structural evidence in the corpus. WTC 7 is partially documented (60%).
- **IG-4: Mechanical, Electrical, & Plumbing (MEP) Drawings** — Missing system risers and detailed mechanical room layouts for floors 7–8, 41–42, 75–76, and 108–109.
- **IG-5: Architectural Elevations & Building Sections** — Detailed facade cladding, column cover profiles, and building vertical cross-sections.
- **IG-6: Foundation & Subgrade Documentation** — Slurry wall ("bathtub") engineering, basement sub-levels 1–5, and PATH station integration.

---

# Success Criteria

*Summarized from `README.md`, `PROJECT_VISION_2026.md`, `RECONSTRUCTION_PLATFORM_VISION.md`, and `WORLD_MODEL_ARCHITECTURE.md`:*

1. **Universal Web Accessibility:** A user can open any modern desktop, tablet, or mobile browser and interact with the 3D WTC complex smoothly with zero installation or plugins.
2. **3D Spatial Navigation:** Users can walk through the Tobin Plaza, descend into the concourse, enter tower lobbies, ride elevators, explore office floors, visit Windows on the World, and step onto the 107th floor Observation Deck.
3. **Interactive Evidence Citation (Click-to-Cite):** Users can click any reconstruction element (wall, column, space) and immediately view an evidence overlay displaying supporting drawings, source provenance, and confidence levels.
4. **Time-Aware Construction Journey:** Users can travel through time (1966–2001) to experience the complex rising chronologically, unlocking a permanent historical archive upon reaching 2001.
5. **Complete World Model Database Population:** 
   - Every floor of Tower A and Tower B represented with spatial boundaries and 3D positioning in PostgreSQL.
   - Every space assigned a functional zone (core, tenant, mechanical, service).
   - Every element linked to `evidence_references`, `confidence_scores`, and `historical_states`.
   - The World Model API serves world data, historical states, and evidence citations with high efficiency.
6. **Platform Performance Targets:** Initial load under 5 seconds, floor transitions under 1 second, year state switching under 2 seconds, evidence overlay opening under 500ms, and rendering performance at 30+ FPS (with a 2D fallback mode for non-WebGL devices).
7. **AI Independence at Runtime:** The entire experience operates with zero dependency on live AI infrastructure or external LLM API availability.

---

# Working Rule

For all future tasks:

**Repository documentation is the source of truth.**

If repository documentation conflicts with external assumptions, personal biases, or unverified claims, **repository documentation wins.**

```text
Audit → Plan → Review → Implement → Verify → Document → Commit
```
