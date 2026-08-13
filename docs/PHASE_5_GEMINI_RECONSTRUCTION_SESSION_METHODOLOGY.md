# Phase 5 Gemini Reconstruction Session Methodology

**Document Status:** ✅ AUTHORITATIVE RECONSTRUCTION SESSION METHODOLOGY  
**Date:** August 12, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1–14)  
**Parent ADR Records:**  
1. [`docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006_GEMINI_PRIMARY_RECONSTRUCTION_ENGINE.md)  
2. [`docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md`](file:///opt/wtc/wtc-twin-towers/docs/ADR-006A_CONFIDENCE_ASSESSMENT_REALIGNMENT.md)  
**Parent Output Specification:** [`docs/GEMINI_RECONSTRUCTION_OUTPUT_SPECIFICATION.md`](file:///opt/wtc/wtc-twin-towers/docs/GEMINI_RECONSTRUCTION_OUTPUT_SPECIFICATION.md)  
**Target Database Baseline:** PostgreSQL 16.14 + PostGIS 3.6.4 (`wtc_evidence`)  

**FINAL METHODOLOGY DECISION:** **`[X] Methodology Approved`**  

---

## Executive Summary

This document establishes the **authoritative Phase 5 Gemini Reconstruction Session Methodology** governing how Gemini operates as the **PRIMARY RECONSTRUCTION ENGINE** when reconstructing World Trade Center spatial entities, directed property graph relationships, 2D/3D geometries, and epistemic evidence citations from architectural blueprints.

Zero implementation code, zero Python scripts, zero SQL modifications, zero database schema changes, and zero web searches were created in this methodology specification document.

The methodology details 15 sequential analysis steps, 5 mandatory architectural reasoning questions, epistemic category separation (**VERIFIED FACTS**, **INFERENCES**, **ASSUMPTIONS**, **UNCERTAINTIES**), ADR-006A composite confidence scoring ($[80, 100]$), human review escalation, and Stage 5/6 payload handoff procedures.

The single selected final recommendation is **`[X] Methodology Approved`**.

---

## 1. Verified Facts

```text
METHODOLOGY BASELINE MATRIX:
┌────────────────────────────────────────────────────────────────────────┬─────────┐
│ Verified Fact Item                                                     │ Status  │
├────────────────────────────────────────────────────────────────────────┼─────────┤
│ 1. ADR-006 Established Gemini as Primary Reconstruction Engine         │ ✅ PASS │
│ 2. ADR-006A Established Evidence-Quality Confidence Model (Option B)   │ ✅ PASS │
│ 3. 15-Step Reconstruction Session Workflow Defined                     │ ✅ PASS │
│ 4. Mandatory 5-Question Explanatory Audit Framework Integrated         │ ✅ PASS │
│ 5. Epistemic Category Separation Enforced                              │ ✅ PASS │
└────────────────────────────────────────────────────────────────────────┴─────────┘
```

---

## 2. Reconstruction Philosophy & 5 Mandatory Questions

```text
MANDATORY 5-QUESTION EXPLANATORY AUDIT FRAMEWORK:
For EVERY proposed entity and relationship, Gemini MUST explicitly document:
1. WHAT WAS OBSERVED? (Direct visual / vector evidence in drawing)
2. WHY DOES THIS EXIST? (Architectural purpose e.g. ventilation, core support)
3. WHAT EVIDENCE SUPPORTS IT? (Sheet codes, bounding regions, text notes)
4. WHAT ALTERNATIVE INTERPRETATIONS EXIST? (Ambiguities or alternative classifications)
5. WHAT CONFIDENCE LEVEL IS JUSTIFIED? (ADR-006A composite score calculation)
```

---

## 3. The 15-Step Reconstruction Session Workflow

```text
15-STEP RECONSTRUCTION SESSION PIPELINE:
Step  1: Drawing Intake & SHA-256 Registration
Step  2: Drawing Orientation & Context Discovery
Step  3: Sheet Classification (Architectural, Structural, Mechanical)
Step  4: Building & Floor Level Identification (WTC 1 / WTC 2 / Complex, Level B1/B2/Floor 1)
Step  5: Structural System Analysis (Grids A–H, 1–16; Core Columns 501–1008)
Step  6: Space & Zone Identification (Mechanical zones, Fan rooms, Corridors)
Step  7: Structural & Architectural Element Identification
Step  8: Directed Property Graph Relationship Discovery (CONTAINS, BOUNDS, ADJACENT_TO)
Step  9: Epistemic Evidence Collection & Primary Source Citation
Step 10: 2D PostGIS Geometry Discovery (EPSG:2263 WKT Polygons)
Step 11: Cross-Sheet Blueprint Corroboration (Multi-Sheet Matching)
Step 12: ADR-006A Composite Confidence Assessment (Option B Formula)
Step 13: Architectural Ambiguity Resolution
Step 14: Human Review Escalation Gate (Scores [70, 79] or Overlap Ambiguity)
Step 15: Reconstruction Session Output Generation (Stage3LayoutContract v1.0.0)
```

---

## 4. Step-by-Step Methodology Details (15 Modules)

### 4.1 Step 1: Drawing Intake
- **Purpose:** Ingest rendered 300 DPI page image and Stage 1/2 metadata.
- **Inputs:** 300 DPI page PNG + `Stage1OutputContract` + `Stage2VectorContract`.
- **Analysis Performed:** Verify SHA-256 hash, check file signature.
- **Expected Outputs:** Validated intake job payload.
- **Governance Requirements:** Reject unvalidated inputs.
- **Failure Conditions:** Truncated file or missing contract metadata.

### 4.2 Step 2: Drawing Orientation & Context Discovery
- **Purpose:** Determine North arrow direction and sheet coordinate orientation.
- **Inputs:** 300 DPI page image.
- **Analysis Performed:** Locate North arrow symbol, detect 0°, 90°, 180°, 270° rotation angle.
- **Expected Outputs:** Rotation normalization metadata.
- **Governance Requirements:** Re-orient image if rotation is non-zero.
- **Failure Conditions:** Missing North arrow or illegible title block orientation.

### 4.3 Step 3: Sheet Classification
- **Purpose:** Classify sheet domain (`ARCHITECTURAL`, `STRUCTURAL`, `MECHANICAL`, `PLUMBING`).
- **Inputs:** Title block text & drawing graphics.
- **Analysis Performed:** Match title block sheet code prefix (`A-A-`, `S-`, `M-`).
- **Expected Outputs:** Sheet domain classification tag.
- **Governance Requirements:** Reject non-standard sheet classifications.
- **Failure Conditions:** Illegible sheet code prefix.

### 4.4 Step 4: Building & Floor Identification
- **Purpose:** Map drawing to specific WTC complex building (`wtc1_tower_a`, `wtc2_tower_b`, `wtc_complex_podium`) and floor level (`B1`, `B2`, `Floor 1`).
- **Inputs:** Title block text notes & floor elevation tags.
- **Analysis Performed:** Parse building ID and floor level tags (e.g. `SUB-GRADE B1`).
- **Expected Outputs:** Target `building_id` and `floor_id`.
- **Governance Requirements:** Enforce Tower A vs Tower B separation (Principle 7).
- **Failure Conditions:** Ambiguous building association.

### 4.5 Step 5: Structural System Analysis
- **Purpose:** Identify structural grid lines (Grids A–H, 1–16) and core box columns (Columns 501–1008).
- **Inputs:** Structural CAD polylines & column grid bubbles.
- **Analysis Performed:** Correlate grid intersections with core box column positions.
- **Expected Outputs:** Structural grid framework & column registry.
- **Governance Requirements:** Core columns 501–1008 MUST align with frozen database baseline.
- **Failure Conditions:** Unaligned column grid coordinates.

### 4.6 Step 6: Space & Zone Identification
- **Purpose:** Discover enclosed rooms, mechanical core zones, corridors, elevator shafts, and stairwells.
- **Inputs:** Wall polyline boundaries & room text labels.
- **Analysis Performed:** Closed polygon ring discovery & category classification (`service_area`, `mechanical_area`, `elevator_bank`).
- **Expected Outputs:** Discovered space entity proposals.
- **Governance Requirements:** Category ENUM string MUST match canonical World Model taxonomy.
- **Failure Conditions:** Unclosed wall boundary ($> 0.5\text{pt}$ gap).

### 4.7 Step 7: Element Identification
- **Purpose:** Discover equipment elements (chillers, pumps, air handling units, doors).
- **Inputs:** CAD symbol graphics & equipment text tags.
- **Analysis Performed:** Equipment symbol recognition & bounding box calculation.
- **Expected Outputs:** Element entity proposals.
- **Governance Requirements:** Parent space ID MUST be non-null.
- **Failure Conditions:** Orphan element without parent space.

### 4.8 Step 8: Relationship Discovery
- **Purpose:** Infer spatial relationships (`CONTAINS`, `BOUNDS`, `ADJACENT_TO`, `CONNECTS_TO`).
- **Inputs:** Discovered entities & PostGIS spatial topology.
- **Analysis Performed:** Evaluate PostGIS 2D containment (`ST_Contains`) and adjacency (`ST_Touches`).
- **Expected Outputs:** Directed property graph relationship proposals.
- **Governance Requirements:** Non-reflexivity `subject_entity_id != object_entity_id`.
- **Failure Conditions:** Self-loop relationship edge.

### 4.9 Step 9: Evidence Collection
- **Purpose:** Collect primary source evidence citations for every entity and relationship (Principle 2).
- **Inputs:** Stage 1 sheet codes & Stage 2 CAD vector bounding boxes.
- **Analysis Performed:** Attach sheet code (`A-A-18`), drawing region, and visual observation text.
- **Expected Outputs:** Evidence citation list.
- **Governance Requirements:** No entity may exist without supporting evidence citations.
- **Failure Conditions:** Missing primary source citation.

### 4.10 Step 10: Geometry Discovery
- **Purpose:** Construct PostGIS-compatible 2D spatial geometries in `EPSG:2263`.
- **Inputs:** Stage 2 vector polygon coordinates.
- **Analysis Performed:** Transform PDF points to PostGIS NAD83 NYC State Plane Feet (`EPSG:2263`) and execute `ST_IsValid`.
- **Expected Outputs:** 2D PostGIS WKT polygon strings.
- **Governance Requirements:** `srid = 2263`, `ST_IsValid = true`.
- **Failure Conditions:** Self-intersecting polygon.

### 4.11 Step 11: Cross-Sheet Corroboration
- **Purpose:** Match entity across multiple independent drawing sheets (e.g. Floor Plan `A-A-18` + Core Elevation `A-A-121`).
- **Inputs:** Multi-sheet drawing set payloads.
- **Analysis Performed:** Execute spatial IoU overlap ($\text{IoU} \ge 0.90$) across sheet drawings.
- **Expected Outputs:** Corroborated entity list with lifecycle state promoted to `CORROBORATED`.
- **Governance Requirements:** 2nd independent sheet match promotes `DRAFT_SEED` ──► `CORROBORATED`.
- **Failure Conditions:** Disjoint multi-sheet spatial coordinates.

### 4.12 Step 12: Confidence Assessment (ADR-006A)
- **Purpose:** Compute composite epistemic confidence score using the ADR-006A Option B formula.
- **Inputs:** Reasoning scores, evidence quality, corroboration count, geometry validity.
- **Analysis Performed:** Calculate composite score: $0.30 \cdot \text{Reasoning} + 0.25 \cdot \text{Evidence} + 0.25 \cdot \text{Corroboration} + 0.10 \cdot \text{Geometry} + 0.10 \cdot \text{Clarity}$.
- **Expected Outputs:** Composite confidence score $[80, 100]$.
- **Governance Requirements:** Score $< 80$ triggers quarantine.
- **Failure Conditions:** Composite score calculation failure.

### 4.13 Step 13: Ambiguity Resolution
- **Purpose:** Resolve visual drawing overlaps or conflicting sheet notes.
- **Inputs:** Identified drawing discrepancies.
- **Analysis Performed:** Apply repository evidence precedence rules.
- **Expected Outputs:** Ambiguity resolution log.
- **Governance Requirements:** Stored repository evidence PREVAILS over ambiguous drawing notes.
- **Failure Conditions:** Unresolvable drawing conflict.

### 4.14 Step 14: Human Review Escalation
- **Purpose:** Escalate ambiguous proposals or confidence scores in $[70, 79]$ to human reviewers.
- **Inputs:** Flagged entity proposals.
- **Analysis Performed:** Set `requires_human_review = true` and log trigger reason.
- **Expected Outputs:** Human review queue ticket payload.
- **Governance Requirements:** Database ingestion BLOCKED until sign-off timestamp is non-null.
- **Failure Conditions:** Bypassing human review sign-off.

### 4.15 Step 15: Reconstruction Output Generation
- **Purpose:** Produce standardized `Stage3LayoutContract` v1.0.0 JSON payload.
- **Inputs:** Approved entity & relationship proposals.
- **Analysis Performed:** Format JSON schema output.
- **Expected Outputs:** `Stage3LayoutContract` v1.0.0 JSON file in `data/processed_pdfs/[HASH]_stage3.json`.
- **Governance Requirements:** Schema MUST match `Stage3LayoutContract` version `1.0.0`.
- **Failure Conditions:** JSON serialization error.

---

## 5. Epistemic Category Separation Rules

Gemini MUST explicitly separate its architectural reasoning summary into 4 distinct categories:

- **VERIFIED FACTS:** Empirical, directly observable drawing data (e.g. *"Sheet code reads A-A-18"*, *"Vector polyline forms closed 4-vertex polygon"*).
- **INFERENCES:** Deductive architectural reasoning (e.g. *"Boundary represents Sub-grade Fan Room 101 based on adjacent ductwork symbols"*).
- **ASSUMPTIONS:** Standard domain parameters applied when details are unstated (e.g. *"Story height assumed equal to standard 12'-0" elevation"*).
- **UNCERTAINTIES:** Drawing degradations or overlapping callouts requiring review.

---

## 6. Final Recommendation

```text
FINAL METHODOLOGY SELECTION:
[ ] Methodology Incomplete
[ ] Methodology Requires Revision
[X] Methodology Approved ◄── SOLE SELECTED RECOMMENDATION
```

### Detailed Justification for `[X] Methodology Approved`:
The Phase 5 Gemini Reconstruction Session Methodology defines 100% of the 15-step workflow, 5 mandatory audit questions, epistemic category separation, ADR-006A confidence scoring, and human review escalation rules. The methodology is **FORMALLY APPROVED**.
