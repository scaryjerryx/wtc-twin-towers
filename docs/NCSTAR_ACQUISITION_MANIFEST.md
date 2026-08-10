# NCSTAR Acquisition Manifest

## Date

August 10, 2026

## Status

4 of 5 files downloaded successfully (197.9MB total). 1 file still downloading.

---

## NCSTAR 1-1: Design, Construction, and Maintenance of Structural and Life Safety Systems

### Main Report

| Field | Value |
|---|---|
| **Title** | Design and Construction of Structural Systems |
| **Internet Archive ID** | `NIST_WTC_Investigation_Reports-101000` |
| **Direct download URL** | `https://archive.org/download/NIST_WTC_Investigation_Reports-101000/NIST_WTC_Investigation_Reports-101000.pdf` |
| **File size** | 9.7MB |
| **Download status** | ✅ Downloaded |
| **Local path** | `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-1_Design_Construction.pdf` |
| **Expected evidence categories** | Floor plans, site plans, tower architectural layouts, exterior wall schedules, foundation layouts, construction chronology |
| **Reconstruction value** | **Critical** — Addresses CG-2, CG-3, CG-4, IG-6 |

### Appendix A-B

| Field | Value |
|---|---|
| **Title** | Design and Construction of Structural Systems (Appendixes A-B) |
| **Internet Archive ID** | `NIST_WTC_Investigation_Reports-909013` |
| **Direct download URL** | `https://archive.org/download/NIST_WTC_Investigation_Reports-909013/NIST_WTC_Investigation_Reports-909013.pdf` |
| **File size** | 13.4MB |
| **Download status** | ✅ Downloaded |
| **Local path** | `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-1_Appendix_A-B.pdf` |
| **Expected evidence categories** | Structural drawings, design criteria, construction history |

### Appendix C-G

| Field | Value |
|---|---|
| **Title** | Design and Construction of Structural Systems (Appendices C-G) |
| **Internet Archive ID** | `NIST_WTC_Investigation_Reports-101334` |
| **Direct download URL** | `https://archive.org/download/NIST_WTC_Investigation_Reports-101334/NIST_WTC_Investigation_Reports-101334.pdf` |
| **File size** | TBD (download in progress) |
| **Download status** | ⏳ Downloading |
| **Local path** | `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-1_Appendix_C-G.pdf` |
| **Expected evidence categories** | Detailed structural drawings, floor plans, connection details |

---

## NCSTAR 1-2: Baseline Structural Performance and Aircraft Impact Damage Analysis

### Main Report

| Field | Value |
|---|---|
| **Title** | Baseline Structural Performance and Aircraft Impact Damage Analysis of the World Trade Center Towers |
| **Internet Archive ID** | `NIST_WTC_Investigation_Reports-101012` |
| **Direct download URL** | `https://archive.org/download/NIST_WTC_Investigation_Reports-101012/NIST_WTC_Investigation_Reports-101012.pdf` |
| **File size** | 60.2MB |
| **Download status** | ✅ Downloaded |
| **Local path** | `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-2_Baseline_Structural.pdf` |
| **Expected evidence categories** | Tower structural layouts, column schedules, beam schedules, floor framing plans, connection details, structural models for both towers |
| **Reconstruction value** | **Critical** — Addresses CG-1 (Tower B — partial), CG-4 |

---

## NCSTAR 1-8: Visual Evidence, Damage Estimates, and Timeline Analysis

### Main Report (Chapters 1-8)

| Field | Value |
|---|---|
| **Title** | Visual Evidence, Damage Estimates, and Timeline Analysis (Chapters 1-8) |
| **Internet Archive ID** | `NIST_WTC_Investigation_Reports-101356` |
| **Direct download URL** | `https://archive.org/download/NIST_WTC_Investigation_Reports-101356/NIST_WTC_Investigation_Reports-101356.pdf` |
| **File size** | 114.6MB |
| **Download status** | ✅ Downloaded |
| **Local path** | `WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-8_Visual_Evidence_Ch1-8.pdf` |
| **Expected evidence categories** | Construction chronology, visual evidence, exterior photographs, interior photographs, timeline of events |
| **Reconstruction value** | **Critical** — Addresses IG-1, IG-2, IG-5 (partial) |

### Additional Volumes (Manual Download Required)

| Item ID | Title | URL |
|---|---|---|
| `NIST_WTC_Investigation_Reports-101030` | Visual Evidence (Chapters 9-Appendix C) | `https://archive.org/details/NIST_WTC_Investigation_Reports-101030` |
| `NIST_WTC_Investigation_Reports-101358` | Visual Evidence (Appendices D-G) | `https://archive.org/details/NIST_WTC_Investigation_Reports-101358` |
| `NIST_WTC_Investigation_Reports-101359` | Visual Evidence (Appendices H-M) | `https://archive.org/details/NIST_WTC_Investigation_Reports-101359` |

---

## Download Summary

| Report | Files Downloaded | Total Size | Status |
|---|---|---|---|
| NCSTAR 1-1 (main + appendix A-B) | 2 | 23.1MB | ✅ Complete |
| NCSTAR 1-1 (appendix C-G) | 0 | TBD | ⏳ Downloading |
| NCSTAR 1-2 (main) | 1 | 60.2MB | ✅ Complete |
| NCSTAR 1-8 (Ch 1-8) | 1 | 114.6MB | ✅ Complete |
| **Total** | **4** | **197.9MB** | **4 of 5 complete** |

---

## Manual Download Commands

```bash
# NCSTAR 1-1 Appendix C-G
curl -L -o WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-1_Appendix_C-G.pdf \
  "https://archive.org/download/NIST_WTC_Investigation_Reports-101334/NIST_WTC_Investigation_Reports-101334.pdf"

# NCSTAR 1-8 remaining volumes
curl -L -o WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-8_Ch9-AppC.pdf \
  "https://archive.org/download/NIST_WTC_Investigation_Reports-101030/NIST_WTC_Investigation_Reports-101030.pdf"

curl -L -o WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-8_Appendix_D-G.pdf \
  "https://archive.org/download/NIST_WTC_Investigation_Reports-101358/NIST_WTC_Investigation_Reports-101358.pdf"

curl -L -o WTC_CORPUS/engineering-reports/ncstar/NCSTAR_1-8_Appendix_H-M.pdf \
  "https://archive.org/download/NIST_WTC_Investigation_Reports-101359/NIST_WTC_Investigation_Reports-101359.pdf"
```

---

## Expected Readiness Improvement

| Area | Current | After These 3 NCSTAR Reports | Increase |
|---|---|---|---|
| Site | 0% | 40% | +40% |
| Plaza | 0% | 25% | +25% |
| Tower A | 8% | 35% | +27% |
| Tower B | 1% | 25% | +24% |
| Concourse | 0% | 25% | +25% |
| WTC 7 | 25% | 30% | +5% |
| Observation Deck | 0% | 15% | +15% |
| Windows on the World | 0% | 15% | +15% |
| **Overall** | **~8%** | **~30%** | **+22%** |
