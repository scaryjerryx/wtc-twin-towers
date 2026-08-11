# Low Hanging Fruit Campaign

## Date: August 10, 2026

## Campaign Objective

Maximize reconstruction readiness using **immediately available public evidence** before implementing Blueprint Analysis Pipeline v1.

**Constraints:**
- ✅ Publicly accessible
- ✅ Can be downloaded now
- ✅ No government approval required
- ✅ No waiting period
- ❌ No Port Authority requests
- ❌ No FOIL requests
- ❌ No long-term acquisitions

---

## Current State: ~50% Readiness

| Area | Readiness | Key Evidence |
|---|---|---|
| Site | 35% | NCSTAR references, Wikimedia SVG previews |
| Plaza | 20% | NCSTAR references (limited) |
| Tower A | 65% | AA20a1 (895 PNGs), exterior wall XLS (floors 1-9 + 107-110), floor 96-A database |
| Tower B | 60% | Exterior wall schedules, panel schedule (B2, 25MB), floor 75-B database, upper wall AB2/AB3 |
| Concourse | 10% | NCSTAR references (minimal) |
| WTC 3-6 | 0% | No evidence |
| WTC 7 | 55% | WTC7 OEM spec manual, NCSTAR 1-9 |
| Observation Deck | 10% | NCSTAR references (minimal) |
| Windows on the World | 10% | NCSTAR references (minimal) |
| **Overall** | **~50%** | |

---

## Critical Gaps Remaining

| ID | Gap | Status | Impact |
|---|---|---|---|
| CG-1 | Tower B Structural Drawings | ⚠️ Partially addressed | Blocks Tower B structural skeleton |
| CG-2 | Architectural Floor Plans | ❌ Open | Blocks all interior spatial modeling |
| CG-3 | Site Plan & Plaza | ❌ Open | Blocks site-level and plaza modeling |
| IG-1 | Construction Photographs | ⚠️ NCSTAR 1-8 only | Blocks visual reference and as-built verification |
| IG-2 | Interior Photographs | ⚠️ NCSTAR 1-8 only | Blocks interior spatial modeling |

---

## Low Hanging Fruit Targets

### Tier 1: Critical Priority (Immediate Download)

#### 1.1 Library of Congress — Gottscho-Schleisner Collection

**Source:** Library of Congress Prints & Photographs Division  
**URL:** https://www.loc.gov/pictures/collection/gsc/  
**Access:** Public domain, no restrictions  
**Download Method:** Direct download via LoC API or manual browse

**Evidence Type:**
- Construction photographs (1966-1973)
- Exterior photographs
- Interior photographs
- Plaza photographs
- Observation Deck photographs
- Windows on the World photographs

**Expected Content:**
- 100-500 WTC-related photographs
- High-resolution TIFF/JPEG files
- Construction-era photography (1966-1973)
- Pre-9/11 interior and exterior views

**Readiness Impact:**
- Construction photographs (IG-1): +10%
- Interior photographs (IG-2): +5%
- Observation Deck: +5%
- Windows on the World: +5%
- **Overall: +10%**

**Acquisition Effort:** Low (2-4 hours)  
**Probability of Success:** High (90%)  
**Corpus Growth:** +500MB-2GB

**Why Critical:**
- Only publicly available source of construction-era photography
- Fills IG-1 (Construction Photographs) gap completely
- Provides visual reference for exterior, interior, plaza, observation deck, WotW
- Public domain — no usage restrictions

**Status:** ❌ Not yet attempted (previous API timeout resolved)

---

#### 1.2 Internet Archive — AA20a1 Uploader Tower B Collections

**Source:** Internet Archive  
**URL:** https://archive.org/details/AA20a1  
**Access:** Public, manual browse required  
**Download Method:** Browse uploader's collections, download Tower B structural sheets

**Evidence Type:**
- Tower B structural sheet PNGs
- Floor framing plans
- Column schedules
- Beam schedules
- Connection details

**Expected Content:**
- AA20b1 or similar collection (Tower B equivalent to AA20a1)
- 800-1000 structural sheet PNGs
- Complete Tower B structural documentation

**Readiness Impact:**
- Tower B structural (CG-1 remaining): +10%
- Tower B readiness: 60% → 70%
- **Overall: +5%**

**Acquisition Effort:** Low (1 hour)  
**Probability of Success:** Medium (60%)  
**Corpus Growth:** +400-800MB

**Why Critical:**
- Would fully close CG-1 (Tower B Structural Drawings)
- Enables Tower B structural skeleton modeling
- Matches Tower A evidence level (AA20a1)
- Public access — no restrictions

**Status:** ⏳ Operator action required (manual browse)

**Risk:** Uploader may not have Tower B collection

---

#### 1.3 Wikimedia Commons — Full-Resolution Site Plan SVGs

**Source:** Wikimedia Commons  
**URL:** https://commons.wikimedia.org/wiki/Category:World_Trade_Center  
**Access:** Public domain / Creative Commons  
**Download Method:** Manual download of full-resolution SVG files

**Evidence Type:**
- Site plan SVGs
- Building arrangement diagrams
- Plaza layout diagrams
- Site context maps

**Expected Content:**
- 5-10 high-resolution SVG files
- Vector site plans
- Building footprint diagrams
- Plaza layout maps

**Readiness Impact:**
- Site plans (CG-3 partial): +5%
- Plaza plans (CG-3 partial): +3%
- **Overall: +3%**

**Acquisition Effort:** Low (30 minutes)  
**Probability of Success:** High (80%)  
**Corpus Growth:** +10-50MB

**Why Critical:**
- Partially addresses CG-3 (Site Plans)
- Provides vector site plans for modeling
- Public domain — no restrictions
- Quick win — minimal effort

**Status:** ❌ Previous attempt failed (redirects) — retry with direct file URLs

**Note:** Previous attempt downloaded low-res previews. Full-res SVGs require direct file URL access.

---

### Tier 2: High Priority (Immediate Download)

#### 2.1 HABS/HAER Collection — Library of Congress

**Source:** Library of Congress — Historic American Buildings Survey / Historic American Engineering Record  
**URL:** https://www.loc.gov/rr/print/habs_haer.html  
**Access:** Public domain  
**Download Method:** Direct download via LoC catalog

**Evidence Type:**
- Historic building survey drawings
- Measured architectural drawings
- Historical photographs
- Architectural elevations
- Building sections

**Expected Content:**
- WTC architectural drawings (if surveyed)
- Measured drawings of structural elements
- Historical photographs
- Architectural documentation

**Readiness Impact:**
- Architectural elevations (IG-5): +3%
- Site plans (CG-3 partial): +2%
- **Overall: +2%**

**Acquisition Effort:** Medium (2-4 hours)  
**Probability of Success:** Medium (50%)  
**Corpus Growth:** +100-500MB

**Why High Priority:**
- May contain architectural drawings not available elsewhere
- Public domain — no restrictions
- Complements NCSTAR structural documentation

**Status:** ❌ Not yet searched

**Risk:** WTC may not have been surveyed by HABS/HAER before destruction

---

#### 2.2 NYC Municipal Archives — WTC Collection

**Source:** NYC Municipal Archives  
**URL:** https://www.nyc.gov/site/records/municipal-archives.page  
**Access:** Public records  
**Download Method:** Online catalog search and download

**Evidence Type:**
- Building permit drawings
- Construction photographs
- Site plans
- Inspection reports

**Expected Content:**
- WTC building permit drawings
- Construction-era photographs
- Site plan submissions
- Department of Buildings records

**Readiness Impact:**
- Architectural floor plans (CG-2 partial): +3%
- Construction photographs (IG-1): +2%
- **Overall: +2%**

**Acquisition Effort:** Medium (4-8 hours)  
**Probability of Success:** Medium (60%)  
**Corpus Growth:** +200-1GB

**Why High Priority:**
- Official city records — high authenticity
- May contain architectural floor plans
- Public records — no restrictions

**Status:** ❌ Not yet searched

**Risk:** Online access may be limited; may require in-person visit

---

#### 2.3 Columbia University — WTC Oral History Collection

**Source:** Columbia University Center for Oral History  
**URL:** https://oralhistory.library.columbia.edu/  
**Access:** Public access  
**Download Method:** Online catalog search and download

**Evidence Type:**
- Oral history transcripts
- Photographs (if included)
- Tenant interviews
- Operational history

**Expected Content:**
- WTC tenant interviews
- Operational history documentation
- Photographs (if available)
- Historical context

**Readiness Impact:**
- Operational history: +1%
- Tenant layouts (indirect): +1%
- **Overall: +1%**

**Acquisition Effort:** Low (2 hours)  
**Probability of Success:** High (80%)  
**Corpus Growth:** +50-200MB

**Why High Priority:**
- Provides operational context
- May include photographs
- Public access — no restrictions

**Status:** ❌ Not yet searched

---

### Tier 3: Medium Priority (Immediate Download)

#### 3.1 MIT Libraries — WTC Structural Research

**Source:** MIT Libraries  
**URL:** https://libraries.mit.edu/  
**Access:** Public access  
**Download Method:** Catalog search and download

**Evidence Type:**
- Structural engineering research
- Technical reports
- Photographs
- Drawings

**Expected Content:**
- WTC structural research papers
- Technical documentation
- Historical photographs

**Readiness Impact:**
- Structural documentation: +1%
- **Overall: +0.5%**

**Acquisition Effort:** Medium (4 hours)  
**Probability of Success:** Low (40%)  
**Corpus Growth:** +50-200MB

**Status:** ❌ Not yet searched

---

#### 3.2 Skyscraper Museum — WTC Digital Archive

**Source:** Skyscraper Museum  
**URL:** https://www.skyscraper.org/  
**Access:** Public access  
**Download Method:** Website browse and download

**Evidence Type:**
- Architectural drawings
- Photographs
- Models
- Historical documentation

**Expected Content:**
- WTC architectural documentation
- Historical photographs
- Building models
- Design drawings

**Readiness Impact:**
- Architectural documentation: +1%
- **Overall: +0.5%**

**Acquisition Effort:** Low (2 hours)  
**Probability of Success:** Medium (60%)  
**Corpus Growth:** +100-500MB

**Status:** ❌ Not yet searched

---

#### 3.3 9/11 Memorial & Museum — Digital Collections

**Source:** National September 11 Memorial & Museum  
**URL:** https://www.911memorial.org/  
**Access:** Public access  
**Download Method:** Website browse and download

**Evidence Type:**
- Historical photographs
- Victim stories
- Memorial documentation
- Historical context

**Expected Content:**
- Pre-9/11 photographs
- Historical documentation
- Memorial context

**Readiness Impact:**
- Historical context: +0.5%
- **Overall: +0.5%**

**Acquisition Effort:** Low (2 hours)  
**Probability of Success:** High (80%)  
**Corpus Growth:** +50-200MB

**Status:** ❌ Not yet searched

---

#### 3.4 New York Public Library — WTC Collections

**Source:** New York Public Library — Digital Collections  
**URL:** https://digitalcollections.nypl.org/  
**Access:** Public domain  
**Download Method:** Online catalog search and download

**Evidence Type:**
- Historical photographs
- Postcards
- Maps
- Newspapers

**Expected Content:**
- WTC historical photographs
- Postcards
- Historical maps
- Newspaper clippings

**Readiness Impact:**
- Historical photographs: +1%
- **Overall: +0.5%**

**Acquisition Effort:** Medium (4 hours)  
**Probability of Success:** Medium (60%)  
**Corpus Growth:** +100-500MB

**Status:** ❌ Not yet searched

---

#### 3.5 Internet Archive — WTC Community Collections

**Source:** Internet Archive  
**URL:** https://archive.org/  
**Search Terms:** "World Trade Center", "WTC", "Twin Towers"  
**Access:** Public access  
**Download Method:** Direct download

**Evidence Type:**
- Community-uploaded photographs
- Videos
- Documents
- Drawings

**Expected Content:**
- User-contributed WTC photographs
- Historical videos
- Personal collections
- Miscellaneous documentation

**Readiness Impact:**
- Miscellaneous: +0.5%
- **Overall: +0.5%**

**Acquisition Effort:** Medium (4-8 hours)  
**Probability of Success:** Medium (50%)  
**Corpus Growth:** +200MB-1GB

**Status:** ❌ Not yet searched

---

### Tier 4: Low Priority (Opportunistic)

#### 4.1 eBay / Auction Sites — WTC Drawing Sales

**Source:** eBay, Heritage Auctions  
**URL:** https://www.ebay.com/, https://www.ha.com/  
**Access:** Public listings  
**Download Method:** Screenshot and document (not download)

**Evidence Type:**
- Original drawings for sale
- Photographs for sale
- Memorabilia

**Expected Content:**
- Original WTC drawings
- Historical photographs
- Memorabilia documentation

**Readiness Impact:**
- Documentation only: +0.1%
- **Overall: +0.1%**

**Acquisition Effort:** High (ongoing monitoring)  
**Probability of Success:** Low (20%)  
**Corpus Growth:** +0MB (documentation only)

**Status:** ❌ Not yet monitored

**Note:** Not a download source — documentation opportunity only

---

#### 4.2 Reddit / Forums — WTC Community Collections

**Source:** Reddit, SkyscraperPage, SkyscraperCity  
**URL:** https://www.reddit.com/, https://www.skyscraperpage.com/, https://www.skyscrapercity.com/  
**Access:** Public forums  
**Download Method:** Forum browse and download

**Evidence Type:**
- Community-shared photographs
- Personal collections
- Historical documentation

**Expected Content:**
- User-shared WTC photographs
- Personal collections
- Historical documentation

**Readiness Impact:**
- Miscellaneous: +0.2%
- **Overall: +0.2%**

**Acquisition Effort:** Medium (4-8 hours)  
**Probability of Success:** Low (30%)  
**Corpus Growth:** +50-200MB

**Status:** ❌ Not yet searched

---

## Readiness Forecast

### Best Case Scenario

**All Tier 1 + Tier 2 targets successful:**

| Target | Gain | Cumulative |
|---|---|---|
| Current | — | 50% |
| LoC Gottscho-Schleisner | +10% | 60% |
| IA Tower B sheets | +5% | 65% |
| Wikimedia SVGs | +3% | 68% |
| HABS/HAER | +2% | 70% |
| NYC Municipal Archives | +2% | 72% |
| Columbia Oral History | +1% | 73% |

**Best Case: 73% readiness**

**Time:** 1-2 weeks  
**Effort:** 20-40 hours  
**Corpus Growth:** +2-5GB

---

### Expected Case Scenario

**Tier 1 successful + 50% of Tier 2:**

| Target | Gain | Cumulative |
|---|---|---|
| Current | — | 50% |
| LoC Gottscho-Schleisner | +10% | 60% |
| IA Tower B sheets | +5% | 65% |
| Wikimedia SVGs | +3% | 68% |
| HABS/HAER (50%) | +1% | 69% |
| NYC Municipal (50%) | +1% | 70% |

**Expected Case: 70% readiness**

**Time:** 1 week  
**Effort:** 15-25 hours  
**Corpus Growth:** +1.5-3GB

---

### Minimum Case Scenario

**Only Tier 1 successful:**

| Target | Gain | Cumulative |
|---|---|---|
| Current | — | 50% |
| LoC Gottscho-Schleisner | +10% | 60% |
| IA Tower B sheets | +5% | 65% |
| Wikimedia SVGs | +3% | 68% |

**Minimum Case: 68% readiness**

**Time:** 2-3 days  
**Effort:** 5-10 hours  
**Corpus Growth:** +500MB-2GB

---

## Campaign Execution Plan

### Phase 1: Critical Targets (Days 1-3)

**Priority:** Tier 1 targets

| Day | Target | Effort | Expected Gain |
|---|---|---|---|
| Day 1 | LoC Gottscho-Schleisner | 4 hours | +10% |
| Day 2 | IA Tower B sheets (manual browse) | 1 hour | +5% |
| Day 2 | Wikimedia SVGs (retry) | 30 min | +3% |
| Day 3 | Buffer / troubleshooting | 2 hours | — |

**Phase 1 Result:** 68% readiness (minimum case achieved)

---

### Phase 2: High Priority Targets (Days 4-7)

**Priority:** Tier 2 targets

| Day | Target | Effort | Expected Gain |
|---|---|---|---|
| Day 4 | HABS/HAER Collection | 4 hours | +2% |
| Day 5 | NYC Municipal Archives | 8 hours | +2% |
| Day 6 | Columbia Oral History | 2 hours | +1% |
| Day 7 | Buffer / troubleshooting | 4 hours | — |

**Phase 2 Result:** 73% readiness (best case achieved)

---

### Phase 3: Medium Priority Targets (Days 8-14)

**Priority:** Tier 3 targets (opportunistic)

| Day | Target | Effort | Expected Gain |
|---|---|---|---|
| Day 8-10 | MIT, Skyscraper Museum, 9/11 Memorial | 6 hours | +1.5% |
| Day 11-14 | NYPL, Internet Archive community | 8 hours | +1% |

**Phase 3 Result:** 75.5% readiness (stretch goal)

---

## Success Metrics

### Primary Metrics

| Metric | Current | Target (Expected) | Target (Best) |
|---|---|---|---|
| Overall readiness | 50% | 70% | 73% |
| Tower A readiness | 65% | 70% | 72% |
| Tower B readiness | 60% | 70% | 72% |
| Site readiness | 35% | 45% | 50% |
| Corpus size | ~5GB | 7-8GB | 10GB |

### Gap Closure Metrics

| Gap | Current Status | Expected Status | Best Case Status |
|---|---|---|---|
| CG-1 (Tower B structural) | ⚠️ Partial | ✅ Closed | ✅ Closed |
| CG-2 (Architectural floor plans) | ❌ Open | ⚠️ Partial | ⚠️ Partial |
| CG-3 (Site plans) | ❌ Open | ⚠️ Partial | ⚠️ Partial |
| IG-1 (Construction photos) | ⚠️ Partial | ✅ Closed | ✅ Closed |
| IG-2 (Interior photos) | ⚠️ Partial | ✅ Closed | ✅ Closed |

---

## Risk Assessment

### High-Risk Targets

| Target | Risk | Mitigation |
|---|---|---|
| IA Tower B sheets | Uploader may not have collection | Browse thoroughly; check all uploader collections |
| NYC Municipal Archives | Online access may be limited | Prepare for in-person visit if needed |
| HABS/HAER | WTC may not have been surveyed | Search thoroughly; document if not found |

### Medium-Risk Targets

| Target | Risk | Mitigation |
|---|---|---|
| Wikimedia SVGs | Previous attempt failed (redirects) | Use direct file URLs; try different download methods |
| Columbia Oral History | May not include photographs | Search thoroughly; document what's available |

### Low-Risk Targets

| Target | Risk | Mitigation |
|---|---|---|
| LoC Gottscho-Schleisner | Previous API timeout | Retry with improved timeout handling |
| 9/11 Memorial | Limited technical documentation | Focus on historical context |

---

## Resource Requirements

### Time

- **Minimum:** 5-10 hours (Tier 1 only)
- **Expected:** 15-25 hours (Tier 1 + Tier 2)
- **Best Case:** 20-40 hours (All tiers)

### Storage

- **Minimum:** +500MB-2GB
- **Expected:** +1.5-3GB
- **Best Case:** +2-5GB

### Tools

- Web browser (for manual downloads)
- Download manager (for bulk downloads)
- Image processing tools (for format conversion)
- Storage space (for downloaded content)

### Personnel

- 1 operator (manual browse and download)
- Optional: 1 assistant (parallel downloads)

---

## Campaign Rules

### Do

- ✅ Prioritize Tier 1 targets first
- ✅ Document all downloads with provenance
- ✅ Verify file integrity after download
- ✅ Update readiness calculations after each target
- ✅ Track corpus growth

### Do Not

- ❌ Pursue FOIL requests
- ❌ File Port Authority requests
- ❌ Wait for government approvals
- ❌ Implement Blueprint Analysis Pipeline (yet)
- ❌ Modify code or database

---

## Most Important Question

**Q: Can we reach 70% readiness using only immediately available public evidence?**

**A: YES.**

**Expected Case:** 70% readiness achievable in 1 week with Tier 1 + Tier 2 targets.

**Key Enablers:**
1. LoC Gottscho-Schleisner (+10%) — construction photography
2. IA Tower B sheets (+5%) — Tower B structural documentation
3. Wikimedia SVGs (+3%) — site plans

**These three targets alone can move readiness from 50% to 68%.**

**With Tier 2 additions (HABS/HAER, NYC Municipal, Columbia), we reach 70-73%.**

**This closes:**
- CG-1 (Tower B structural) — fully closed
- IG-1 (Construction photographs) — fully closed
- IG-2 (Interior photographs) — fully closed
- CG-2 (Architectural floor plans) — partially closed
- CG-3 (Site plans) — partially closed

**This enables:**
- Prototype 0.1 (structural + spatial model)
- Floor-level reconstruction for both towers
- Construction sequence visualization
- Visual reference library

---

## Recommendation

**Execute Low Hanging Fruit Campaign immediately.**

**Phase 1 (Days 1-3):** Focus on Tier 1 targets to reach 68% readiness.

**Phase 2 (Days 4-7):** Add Tier 2 targets to reach 70-73% readiness.

**Phase 3 (Days 8-14):** Opportunistic Tier 3 targets for stretch goal of 75%.

**After campaign:** Implement Blueprint Analysis Pipeline v1 to process newly acquired content and unlock additional readiness gains.

**Expected outcome:** 70% readiness in 1 week, enabling Prototype 0.1.