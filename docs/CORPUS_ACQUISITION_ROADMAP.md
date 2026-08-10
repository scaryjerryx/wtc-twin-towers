# WTC Corpus Acquisition Roadmap

## Date

August 10, 2026

## Basis

Derived from `docs/CORPUS_INVENTORY.md`, `docs/CORPUS_RECONSTRUCTION_ASSESSMENT.md`, and `docs/EVIDENCE_GAP_REPORT.md`.

---

## 1. Acquisition Strategy

### Strategy Overview

The current corpus was acquired as a bulk ZIP download — likely from Internet Archive or a similar repository. This is an effective bootstrap method but is not sustainable for ongoing evidence acquisition. The project must transition from bulk imports to targeted, source-specific acquisition.

### Recommended Approach

```
Phase A: Corpus Ingestion (current corpus only)
    ↓
Phase B: Targeted Gap Acquisition (search → candidate → discovery → download)
    ↓
Phase C: Continuous Discovery (scheduled searches across multiple sources)
    ↓
Phase D: Community & Archive Partnerships
```

### Guiding Principles

1. **One source at a time** — Do not begin broad crawling. Test one search, one download, one asset registration per source.
2. **Verify before scaling** — Every source must be tested with a controlled search before broader searches are executed.
3. **Respect access policies** — Review robots.txt, terms of service, and rights before downloading from any source.
4. **Preserve provenance** — Every asset must trace back to its discovery URL and source.
5. **Deduplicate aggressively** — SHA-256 hash deduplication prevents redundant storage and processing.

---

## 2. Agent Reuse Assessment

### Existing Acquisition Infrastructure

| Component | Module | Status | Reuse? |
|---|---|---|---|
| Source configuration | `agents/discovery/sources.json` | 7 sources configured, 3 verified | ✅ Reuse — add new sources |
| Source seeding | `agents/discovery/main.py` | Idempotent URL upsert | ✅ Reuse as-is |
| Search request generation | `agents/discovery/build_searches.py` | Generates search_candidates from source templates | ✅ Reuse — add search URL templates for new sources |
| Candidate discovery | `agents/discovery/find_candidates.py` | Wikimedia Commons tested | ⚠️ Enhance — add source-specific scrapers for new repositories |
| Manual promotion | `agents/discovery/manual_promote.py` | Human-in-the-loop review | ✅ Reuse as-is |
| Discovery queue | `agents/discovery/queue_discoveries.py` | Idempotent queue creation | ✅ Reuse as-is |
| Downloader | `agents/downloader/main.py` | SHA-256, content-type, R2 upload | ✅ Reuse — may need content-type additions for new file types |
| Asset registration | `agents/downloader/register_asset.py` | asset_sources provenance | ✅ Reuse as-is |
| R2 storage | `agents/downloader/r2.py` | Operational | ✅ Reuse as-is |
| Orchestrator | `agents/run_pipeline.py` | 6 automated stages | ✅ Reuse as-is |
| Metadata processing | `agents/metadata/ai_analyze.py` | OpenRouter AI analysis | ✅ Reuse — already handles images and documents |
| Knowledge engine | `agents/engine/run_engine.py` | 7-stage pipeline | ✅ Reuse as-is |

### Required Enhancements

| Enhancement | Priority | Description |
|---|---|---|
| **Corpus bulk import path** | High | Current acquisition pipeline processes one URL at a time. A local file bulk importer would handle the existing corpus (ZIP files already on disk) without requiring HTTP downloads. |
| **Source-specific scrapers** | High | `find_candidates.py` currently only handles Wikimedia Commons HTML. New sources (Internet Archive, NIST, Library of Congress) require source-specific HTML/API parsers. |
| **Search URL templates for new sources** | High | `build_searches.py` needs verified search URL templates for Internet Archive, NIST, and other repositories. |
| **XLS/XLSX processor** | Medium | The exterior wall schedule is an Excel file. No spreadsheet processor exists. |
| **DJVU processor** | Medium | Much of the corpus is DJVU-OCR text. A dedicated DJVU text processor would improve extraction quality. |
| **PNG/TIFF sheet processor** | Medium | The AA20a1 collection is 895 PNG structural sheets. A blueprint/sheet processor exists as a placeholder (`agents/processors/blueprint_processor.py`) but is not implemented. |
| **Bulk deduplication** | Low | Within-corpus deduplication (duplicate ZIPs, duplicate DJVU files) should be handled before ingestion. |

---

## 3. Targeted Gap Acquisition Plan

### Phase B-1: Tower B Structural Drawings (CG-1)

| Field | Detail |
|---|---|
| **Target** | Structural sheets for WTC 2 (South Tower) equivalent to AA20a1 |
| **Primary source** | Internet Archive — search for "AA20" (sister collection to AA20a1) |
| **Secondary sources** | NIST FOIA releases, LERA archives |
| **Search URL template** | `https://archive.org/search?query=WTC+tower+B+structural+sheets` |
| **Expected file types** | ZIP archives containing PNG/TIFF sheets |
| **Estimated volume** | 400-900MB (similar to AA20a1) |
| **Agent readiness** | `find_candidates.py` needs Internet Archive search result parser |

### Phase B-2: Architectural Floor Plans (CG-2)

| Field | Detail |
|---|---|
| **Target** | Floor plans for all WTC buildings showing architectural layouts |
| **Primary source** | NIST investigation records (NCSTAR reports contain floor plan reproductions) |
| **Secondary sources** | Port Authority archives, Yamasaki archives, NYC DOB records |
| **Search URL template** | NIST: `https://www.nist.gov/world-trade-center-investigation/NCSTAR-reports` |
| **Expected file types** | PDF reports containing embedded floor plans, standalone TIFF/PDF drawings |
| **Estimated volume** | 500MB-2GB (NCSTAR reports are comprehensive) |
| **Agent readiness** | `find_candidates.py` needs NIST publication page parser |

### Phase B-3: Site Plan and Plaza (CG-3)

| Field | Detail |
|---|---|
| **Target** | Site-level plans, plaza drawings, concourse level plans |
| **Primary source** | Internet Archive, Yamasaki archives |
| **Secondary sources** | Port Authority archives, NYC City Planning |
| **Expected file types** | PDF drawings, TIFF scans |
| **Estimated volume** | 50-200MB |
| **Agent readiness** | Same as B-1 |

### Phase B-4: Tower A Upper Wall Schedules (CG-4)

| Field | Detail |
|---|---|
| **Target** | Exterior wall schedules for Tower A floors 10-110 |
| **Primary source** | LERA/Skilling archives, NIST structural reports |
| **Expected file types** | Excel spreadsheets, PDF schedules |
| **Estimated volume** | 5-50MB |
| **Agent readiness** | Reuse existing downloader; may need XLSX processor |

### Phase B-5: Construction and Interior Photographs (IG-1, IG-2)

| Field | Detail |
|---|---|
| **Target** | Construction photographs (1966-1973) and interior photographs (1973-2001) |
| **Primary source** | Library of Congress HABS/HAER collection, Wikimedia Commons |
| **Secondary sources** | Historical photograph archives, Port Authority promotional materials |
| **Search URL templates** | Wikimedia Commons: existing template works. LoC: needs custom search URL |
| **Expected file types** | JPEG, TIFF photographs |
| **Estimated volume** | 1-5GB (photographs are larger files) |
| **Agent readiness** | Wikimedia Commons already supported. LoC needs new scraper. Photo processor already exists (M21). |

### Phase B-6: Buildings 3-7 (IG-3)

| Field | Detail |
|---|---|
| **Target** | Structural and architectural drawings for WTC 3-7 |
| **Primary source** | NIST investigation records (WTC 7 extensively documented), Port Authority archives |
| **Expected file types** | PDF reports, structural sheets, architectural drawings |
| **Estimated volume** | 200MB-1GB |
| **Agent readiness** | Same as B-2 |

---

## 4. Source Configuration Plan

### New Sources to Add to `sources.json`

| Source | URL | Type | Priority | Search Template |
|---|---|---|---|---|
| Internet Archive | `https://archive.org/` | archive | Critical | `https://archive.org/search?query={query}` |
| NIST WTC Investigation | `https://www.nist.gov/world-trade-center-investigation/` | government | Critical | `https://www.nist.gov/search?query={query}&type=publication` |
| Library of Congress | `https://www.loc.gov/` | library | Important | `https://www.loc.gov/search/?q={query}` |
| NYC Department of Buildings | `https://www.nyc.gov/site/buildings/index.page` | government | Important | TBD — may require FOIL request |
| Wikimedia Commons | (existing) | commons | Operational | Existing template verified |

### Source Verification Protocol

For each new source:

1. Add source to `sources.json` with `status: "pending_review"`
2. Review access policies, robots.txt, terms of service
3. Configure rate limits conservatively (1 request/second minimum)
4. Test one controlled search
5. Review returned candidates for relevance
6. Test one permitted download
7. Verify provenance and deduplication
8. Update source status to `active`
9. Obtain approval before scaling

---

## 5. Corpus Ingestion Plan (Phase A)

Before any new acquisition, the existing corpus must be ingested into the evidence engine.

### Bulk Import Path Design

The current acquisition pipeline expects HTTP downloads from discovery URLs. A bulk import path would:

1. Scan the `WTC_CORPUS/` directory for eligible files
2. Create asset records with `source_id` referencing a "WTC Corpus" source
3. Calculate SHA-256 hashes
4. Upload to R2
5. Register in `asset_sources` with `original_url` set to the local file path
6. Create `metadata_queue` entries for AI analysis
7. Feed into the existing knowledge engine

### Ingestion Order

| Priority | Files | Count | Rationale |
|---|---|---|---|
| 1 | `AA20a1.zip` (extracted PNGs) | 895 | Largest, highest-value collection |
| 2 | `wtc-exterior-wall-to-9th-floor-schedules-tower-a.zip` (XLS) | 1 | Structured data, directly usable |
| 3 | `WTCI-000151-P - WTC7 OEM fl 23 spec manual_hocr_searchtext.txt.gz` | 1 | Best OCR quality |
| 4 | `wtci-000131-l-002_202603.zip` (extracted DJVU) | 250+ | Largest text corpus (after dedup) |
| 5 | Drawing Book ZIPs (deduplicated) | 10 | Structural drawing book index pages |
| 6 | Standalone DJVU text files | 8 | Smaller files, lower priority |
| 7 | Duplicates and low-value files | — | Skip during ingestion |

### Files to Skip

- `WTCI000016L (1).zip` (duplicate of `WTCI000016L.zip`)
- `WTCI000131L002 (1).zip` (duplicate of `WTCI000131L002.zip`)
- `wtci-000038-l.zip` (partial duplicate — only unique file is WTCI-000039-L variant)
- `WTCI-000214-P jfk incident logs on 911_djvu.txt` (not reconstruction-relevant)
- `TTStructuralArchivedIndexToBooksApr20195_201906.zip` (finding aid only)
- `AA20a1_archive.torrent`, `AA20a1_meta.xml`, `AA20a1_files.xml` (metadata, not evidence)
- Empty category directories

---

## 6. Readiness Assessment

### Reconstruction Readiness by Area

| Area | Current Readiness | With Corpus Ingestion | With Critical Gaps Filled | With All Gaps Filled |
|---|---|---|---|---|
| **Site** | 0% | 5% | 60% | 85% |
| **Tower A** | 5% | 40% | 80% | 90% |
| **Tower B** | 0% | 0% | 60% | 85% |
| **Plaza** | 0% | 0% | 50% | 80% |
| **Concourse** | 0% | 0% | 40% | 75% |
| **WTC 3 (Marriott)** | 0% | 0% | 30% | 70% |
| **WTC 4** | 0% | 0% | 30% | 65% |
| **WTC 5** | 0% | 0% | 30% | 65% |
| **WTC 6** | 0% | 0% | 30% | 65% |
| **WTC 7** | 5% | 15% | 50% | 75% |

### Readiness Definitions

| Percentage | Definition |
|---|---|
| 0% | No evidence available |
| 5-15% | Some documentation exists (specifications, partial structural) |
| 30-50% | Key structural/architectural evidence acquired |
| 60-80% | Sufficient evidence for reconstruction modelling |
| 85-95% | Comprehensive evidence with photographic and operational documentation |

### Key Observations

1. **Tower A** is the most achievable near-term reconstruction target — the corpus already provides structural sheets and wall schedules for lower floors.

2. **Tower B** is the highest-priority gap — no structural evidence exists for the South Tower. This must be acquired before any Tower B reconstruction can begin.

3. **Site, Plaza, and Concourse** require architectural evidence that is completely absent from the corpus. These are the defining public spaces of the WTC complex.

4. **Buildings 3-7** are distant targets. The corpus provides WTC7 specifications only. Significant acquisition work is needed.

5. **Even with all gaps filled**, some areas may never reach 100% readiness — some evidence may simply not exist or not be accessible. The reconstruction should embrace uncertainty where evidence cannot be obtained.

---

## 7. Recommended Next Actions

### Immediate (Phase A)

1. **Design and implement corpus bulk import path** — This unblocks ingestion of the existing 1,640 files.
2. **Deduplicate the corpus** — Remove duplicate ZIPs and DJVU files before ingestion.
3. **Ingest Priority 1-3 files** — AA20a1 sheets, wall schedules, WTC7 specs.
4. **Run AI metadata analysis on ingested sheets** — Use existing OpenRouter integration to generate descriptions and classifications for structural sheets.

### Short-Term (Phase B)

5. **Add Internet Archive as a configured source** — This is the most likely repository for Tower B structural sheets and site plans.
6. **Add NIST as a configured source** — NCSTAR reports are the best source for floor plans and structural analysis.
7. **Implement Internet Archive search result parser** in `find_candidates.py`.
8. **Develop XLS/XLSX processor** for structured spreadsheet evidence.

### Medium-Term (Phase C)

9. **Add Library of Congress as a configured source** — Primary source for construction and historical photographs.
10. **Implement blueprint/sheet processor** — Replace the placeholder in `agents/processors/blueprint_processor.py`.
11. **Enable scheduled discovery** — Move from manual pipeline invocation to periodic automated searches.

### Deferred

12. **Community and archive partnerships** — Direct outreach to archives for access to non-public materials.
13. **FOIL/FOIA requests** — Formal requests for government-held records not publicly available.
14. **Audio/video acquisition** — Lower priority; enhances experience but not required for structural reconstruction.