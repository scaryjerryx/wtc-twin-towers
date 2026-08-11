# WTCI-000262-L Deep Assessment

## Date: August 10, 2026

## Source

`WTC_CORPUS/skyscraperforum.zip` → `Book 7/WTCI-000262-L/`

WTCI (World Trade Center Information) drawing book 000262-L — a structural engineering drawing book from the Port Authority/NIST document series.

---

## Inventory

| Metric | Value |
|---|---|
| Total files | 1,364 TIFF |
| Total size | ~350MB |
| Average file size | ~257KB |
| File size range | ~50KB — 1.2MB |
| Subdirectories | 14 (0001, 0100, 0200, 0300, 0400, 0500, 0600, 0700, 0800, 0900, 1000, 1100, 1200, 1300) |
| Files per directory | ~97 (1,364 ÷ 14) |
| Format | TIFF (scanned structural engineering sheets) |

### Subdirectory Structure

| Directory | File Range | Estimated Pages | Notes |
|---|---|---|---|
| 0001/ | 0001-0099 | ~99 | Beginning of book |
| 0100/ | 0100-0199 | ~99 | |
| 0200/ | 0200-0299 | ~99 | |
| 0300/ | 0300-0399 | ~99 | |
| 0400/ | 0400-0499 | ~99 | |
| 0500/ | 0500-0599 | ~99 | |
| 0600/ | 0600-0699 | ~99 | |
| 0700/ | 0700-0799 | ~99 | |
| 0800/ | 0800-0899 | ~99 | |
| 0900/ | 0900-0999 | ~99 | |
| 1000/ | 1000-1099 | ~99 | |
| 1100/ | 1100-1199 | ~99 | |
| 1200/ | 1200-1299 | ~99 | |
| 1300/ | 1300-1364 | ~64 | End of book |

**The subdirectory names (0001, 0100, 0200...) are page number ranges, not floor numbers.** This is a sequentially numbered drawing book with 1,364 pages.

---

## WTCI Identifier Context

### WTCI-000262-L vs Existing Corpus

| WTCI ID | In Existing Corpus? | Format | Notes |
|---|---|---|---|
| WTCI-000016-L | ✅ WTCI000016L.zip | ZIP | Drawing book |
| WTCI-000017-L | ✅ WTCI000017L.zip | ZIP | Drawing book |
| WTCI-000020-L | ✅ WTCI000020L.zip | ZIP | Drawing book |
| WTCI-000030-L | ❌ (new in SkyscraperForum) | PDF | Drawing book |
| WTCI-000031-L | ❌ (new in SkyscraperForum) | PDF | Drawing book |
| WTCI-000033-L | ✅ WTCI000033L.zip | ZIP | Drawing book |
| WTCI-000034-L | ✅ WTCI000034L.zip | ZIP | Drawing book |
| WTCI-000036-L | ✅ WTCI000036L.zip | ZIP | Drawing book |
| WTCI-000037-L | ✅ WTCI000037L.zip | ZIP | Drawing book |
| WTCI-000038-L | ✅ WTCI000038L.zip | ZIP | Drawing book |
| WTCI-000040-L | ✅ WTCI000040L.zip | ZIP | Drawing book |
| WTCI-000059-L | ❌ (new in SkyscraperForum) | TIFF | Partial media file |
| WTCI-000131-L | ✅ WTCI000131L002.zip | ZIP | Drawing book |
| WTCI-000262-L | ❌ **NOT in corpus** | TIFF | **This assessment** |
| WTCI-000721-L | ✅ Test document | PDF | Engine validation |
| WTCI-000722-L | ✅ WTCI000722L.zip | ZIP | Drawing book |
| WTCI-001040-L | ✅ WTCI001040L.zip | ZIP | Drawing book |
| WTCI-001067-L | ✅ WTCI001067L.zip | ZIP | Drawing book |

**WTCI-000262-L is not in the existing corpus.** It fills a gap in the WTCI drawing book sequence between 000131-L and 000721-L.

### WTCI Numbering Pattern

WTCI identifiers appear to follow a sequential numbering system:
- Lower numbers (000016-000040): Early drawing books — likely Tower A focused
- Mid numbers (000059, 000131, 000262): Middle-range books — **potential Tower B content**
- Higher numbers (000721-001067): Later books — likely Tower A or mixed

WTCI-000262-L sits in the middle range where Tower B content is most likely.

---

## Content Assessment

### What WTCI Drawing Books Typically Contain

Based on the existing WTCI books in the corpus (which have been partially processed through the knowledge engine), WTCI structural drawing books contain:

| Content Type | Typical Presence | Reconstruction Value |
|---|---|---|
| Structural framing plans | ✅ Yes | High — floor-by-floor column and beam layouts |
| Column schedules | ✅ Yes | High — column types, sizes, locations |
| Beam schedules | ✅ Yes | High — beam types, spans, connections |
| Floor deck details | ✅ Yes | Medium — floor slab construction |
| Connection details | ✅ Yes | Medium — beam-to-column, column splice |
| Exterior wall details | ⚠️ Sometimes | High — panel types, column covers |
| Core details | ⚠️ Sometimes | High — elevator banks, stairwells, mechanical shafts |
| Mechanical floor details | ⚠️ Sometimes | Medium — mechanical floor framing |
| Hat truss details | ⚠️ Sometimes | High — upper floor structural system |
| Tower identification | ✅ Yes | Critical — "WTC 1" or "WTC 2" or "1WTC"/"2WTC" on title blocks |
| Floor identification | ✅ Yes | Critical — floor numbers on framing plans |
| Drawing numbers | ✅ Yes | Medium — cross-referencing |
| Revision history | ✅ Yes | Medium — as-built vs design intent |

### Tower A vs Tower B Assessment

**Unknown — requires content inspection.** The OCR attempt on sample TIFFs timed out (files too large for tesseract at ~500KB-1.2MB each). Visual inspection of title blocks is needed to determine tower assignment.

**Indicators favoring Tower B content:**
1. WTCI-000262-L is in the middle of the WTCI numbering range (000016-001067), where Tower B books may be concentrated
2. The existing corpus has 14 WTCI books, all heavily Tower A-focused — the missing books in the sequence may include Tower B
3. The large page count (1,364 pages) suggests a comprehensive book — possibly covering an entire tower's structural system

**Indicators favoring Tower A content:**
1. Most WTCI books in the existing corpus are Tower A
2. Tower B structural documentation is generally scarcer than Tower A
3. No direct evidence of Tower B content without visual inspection

**Best estimate: 40-60% chance of Tower B content, 60-80% chance of Tower A content, possibly both.**

---

## Structural Systems Potentially Represented

Based on the page count (1,364 pages) and typical WTCI book content:

| System | Likelihood | Estimated Pages | Notes |
|---|---|---|---|
| Floor framing plans | **High** | 200-400 | One plan per floor or floor type |
| Column schedules | **High** | 100-200 | Column types, sizes, locations by floor |
| Beam schedules | **High** | 100-200 | Beam types, spans, connections |
| Exterior wall panels | **Medium** | 50-100 | Panel types, dimensions, column covers |
| Core details | **Medium** | 50-100 | Elevator banks, stairwells, mechanical shafts |
| Connection details | **Medium** | 100-200 | Beam-to-column, column splice, bracing |
| Mechanical floors | **Low-Medium** | 20-50 | Floors 7-8, 41-42, 75-76, 108-109 |
| Hat truss | **Low** | 10-30 | Floors 107-110 structural system |
| Foundation/base | **Low** | 10-20 | Column base plates, foundation interface |
| General notes/index | **High** | 10-20 | Drawing index, general notes, abbreviations |

---

## Comparison Against Other Structural Collections

| Collection | Format | Pages/Sheets | Tower Coverage | Overlap with WTCI-000262-L |
|---|---|---|---|---|
| AA20a1 | 895 PNGs | 895 | Tower A only | **Different format, different books** — AA20a1 is a separate collection, not WTCI |
| Existing WTCI books (14) | ZIP/DJVU | ~500-1000+ | Mostly Tower A | **No overlap** — WTCI-000262-L is a different book |
| Gerrycan AA20a1 | 910 entries | 910 | Tower A only | **No overlap** — different collection |
| Gerrycan floor databases | SDB | 2 floors | Tower A (96) + Tower B (75) | **No overlap** — SDB vs TIFF, different data types |
| NCSTAR 1-1/1-2 | PDF | ~500 pages | Both towers | **Complementary** — NCSTAR describes systems; WTCI provides detailed sheets |
| SkyscraperForum Books 2-6, 20 | TIFF | ~620 | Unknown | **No overlap** — different books |

**WTCI-000262-L is unique in the corpus.** No other collection has this WTCI identifier or this specific set of 1,364 structural sheets.

---

## Reconstruction Value Estimate

### If Tower A Only

| Area | Current Readiness | Gain | New Readiness | Source of Gain |
|---|---|---|---|---|
| Tower A | 65% | +2% | 67% | Additional structural detail — column schedules, beam schedules, connection details |
| Tower B | 60% | 0% | 60% | No Tower B content |
| Overall | ~50% | +0.5% | ~50.5% | Marginal — Tower A already well-evidenced |

### If Tower B Content Present

| Area | Current Readiness | Gain | New Readiness | Source of Gain |
|---|---|---|---|---|
| Tower A | 65% | +1% | 66% | Supplementary Tower A detail |
| Tower B | 60% | +5-8% | 65-68% | **Tower B structural sheets — partially closes CG-1** |
| Overall | ~50% | +2-3% | ~52-53% | Significant — Tower B is the largest remaining structural gap |

### If Both Towers

| Area | Current Readiness | Gain | New Readiness |
|---|---|---|---|
| Tower A | 65% | +1% | 66% |
| Tower B | 60% | +5-8% | 65-68% |
| Overall | ~50% | +2-3% | ~52-53% |

**Best case: +2-3% overall readiness if Tower B content is present. Worst case: +0.5% if Tower A only.**

---

## Is WTCI-000262-L One of the Highest-Value Remaining Structural Collections?

### Ranking of Unassessed Structural Collections

| Rank | Collection | Files | Potential Gain | Key Factor |
|---|---|---|---|---|
| **1** | **IA AA20a1 uploader Tower B sheets** | Unknown | **+10%** | Would fully close CG-1 if found |
| **2** | **WTCI-000262-L (this collection)** | 1,364 TIFFs | **+2-3%** | Largest unassessed WTCI book; possible Tower B content |
| 3 | WTCI-000030-L | 1 PDF | +0.5% | New WTCI book, small |
| 4 | WTCI-000031-L | 1 PDF | +0.5% | New WTCI book, small |
| 5 | WTCI-000059-L | 195 TIFFs | +0.5% | Partial media file |
| 6 | SkyscraperForum Books 2-6, 20 | ~620 TIFFs | +0.5-1% | Unidentified — may overlap with existing books |

**Yes — WTCI-000262-L is the second highest-value unassessed structural collection in the corpus**, behind only the undiscovered IA AA20a1 Tower B sheets. Its 1,364 pages and mid-range WTCI number make it the most promising candidate for Tower B structural content among all currently held collections.

### Why It Matters

1. **Size:** 1,364 pages is the largest single WTCI book in or out of the corpus
2. **Uniqueness:** Not duplicated in any existing collection
3. **Position:** Mid-range WTCI number (000262) — where Tower B books are most likely
4. **Gap:** CG-1 (Tower B structural drawings) is the most critical remaining structural gap
5. **Format:** TIFF scans of original structural sheets — directly usable for modeling

---

## Recommendation

1. **Extract WTCI-000262-L from the ZIP** to `WTC_CORPUS/structural-drawings/wtci-000262-l/`
2. **Visually inspect 20-30 sample sheets** across the page range (0001, 0300, 0600, 0900, 1200) to determine:
   - Tower assignment (WTC 1 vs WTC 2 on title blocks)
   - Content types (framing plans, column schedules, beam schedules)
   - Floor coverage (which floors are represented)
3. **If Tower B content is confirmed:** This becomes a **Priority 1** collection — immediately after IA Tower B sheet search
4. **If Tower A only:** This becomes a **Priority 3** collection — valuable supplementary detail but not gap-closing
5. **OCR is not practical** for 1,364 large TIFFs — visual inspection of title blocks is the fastest assessment method

**This collection warrants extraction and visual inspection. It is the most promising unassessed source of Tower B structural evidence currently held.**