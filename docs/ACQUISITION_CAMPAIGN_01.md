# Acquisition Campaign 01: Tower B Structural Drawings (CG-1)

**Campaign Identifier:** ACQ-CAMPAIGN-01  
**Target Gap:** **CG-1 — Tower B (South Tower / WTC 2) Structural Drawings**  
**Date:** August 11, 2026  
**Author:** Research Lead  
**Governing Standard:** [`docs/AI_WORKING_PRINCIPLES.md`](file:///opt/wtc/wtc-twin-towers/docs/AI_WORKING_PRINCIPLES.md) (Principles 1, 7, 14)  
**Basis Document:** [`docs/CRITICAL_GAP_ACQUISITION_STRATEGY.md`](file:///opt/wtc/wtc-twin-towers/docs/CRITICAL_GAP_ACQUISITION_STRATEGY.md)  

---

## 1. Target Evidence Gap

- **Gap Identifier:** `CG-1`
- **Description:** Absence of dedicated high-resolution structural engineering drawings and sheet scans for Tower B (WTC 2), equivalent to the 895 PNGs held for Tower A in the `AA20a1` collection.
- **Target Items:** Structural framing plans, core column schedules, perimeter spandrel connection sheets, floor truss assemblies, mechanical floor framing, and rooftop structural details for WTC 2.

---

## 2. Rationale for Selection

Campaign 01 selects **CG-1** as the #1 highest-value acquisition target for the following strategic reasons:

1. **Largest Single Readiness Gain:** Moving Tower B from **25% to 60%** (+35% readiness jump) delivers the single largest readiness increase achievable across any individual evidence gap.
2. **Governance Compliance:** Resolves the critical compliance violation of **Principle 7 (*No Symmetry Assumptions*)**, ending reliance on Tower A geometry to model Tower B.
3. **High Acquisition Likelihood:** The `AA20a1` collection on Internet Archive was uploaded as part of a multi-part release. Sister collections containing Tower B drawings (e.g., `AA20b1` or related uploader sets) have a high probability of existing in public digital archives.
4. **Buildability Priority:** Aligns with **Principle 14 (*Preserve Buildability*)** by prioritizing primary physical structural geometry over decorative or interior features.
5. **Low Effort / Fast Turnaround:** The initial discovery campaign targets public web archives requiring low operational effort (~1 hour search campaign).

---

## 3. Most Promising Repositories

| Repository | URL / Endpoint | Target Collection | Expected Format |
|---|---|---|---|
| **Internet Archive** | `https://archive.org/details/AA20a1` | `AA20a1` Uploader Profile & Sister Uploads | ZIP files containing PNG/TIFF sheet scans (~4896x3632 px) |
| **NIST FOIA Public Repository** | `https://www.nist.gov/world-trade-center-investigation` | NCSTAR 1-1 / 1-2 Structural Drawing Appendix Releases | PDF drawing sets, TIFF image archives |
| **LERA Digital Archives** | Leslie E. Robertson Associates Historical Archive | WTC 2 Structural Contract Drawings | High-resolution PDF / TIFF blueprints |
| **Port Authority of NY/NJ Archives** | PANYNJ Digital Records / FOIL Repository | WTC 2 Engineering Contract Drawings | Scanned engineering sheet sets |

---

## 4. Specific Search Queries

### Internet Archive API & UI Queries
```text
uploader:AA20a1
identifier:AA20b1 OR identifier:AA20-B OR identifier:AA20_Tower_B
"South Tower structural drawings"
"WTC 2 structural sheets"
"World Trade Center Tower 2 structural drawings"
"AA20" AND "Tower B"
"LERA South Tower structural"
```

### Automated Discovery Agent Configuration (`agents/discovery/sources.json`)
```json
{
  "source_id": "internet_archive_wtc2_structural",
  "name": "Internet Archive - WTC 2 Structural Sheets",
  "base_url": "https://archive.org/advancedsearch.php",
  "query_template": "q=title:({query})+AND+mediatype:(texts+OR+image)&fl[]=identifier,title,creator,publicdate,downloads&sort[]=downloads+desc&rows=50&page=1&output=json",
  "search_terms": [
    "WTC 2 structural drawings",
    "South Tower structural sheets",
    "AA20b1",
    "WTC Tower B framing plans",
    "Leslie E Robertson WTC 2"
  ]
}
```

---

## 5. Expected Evidence Types

- **High-Resolution PNG/TIFF Image Scans:** Dimensional scans (~4896x3632 pixels) of original 1967 structural engineering sheets showing column line grids, beam schedules, and truss connections.
- **Multi-page PDF Drawing Books:** Vector or scanned PDF drawing sets covering foundation steel, core framing, and floor deck layouts.
- **XLS / CSV Structural Schedules:** Steel column member schedules, spandrel thickness tables, and plate thickness specifications.

---

## 6. Estimated Readiness Impact

| Metric | Pre-Campaign State | Post-Campaign Expected State | Impact Net Change |
|---|---|---|---|
| **Tower B Readiness** | **25%** | **60%** | **+35%** |
| **Overall Complex Readiness** | **~60%** | **~65%** | **+5%** |
| **Tower B Structural Confidence** | *25% Speculative / 50% Provisional* | **85% Well Supported** | **+35–60% Confidence** |
| **Critical Gaps Status** | CG-1 Open | **CG-1 Closed** | **1 Blocker Resolved** |

---

## 7. Success Criteria

1. **Acquisition Threshold:** Successful discovery and download of at least **100+ high-resolution structural sheet scans** explicitly designated for WTC 2 (Tower B).
2. **Structural Coverage:** Acquired drawings must cover at least 3 major building zones:
   - Base & Lower Zone framing (Floors 1–9)
   - Typical Floor framing (Floors 10–40 / 43–74 / 77–106)
   - Mechanical Floor structural framing (Floors 7–8, 41–42, 75–76, or 108–109)
3. **Pipeline Integration:**
   - 100% of acquired files downloaded and verified with SHA-256 hashes.
   - Asset registration complete in PostgreSQL `assets` and `asset_sources` tables.
   - Binary files stored in Cloudflare R2 object storage with correct MIME types.
4. **World Model Population:** Structural column grid coordinates and spandrel beam specs for WTC 2 populated in PostgreSQL `elements` table with `confidence_score = 85`.

---

## 8. Acquisition Execution Checklist

### Phase 1: Discovery & Acquisition (Hours 1–2)
- [ ] **Step 1.1:** Navigate to `https://archive.org/details/AA20a1` in web browser.
- [ ] **Step 1.2:** Click the uploader username profile link to view all uploaded collections.
- [ ] **Step 1.3:** Search uploader collections for `"AA20b1"`, `"Tower B"`, `"South Tower"`, `"WTC 2"`.
- [ ] **Step 1.4:** Execute automated discovery sweep via `python -m agents.discovery.main --build-searches`.
- [ ] **Step 1.5:** Run candidate finder `python -m agents.discovery.find_candidates` against configured search terms.
- [ ] **Step 1.6:** Download discovered ZIP archives and place in `WTC_CORPUS/structural-drawings/tower-b/`.

### Phase 2: Processing & Registration (Hours 3–4)
- [ ] **Step 2.1:** Execute SHA-256 hashing and deduplication check on downloaded files.
- [ ] **Step 2.2:** Upload verified files to Cloudflare R2 storage bucket using `agents/downloader/r2.py`.
- [ ] **Step 2.3:** Register acquired assets in PostgreSQL database `assets` and `asset_sources` tables via `agents/downloader/register_asset.py`.
- [ ] **Step 2.4:** Run classification agent `python -m agents.classification.asset_classifier` to mark assets as `Blueprint` / `Structural Drawing`.

### Phase 3: Verification & Governance Update (Hours 5–6)
- [ ] **Step 3.1:** Execute metadata analysis via `agents/metadata/ai_analyze.py` to extract sheet numbers and floor designation ranges.
- [ ] **Step 3.2:** Verify column line grid alignment against NIST NCSTAR 1-2 structural text descriptions.
- [ ] **Step 3.3:** Populate `evidence_references` and update `confidence_scores` to 85 (Well Supported) for WTC 2 structural elements in PostgreSQL.
- [ ] **Step 3.4:** Update `README.md` and `docs/CURRENT_STATE.md` to record CG-1 as **CLOSED** and update Tower B readiness to **60%**.

---

**Campaign Prepared:** August 11, 2026  
**Status:** ✅ CAMPAIGN 01 READY FOR EXECUTION
