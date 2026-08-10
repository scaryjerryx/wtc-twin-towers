# Phase 1 Execution Order

## Date: August 10, 2026

## Tasks Ordered by Readiness Gain per Hour

| Order | Task | Gain | Time | Gain/Hour | Automatable? |
|---|---|---|---|---|---|
| 1 | Wikimedia full-res SVGs | +5% | 30 min | **+10%/hr** | ✅ Yes |
| 2 | NCSTAR floor plan extraction | +5% | 2-4 hrs | **+1.7%/hr** | ✅ Yes |
| 3 | NCSTAR visual evidence extraction | +5% | 1-2 hrs | **+3.3%/hr** | ✅ Yes |
| 4 | LoC Gottscho-Schleisner photos | +10% | 2-4 hrs | **+3.3%/hr** | ⚠️ Partial |
| 5 | IA Tower B structural collections | +15% | 1 hr | **+15%/hr** | ❌ No |

## Recommended Execution Sequence

### Step 1: Wikimedia SVGs (30 min, automated)
```bash
# Download full-resolution SVGs
curl -L -o WTC_CORPUS/site-plans/WTC_Site_Plan_Comparison.svg \
  "https://upload.wikimedia.org/wikipedia/commons/7/7e/WTC_Building_Arrangement_and_Site_Plan_comparison.svg"
curl -L -o WTC_CORPUS/site-plans/WTC_Preliminary_Site_Plan.svg \
  "https://upload.wikimedia.org/wikipedia/commons/1/1a/WTC_Building_Arrangement_in_preliminary_site_plan.svg"
curl -L -o WTC_CORPUS/site-plans/WTC_Site_Plan_Overlay.png \
  "https://upload.wikimedia.org/wikipedia/commons/5/5a/WTC_Building_Arrangement_and_Site_Plan_Overlay.png"
```
**Gain: +5% | Time: 30 min | Status: Ready to execute**

### Step 2: NCSTAR Visual Evidence Extraction (1-2 hrs, automated)
```bash
# Extract images from NCSTAR 1-8 PDFs
mkdir -p WTC_CORPUS/construction-photos/ncstar
cd WTC_CORPUS/engineering-reports/ncstar/critical
for f in NCSTAR_1-8_*.pdf; do
  pdfimages -j "$f" "../../../construction-photos/ncstar/$(basename $f .pdf)_"
done
```
**Gain: +5% | Time: 1-2 hrs | Status: Ready to execute**

### Step 3: NCSTAR Floor Plan Extraction (2-4 hrs, automated)
```bash
# Extract images from NCSTAR 1-1 Appendix C-G
mkdir -p WTC_CORPUS/floor-plans/ncstar
cd WTC_CORPUS/engineering-reports/ncstar
pdfimages -j "NCSTAR_1-1_Appendix_C-G.pdf" "../../floor-plans/ncstar/NCSTAR_1-1_AppC-G_"
```
**Gain: +5% | Time: 2-4 hrs | Status: Ready to execute**

### Step 4: LoC Gottscho-Schleisner Photos (2-4 hrs, partial automation)
```bash
# Search LoC API
curl -sL "https://www.loc.gov/pictures/collection/gsc/?q=World+Trade+Center&fo=json&c=500" | \
  python3 -c "import json,sys; d=json.load(sys.stdin); [print(i.get('image_url','')) for i in d.get('results',[])]" > /tmp/loc_urls.txt

# Download each photo
while read url; do
  [ -n "$url" ] && wget -q --timeout=30 -P WTC_CORPUS/construction-photos/loc/ "$url"
done < /tmp/loc_urls.txt
```
**Gain: +10% | Time: 2-4 hrs | Status: API search automatable, downloads automatable**

### Step 5: IA Tower B Structural Collections (1 hr, operator required)
```
OPERATOR ACTION REQUIRED:
1. Visit https://archive.org/details/AA20a1
2. Click the uploader's username
3. Browse all uploaded collections
4. Search for: "AA20", "Tower B", "WTC 2", "South Tower", "structural"
5. Download any Tower B structural ZIP files
6. Place in: WTC_CORPUS/structural-drawings/
```
**Gain: +15% | Time: 1 hr | Status: Operator must execute**

---

## Cumulative Readiness Progression

| Step | Task | Gain | Cumulative Readiness |
|---|---|---|---|
| Start | — | — | 35% |
| 1 | Wikimedia SVGs | +5% | 40% |
| 2 | NCSTAR visual evidence extraction | +5% | 45% |
| 3 | NCSTAR floor plan extraction | +5% | 50% |
| 4 | LoC Gottscho-Schleisner photos | +10% | 60% |
| 5 | IA Tower B structural collections | +15% | 75% |

---

## What Becomes Modelable After Phase 1

| Element | Evidence | Confidence |
|---|---|---|
| WTC 1 structural skeleton | AA20a1 + NCSTAR 1-1 | High |
| WTC 2 structural skeleton | IA Tower B sheets + NCSTAR 1-1/1-2 | High (if Tower B found) |
| Site footprint with building arrangement | Wikimedia SVGs + NCSTAR | High |
| Construction timeline 1966-1969 | NCSTAR 1-1 | High |
| Exterior wall system (WTC 1, floors 1-9) | XLS spreadsheet | High |
| Floor framing plans (both towers) | NCSTAR 1-1 App C-G images | Medium |
| Visual reference library | NCSTAR 1-8 + LoC photos | High |
| Plaza visual reference | LoC photos | Medium |
| Interior visual reference | NCSTAR 1-8 + LoC photos | Medium |
