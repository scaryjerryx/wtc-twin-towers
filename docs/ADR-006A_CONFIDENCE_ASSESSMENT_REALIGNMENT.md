# Architectural Decision Record Amendment (ADR-006A)
## Confidence Assessment Realignment

**Status:** ✅ ADOPTED  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Record:** [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
**Parent Output Spec:** [`docs/GEMINI_RECONSTRUCTION_OUTPUT_SPECIFICATION.md`](file:///opt/wtc/wtc-twin-towers/docs/GEMINI_RECONSTRUCTION_OUTPUT_SPECIFICATION.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL CONFIDENCE REALIGNMENT DECISION:** **`[X] Major Confidence Realignment Required`**  

---

## 1. Decision

The World Model Reconstruction Project formally adopts **ADR-006A**, amending the confidence scoring framework to eliminate legacy OCR-centric formulas and replace them with an **Evidence-Quality & Architectural-Reasoning Confidence Model (Option B)**.

Zero code changes, zero database modifications, zero SQL schema alterations, and zero web searches were created in this architecture decision record amendment.

```text
ADR-006A REALIGNED CONFIDENCE EVALUATION MODEL (OPTION B):
Composite Confidence Score = 
  0.30 × Architectural Consistency & Spatial Logic
+ 0.25 × Evidence Citation Quality & Primary Source Integrity
+ 0.25 × Cross-Sheet Corroboration (Multiple Drawing Linkages)
+ 0.10 × PostGIS Geometric Topology Validity (EPSG:2263 ST_IsValid)
+ 0.10 × Visual Drawing Clarity & Glyph Alignment
```

---

## 2. Legacy Confidence Model Review vs. Realigned Model

```text
CONFIDENCE MODEL COMPARISON:
┌───────────────────────────────────────────────────┬────────────────────────────────────────────────────────┐
│ Legacy Model (Option A - Rejected)                │ Realigned Model (Option B - Adopted ADR-006A)          │
├───────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ 0.4 Vector + 0.4 Vision + 0.2 OCR                 │ Architectural Reasoning + Evidence Quality +           │
│                                                   │ Cross-Sheet Corroboration + Geometry Validity          │
├───────────────────────────────────────────────────┼────────────────────────────────────────────────────────┤
│ • Over-indexed on brittle OCR glyph matching      │ • Focuses on multi-modal architectural logic           │
│ • Penalized valid spaces if text was degraded     │ • Rewards cross-sheet blueprint corroboration           │
│ • Untethered from cross-sheet corroboration      │ • Directly aligned with Principle 2 & Principle 5      │
└───────────────────────────────────────────────────┴────────────────────────────────────────────────────────┘
```

---

## 3. Mandatory Epistemic Scoring Rules

```text
MANDATORY EPISTEMIC SCORING RULES:
1. OCR MAY influence confidence; OCR MAY NOT determine confidence.
2. Vector extraction MAY influence confidence; vector extraction MAY NOT determine confidence.
3. Gemini architectural reasoning MAY determine confidence.
4. Evidence quality MAY determine confidence.
5. Cross-sheet corroboration MAY determine confidence.
6. NO entity MAY receive a score >= 80 without supporting primary source evidence citations.
```

---

## 4. Confidence Factors & Scoring Conditions

### 4.1 Factors Increasing Epistemic Confidence
1. **Cross-Sheet Corroboration ($+10$ to $+15$ pts):** Entity is independently corroborated across $\ge 2$ drawing sheets (e.g. Floor Plan `A-A-18` + Core Elevation `A-A-121`).
2. **PostGIS 2D Spatial Validity ($+10$ pts):** Extruded boundary polygon passes PostGIS `ST_IsValid = true` and `ST_Area > 0` in `EPSG:2263`.
3. **Architectural Structural Logic ($+15$ pts):** Spatial entity aligns logically with structural grid lines (Grids A–H, 1–16) and core box columns (501–1008).

### 4.2 Factors Decreasing Epistemic Confidence
1. **Drawing Sheet Ambiguity ($-10$ to $-20$ pts):** Overlapping drawing lines or contradictory sheet revision callouts.
2. **Missing Primary Source Citation ($-30$ pts):** Candidate proposal lacks explicit sheet code or drawing region attribution.
3. **Un-reconciled Spatial Discrepancy ($-15$ pts):** Bounding footprint conflicts with stored database topology.

---

## 5. Explicit Component Roles in Confidence Assessment

### 5.1 Gemini Architectural Reasoning (`DETERMINES CONFIDENCE`)
- Gemini's multi-modal analysis evaluates architectural logic, structural alignment, and space relationships, providing the primary foundation ($55\%$) for composite confidence scoring.

### 5.2 Evidence Quality & Cross-Sheet Corroboration (`DETERMINES CONFIDENCE`)
- Primary source citations and cross-sheet drawing links directly drive high-confidence ratings ($25\%$), promoting entities from `DRAFT_SEED` to `CORROBORATED`.

### 5.3 Vector Extraction & OCR (`INFLUENCES CONFIDENCE ONLY`)
- CAD vector polygons and OCR labels supply supporting empirical evidence ($20\%$). They CANNOT single-handedly grant or deny high-confidence status to an architectural entity.

### 5.4 Human Review Gate (`ENFORCES GOVERNANCE THRESHOLDS`)
- Candidates scoring in $[70, 79]$ or possessing spatial boundary overlaps are flagged for human sign-off before database ingestion.

---

## 6. Consequences & Final Recommendation

```text
FINAL ADR-006A ADOPTION SELECTION:
[ ] Existing Confidence Model Retained
[ ] Confidence Model Updated
[X] Major Confidence Realignment Required ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Major Confidence Realignment Required`:
ADR-006A eliminates legacy OCR-centric confidence formulas, establishing an Evidence-Quality & Architectural-Reasoning Confidence Model (Option B) fully aligned with ADR-006 and Principles 1–14. **ADR-006A IS FORMALLY ADOPTED**.
