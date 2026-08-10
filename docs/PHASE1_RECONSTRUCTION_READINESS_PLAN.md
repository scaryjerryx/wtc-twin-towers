# Phase 1 Reconstruction Readiness Plan

## Date: August 10, 2026

## Goal: 35% → ~70% Readiness

## Phase 1 Tasks

### Task 1: IA Tower B Structural Collections

| Field | Value |
|---|---|
| **Repository** | Internet Archive — AA20a1 uploader's other collections |
| **Starting point** | `https://archive.org/details/AA20a1` |
| **Action** | Operator must click uploader name, browse all collections for "AA20", "Tower B", "WTC 2", "South Tower" |
| **Automation** | ❌ Not automatable — requires manual browser navigation |
| **Expected gain** | +15% overall readiness |
| **Corpus growth** | 50-400MB (ZIP files of structural sheets) |
| **Processing effort** | Low — ZIP extraction + PNG viewing |
| **Evidence categories** | Tower B structural sheets, floor framing, column schedules |

### Task 2: LoC Gottscho-Schleisner Photographs

| Field | Value |
|---|---|
| **Repository** | Library of Congress — `https://www.loc.gov/pictures/collection/gsc/?q=World+Trade+Center` |
| **Action** | Search LoC API, download high-resolution TIFF/JPEG files |
| **Automation** | ⚠️ Partial — API search automatable, individual downloads may need manual selection |
| **Expected gain** | +10% overall readiness |
| **Corpus growth** | 750MB-2.25GB (150-450 photographs) |
| **Processing effort** | Medium — photo organization, metadata extraction |
| **Evidence categories** | Construction photos, exterior photos, interior photos, plaza photos |

### Task 3: Wikimedia Full-Resolution SVGs

| Field | Value |
|---|---|
| **Repository** | Wikimedia Commons |
| **Action** | Download full-resolution versions of 3 site plan SVGs |
| **Automation** | ✅ Automatable — direct download from file pages |
| **Expected gain** | +5% overall readiness |
| **Corpus growth** | ~1-5MB (3 SVG files) |
| **Processing effort** | Low — SVG viewing and analysis |
| **Evidence categories** | Site plans, building arrangement |

### Task 4: NCSTAR Floor Plan Extraction

| Field | Value |
|---|---|
| **Repository** | Local corpus — `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-1_Appendix_C-G.pdf` |
| **Action** | Extract embedded images from 43MB image-based PDF |
| **Automation** | ✅ Automatable — `pdfimages` or `pdftoimage` tools |
| **Expected gain** | +5% overall readiness |
| **Corpus growth** | 50-200MB (extracted images) |
| **Processing effort** | Medium — image extraction, organization, OCR |
| **Evidence categories** | Floor plan figures, structural drawing reproductions |

### Task 5: NCSTAR Visual Evidence Processing

| Field | Value |
|---|---|
| **Repository** | Local corpus — `WTC_CORPUS/engineering-reports/ncstar/critical/` (4 NCSTAR 1-8 volumes, 412MB) |
| **Action** | Extract embedded photographs from NCSTAR 1-8 PDFs |
| **Automation** | ✅ Automatable — `pdfimages` extraction |
| **Expected gain** | +5% overall readiness |
| **Corpus growth** | 200-500MB (extracted photographs) |
| **Processing effort** | Medium — image extraction, categorization |
| **Evidence categories** | Construction photos, interior photos, exterior photos, damage documentation |

---

## Automation vs Operator Summary

| Task | Automatable? | Operator Required? |
|---|---|---|
| IA Tower B collections | ❌ No | ✅ Yes — manual browser navigation |
| LoC Gottscho-Schleisner | ⚠️ Partial | ✅ Yes — API search + manual selection |
| Wikimedia SVGs | ✅ Yes | ❌ No — direct download |
| NCSTAR floor plan extraction | ✅ Yes | ❌ No — local processing |
| NCSTAR visual evidence extraction | ✅ Yes | ❌ No — local processing |

---

## Expected Phase 1 Results

### Readiness After Phase 1

| Area | Current | After Phase 1 | Gain |
|---|---|---|---|
| Site | 35% | 55% | +20% |
| Plaza | 15% | 30% | +15% |
| Tower A | 55% | 70% | +15% |
| Tower B | 45% | 70% | +25% |
| Concourse | 10% | 20% | +10% |
| WTC 3-6 | 0% | 5% | +5% |
| WTC 7 | 50% | 60% | +10% |
| Observation Deck | 5% | 20% | +15% |
| Windows on the World | 5% | 20% | +15% |
| **Overall** | **~35%** | **~65%** | **+30%** |

### Corpus Growth

| Metric | Before | After | Change |
|---|---|---|---|
| Total files | ~45 | ~600-900 | +550-850 |
| Total size | ~1GB | ~2-4GB | +1-3GB |
| Evidence categories | 6 | 8 | +2 (construction photos, interior photos) |

### Newly Modelable Elements

| Element | Evidence Source | Modelable? |
|---|---|---|
| WTC 1 structural skeleton | AA20a1 + NCSTAR 1-1 | ✅ Full |
| WTC 2 structural skeleton | IA Tower B sheets + NCSTAR 1-1/1-2 | ✅ Full (if Tower B sheets found) |
| Site footprint | Wikimedia SVGs + NCSTAR | ✅ Full |
| Construction timeline 1966-1969 | NCSTAR 1-1 | ✅ Full |
| Exterior wall system (WTC 1, floors 1-9) | XLS spreadsheet | ✅ Full |
| Floor framing plans (both towers) | NCSTAR 1-1 App C-G extraction | ✅ Partial |
| Visual reference (both towers) | NCSTAR 1-8 + LoC photos | ✅ Full |
| Plaza visual reference | LoC photos | ⚠️ Partial |
| Interior visual reference | NCSTAR 1-8 + LoC photos | ⚠️ Partial |
