# WTC Corpus Reconstruction Assessment

## Assessment Date

August 10, 2026

## Assessor

AI-assisted analysis based on full corpus extraction and sampling.

---

## A. What Evidence Categories Are Present?

| Category | Present? | Volume | Quality |
|---|---|---|---|
| Structural Drawing Books | ✅ Yes | Books 2-8, 10-13, 18-20 (14 books) | Fair OCR text; index pages legible |
| Structural Engineering Sheets | ✅ Yes | 895 PNG images (Tower A) | High-resolution scans; no OCR |
| Exterior Wall Schedules | ✅ Yes | 1 Excel spreadsheet (Tower A, floors 1-9) | Structured data; excellent |
| Engineering Specifications | ✅ Yes | WTC7 OEM spec manual (16 divisions) | Good OCR (HOCR variant) |
| Construction Photographs | ❌ No | Empty directory only | — |
| Interior Photographs | ❌ No | Empty directory only | — |
| Floor Plans | ❌ No | Empty directory only | — |
| Site Plans | ❌ No | Empty directory only | — |
| Architectural History | ❌ No | Empty directory only | — |
| Engineering Reports | ❌ No | Empty directory only | — |
| Historical Documents | ✅ Yes | 1 file (JFK 9/11 incident logs) | Fair OCR |
| Structural Database Docs | ✅ Yes | 1 readme file | Fair OCR |
| Finding Aids | ✅ Yes | 1 XML metadata file | N/A |

**Present:** Structural drawings, structural OCR text, exterior wall data, specifications, and metadata.

**Missing:** Photographs (construction or interior), floor plans, site plans, architectural history documents, and engineering reports.

---

## B. What Reconstruction-Critical Evidence Exists?

### Tier 1 — Directly Usable for 3D Reconstruction

| Evidence | Reconstruction Use |
|---|---|
| **AA20a1 Tower A Structural Sheets** (895 PNGs) | Column locations, beam sizes, connection details, floor framing plans. These are the actual structural engineering drawings for the North Tower. |
| **Exterior Wall Schedules** (XLS) | Precise exterior wall panel types, dimensions, and locations for Tower A floors 1-9. Can be programmatically parsed for automated wall generation. |
| **Drawing Book Index Pages** | Sheet inventories with dates, revision codes, and drawing numbers. Provides the roadmap for what structural information exists. |

### Tier 2 — Supports Reconstruction Understanding

| Evidence | Reconstruction Use |
|---|---|
| **Drawing Book OCR Text** (~60 files) | Structural terminology, column type designations (1000-8000), spandrel types (C, D), strut types (D, E, F, H), section references (A-A, B-B, C-C), exterior wall elevations. |
| **WTC7 OEM Specification Manual** | Material types, construction standards, division-level specifications for WTC7. References complex-wide systems. |
| **Comprehensive Corpus** (250+ files) | Broad document coverage including structural reports, project documentation, and correspondence. |

### Tier 3 — Contextual

| Evidence | Reconstruction Use |
|---|---|
| **Structural Database Readme** | May describe database schema for structural elements. |
| **JFK 9/11 Incident Logs** | Historical context only; not reconstruction-relevant. |

---

## C. What Evidence Appears Missing?

### Critical Gaps

1. **Floor Plans** — No architectural floor plans for any WTC building. The structural sheets show framing but not architectural layouts (walls, rooms, corridors, elevators, stairs).

2. **Construction Photographs** — No photographic evidence of the construction process. These would provide visual confirmation of structural systems, material types, and construction sequencing.

3. **Interior Photographs** — No photographs of completed interiors. Critical for understanding spatial layout, finishes, and furnishings.

4. **Site Plans** — No site-level plans showing the relationship between buildings, the plaza, and surrounding infrastructure.

5. **Tower B (South Tower) Structural Sheets** — The AA20a1 collection is Tower A only. No equivalent structural sheet collection for the South Tower.

6. **WTC 3 (Marriott Hotel), WTC 4, WTC 5, WTC 6** — No structural or architectural evidence for the supporting buildings.

7. **Mechanical/Electrical/Plumbing Drawings** — No MEP documentation for any building.

8. **Architectural Drawings** — No architectural elevations, sections, or detail drawings.

9. **Engineering Reports** — No structural analysis reports, wind tunnel studies, or foundation engineering documents.

10. **Change Orders and As-Built Documentation** — No records of design changes during construction or as-built verification.

### Partial Gaps

11. **Drawing Books 1, 9, 14-17, 21+** — The drawing book collection covers Books 2-8, 10-13, and 18-20. Books 1, 9, 14, 15, 16, 17, and any books beyond 20 are not present.

12. **Tower A Exterior Wall Above Floor 9** — The exterior wall schedule only covers floors 1-9. Upper floor exterior wall data is not present.

---

## D. Is This Corpus Sufficient for Spatial Modelling?

### Site → Building → Tower → Floor → Zone → Space Hierarchy

| Level | Sufficient? | Assessment |
|---|---|---|
| **Site** | ❌ No | No site plans, no plaza documentation, no relationship diagrams between buildings |
| **Building** | ⚠️ Partial | Tower A structural system is well-documented. Tower B, WTC 3-7 are not. |
| **Tower** | ⚠️ Partial | Tower A structural framing is documented. Architectural envelope (exterior wall) is partially documented (floors 1-9). |
| **Floor** | ❌ No | No floor plans exist. Structural framing plans exist but do not show architectural layouts. |
| **Zone** | ❌ No | No zone-level documentation (core areas, tenant spaces, mechanical zones). |
| **Space** | ❌ No | No individual space documentation (rooms, corridors, lobbies). |

**Verdict:** The corpus provides a strong structural foundation for Tower A but is insufficient for full spatial modelling of the WTC complex. The structural system can be modelled, but architectural spaces cannot.

---

## E. Is This Corpus a Viable Foundation for Year-by-Year State Generation?

### 1966 → 2001 Timeline States

| Assessment | Detail |
|---|---|
| **Structural system** | ✅ Viable — The structural drawings document the as-designed structural system. Revision dates on drawing book index pages (e.g., 5/1/67, 9/30/69) provide temporal anchors. |
| **Construction sequencing** | ❌ Not viable — No construction photographs or schedules to determine what was built when. |
| **Architectural changes** | ❌ Not viable — No documentation of tenant changes, renovations, or modifications over time. |
| **Operational history** | ❌ Not viable — No operational records, event documentation, or change logs. |
| **1993 bombing effects** | ❌ Not viable — No documentation of damage or repairs. |
| **Pre-9/11 state** | ❌ Not viable — No documentation of the complex's final configuration. |

**Verdict:** The corpus can support a single "design intent" structural model of Tower A with some temporal markers (revision dates). It cannot support year-by-year state generation. The timeline would need to be populated from additional evidence sources.

---

## F. What Should Be Ingested First?

### Priority 1 — Immediate Ingestion

| Item | Rationale |
|---|---|
| **AA20a1 Structural Sheets** (895 PNGs) | Largest single evidence collection. Foundation for Tower A structural model. Requires OCR processing. |
| **Exterior Wall Schedules** (XLS) | Structured data. Directly usable for 3D wall generation. Can be parsed programmatically. |
| **WTC7 OEM Specification Manual** (HOCR variant) | Best OCR quality in the corpus. Provides material and construction standards. |

### Priority 2 — Second Wave

| Item | Rationale |
|---|---|
| **Comprehensive Corpus** (250+ DJVU files) | Broad document coverage. Requires deduplication against Drawing Book files. |
| **Drawing Book Index Pages** | Provides the document inventory and revision history. |

### Priority 3 — Defer

| Item | Rationale |
|---|---|
| **Drawing Book Body Text** (poor OCR) | Low-quality OCR. May benefit from AI-assisted re-extraction before ingestion. |
| **Duplicate ZIPs** | Deduplicate before ingestion. |
| **JFK 9/11 Incident Logs** | Not reconstruction-relevant. Historical context only. |

---

## G. What Should Not Be Ingested Yet?

| Item | Reason |
|---|---|
| **Duplicate ZIP archives** | WTCI000016L (1).zip, WTCI000131L002 (1).zip, and wtci-000038-l.zip are duplicates. Ingesting them would create redundant asset records. |
| **Empty category directories** | No content to ingest. |
| **Finding aid XML** | Metadata only; no evidence content. |
| **Poor-quality DJVU body text** | The heavily degraded OCR text from drawing bodies may produce more noise than signal. Consider AI-assisted re-OCR of the original scans before ingesting these. |
| **JFK 9/11 incident logs** | Not WTC reconstruction evidence. |

---

## Overall Assessment

### Strengths

- **Tower A structural system is well-documented** — 895 structural sheets plus exterior wall schedules provide a solid engineering foundation
- **Drawing book index pages provide document inventory** — We know what sheets exist across 14 drawing books
- **Structured data exists** — The exterior wall spreadsheet is directly machine-readable
- **WTC7 specifications are complete** — Full 16-division spec manual with good OCR quality
- **Corpus is compact and manageable** — 454MB total, 1,640 files

### Weaknesses

- **Tower A only** — No equivalent structural documentation for Tower B or buildings 3-7
- **No architectural evidence** — No floor plans, elevations, or interior documentation
- **No photographic evidence** — No construction or interior photographs
- **OCR quality is poor for most files** — DJVU-OCR on engineering drawings produces heavily degraded text
- **No temporal evidence** — Cannot support year-by-year state generation
- **Significant gaps in drawing book coverage** — Books 1, 9, 14-17, 21+ are missing

### Recommendation

This corpus is a **viable starting point for Tower A structural reconstruction** but is insufficient as a standalone foundation for the full WTC complex reconstruction. The project should:

1. Ingest the high-value items (structural sheets, wall schedules, specifications)
2. Pursue additional evidence sources for:
   - Tower B structural drawings
   - Architectural floor plans (all buildings)
   - Construction and interior photographs
   - Site plans and plaza documentation
   - Buildings 3-7 documentation
3. Consider AI-assisted re-OCR of the AA20a1 structural sheets for better text extraction
4. Treat the DJVU-OCR text as a finding aid rather than authoritative extracted knowledge