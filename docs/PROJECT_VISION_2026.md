# Project Vision 2026

## Date: August 11, 2026

## Strategic Milestone

This document marks a permanent strategic milestone in the World Trade Center Reconstruction Project. It records the project's evolved understanding, architecture, and long-term vision following the acquisition and assessment of the Tower A architectural corpus.

---

## 1. What We Are Building

The project is building:

**A historically accurate, evidence-backed, browser-based, interactive reconstruction of the World Trade Center.**

This is not merely a 3D model. This is a living historical reconstruction platform where every major element can explain where it came from, what evidence supports it, and how confident the reconstruction is.

---

## 2. The Fundamental Shift

### Before

The project was framed as an "Evidence Engine" — a system for discovering, collecting, and processing historical evidence. The reconstruction was a future aspiration.

### After

The project is now framed as a **Reconstruction Platform**. The Evidence Engine remains important, but its role has been clarified:

| Component | Role |
|-----------|------|
| **Reconstruction Platform** | The product. What users experience. |
| **Evidence Engine** | The supporting system. Construction scaffolding. |
| **World Model** | The core asset. The structured representation of the WTC. |

The Evidence Engine builds the World Model. The World Model powers the Reconstruction Platform. The Reconstruction Platform delivers the public experience.

---

## 3. Why We Are Building It

The original World Trade Center no longer exists. Its physical form was destroyed. Its documentation is scattered across archives, government reports, whistleblower releases, and private collections.

This project exists to:

1. **Preserve** — Collect and safeguard historical evidence before it degrades or disappears
2. **Reconstruct** — Build the most historically accurate digital representation possible
3. **Cite** — Make every reconstruction element traceable to its supporting evidence
4. **Share** — Provide a public historical experience accessible to anyone with a browser

The project is not about the destruction. It is about the construction, the life, and the architectural significance of one of the most important building complexes of the 20th century.

---

## 4. Evidence Engine vs Reconstruction Platform

### Evidence Engine

The Evidence Engine is the automated pipeline that:

- Discovers historical evidence from configured sources
- Downloads and registers evidence assets
- Processes documents, images, drawings, and other formats
- Extracts entities, facts, and relationships
- Preserves provenance, citations, and confidence
- Builds the knowledge graph

**The Evidence Engine is construction scaffolding.** It is essential during development but is not what the public sees.

### Reconstruction Platform

The Reconstruction Platform is the browser-based experience that:

- Renders the WTC complex in 3D using React Three Fiber
- Allows users to walk through the plaza, concourse, towers, and spaces
- Supports time travel through construction and operational history
- Displays evidence citations for every reconstruction element
- Shows confidence levels and uncertainty
- Works on desktop, tablet, and mobile browsers

**The Reconstruction Platform is the building.** It is what the public experiences.

---

## 5. Role of AI

AI systems (Claude, Gemini, future multimodal models) are **development tools**.

Their role includes:

- Blueprint interpretation and analysis
- Evidence understanding and classification
- Reconstruction planning and architecture assistance
- Code generation and review

AI is **NOT** part of the final runtime architecture. The final platform must function without requiring an active AI model. AI assists in building the platform; it does not power the platform.

---

## 6. Target Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **World Database** | PostgreSQL | Structured WTC world model |
| **API Layer** | TBD (Python/Node.js) | Serve world data to frontend |
| **Frontend Framework** | Next.js | Application shell and routing |
| **3D Rendering** | React Three Fiber | Browser-based 3D reconstruction |
| **Evidence System** | Custom | Citation lookup and display |
| **Deployment** | Web server | Public access via browser |

### Browser-First Requirements

The platform must work on:

- Desktop browsers (Chrome, Firefox, Safari, Edge)
- Mobile browsers (iOS Safari, Android Chrome)
- Tablet browsers

No installation required. No downloadable client. No app-store dependency.

---

## 7. The World Model

The core asset of the project is the **World Model** — a structured, time-aware, evidence-backed representation of the World Trade Center complex.

### Hierarchy

```
World Trade Center Complex
 └── Site
      ├── Building (WTC 1, WTC 2, WTC 3, WTC 4, WTC 5, WTC 6, WTC 7)
      │    └── Tower
      │         └── Floor
      │              ├── Zone (Core, Tenant, Mechanical, Service)
      │              └── Space (Office, Corridor, Elevator, Stairwell, Lobby, Restroom)
      ├── Plaza (Austin J. Tobin Plaza)
      │    └── Concourse (Underground mall, PATH station, subway connections)
      └── Infrastructure (Transportation, utilities, services)
```

### World Model Properties

Every element in the World Model should eventually support:

- **Spatial position** — Where it is in 3D space
- **Historical state** — What it looked like at any given time
- **Evidence references** — What sources support its reconstruction
- **Confidence score** — How certain the reconstruction is
- **Provenance** — Where the evidence came from

---

## 8. Evidence Citation System

Every reconstruction element should eventually support evidence lookup.

### Citation Chain

```
Reconstruction Element (Wall, Column, Room, etc.)
        ↓
Evidence Reference (Blueprint, Photo, Report)
        ↓
Source (Organization, Archive, Collection)
        ↓
Confidence (Verified, Supported, Inferred)
        ↓
Provenance (Acquisition date, URL, file hash)
```

### User Interaction

A user should be able to:

1. Click on any reconstruction element
2. See what evidence supports it
3. View the original source material
4. Understand the confidence level
5. Trace provenance back to acquisition

This evidence traceability is one of the defining features of the project.

---

## 9. Historical Timeline Experience

### Construction Journey

The public should experience the World Trade Center as a **construction journey**, not a completed timeline.

**Release Schedule:**

| Public Day | Historical Year | Content |
|------------|----------------|---------|
| Day 1 | 1966 | Site preparation, foundation work |
| Day 2 | 1967 | Steel erection begins |
| Day 3 | 1968 | Tower A rising |
| ... | ... | ... |
| Day 35 | 2001 | Full operational complex |

### Timeline Rules

- Users may travel backward and revisit earlier years
- Users may compare historical states
- Users may NOT access future unreleased states
- After reaching 2001, the full timeline unlocks as a historical archive

### Construction Experience

Long-term vision includes:

- Active construction sites with cranes
- Steel erection sequences
- Concrete placement
- Construction staging areas
- Temporary structures
- Evolving site conditions

The audience should feel as though construction is happening live.

---

## 10. Public Experience Vision

A user opens a browser. They see the World Trade Center site.

They can:

- Walk through the plaza
- Descend into the concourse
- Enter the towers
- Ride elevators to the observation deck
- Visit Windows on the World
- Explore office floors
- Travel through time (1966-2001)
- Inspect evidence for any element
- Understand construction history
- Compare historical states

Every major reconstruction element can explain:

- Where it came from
- What evidence supports it
- How confident the reconstruction is

This is not merely a model. This is a living historical reconstruction platform.

---

## 11. Long-Term Historical Vision

Future phases may include:

- Tenant history and company occupancy
- Leasing history and space changes
- Historical stories and community information
- Memorial information
- Human stories layer

However, these are secondary to reconstruction. The physical reconstruction must come first.

---

## 12. Current Milestone

As of August 11, 2026:

- **Tower A architectural corpus acquired:** 211 drawings, 110 floors + 5 sub-levels
- **CG-2 (Architectural Floor Plans):** Substantially closed for Tower A
- **Tower A Readiness:** 65% → 85%
- **Overall Project Readiness:** ~50% → ~65-70%
- **Prototype 0.1:** Enabled

The project has crossed a major threshold. It is no longer asking "Can reconstruction be done?" It is now asking "How should reconstruction be represented and experienced?"

---

## 13. What Success Looks Like

A user opens a browser. The user walks through the plaza, concourse, towers, restaurants, observation deck, and office floors. The user can travel through time, inspect evidence, understand construction, and explore history.

Every major reconstruction element can explain where it came from, what evidence supports it, and how confident the reconstruction is.

This is not merely a model. This is a living historical reconstruction platform.

---

**Document prepared:** August 11, 2026  
**Status:** ✅ PERMANENT STRATEGIC MILESTONE