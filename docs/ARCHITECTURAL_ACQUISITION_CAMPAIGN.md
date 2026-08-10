# Architectural Evidence Acquisition Campaign

## Date: August 10, 2026

## Purpose

This document is the dedicated acquisition campaign plan for closing **CG-2 (Architectural Floor Plans)** and **CG-3 (Site Plan & Plaza Documentation)** — the two largest remaining blockers to reconstruction readiness. It identifies every known source of architectural evidence, ranks them by gain/likelihood/effort, and prescribes an exact acquisition order to move from ~50% to ~70% readiness.

---

## Current Architectural Evidence Baseline

### What We Have (Architectural Only)

| Evidence | Source | Coverage | Quality |
|---|---|---|---|
| NCSTAR 1-1 Appendix C-G (44MB) | Already acquired | Structural drawing reproductions — may contain floor plan figures for both towers | ⚠️ Image-based PDF — extraction failed previously |
| NCSTAR 1-7 (4.4MB) | Already acquired | Egress/occupant behavior plans — floor-plan derivatives showing stairwells, corridors, elevator banks | ⚠️ Not yet deep-extracted |
| NCSTAR 1-1 floor plan references | Already acquired | 3 text references to "floor plan" — descriptive only, not drawings | Low — text references only |
| Wikimedia Commons site plan SVGs | Already acquired (low-res previews) | WTC Building Arrangement, Preliminary Site Plan, Site Plan Comparison | ⚠️ Low-resolution previews — full-res downloads failed (redirects) |
| WTC Site Plan Overlay PNGs | Already acquired | 2 overlay PNGs derived from Wikimedia SVGs | Low — derivative work, not originals |

### What We Do NOT Have

| Evidence Type | Gap ID | Impact |
|---|---|---|
| Architectural floor plans (walls, rooms, corridors, elevators, stairs, spatial layout) | CG-2 | **Blocks all interior spatial modeling for every building** |
| Site plans (building relationships, plaza, concourse, street interfaces) | CG-3 | **Blocks site-level and plaza-level modeling** |
| Plaza plans (Austin J. Tobin Plaza layout, sculpture, landscaping) | CG-3 | **Blocks plaza reconstruction** |
| Concourse plans (underground mall, PATH station, subway connections) | CG-3 | **Blocks concourse reconstruction** |
| Observation Deck plans (WTC 1, floor 107) | CG-2 subset | **Blocks observation deck reconstruction** |
| Windows on the World plans (WTC 1, floor 107) | CG-2 subset | **Blocks WotW reconstruction** |
| Architectural elevations (exterior appearance, window patterns, cladding) | IG-5 | Blocks exterior visual accuracy |
| Building sections (vertical organization, mechanical floor relationships) | IG-5 | Blocks vertical spatial understanding |

---

## Every Known Source of Architectural Evidence

### Category A: Floor Plans (CG-2)

#### A1. NCSTAR 1-1 Appendix C-G — Structural Drawing Reproductions

| Field | Detail |
|---|---|
| **Repository** | Local corpus (`WTC_CORPUS/engineering-reports/ncstar/`) |
| **Status** | ✅ Already acquired |
| **Content** | 44MB image-based PDF. Appendix C-G of NCSTAR 1-1 contains reproductions of structural drawings, column schedules, and framing plans. May include floor plan figures for both towers. |
| **Extraction method** | `pdfimages` or `pdftoppm` — image-based PDF requires page-by-page raster conversion |
| **Previous attempt** | Failed — `pdfimages` produced no output, `pdftoppm` may work |
| **Readiness gain** | +5% (floor plan figures for both towers, if present) |
| **Likelihood of success** | **Medium** — content is there but extraction is technically challenging |
| **Effort** | Low (local processing, 2-4 hours) |
| **Priority** | **#1** — already acquired, just needs extraction |

#### A2. NCSTAR 1-7 — Egress and Occupant Behavior Plans

| Field | Detail |
|---|---|
| **Repository** | Local corpus (`WTC_CORPUS/engineering-reports/ncstar/`) |
| **Status** | ✅ Already acquired |
| **Content** | 4.4MB PDF. Focuses on occupant behavior, egress paths, and stairwell usage. Contains floor-plan derivatives showing stairwell locations, elevator banks, and corridor layouts. |
| **Extraction method** | Standard PDF text extraction + embedded image extraction |
| **Readiness gain** | +3% (egress plans = floor-plan derivatives) |
| **Likelihood of success** | **High** — standard PDF, should extract cleanly |
| **Effort** | Low (1-2 hours) |
| **Priority** | **#2** — low-hanging fruit |

#### A3. NYC Department of Buildings — Building Permit Drawings

| Field | Detail |
|---|---|
| **Repository** | NYC Department of Buildings |
| **Access method** | FOIL (Freedom of Information Law) request |
| **Status** | ❌ Not requested |
| **Content** | Building permit drawings filed for WTC 1 and WTC 2. Permit drawings typically include floor plans, structural layouts, and site plans — albeit at permit-level detail (less detailed than construction documents, but still architectural plans). |
| **Likely file types** | PDF scans, TIFF scans of original drawings |
| **Readiness gain** | +10% (architectural floor plans for both towers) |
| **Likelihood of success** | **Medium-High** — public records exist but FOIL turnaround is 2-4 weeks; may require fees; some records may have been transferred to Port Authority or destroyed |
| **Effort** | Medium (FOIL process, 2-4 weeks) |
| **Priority** | **#4** — highest-value external source, but delayed gratification |

#### A4. Port Authority of NY/NJ — Original Architectural Drawings

| Field | Detail |
|---|---|
| **Repository** | Port Authority Archives (PANYNJ) |
| **Access method** | Formal records request / FOIL |
| **Status** | ❌ Not requested |
| **Content** | Original architectural floor plans for all WTC buildings. The Port Authority was the owner and operator. Their archives likely contain the most complete set of architectural and structural drawings in existence — including floor plans, tenant layouts, interior elevations, and as-built revisions. |
| **Likely file types** | PDF scans of original drawings, possibly original CAD files or microfilm |
| **Readiness gain** | +15% (comprehensive floor plans + interior layouts + site/plaza/concourse) |
| **Likelihood of success** | **Medium** — records exist but Port Authority is a large bureaucracy; 4-8 week turnaround; may restrict access or charge substantial fees; sensitive post-9/11 |
| **Effort** | High (formal request, 4-8 weeks, possible fees) |
| **Priority** | **#7** — highest ultimate value, but slowest path |

#### A5. Minoru Yamasaki Associates Records

| Field | Detail |
|---|---|
| **Repository** | Unknown — possibly held by university archive or private collection |
| **Access method** | Unknown — requires locating the archive first |
| **Status** | ❌ Not located |
| **Content** | Original architectural design drawings for both towers. Yamasaki was the design architect. His firm's records would contain architectural elevations, floor plans, lobby designs, plaza designs, and exterior detailing. |
| **Likely file types** | Original drawings, possibly scanned or microfilmed |
| **Readiness gain** | +10% (design-level architectural drawings) |
| **Likelihood of success** | **Low** — archive location unknown; may be at Michigan State University or dispersed; private archive may restrict access |
| **Effort** | High (unknown location, private archive) |
| **Priority** | **#10** — high-value but uncertain path |

#### A6. Emery Roth & Sons Records

| Field | Detail |
|---|---|
| **Repository** | Unknown — possibly held by university archive or private collection |
| **Access method** | Unknown — requires locating the archive first |
| **Status** | ❌ Not located |
| **Content** | Architectural working drawings. Emery Roth & Sons was the architect of record — they produced the construction documents. Their records would contain the most detailed floor plans, including tenant layout variations, core configurations, and construction details. |
| **Likely file types** | Original construction drawings, possibly scanned or microfilmed |
| **Readiness gain** | +10% (construction-level architectural floor plans) |
| **Likelihood of success** | **Low** — archive location unknown; firm closed in 1990s; records may be lost or dispersed |
| **Effort** | High (unknown location, possibly lost) |
| **Priority** | **#11** — high-value but likely lost |

---

### Category B: Site Plans (CG-3)

#### B1. Wikimedia Commons — Full-Resolution Site Plan SVGs

| Field | Detail |
|---|---|
| **Repository** | commons.wikimedia.org |
| **Access method** | Direct download of full-resolution SVG files |
| **Status** | ⚠️ Attempted — only low-res previews acquired; full-res downloads returned 120-byte redirects |
| **Content** | 5 SVG files: WTC Building Arrangement and Site Plan comparison, WTC Preliminary Site Plan, WTC Site Plan Comparison, WTC Building Arrangement in preliminary site plan, plus 2 PNG overlays |
| **Alternative approach** | Use browser dev tools to capture the actual SVG content from the MediaWiki viewer, or use the `?download=1` parameter, or use the raw file URL from the "Original file" link on each file page |
| **Readiness gain** | +5% (vector site plans with building footprints and spatial relationships) |
| **Likelihood of success** | **Medium-High** — files exist but automated download failed; manual browser download should work |
| **Effort** | Low (manual download, 30 min) |
| **Priority** | **#3** — quick win, already identified |

#### B2. Port Authority of NY/NJ — Site, Plaza, and Concourse Plans

| Field | Detail |
|---|---|
| **Repository** | Port Authority Archives (PANYNJ) |
| **Access method** | Formal records request (same as A4 above) |
| **Status** | ❌ Not requested |
| **Content** | Original site plans, Austin J. Tobin Plaza plans, underground concourse plans, PATH station integration, street-level entrance plans, and landscaping plans. The Port Authority owns the most comprehensive site-level documentation in existence. |
| **Likely file types** | PDF scans of original site plans, CAD files |
| **Readiness gain** | +10% (site plans + plaza + concourse — closes CG-3) |
| **Likelihood of success** | **Medium** — same as A4 (bureaucracy, turnaround time) |
| **Effort** | High (4-8 weeks, possible fees) |
| **Priority** | **#7** — combined with A4 request |

#### B3. NYC DOT — Underground Concourse/Subway Maps

| Field | Detail |
|---|---|
| **Repository** | NYC Department of Transportation |
| **Access method** | Public records request |
| **Status** | ❌ Not requested |
| **Content** | Underground concourse maps, subway station layouts (Cortlandt Street, World Trade Center stations), pedestrian tunnel maps. The WTC concourse was an integrated transportation hub connecting PATH trains, NYC subways, and pedestrian tunnels. |
| **Likely file types** | PDF maps, CAD files |
| **Readiness gain** | +5% (concourse/subway level maps) |
| **Likelihood of success** | **Medium** — public records but may require formal request |
| **Effort** | Medium (1-2 weeks) |
| **Priority** | **#8** — specialized, concourse-level only |

#### B4. Library of Congress HABS/HAER Collection

| Field | Detail |
|---|---|
| **Repository** | Library of Congress |
| **Access method** | API or manual search on loc.gov |
| **Status** | ❌ Not acquired |
| **Content** | Historic American Buildings Survey / Historic American Engineering Record. May include photographic documentation and measured drawings of the WTC complex, including site plans, elevations, and structural details. |
| **Likely file types** | TIFF photographs, PDF measured drawings |
| **Readiness gain** | +5% (historic survey — photographs + measured drawings) |
| **Likelihood of success** | **Low-Medium** — WTC may not have been surveyed before destruction |
| **Effort** | Medium (API search, 2-4 hours) |
| **Priority** | **#9** — uncertain content |

---

### Category C: Observation Deck Plans (WTC 1, Floor 107)

#### C1. Port Authority Interior Plans (subset of A4)

| Field | Detail |
|---|---|
| **Repository** | Port Authority Archives |
| **Content** | The observation deck occupied the 107th floor of WTC 1 (South Tower). It included an indoor viewing area, outdoor rooftop deck, gift shop, and ticket counters. Floor plans would show the spatial layout, viewing positions, and visitor circulation. |
| **Readiness gain** | Included in A4 estimate (+5% specifically for Observation Deck) |
| **Priority** | **#7** — same as A4 |

#### C2. LoC Gottscho-Schleisner Photographs

| Field | Detail |
|---|---|
| **Repository** | Library of Congress |
| **Content** | May include interior photographs of the observation deck, providing visual reference for spatial layout even without formal floor plans |
| **Readiness gain** | +3% (visual reference) |
| **Priority** | **#5** (see separate photographic acquisition campaign) |

---

### Category D: Windows on the World Plans (WTC 1, Floor 107)

#### D1. Port Authority Interior Plans (subset of A4)

| Field | Detail |
|---|---|
| **Repository** | Port Authority Archives |
| **Content** | Windows on the World occupied the 107th floor of WTC 1 (North Tower). It was a full-service restaurant complex including main dining room, bar, private dining rooms, and kitchen facilities. Floor plans would show the restaurant layout, kitchen configuration, and dining area arrangement. |
| **Readiness gain** | Included in A4 estimate (+5% specifically for WotW) |
| **Priority** | **#7** — same as A4 |

#### D2. LoC Gottscho-Schleisner Photographs

| Field | Detail |
|---|---|
| **Repository** | Library of Congress |
| **Content** | May include interior photographs of Windows on the World, providing visual reference for spatial layout |
| **Readiness gain** | +3% (visual reference) |
| **Priority** | **#5** (see separate campaign) |

---

### Category E: Architectural Elevations and Sections (IG-5)

#### E1. NCSTAR 1-8 Visual Evidence (Already Acquired)

| Field | Detail |
|---|---|
| **Repository** | Local corpus |
| **Content** | 657 extracted images (2.9GB). While damage-focused, may contain some pre-9/11 exterior photographs showing architectural elevations, window patterns, cladding details, and entrance designs. |
| **Readiness gain** | +2% (visual reference for elevations) |
| **Priority** | **#6** — already acquired, needs cataloging |

#### E2. Yamasaki Archives (A5) and Emery Roth Archives (A6)

| Field | Detail |
|---|---|
| **Content** | Both archives would contain architectural elevation drawings and building sections |
| **Readiness gain** | Included in A5/A6 estimates |
| **Priority** | **#10/#11** — same constraints |

---

## Ranked Acquisition Order

| Priority | Source | Category | Readiness Gain | Likelihood | Effort | Time | Cumulative Gain |
|---|---|---|---|---|---|---|---|
| **1** | NCSTAR 1-1 App C-G extraction | Floor plans (A1) | +5% | Medium | Low | 2-4 hrs | +5% |
| **2** | NCSTAR 1-7 egress plan extraction | Floor plans (A2) | +3% | High | Low | 1-2 hrs | +8% |
| **3** | Wikimedia full-res site plan SVGs | Site plans (B1) | +5% | Med-High | Low | 30 min | +13% |
| **4** | NYC DOB FOIL — building permits | Floor plans (A3) | +10% | Med-High | Medium | 2-4 wks | +23% |
| **5** | LoC Gottscho-Schleisner photos | Elevations/interiors (C2/D2) | +6% | High | Low | 2-4 hrs | +29% |
| **6** | NCSTAR 1-8 visual cataloging | Elevations (E1) | +2% | High | Low | 1-2 hrs | +31% |
| **7** | Port Authority formal request | Floor plans + site + plaza + concourse (A4/B2) | +15% | Medium | High | 4-8 wks | +46% |
| **8** | NYC DOT concourse maps | Concourse (B3) | +5% | Medium | Medium | 1-2 wks | +51% |
| **9** | HABS/HAER Collection | Site/elevations (B4) | +5% | Low-Med | Medium | 2-4 hrs | +56% |
| **10** | Yamasaki Associates records | Floor plans + elevations (A5) | +10% | Low | High | Unknown | +66% |
| **11** | Emery Roth & Sons records | Floor plans (A6) | +10% | Low | High | Unknown | +76% |

---

## Fastest Architectural Route: ~50% → ~70%

### Phase 1: Immediate — Local Processing (1 day)

| Step | Action | Gain | Cumulative Readiness |
|---|---|---|---|
| 1 | Extract floor plan figures from NCSTAR 1-1 App C-G (`pdfimages` or `pdftoppm`) | +5% | 55% |
| 2 | Extract egress plans from NCSTAR 1-7 | +3% | 58% |
| 3 | Manually download Wikimedia full-res site plan SVGs | +5% | 63% |
| 4 | Catalog NCSTAR 1-8 images for architectural content | +2% | 65% |

**Phase 1 result: ~65% in 1 day (low effort, local processing only)**

### Phase 2: Short-term — External Public Archives (1-4 weeks)

| Step | Action | Gain | Cumulative Readiness |
|---|---|---|---|
| 5 | Download LoC Gottscho-Schleisner WTC photographs | +6% | 71% |
| 6 | File NYC DOB FOIL request for building permit drawings | +10% | 81% |
| 7 | Download HABS/HAER WTC survey (if available) | +5% | 86% |

**Phase 2 result: ~71% in 1-4 weeks (LoC photos alone push through 70% threshold)**

### Phase 3: Long-term — Formal Requests (4-8 weeks)

| Step | Action | Gain | Cumulative Readiness |
|---|---|---|---|
| 8 | File Port Authority formal request (floor plans, site, plaza, concourse, interior) | +15% | 86% |
| 9 | Request NYC DOT concourse/subway maps | +5% | 91% |

**Phase 3 result: ~86% in 4-8 weeks (Port Authority is the single highest-value source)**

---

## Estimated Readiness After Each Phase

| Area | Current (~50%) | After Phase 1 (~65%) | After Phase 2 (~71%) | After Phase 3 (~86%) |
|---|---|---|---|---|
| Site | 35% | 45% | 55% | 70% |
| Plaza | 20% | 25% | 35% | 55% |
| Tower A | 65% | 70% | 75% | 85% |
| Tower B | 60% | 65% | 70% | 85% |
| Concourse | 10% | 15% | 25% | 50% |
| WTC 3-6 | 0% | 5% | 10% | 20% |
| WTC 7 | 55% | 60% | 65% | 70% |
| Observation Deck | 10% | 15% | 25% | 40% |
| Windows on the World | 10% | 15% | 25% | 40% |
| **Overall** | **~50%** | **~65%** | **~71%** | **~80-86%** |

---

## Observation Deck and Windows on the World — Specific Plan

Both occupy **floor 107** of Tower A (WTC 1). They are currently at 10% readiness — among the lowest of any area.

| Source | Evidence Type | Readiness Gain | Notes |
|---|---|---|---|
| Port Authority interior plans (A4) | Floor plan drawings of 107th floor layout | +15% | Single highest-value source — would show both OD and WotW in one floor plan |
| LoC Gottscho-Schleisner (C2/D2) | Interior photographs of observation deck and restaurant | +10% | Visual confirmation of spatial layout, finishes, furnishings |
| Yamasaki records (A5) | Original design drawings for OD and WotW | +10% | May include interior elevations and design details |
| NCSTAR 1-8 (E1) | Post-9/11 damage photos of floor 107 | +2% | Limited — damage context only |

**To reach 50%+ for Observation Deck and Windows on the World:** Port Authority interior plans for floor 107 + LoC Gottscho-Schleisner interior photographs.

---

## What the 70% Threshold Unlocks

Crossing 70% with architectural evidence enables:

| Capability | Required Evidence | Status at 70% |
|---|---|---|
| Tower A floor-level spatial modeling | Floor plans + egress plans | ✅ Possible — rooms, corridors, core layout derivable |
| Tower B floor-level spatial modeling | Floor plans + egress plans | ✅ Possible — same as Tower A |
| Site-level building relationship model | Site plan SVGs + NCSTAR references | ✅ Possible — building footprints, plaza outline |
| Plaza spatial modeling | Site plan SVGs (partial) | ⚠️ Partial — layout known but details missing |
| Core zone modeling (elevators, stairs) | Egress plans (NCSTAR 1-7) | ✅ Possible — stairwell and elevator locations known |
| Construction-era visual reference | LoC Gottscho-Schleisner photos | ✅ Possible — professional photographs of construction |
| Prototype 0.1 (structural + spatial) | All of the above | ✅ **Enabled** — structural skeletons + floor-level spaces + site context |

---

## Recommended Exact Acquisition Order

```
ARCHITECTURAL ACQUISITION ORDER:

IMMEDIATE (next 1-2 days, local only):
  1. pdftoppm NCSTAR 1-1 Appendix C-G → extract floor plan figures
  2. pdftotext + pdfimages NCSTAR 1-7 → extract egress plans
  3. Manual browser: Wikimedia Commons → download full-res WTC site plan SVGs
  4. Catalog NCSTAR 1-8 images → identify architectural/exterior/interior content

SHORT-TERM (next 1-2 weeks, external):
  5. Loc.gov API → download Gottscho-Schleisner WTC photographs
  6. File NYC DOB FOIL request for WTC building permit drawings
  7. Loc.gov API → check HABS/HAER for WTC survey

LONG-TERM (4-8 weeks, formal requests):
  8. File Port Authority formal records request for:
     - WTC 1 & 2 architectural floor plans (all floors)
     - Site plan and Austin J. Tobin Plaza plan
     - Underground concourse plan
     - Floor 107 plan (Observation Deck + Windows on the World)
     - Interior layout drawings
  9. Request NYC DOT concourse/subway level maps

UNCERTAIN (location unknown):
  10. Research Yamasaki Associates archive location
  11. Research Emery Roth & Sons archive location
```

---

## Fastest Single Route from 50% to 70%

**Answer: Phase 1 (local extraction) + Phase 2 (LoC photos).**

| Step | Action | Gain | Cumulative |
|---|---|---|---|
| 1 | Extract NCSTAR 1-1 App C-G floor plans | +5% | 55% |
| 2 | Extract NCSTAR 1-7 egress plans | +3% | 58% |
| 3 | Download Wikimedia full-res SVGs | +5% | 63% |
| 4 | Download LoC Gottscho-Schleisner photos | +6% | 69% |
| 5 | Catalog NCSTAR 1-8 architectural content | +2% | 71% |

**5 steps, 1-2 days, all low effort, all from public/local sources. No FOIL requests required to cross 70%.**

The NYC DOB FOIL (Step 6, +10%) would push from 71% to ~81% — crossing the 80% threshold — but requires 2-4 weeks turnaround.

---

## Summary

| Question | Answer |
|---|---|
| How many known architectural evidence sources exist? | **11 distinct sources** across 5 categories (floor plans, site plans, observation deck, WotW, elevations) |
| Fastest route from 50% to 70%? | Phase 1 (4 local processing steps) + LoC photos = 71% in 1-2 days |
| Which source has highest single gain? | Port Authority formal request (+15%) — but 4-8 week turnaround |
| Which source has best gain/effort ratio? | NCSTAR 1-1 App C-G extraction (+5%, already acquired, 2-4 hours) |
| What blocks 80%? | NYC DOB FOIL floor plans (+10%) or Port Authority request (+15%) — both require formal requests |
| Can 70% be reached without any FOIL/formal request? | **Yes** — local processing + LoC public domain photos = 71% |
| What about Observation Deck and WotW? | Heavily dependent on Port Authority floor 107 plans. Without those, LoC photos provide partial visual reference only. |
| Single most impactful next action? | Extract floor plan figures from NCSTAR 1-1 Appendix C-G using `pdftoppm` |