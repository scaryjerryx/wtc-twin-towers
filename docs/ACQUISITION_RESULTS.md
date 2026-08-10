# Evidence Acquisition Results

## Date

August 10, 2026

## Search Summary

12 searches executed across Internet Archive and Wikimedia Commons. 0 errors.

---

## Results by Critical Gap

### CG-1: Tower B Structural Drawings

| Source | Results | Status |
|---|---|---|
| Internet Archive: "AA20 WTC structural" | 1 result (unrelated) | ❌ Not found |
| Internet Archive: "WTC structural drawings" | 23 results (mostly unrelated) | ❌ Not found |

**Assessment:** No Tower B structural sheet collection located. The AA20a1 Tower A collection exists on Internet Archive but no sister AA20 collection for Tower B was found. The uploader of AA20a1 should be manually inspected for related collections.

**Manual action required:** Visit `https://archive.org/details/AA20a1`, click the uploader name, browse all their collections for "AA20", "Tower B", "WTC 2", or "South Tower" items.

---

### CG-2: Architectural Floor Plans

| Source | Results | Status |
|---|---|---|
| Internet Archive: "WTC floor plans architectural" | 4 results (unrelated) | ❌ Not found |
| Wikimedia Commons: "WTC floor plan" | 10 results (NIST reports) | ⚠️ Partial |

**Assessment:** No standalone architectural floor plans located. The NIST NCSTAR reports on Internet Archive (84 items in `NIST_WTC_Investigation_Reports` collection) contain reproduced floor plans as embedded figures within the PDFs. These are the best available source.

**Manual action required:** Download NIST NCSTAR 1-1 through 1-9 from `https://archive.org/details/NIST_WTC_Investigation_Reports-861612`. Floor plans are embedded as figures within these reports.

---

### CG-3: Site Plan and Plaza Documentation

| Source | Results | Status |
|---|---|---|
| Wikimedia Commons: "WTC site plan" | 10 results | ✅ Found |
| Internet Archive: "WTC site plan" | 34 results (mostly unrelated) | ❌ Not found |

**Located files:**

| File | Source | Type |
|---|---|---|
| `WTC_Building_Arrangement_and_Site_Plan_comparison.svg` | Wikimedia Commons | SVG site plan |
| `WTC_Building_Arrangement_in_preliminary_site_plan.svg` | Wikimedia Commons | SVG site plan |
| `WTC_Building_Arrangement_and_Site_Plan_Overlay.png` | Wikimedia Commons | PNG site plan overlay |

**Download status:** 3 files downloaded to `WTC_CORPUS/site-plans/`. Files are small (redirects from thumbnail URLs) — full-resolution versions need direct Wikimedia Commons download.

**Manual action required:** Download full-resolution versions from:
- `https://commons.wikimedia.org/wiki/File:WTC_Building_Arrangement_and_Site_Plan_comparison.svg`
- `https://commons.wikimedia.org/wiki/File:WTC_Building_Arrangement_in_preliminary_site_plan.svg`
- `https://commons.wikimedia.org/wiki/File:WTC_Building_Arrangement_and_Site_Plan_Overlay.png`

---

### CG-4: Tower A Exterior Wall Schedules (Upper Floors)

| Source | Results | Status |
|---|---|---|
| Internet Archive: "WTC exterior wall schedule" | 0 results | ❌ Not found |

**Assessment:** No upper-floor exterior wall schedules located. The existing floors 1-9 spreadsheet is the only known copy.

---

### IG-1: Construction Photographs

| Source | Results | Status |
|---|---|---|
| Internet Archive: "WTC construction photos" | 178 results (mostly unrelated) | ❌ Not found |
| Wikimedia Commons: "WTC construction" | 10 results (modern construction) | ❌ Not found |

**Assessment:** Wikimedia Commons search returned modern One WTC construction photos, not original 1966-1973 WTC construction. The search query needs refinement.

**Manual action required:** Search Wikimedia Commons for "World Trade Center 1970 construction" or "WTC steel erection 1969". Search Library of Congress Gottscho-Schleisner collection at `https://www.loc.gov/pictures/collection/gsc/`.

---

### IG-2: Interior Photographs

**Not searched in this session.** Deferred to manual acquisition.

---

### Engineering Reports (NIST NCSTAR)

| Source | Results | Status |
|---|---|---|
| Internet Archive: "NIST NCSTAR reports" | 84 results | ✅ Collection located |
| Wikimedia Commons: "WTC structural drawing" | 10 results (NIST PDFs) | ✅ Located |

**Located collection:** `NIST_WTC_Investigation_Reports` on Internet Archive — 84 items including:
- NCSTAR 1-1: Design and Construction of Structural Systems
- NCSTAR 1-1A: Appendix
- NCSTAR 1-3: Mechanical and Metallurgical Analysis
- NCSTAR 1-6: Structural Fire Response
- NCSTAR 1-7: Occupant Behavior, Egress, and Emergency Communication
- Final Report on WTC 7 Collapse
- Visual Evidence, Damage Estimates, and Timeline Analysis

**Download status:** Direct download URLs failed (timeout). The Internet Archive collection identifier `NIST_WTC_Investigation_Reports-861612` is correct but individual file paths within the collection need verification.

**Manual action required:** Browse `https://archive.org/details/NIST_WTC_Investigation_Reports-861612` and download all NCSTAR 1-1 through 1-9 PDFs. These are public-domain U.S. government documents.

---

## Download Summary

| Category | Files Located | Files Downloaded | Status |
|---|---|---|---|
| Site Plans | 3 | 3 (low-res) | ⚠️ Need full-resolution |
| Engineering Reports | 84 (collection) | 0 | ❌ Download failed |
| Tower B Structural | 0 | 0 | ❌ Not found |
| Floor Plans | 0 (embedded in reports) | 0 | ⚠️ In NIST reports |
| Construction Photos | 0 | 0 | ❌ Not found |
| Exterior Wall (upper) | 0 | 0 | ❌ Not found |

---

## Recommended Manual Acquisition

The operator should manually download from these exact URLs:

### Priority 1 — NIST NCSTAR Reports (contains floor plans, structural details, site diagrams)

1. Visit: `https://archive.org/details/NIST_WTC_Investigation_Reports-861612`
2. Download all PDFs, especially:
   - NIST_NCSTAR_1-1_Design_Construction.pdf
   - NIST_NCSTAR_1-1A_Design_Construction_Appendix.pdf
   - NIST_NCSTAR_1-3_Mechanical_Metallurgical.pdf
   - NIST_NCSTAR_1-6_Structural_Fire_Response.pdf
3. Place in: `WTC_CORPUS/engineering-reports/`

### Priority 2 — WTC Site Plans (full resolution)

1. Visit: `https://commons.wikimedia.org/wiki/File:WTC_Building_Arrangement_and_Site_Plan_comparison.svg`
2. Click "Original file" to download full-resolution SVG
3. Repeat for the other two site plan files
4. Place in: `WTC_CORPUS/site-plans/`

### Priority 3 — Tower B Structural Drawings

1. Visit: `https://archive.org/details/AA20a1`
2. Click the uploader name to see all their collections
3. Look for any "AA20" (without "a1"), "Tower B", "WTC 2", or "South Tower" collections
4. Download any structural sheet ZIPs found
5. Place in: `WTC_CORPUS/structural-drawings/`

### Priority 4 — Construction Photographs

1. Visit: `https://www.loc.gov/pictures/collection/gsc/`
2. Search for "World Trade Center"
3. Download relevant construction and completed-building photographs
4. Place in: `WTC_CORPUS/construction-photos/`

---

## Internet Archive Collection Reference

The NIST WTC Investigation Reports collection is at:
- Collection ID: `NIST_WTC_Investigation_Reports`
- Item ID: `NIST_WTC_Investigation_Reports-861612`
- Browse URL: `https://archive.org/details/NIST_WTC_Investigation_Reports-861612`
- API: `https://archive.org/metadata/NIST_WTC_Investigation_Reports-861612`

To list all files in the collection via API:
```
curl -sL "https://archive.org/metadata/NIST_WTC_Investigation_Reports-861612" | python3 -c "import json,sys; d=json.load(sys.stdin); [print(f['name']) for f in d.get('files',[])]"