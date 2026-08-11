# Library of Congress Acquisition Report

## Date: August 10, 2026

## Acquisition Attempt Summary

**Target:** Library of Congress Gottscho-Schleisner Collection  
**Objective:** Acquire WTC construction photography (1966-1973)  
**Status:** ❌ FAILED - Wrong collection searched

---

## Search Details

**Search Query:** "world trade center"  
**Collection Filter:** None (searched all LoC collections)  
**Total Results:** 877 items  
**Pages Reviewed:** 1 of 44 (first 20 items)  
**Search URL:** https://www.loc.gov/pictures/search?q=world+trade+center&c=20&sp=1&fo=json

---

## Files Acquired

**None.**

No files were downloaded because the search did not return Gottscho-Schleisner construction photography.

---

## What We Found

### Category Breakdown (First 20 Items)

| Category | Count | Date Range | Reconstruction Value |
|---|---|---|---|
| HABS/HAER documentation | 6 | 2004 | Low |
| 9/11 attack photos | 3 | 2001 | None |
| Post-9/11 memorial | 6 | 2018 | None |
| Architectural models | 4 | 1976 | Low |
| Design proposals | 1 | 2001-2002 | None |
| **Total** | **20** | **2001-2018** | **Very Low** |

### Sample Items Found

1. **HABS Aerial Views (2004)**
   - Title: "Aerial view of Section A, World Trade Center 1 from World Trade Center 7"
   - Date: 2004
   - Value: Low (post-construction documentation)

2. **9/11 Attack Photos (2001)**
   - Title: "People crossing the Brooklyn Bridge away from Manhattan, with the towers of the World Trade Center smoking heavily"
   - Date: c2001
   - Value: None (disaster documentation)

3. **Post-9/11 Memorial (2018)**
   - Title: "Calatrava's Oculus, a 335-foot-long, spiky-skylighted transportation hub"
   - Date: 2018
   - Value: None (memorial, not original construction)

4. **Architectural Models (1976)**
   - Title: "Model of skyline with World Trade Center towers"
   - Date: [1976]
   - Value: Low (model photography, not construction)

5. **Yamasaki with Model (1976)**
   - Title: "Architect Minoru Yamasaki on a ladder looking down at a model of the World Trade Center"
   - Date: [1976]
   - Value: Low-Medium (shows designer with model)

---

## What We Needed

**Gottscho-Schleisner construction photography (1966-1973):**
- Construction photographs
- Steel erection photographs
- Excavation photographs
- Site photographs during construction
- Exterior photographs during construction
- Aerial photographs during construction

**Expected characteristics:**
- Date range: 1966-1973
- Collection: Gottscho-Schleisner, Inc. (gsc)
- Format: High-resolution TIFF/JPEG
- Quantity: 100-500 photographs
- Value: HIGH (construction-era documentation)

---

## Why This Failed

### Root Cause

**The search did not filter to the Gottscho-Schleisner collection.**

The search returned items from ALL LoC collections, primarily:
- HABS/HAER (Historic American Buildings Survey)
- 9/11 attack collection
- Highsmith memorial photography
- Korab architectural photography
- Design proposal archives

**None of these are the Gottscho-Schleisner construction photography collection.**

### Technical Issue

The LoC API search requires explicit collection filtering:
```
Correct: ?q=world+trade+center&fa=collection%3Agsc
Incorrect: ?q=world+trade+center (no collection filter)
```

---

## Readiness Impact

### Current State
- Overall readiness: ~50%
- Construction photographs (IG-1): ⚠️ Partial (NCSTAR 1-8 only)
- Timeline coverage: 1966-1973 (from NCSTAR 1-1 text references)

### After This Acquisition Attempt
- Overall readiness: ~50% (NO CHANGE)
- Construction photographs (IG-1): ⚠️ Partial (still NCSTAR 1-8 only)
- Timeline coverage: 1966-1973 (unchanged)

### Readiness Gain

**0%**

No construction-era photography was acquired.

---

## Timeline Impact Assessment

### Question: Does this improve timeline states?

**Answer: NO**

| Timeline State | Before | After | Change |
|---|---|---|---|
| 1966 | 15% | 15% | 0% |
| 1967 | 20% | 20% | 0% |
| 1968 | 15% | 15% | 0% |
| 1969 | 17% | 17% | 0% |
| 1970 | 5% | 5% | 0% |
| 1971 | 5% | 5% | 0% |
| 1972 | 3% | 3% | 0% |
| 1973 | 8% | 8% | 0% |

**No construction photography was acquired, so no timeline states were improved.**

---

## Recalculated Readiness

### Site Readiness
- Before: 35%
- After: 35%
- Change: 0%
- Reason: No site photographs acquired

### Tower A Readiness
- Before: 65%
- After: 65%
- Change: 0%
- Reason: No construction photographs acquired

### Tower B Readiness
- Before: 60%
- After: 60%
- Change: 0%
- Reason: No construction photographs acquired

### Timeline Readiness
- Before: 15-20% (1966-1969)
- After: 15-20% (1966-1969)
- Change: 0%
- Reason: No construction-era photography acquired

### Overall Readiness
- Before: ~50%
- After: ~50%
- Change: 0%
- Reason: No reconstruction-relevant evidence acquired

---

## Next Steps

### Required Action

**Search specifically for Gottscho-Schleisner collection:**

1. **Direct collection search:**
   ```
   URL: https://www.loc.gov/pictures/collection/gsc/
   Search: "world trade center" OR "twin towers"
   ```

2. **Filtered search:**
   ```
   URL: https://www.loc.gov/pictures/search?q=world+trade+center&fa=collection%3Agsc&c=100&sp=1&fo=json
   ```

3. **Date-filtered search:**
   ```
   URL: https://www.loc.gov/pictures/search?q=world+trade+center&fa=collection%3Agsc&fi=1966-1973&c=100&sp=1&fo=json
   ```

### Expected Results (If Successful)

If Gottscho-Schleisner collection contains WTC construction photography:
- 100-500 construction photographs
- Date range: 1966-1973
- Readiness impact: +10% overall
- Timeline impact: +5-10% for 1966-1973 states
- Corpus growth: +500MB-2GB

---

## Conclusion

**This acquisition attempt failed.**

The search returned 877 items from various LoC collections, but NONE were from the Gottscho-Schleisner construction photography collection (1966-1973).

**Results:**
- Files acquired: 0
- Total size: 0MB
- Years represented: None (no 1966-1973)
- Readiness impact: 0%
- Timeline impact: 0%

**Status:** ❌ FAILED

**Recommendation:** Retry with explicit collection filter for Gottscho-Schleisner (gsc).

---

## Appendix: Sample URLs from Search

### HABS Documentation (2004)
- https://www.loc.gov/pictures/item/ny2014.photos.362127p/
- https://www.loc.gov/pictures/item/ny2014.photos.362088p/

### 9/11 Attack Photos (2001)
- https://www.loc.gov/pictures/item/2002712437/
- https://www.loc.gov/pictures/item/2002716343/

### Post-9/11 Memorial (2018)
- https://www.loc.gov/pictures/item/2018699939/
- https://www.loc.gov/pictures/item/2018699980/

### Architectural Models (1976)
- https://www.loc.gov/pictures/item/2021644072/
- https://www.loc.gov/pictures/item/2021645155/

### Design Proposals (2001-2002)
- https://www.loc.gov/pictures/item/2010646892/

**None of these are construction-era (1966-1973) photography.**