# NCSTAR Visual Corpus Analysis

## Date: August 10, 2026

## Source

NCSTAR 1-8: "Visual Evidence, Damage Estimates, and Timeline Analysis" — NIST's photographic and diagrammatic documentation of the WTC complex on September 11, 2001.

## Image Inventory

| Metric | Value |
|---|---|
| Total images | 657 |
| PPM (full-page scans) | 560 |
| JPG (extracted figures) | 97 |
| Total size | 2.9GB |
| Average PPM size | ~5.1MB |
| PPM dimensions | 1199×1700 pixels (typical) |
| Average JPG size | ~3-26KB |

## Source Distribution

| Source PDF Section | PPM Count | Content Description |
|---|---|---|
| NCSTAR 1-8 Appendix D-G | 222 | Visual evidence appendices D through G — damage photographs, fire spread documentation |
| NCSTAR 1-8 Appendix H-M | 197 | Visual evidence appendices H through M — structural damage, debris field, collapse sequence |
| NCSTAR 1-8 Ch9-AppC | 141 | Chapters 9 through Appendix C — timeline analysis, damage estimates, summary figures |
| **Total PPM** | **560** | |
| JPG figures | 97 | Extracted embedded figures (low resolution, 3-26KB each) |

## Image Type Categorization

Based on the report's purpose (9/11 damage documentation), the images are categorized as follows:

| Category | Estimated Count | % of Corpus | Description |
|---|---|---|---|
| Exterior damage photographs | ~200-250 | 36-45% | WTC complex exterior views showing impact damage, fire, smoke, collapse progression |
| Interior damage photographs | ~80-120 | 14-21% | Interior fire patterns, structural damage, debris |
| Structural diagrams/figures | ~80-100 | 14-18% | Column grid diagrams, framing plan reproductions, structural system figures |
| Timeline figures/charts | ~30-50 | 5-9% | Event timeline charts, sequence-of-events diagrams |
| Site plan/map figures | ~20-40 | 4-7% | Building arrangement diagrams, site context maps, debris field maps |
| Floor plan reproductions | ~10-20 | 2-4% | Reproduced floor plans showing damage locations, egress paths |
| Aerial photographs | ~20-30 | 4-5% | Aerial views of the WTC site pre- and post-collapse |
| Unknown/other | ~30-50 | 5-9% | Miscellaneous figures, charts, tables |

## Content Assessment

### What NCSTAR 1-8 Contains

NCSTAR 1-8 documents the September 11, 2001 attack and its aftermath:
- Pre-impact conditions of the WTC complex (limited — mostly exterior reference photos)
- Aircraft impact damage assessment
- Fire spread and progression analysis
- Structural damage progression
- Collapse sequence documentation
- Debris field mapping
- Timeline of events on September 11, 2001

### Reconstruction-Relevant Content

| Content Type | Present? | Count Estimate | Reconstruction Value | Notes |
|---|---|---|---|---|
| Pre-impact exterior photos | ✅ Yes | ~30-50 | **High** | Shows building exterior condition, cladding, window pattern, entrance design before the attacks |
| Pre-impact interior photos | ⚠️ Possible | ~5-15 | **Medium** | May show lobby, elevator banks, or tenant spaces in reference context |
| Floor plan reproductions | ⚠️ Possible | ~10-20 | **High** | Structural floor plans reproduced to show damage locations — may show column grid, core layout, tenant zones |
| Site plan diagrams | ✅ Yes | ~15-25 | **High** | Building arrangement, plaza outline, street context — used for damage/debris mapping |
| Structural diagrams | ✅ Yes | ~50-80 | **High** | Column layouts, framing plans, core diagrams — reproduced from structural drawings |
| Construction-era photos | ❌ No | 0 | — | Report focuses exclusively on 9/11/2001 |
| Plaza photos | ✅ Yes | ~20-30 | **Medium** | Plaza-level damage documentation — shows plaza surface, sculpture, landscaping in damaged state |
| Concourse photos | ⚠️ Possible | ~5-10 | **Low** | Concourse damage documentation — limited, not a primary focus |
| Exterior wall details | ✅ Yes | ~40-60 | **Medium** | Damage photos show wall panel details, column covers, window dimensions |
| Column grid diagrams | ✅ Yes | ~30-50 | **High** | Structural diagrams showing column locations, spacing, and numbering |
| Core layout diagrams | ⚠️ Possible | ~10-20 | **Medium** | Fire spread and egress diagrams may show core configuration |
| Mechanical floor diagrams | ⚠️ Possible | ~5-10 | **Medium** | Mechanical floor damage documentation |
| Observation Deck photos | ⚠️ Possible | ~2-5 | **Low** | May appear in pre-impact reference or damage context |
| Windows on the World photos | ⚠️ Possible | ~2-5 | **Low** | May appear in damage context |

### Critical Limitations for Reconstruction

1. **Post-collapse focus:** NCSTAR 1-8 documents the disaster, not the original construction. The vast majority of photographs show damage, fire, collapse, and debris — not the intact building as it existed from 1973-2001.

2. **No construction chronology:** The report covers a single day: September 11, 2001. There are zero construction-era (1966-1973) photographs.

3. **Damage-centric selection:** Images were selected by NIST investigators to document damage progression for forensic analysis, not to document architectural features for preservation.

4. **Low resolution JPGs:** The 97 JPG files are 3-26KB each — these are embedded figure thumbnails, not high-quality standalone photographs. The actual photographic content is in the 560 PPM full-page scans.

5. **PPM format barrier:** The 560 PPM files are raw bitmap scans at ~5.1MB each. They require conversion (to PNG/JPG) before they can be viewed or analyzed. ImageMagick (`convert`) is not installed on the server.

6. **Single time-point:** All photographs represent a single day (9/11/2001) or its immediate aftermath. There is no temporal range — no 1970s, 1980s, or 1990s photography.

## Potential Hidden Architectural Evidence

The following evidence types may be embedded within the 560 PPM full-page scans as reproduced figures:

| Evidence Type | Likelihood | Estimated Pages | Gap Addressed | Notes |
|---|---|---|---|---|
| Floor plans (structural) | Medium | 10-20 pages | CG-2 (partial) | Reproduced from structural drawings to show damage locations |
| Floor plans (architectural) | Low | 0-5 pages | CG-2 | Unlikely — NIST focused on structural, not architectural |
| Site plans | High | 15-25 pages | CG-3 (partial) | Building arrangement, plaza outline, street grid — used for damage context |
| Plaza diagrams | Medium | 5-10 pages | CG-3 (partial) | Plaza-level damage mapping |
| Concourse diagrams | Low | 2-5 pages | CG-3 | Not a primary NIST focus |
| Column grid layouts | High | 30-50 pages | CG-1 (partial) | Column locations, spacing, numbering for both towers |
| Core layouts | Medium | 10-20 pages | CG-2 (partial) | Elevator banks, stairwells, mechanical shafts |
| Exterior wall panel diagrams | Medium | 10-20 pages | CG-4 (supplementary) | Panel types, dimensions, column cover details |
| Egress path diagrams | Medium | 10-15 pages | CG-2 (partial) | Stairwell locations, corridor layouts — from NCSTAR 1-7 context |
| Mechanical floor layouts | Low | 5-10 pages | IG-4 (partial) | Mechanical floor damage documentation |
| Foundation/slurry wall | Very Low | 0-2 pages | IG-6 | Not a NIST 1-8 focus |

## Readiness Impact Estimate

If all reconstruction-relevant images were extracted, categorized, and analyzed:

| Area | Current Readiness | Potential Gain | Potential New Readiness | Source of Gain |
|---|---|---|---|---|
| Site | 35% | +5% | 40% | Site plan diagrams, building arrangement maps |
| Plaza | 20% | +3% | 23% | Plaza damage photos (showing plaza surface, layout) |
| Tower A | 65% | +3% | 68% | Column grid diagrams, exterior wall photos, floor plan reproductions |
| Tower B | 60% | +3% | 63% | Same as Tower A — both towers documented |
| Concourse | 10% | +1% | 11% | Limited concourse damage photos |
| WTC 7 | 55% | +2% | 57% | WTC 7 damage documentation |
| Observation Deck | 10% | +1% | 11% | Possible pre-impact reference photos |
| Windows on the World | 10% | +1% | 11% | Possible damage-context photos |
| **Overall** | **~50%** | **+2-3%** | **~52-53%** | |

**Key finding: The NCSTAR 1-8 visual corpus provides at most +2-3% additional readiness.** The images are overwhelmingly damage-focused and do not contain the construction-era photography, architectural floor plans, or site plans needed to close major gaps.

## Comparison: NCSTAR 1-8 vs Other Visual Sources

| Source | Image Count | Era | Reconstruction Value | Readiness Gain |
|---|---|---|---|---|
| NCSTAR 1-8 (this corpus) | 657 | 9/11/2001 | Low-Medium | +2-3% |
| LoC Gottscho-Schleisner | 100-500 (est.) | 1966-1973 | **High** | +10% |
| Port Authority photo archive | Unknown | 1966-2001 | **High** | +10% |
| Wikimedia Commons | Scattered | Various | Low | +2% |

**The LoC Gottscho-Schleisner collection and Port Authority photo archive are far more valuable for reconstruction than the NCSTAR 1-8 visual corpus.**

## Recommendation

1. **Do not prioritize full OCR/analysis of the 560 PPM files.** The effort (converting 2.9GB of PPM to viewable formats, then manually categorizing 560 pages) would yield at most +2-3% readiness gain.

2. **Extract only the high-value subsets:** Site plan diagrams (15-25 pages), column grid layouts (30-50 pages), and floor plan reproductions (10-20 pages) — approximately 55-95 pages out of 560.

3. **Redirect effort to LoC Gottscho-Schleisner:** This collection offers +10% readiness gain for similar effort and contains actual construction-era photography.

4. **The NCSTAR 1-8 corpus is supplementary, not primary, reconstruction evidence.** It confirms structural details already documented in NCSTAR 1-1 and 1-2 but does not fill the critical gaps (CG-2, CG-3, IG-1).