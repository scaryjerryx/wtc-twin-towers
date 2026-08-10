# WTC Evidence Corpus Inventory

## Inspection Date

August 10, 2026

## Source

`/opt/wtc/wtc-twin-towers/WTC_CORPUS/` (extracted from `WTC_CORPUS.zip`, 455MB, 39 original files)

## Summary Statistics

| Metric | Count |
|---|---|
| Top-level files | 31 |
| Top-level directories | 7 (empty category placeholders) |
| Extracted files (after unzipping all archives) | 1,640 |
| Total extracted size | 454MB |
| File types | PNG (895), TXT (725), XML (6), SQLite (3), XLS/XLSX (2), JPG (1), other (8) |

---

## Collection Inventory

### 1. AA20a1 — Tower A Structural Sheets

| Field | Value |
|---|---|
| Source filename | `AA20a1.zip` |
| Size | 401MB |
| File count | 895 PNG images + 3 metadata files |
| Category | **Structural Drawings** |
| Reconstruction relevance | **Critical** |

**Contents:**

- `TT A Sheets/` — Tower A structural drawing sheets organized in 9 packs (Pack1 through Pack4 plus Pack3-1 through Pack3-6)
- 895 PNG images named by sheet designation (e.g., `SA401_0.png` through `SA404_3.png`, `SKA10-84_0.png` through `SKA12-84_3.png`, `A-A-10_0.png` through `A-A-13_3.png`)
- Each sheet appears to be a 4-tile split (`_0` through `_3`) — high-resolution scans of large-format structural drawings
- `AA20a1_meta.sqlite` — SQLite database (likely sheet index/metadata)
- `AA20a1_files.xml` and `AA20a1_meta.xml` — Internet Archive metadata

**Reconstruction value:** These are the actual structural engineering sheets for Tower A (North Tower). Contains column layouts, beam schedules, connection details, and structural system drawings. Fundamental for any spatial reconstruction.

**OCR assessment:** Images only (no embedded text). Would require OCR processing for automated fact extraction. Sheet designations and metadata may be in the SQLite database.

---

### 2. Structural Drawing Books — DJVU OCR Text

| Field | Value |
|---|---|
| Source filenames | 12 ZIP files (WTCI000016L through WTCI001067L, plus wtci-000038-l) |
| Total size | ~8MB (combined) |
| File count | ~60 DJVU text files |
| Category | **Structural Drawing Books** |
| Reconstruction relevance | **High** |

**Drawing Books Present:**

| Book | Source ZIP | Key Files |
|---|---|---|
| Drawing Book 2 | WTCI000722L.zip | WTCI-000012-L, WTCI-000722-L |
| Drawing Book 3 | (in wtci-000131-l-002) | WTCI-000013-L through WTCI-000025-L |
| Drawing Book 4 | WTCI000017L.zip | WTCI-000014-L through WTCI-000019-L, WTCI-000538-L, WTCI-000540-L, WTCI-000709-L |
| Drawing Book 5 | WTCI000016L.zip | WTCI-000016-L, WTCI-000710-L (duplicate in "(1)" variant) |
| Drawing Book 6 | WTCI000020L.zip | WTCI-000020-L through WTCI-000023-L |
| Drawing Book 7 | WTCI000131L002.zip | WTCI-000024-L through WTCI-001061-L (12 files, duplicated in "(1)" variant) |
| Drawing Book 8 | WTCI001067L.zip | WTCI-000703-L, WTCI-001059-L through WTCI-001068-L (9 files) |
| Drawing Book 10 | WTCI001040L.zip | WTCI-000032-L, WTCI-001040-L |
| Drawing Book 11 | WTCI000033L.zip | WTCI-000033-L, WTCI-000705-L, WTCI-001041-L |
| Drawing Book 12 | WTCI000034L.zip | WTCI-000034-L, WTCI-000035-L, WTCI-001042-L |
| Drawing Book 13 | WTCI000036L.zip | WTCI-000036-L, WTCI-001043-L |
| Drawing Book 18 | WTCI000037L.zip | WTCI-000037-L, WTCI-000707-L, WTCI-001044-L |
| Drawing Book 19 | WTCI000038L.zip | WTCI-000038-L, WTCI-000039-L (duplicate in wtci-000038-l) |
| Drawing Book 20 | WTCI000040L.zip | WTCI-000040-L, WTCI-001046-L |

**OCR Quality:** Fair to Poor. The DJVU OCR process extracts text from scanned engineering drawings. Tables of contents and index pages are partially legible with dates, sheet numbers, and revision codes visible. Drawing body text is heavily degraded with OCR artifacts, Cyrillic character substitution, and line noise. Structural terminology (column types, beam designations, floor numbers) is intermittently recognizable.

**Reconstruction value:** These are the drawing book index pages and OCR-extracted text from the full Structural Drawing Book collection. The WTCI IDs map to the original document numbering system. Critical for understanding which sheets exist and what each drawing book contains.

---

### 3. WTCI-000131-L-002 Comprehensive Collection

| Field | Value |
|---|---|
| Source filename | `wtci-000131-l-002_202603.zip` |
| Size | 35MB |
| File count | 250+ DJVU text files |
| Category | **Comprehensive Document Corpus** |
| Reconstruction relevance | **Critical** |

**Contents:**

The largest single text collection, containing DJVU-OCR text for 250+ WTCI documents spread across structural (-L suffix), various (-P suffix), and structural drawing book (-STB suffix) types.

**Document types present:**

- **-L suffix (~40 files):** Structural/engineering drawings and drawing book pages. Examples: WTCI-000010-L through WTCI-000040-L, WTCI-000130-L, WTCI-000131-L, WTCI-000472-L, WTCI-000538-L, WTCI-000540-L, WTCI-000702-L through WTCI-000710-L, WTCI-000721-L, WTCI-000722-L, WTCI-000733-L, WTCI-001040-L through WTCI-001068-L
- **-P suffix (~200 files):** Various document types (specifications, reports, correspondence). Examples: WTCI-000002-P through WTCI-000715-P covering structural reports, incident logs, project documentation
- **Key documents:** WTCI-000721-L (the 39-page engineering drawing book already used as test evidence), WTCI-000265-P (large document), WTCI-000151-P (WTC7 OEM spec manual — also present as separate file)

**OCR Quality:** Fair. Same DJVU-OCR limitations as the Drawing Books. Engineering drawings with structured data (tables, schedules) retain more usable text than narrative documents. Dates, numbers, and codes are the most reliably extracted information.

---

### 4. WTC7 OEM Specification Manual

| Field | Value |
|---|---|
| Source filenames | `WTCI-000151-P - WTC7 OEM fl 23 spec manual_djvu.txt` (669KB), `WTCI-000151-P - WTC7 OEM fl 23 spec manual_hocr_searchtext.txt.gz` (187KB compressed) |
| Size | ~856KB |
| File count | 2 text variants |
| Category | **Engineering Reports / Specifications** |
| Reconstruction relevance | **High** |

**Contents:**

Mayor's Office of Emergency Management specification manual for 7 World Trade Center, issued by Swanke Hayden Connell Architects. Contains the full Division 1-16 specification sections including general requirements, site work, concrete, masonry, metals, structural steel, thermal/moisture protection, doors/windows, finishes, specialties, equipment, furnishings, conveying systems, mechanical, and electrical.

**OCR Quality:** Good. The HOCR (hOCR) variant provides cleaner, better-structured text than the DJVU variant. Specification sections are clearly delineated with division numbers and titles. Text is largely complete and readable.

**Reconstruction value:** Detailed specifications for WTC7 construction. Provides material types, standards, and construction requirements. Also references WTC complex-wide systems (PATH, Plaza, Concourse).

---

### 5. Exterior Wall Schedules — Tower A

| Field | Value |
|---|---|
| Source filename | `wtc-exterior-wall-to-9th-floor-schedules-tower-a.zip` |
| Size | 1.5MB |
| File count | 1 Excel file (.xls) |
| Category | **Structural Drawings / Engineering Data** |
| Reconstruction relevance | **Critical** |

**Contents:**

`WTC - Exterior Wall to 9th Floor Schedules - Tower A.xls` — An Excel spreadsheet containing exterior wall schedule data for Tower A up to the 9th floor. Contains structured tabular data (column locations, wall panel types, elevations).

**OCR Quality:** N/A (structured spreadsheet, not OCR-derived)

**Reconstruction value:** Directly provides exterior wall panel dimensions, locations, and types for the lower floors of the North Tower. This is precise geometric data suitable for 3D reconstruction. The spreadsheet format means it can be programmatically parsed.

---

### 6. WTC Twin Towers Structural Database

| Field | Value |
|---|---|
| Source filename | `wtc-twin-towers-structural-database.zip` |
| Size | 9.3KB |
| File count | 1 text file |
| Category | **Structural Database / Metadata** |
| Reconstruction relevance | **Moderate** |

**Contents:**

`readme - WTC1_djvu.txt` — Readme/documentation for the structural database. Likely describes the database schema or contents.

**Reconstruction value:** Metadata and documentation for the structural database. May describe column/beam designations, material specifications, or database organization.

---

### 7. TT Structural Archived Index

| Field | Value |
|---|---|
| Source filename | `TTStructuralArchivedIndexToBooksApr20195_201906.zip` |
| Size | 36KB |
| File count | 1 XML metadata file |
| Category | **Index / Finding Aid** |
| Reconstruction relevance | **Low (finding aid)** |

**Contents:**

`TTStructuralArchivedIndexToBooksApr20195_201906_meta.xml` — Internet Archive metadata XML for the structural drawing book index.

**Reconstruction value:** Finding aid only. Describes the archived collection. No structural data.

---

### 8. Standalone DJVU Text Files (Top-Level)

| File | Size | Category |
|---|---|---|
| `WTCI-000013-L_djvu.txt` | 313KB | Structural (Drawing Book 3 index) |
| `WTCI-000043-L_djvu.txt` | 31KB | Structural |
| `WTCI-000158-STB_djvu.txt` | 224KB | Structural Drawing Book |
| `WTCI-000163-STB_djvu.txt` | 63KB | Structural Drawing Book |
| `WTCI-000228-STB_djvu.txt` | 88KB | Structural Drawing Book |
| `WTCI-000335-STB_djvu.txt` | 252KB | Structural Drawing Book |
| `WTCI-000354-STB_djvu.txt` | 72KB | Structural Drawing Book |
| `WTCI-000214-P jfk incident logs on 911_djvu.txt` | 12KB | Historical Document |

These are standalone OCR text files not inside any ZIP archive. Six are structural drawing books (-STB suffix). One (WTCI-000214-P) is JFK airport incident logs from 9/11 — a historical document, not reconstruction-critical.

**OCR Quality:** Fair to Poor (same DJVU limitations as other structural files).

---

### 9. Empty Category Directories

| Directory | Intended Content |
|---|---|
| `architecture-history/` | Architectural history documents |
| `construction-photos/` | Construction photographs |
| `engineering-reports/` | Engineering reports |
| `floor-plans/` | Floor plans |
| `interior-photos/` | Interior photographs |
| `site-plans/` | Site plans |
| `structural-drawings/` | Structural drawings |

These are empty organizational placeholders. The actual content exists in the ZIP archives at the top level.

---

## OCR Quality Summary

| Quality Rating | Files | Description |
|---|---|---|
| **Good** | ~2 (WTC7 spec HOCR, index pages) | Clean, readable text with minimal artifacts |
| **Fair** | ~250+ (corpus DJVU files) | Partially legible; dates, numbers, codes reliable; narrative text degraded |
| **Poor** | ~700+ (drawing body text) | Heavy OCR artifacts; structural terminology intermittently recognizable; requires AI-assisted interpretation |

**Note:** The AA20a1 collection (895 PNGs) has no embedded OCR — these are raw structural sheet scans requiring fresh OCR processing.

---

## Duplicate Detection

| Duplicate Set | Files |
|---|---|
| WTCI000016L | `WTCI000016L.zip` and `WTCI000016L (1).zip` — identical contents (Drawing Book 5) |
| WTCI000131L002 | `WTCI000131L002.zip` and `WTCI000131L002 (1).zip` — identical contents (Drawing Book 7) |
| Drawing Book 19 | Extracted from `WTCI000038L.zip` and `wtci-000038-l.zip` — same WTCI-000038-L and WTCI-000039-L files |

3 duplicate ZIP pairs identified. De-duplication should be addressed during ingestion.

---

## Summary by Category

| Category | Files | Size | Reconstruction Value |
|---|---|---|---|
| Structural Drawings (images) | 895 PNGs | 401MB | Critical |
| Structural Drawing Book OCR | ~60 TXT | ~8MB | High |
| Comprehensive Document Corpus | 250+ TXT | 35MB | Critical |
| Engineering Specifications | 2 TXT | ~1MB | High |
| Exterior Wall Data | 1 XLS | 1.5MB | Critical |
| Structural Database Docs | 1 TXT | 9KB | Moderate |
| Finding Aids/Indexes | 1 XML | 36KB | Low |
| Historical Documents | 1 TXT | 12KB | Low |
| **TOTAL** | **~1,640** | **~454MB** | — |