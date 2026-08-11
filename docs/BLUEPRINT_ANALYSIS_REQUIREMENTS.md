# Blueprint Analysis Requirements

## Date: August 10, 2026

## Purpose

This document analyzes all failed visual inspection attempts, identifies technical gaps, and defines the minimum requirements for operational blueprint analysis capability.

---

## 1. Failed Visual Inspection Attempts

### 1.1 TIFF Files (WTCI-000262-L)

**Attempt:** Visual inspection of 30 sample pages from WTCI-000262-L structural drawing book

**Failure Points:**
- ImageMagick `convert` command not available on server
- PIL/Pillow Python module not installed
- PNG files exceeded 7500px dimension limit for direct viewing
- OCR timed out on large TIFF files (>20 seconds per file)

**Root Cause:** Missing image processing toolchain

**Impact:** Could not determine tower designation (Tower A vs Tower B) for 1,364-page collection

### 1.2 PPM Files (NCSTAR 1-8 Visual Corpus)

**Attempt:** Visual inspection of 560 PPM files extracted from NCSTAR 1-8

**Failure Points:**
- PPM (Portable Pixmap) format not directly viewable
- ImageMagick `convert` not available for format conversion
- OCR timed out on large files (~5MB each)
- No batch conversion capability

**Root Cause:** Missing image format conversion tools

**Impact:** Could not categorize 657 images by content type (construction photos, floor plans, diagrams, etc.)

### 1.3 Image-Based PDFs (NCSTAR 1-1 Appendix C-G)

**Attempt:** Extract floor plan figures from 44MB image-based PDF

**Failure Points:**
- `pdfimages` produced no output (PDF uses embedded images, not vector graphics)
- `pdftoppm` not successfully executed
- PDF is scanned pages, not searchable text
- No page-by-page extraction capability

**Root Cause:** Missing PDF image extraction tools

**Impact:** Could not extract potential floor plans and structural diagrams embedded in NCSTAR 1-1

### 1.4 Summary of Failures

| Format | Count | Size | Failure Reason | Blocking Issue |
|---|---|---|---|---|
| TIFF | 1,364 | ~350MB | No image processing tools | Missing PIL/Pillow, ImageMagick |
| PPM | 560 | ~2.9GB | Format not viewable | Missing ImageMagick |
| PDF (image-based) | 1 | 44MB | No image extraction | Missing poppler-utils |
| PNG (large) | 30 | ~150MB | Exceeds view limit | No resize capability |

**Total blocked content:** ~2,000+ images, ~3.4GB

---

## 2. Required Libraries and Tooling

### 2.1 Image Processing

**Required:**
- **PIL/Pillow** (Python Imaging Library)
  - Format conversion (TIFF → PNG, PPM → PNG)
  - Image resizing
  - Metadata extraction
  - Batch processing
  
- **ImageMagick**
  - Command-line image conversion
  - Format support (TIFF, PPM, PNG, JPG, PDF)
  - Batch operations
  - Quality adjustment

**Installation:**
```bash
apt install imagemagick
pip install Pillow
```

### 2.2 PDF Processing

**Required:**
- **poppler-utils**
  - `pdftoppm`: Convert PDF pages to images
  - `pdfimages`: Extract embedded images from PDFs
  - `pdftotext`: Extract text from text-based PDFs
  
- **PyMuPDF (fitz)**
  - Python PDF processing
  - Page-by-page image extraction
  - Metadata extraction
  - Text and image separation

**Installation:**
```bash
apt install poppler-utils
pip install PyMuPDF
```

### 2.3 OCR and Text Extraction

**Current:**
- Tesseract OCR (installed, but slow on large files)

**Required Improvements:**
- GPU acceleration for Tesseract
- Batch processing capability
- Timeout handling for large files
- Pre-processing pipeline (deskew, denoise, contrast enhancement)

**Optional:**
- **EasyOCR** (GPU-accelerated, multi-language)
- **PaddleOCR** (high accuracy on technical drawings)

### 2.4 Blueprint-Specific Tools

**Required:**
- **OpenCV** (computer vision)
  - Line detection
  - Shape recognition
  - Title block detection
  - Scale bar detection
  
- **Custom blueprint parser**
  - Title block extraction
  - Drawing number parsing
  - Revision history extraction
  - Scale interpretation

**Installation:**
```bash
pip install opencv-python
```

---

## 3. Required Model Capabilities

### 3.1 Current Capability: DeepSeek V4 Flash

**Type:** Text-only LLM

**Capabilities:**
- Text analysis
- OCR post-processing
- Metadata interpretation
- Knowledge extraction

**Limitations:**
- Cannot process images
- Cannot interpret visual content
- Cannot identify drawing types
- Cannot extract title blocks

**Verdict:** **Insufficient for blueprint analysis**

### 3.2 Required Capability: Multimodal Vision-Language Model

**Type:** Multimodal LLM with vision capabilities

**Required Capabilities:**
- Image understanding
- Title block extraction
- Drawing type classification
- Tower identification from visual cues
- Floor identification from annotations
- Structural system recognition
- Floor plan interpretation

**Candidate Models:**

| Model | Provider | Vision Capability | Cost | Notes |
|---|---|---|---|---|
| GPT-4V | OpenAI | ✅ High | $0.01-0.03/image | Best accuracy, expensive |
| Claude 3 Sonnet | Anthropic | ✅ High | $0.003-0.015/image | Good balance |
| Gemini Pro Vision | Google | ✅ High | $0.00025-0.001/image | Cost-effective |
| LLaVA | Open source | ✅ Medium | Free (self-hosted) | Requires GPU |
| Qwen-VL | Open source | ✅ Medium | Free (self-hosted) | Requires GPU |

**Recommendation:** **Claude 3 Sonnet or Gemini Pro Vision** for cost-effectiveness and accuracy

### 3.3 Multimodal Model Impact Assessment

| Task | Text-Only (Current) | Multimodal (Required) | Improvement |
|---|---|---|---|
| Title block extraction | ❌ Impossible | ✅ High accuracy | +100% |
| Tower identification | ⚠️ OCR-only, unreliable | ✅ Visual + text | +80% |
| Floor identification | ⚠️ OCR-only, unreliable | ✅ Visual + text | +80% |
| Structural system ID | ❌ Impossible | ✅ High accuracy | +100% |
| Floor plan discovery | ❌ Impossible | ✅ High accuracy | +100% |
| Drawing type classification | ❌ Impossible | ✅ High accuracy | +100% |

**Verdict:** **Multimodal model would materially improve all blueprint analysis tasks**

---

## 4. Blueprint Analysis Pipeline v1

### 4.1 Input Formats

```
Input:
  - TIFF (scanned drawings, high resolution)
  - PDF (image-based or text-based)
  - PNG (converted images)
  - PPM (Netpbm format, requires conversion)
```

### 4.2 Processing Stages

```
Stage 1: Format Normalization
  Input:  TIFF/PDF/PNG/PPM
  Output: PNG (resized to 2000px max dimension)
  Tools:  PIL/Pillow, ImageMagick, poppler-utils

Stage 2: Pre-Processing
  Input:  PNG
  Output: Enhanced PNG (deskewed, denoised, contrast-adjusted)
  Tools:  OpenCV, PIL/Pillow

Stage 3: OCR Extraction
  Input:  Enhanced PNG
  Output: Text layer (title block, annotations, notes)
  Tools:  Tesseract, EasyOCR, or PaddleOCR

Stage 4: Visual Analysis (Multimodal AI)
  Input:  Enhanced PNG + OCR text
  Output: Structured metadata
  Tools:  Claude 3 Sonnet or Gemini Pro Vision
  Model:  Multimodal LLM with vision

Stage 5: Metadata Extraction
  Input:  AI analysis output
  Output: Structured data (JSON)
  Fields:
    - Tower (A/B/Both/Unknown)
    - Floor (number or range)
    - Structural System (truss/column/wall/core/etc.)
    - Drawing Type (framing plan/elevation/section/detail/schedule)
    - Confidence (0.0-1.0)
    - Drawing Number
    - Revision
    - Scale
```

### 4.3 Output Schema

```json
{
  "file": "WTCI-000262-L/0001/0001.tif",
  "tower": "A",
  "floor": "1-10",
  "structural_system": "floor_truss",
  "drawing_type": "framing_plan",
  "confidence": 0.85,
  "drawing_number": "S-101",
  "revision": "C",
  "scale": "1/8\" = 1'-0\"",
  "title_block": {
    "project": "World Trade Center Tower A",
    "drawing_title": "Floor Framing Plan",
    "drawn_by": "LERA",
    "date": "1968-03-15"
  },
  "annotations": [
    "FLOOR TRUSSES TYPICAL",
    "EXT. COL. REF. LINE"
  ],
  "ai_model": "claude-3-sonnet",
  "processing_date": "2026-08-10"
}
```

---

## 5. Current DeepSeek Workflow Assessment

### 5.1 Current Workflow

```
Input: Text (OCR output, metadata)
  ↓
DeepSeek V4 Flash (text-only LLM)
  ↓
Output: Text analysis, knowledge extraction
```

### 5.2 Limitations

- **Cannot process images** — DeepSeek V4 Flash is text-only
- **Cannot interpret visual content** — No vision capability
- **Cannot identify drawing types** — Requires visual understanding
- **Cannot extract title blocks** — Requires image analysis
- **Cannot classify structural systems** — Requires visual recognition

### 5.3 Verdict

**Current DeepSeek workflow is INSUFFICIENT for blueprint analysis.**

**Reason:** Blueprint analysis requires visual understanding, not just text processing. The current model cannot:
- See the drawing
- Identify visual patterns
- Interpret graphical content
- Extract visual metadata

**Required:** Multimodal model with vision capabilities

---

## 6. Minimum Technical Stack

### 6.1 Hardware Requirements

**Minimum:**
- CPU: 4+ cores
- RAM: 16GB+
- Storage: 100GB+ free space
- GPU: Optional (for accelerated OCR/AI)

**Recommended:**
- CPU: 8+ cores
- RAM: 32GB+
- Storage: 500GB+ SSD
- GPU: NVIDIA RTX 3060+ (for local AI models)

### 6.2 Software Stack

**Core:**
```
Python 3.10+
├── PIL/Pillow (image processing)
├── OpenCV (computer vision)
├── PyMuPDF (PDF processing)
├── Tesseract (OCR)
└── Multimodal AI client (Claude/Gemini API)
```

**System:**
```
ImageMagick (format conversion)
poppler-utils (PDF tools)
Tesseract OCR (text extraction)
```

### 6.3 API Keys

**Required:**
- OpenRouter API key (for Claude 3 Sonnet or Gemini Pro Vision)
- OR direct API key for Anthropic/Google

**Cost Estimate:**
- Claude 3 Sonnet: ~$0.01/image
- Gemini Pro Vision: ~$0.001/image
- For 2,000 images: $2-$20 total

### 6.4 Processing Targets

| Collection | Format | Count | Size | Priority |
|---|---|---|---|---|
| WTCI-000262-L | TIFF | 1,364 | 350MB | **Critical** |
| NCSTAR 1-8 | PPM | 560 | 2.9GB | High |
| NCSTAR 1-1 App C-G | PDF | 1 | 44MB | High |
| WTCI drawing books | ZIP/DJVU | 14+ | ~500MB | Medium |
| Gerrycan collections | ZIP | 4 | 546MB | Medium |
| SkyscraperForum | ZIP | 1 | 1.4GB | Medium |

**Total:** ~2,000+ images, ~5.7GB

---

## 7. Readiness Gain Estimates

### 7.1 If Blueprint Analysis Becomes Operational

**Immediate Gains (Week 1):**

| Collection | Current Status | After Analysis | Readiness Gain |
|---|---|---|---|
| WTCI-000262-L | Unknown tower | Tower A or B confirmed | +0.5-3% |
| NCSTAR 1-8 images | Uncategorized | Categorized by type | +1-2% |
| NCSTAR 1-1 App C-G | Not extracted | Floor plans extracted | +2-3% |
| WTCI drawing books | Partially processed | Fully analyzed | +1-2% |

**Total Week 1 Gain:** +4.5-10%

**Medium-Term Gains (Month 1):**

| Collection | Analysis | Readiness Gain |
|---|---|---|
| All WTCI books | Complete analysis | +3-5% |
| Gerrycan collections | Structural data extracted | +2-3% |
| SkyscraperForum | Drawing books analyzed | +1-2% |
| Floor plan discovery | Architectural plans found | +5-10% |

**Total Month 1 Gain:** +11-20%

### 7.2 Gap Closure Potential

| Gap | Current Status | After Blueprint Analysis | Closure |
|---|---|---|---|
| CG-1 (Tower B structural) | Partially addressed | **Fully closed** if Tower B sheets found | ✅ |
| CG-2 (Architectural floor plans) | Open | **Partially closed** if floor plans discovered | ⚠️ |
| CG-3 (Site plans) | Open | **Partially closed** if site plans found | ⚠️ |
| CG-4 (Tower A upper wall) | Closed | Remains closed | ✅ |
| IG-1 (Construction photos) | Partial | **Improved** with categorized photos | ⚠️ |

### 7.3 Reconstruction Capability

**Current (50% readiness):**
- Tower A structural skeleton (high confidence)
- Tower B exterior wall (medium-high confidence)
- Construction timeline (high confidence)

**After Blueprint Analysis (60-70% readiness):**
- Tower A + B structural skeletons (high confidence)
- Floor-by-floor framing plans (high confidence)
- Exterior column schedules (high confidence)
- Potential architectural floor plans (medium confidence)
- Categorized visual reference library (high confidence)

**Enables:**
- Prototype 0.1 (structural + spatial model)
- Floor-level reconstruction
- Structural system visualization
- Construction sequence modeling

---

## 8. Implementation Roadmap

### Phase 1: Tool Installation (Day 1)

```bash
# System packages
apt update
apt install imagemagick poppler-utils tesseract-ocr

# Python packages
pip install Pillow opencv-python PyMuPDF pytesseract
pip install easyocr  # Optional: GPU-accelerated OCR
```

**Time:** 1 hour
**Cost:** $0

### Phase 2: Format Conversion (Day 1-2)

**Tasks:**
- Convert 1,364 TIFF files to PNG (WTCI-000262-L)
- Convert 560 PPM files to PNG (NCSTAR 1-8)
- Extract images from NCSTAR 1-1 App C-G PDF
- Resize all images to 2000px max dimension

**Time:** 4-8 hours
**Cost:** $0

### Phase 3: Multimodal AI Integration (Day 2-3)

**Tasks:**
- Set up OpenRouter API key
- Create blueprint analysis prompt template
- Test on 10 sample images
- Refine prompt for accuracy

**Time:** 4-8 hours
**Cost:** $0.10-1.00 (API costs)

### Phase 4: Batch Processing (Day 3-7)

**Tasks:**
- Process 2,000+ images through pipeline
- Extract metadata for each image
- Generate structured JSON output
- Validate results

**Time:** 20-40 hours
**Cost:** $2-20 (API costs)

### Phase 5: Integration (Day 7-14)

**Tasks:**
- Load metadata into database
- Update readiness calculations
- Generate analysis reports
- Document findings

**Time:** 10-20 hours
**Cost:** $0

**Total Implementation Time:** 2 weeks
**Total Cost:** $2-21 (API costs)

---

## 9. Recommendations

### 9.1 Immediate Actions

1. **Install image processing tools** (PIL/Pillow, ImageMagick, poppler-utils)
2. **Obtain multimodal AI API key** (Claude 3 Sonnet or Gemini Pro Vision)
3. **Convert WTCI-000262-L TIFF files to PNG** (highest priority)
4. **Analyze 10 sample pages** to confirm tower designation
5. **If Tower B confirmed:** Prioritize full collection analysis

### 9.2 Strategic Priorities

1. **WTCI-000262-L** — 1,364 pages, potential Tower B structural sheets
2. **NCSTAR 1-1 App C-G** — 44MB PDF, potential floor plans
3. **NCSTAR 1-8 images** — 560 PPM files, visual evidence categorization
4. **WTCI drawing books** — 14+ books, comprehensive structural documentation

### 9.3 Cost-Benefit Analysis

**Cost:**
- Implementation: 2 weeks
- API costs: $2-21
- Hardware: $0 (existing server sufficient)

**Benefit:**
- Readiness gain: +10-20%
- Gap closure: CG-1 (Tower B structural) potentially fully closed
- Capability: Enables Prototype 0.1

**ROI:** **Extremely high** — $2-21 investment for +10-20% readiness gain

---

## 10. Conclusion

**Current State:**
- Blueprint analysis is **blocked** by missing toolchain
- DeepSeek V4 Flash is **insufficient** (text-only, no vision)
- 2,000+ images (~5.7GB) cannot be analyzed

**Required:**
- Image processing tools (PIL/Pillow, ImageMagick, poppler-utils)
- Multimodal AI model (Claude 3 Sonnet or Gemini Pro Vision)
- Blueprint analysis pipeline (5-stage processing)

**Impact:**
- Readiness gain: +10-20%
- Gap closure: CG-1 potentially fully closed
- Capability: Enables Prototype 0.1

**Recommendation:** **Implement blueprint analysis pipeline immediately.** Cost is minimal ($2-21), time is short (2 weeks), and impact is transformative (+10-20% readiness).