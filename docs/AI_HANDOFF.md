# AI HANDOFF

## Project

WTC Knowledge Engine

Purpose:

Build an evidence-backed knowledge engine and digital twin for the World Trade Center archive.

The system ingests images, documents, engineering drawings and historical records and converts them into structured knowledge with provenance.

---

# Current Architecture

PDF
 ↓
OCR
 ↓
Text Extraction
 ↓
Entity Extraction
 ↓
Fact Extraction
 ↓
Fact Normalization
 ↓
Fact Cleaning
 ↓
Fact Deduplication
 ↓
Knowledge Graph
 ↓
Relationships
 ↓
Source Attribution
 ↓
Page Attribution

---

# Core Components

## OCR

File:

agents/processors/pdf_text_extractor.py

Capabilities:

- PyPDF2 text extraction
- OCR fallback using Tesseract
- pdf2image support
- scanned PDF support
- page-level extraction

Functions:

- extract_text()
- extract_pages()

Status:

✅ Working

---

## Entity Extraction

File:

agents/knowledge/knowledge_extractor.py

Capabilities:

- Extract known WTC entities
- Extract engineering entities
- Entity recognition from OCR text

Status:

✅ Working

---

## Fact Extraction

File:

agents/knowledge/knowledge_extractor.py

Capabilities:

Extract:

- Drawing Books
- Column Types
- Spandrel Types
- Strut Types
- Sections
- Years
- Exterior Wall references

Status:

✅ Working

---

## Fact Normalization

File:

agents/knowledge/fact_normalizer.py

Purpose:

Convert OCR variants into canonical facts.

Examples:

DRAWING BOOK 1

↓

Drawing Book 1

EXTERIOR WALL TO EL.363

↓

Exterior Wall To EL. 363

Status:

✅ Working

---

## Fact Cleaning

File:

agents/knowledge/fact_cleaner.py

Purpose:

Validate facts before insertion.

Current validations:

- Column Type whitelist
- Strut Type whitelist
- Spandrel Type whitelist
- Section validation
- Year filtering

Status:

✅ Working

---

## PDF Knowledge Pipeline

File:

agents/knowledge/pdf_knowledge_pipeline.py

Purpose:

Process engineering PDFs.

Pipeline:

PDF
 ↓
OCR
 ↓
Extract Facts
 ↓
Normalize Facts
 ↓
Clean Facts
 ↓
Store Facts
 ↓
Store Provenance

Status:

✅ Working

---

## Relationship Mining

File:

agents/knowledge/fact_relationship_builder.py

Purpose:

Create relationships from page-level co-occurrence.

Current relationships:

appears_in

associated_with

Examples:

Column Type 7000
 ↓
associated_with
 ↓
Exterior Wall To EL. 363

Status:

✅ Working

---

# Database

Database:

wtc_evidence

Current tables:

## entities

Stores entities.

Examples:

- World Trade Center
- North Tower
- South Tower
- Drawing Book 1
- Column Type 7000

---

## facts

Stores unique facts.

Important constraints:

unique_fact

Current fields:

- id
- entity_id
- fact_text
- confidence
- verification_status
- source_file
- source_page

Status:

✅ Working

---

## fact_sources

Stores fact provenance.

Purpose:

One fact can appear in many documents and many pages.

Fields:

- id
- fact_id
- source_file
- source_page
- confidence

Constraint:

unique_fact_source

Status:

✅ Working

---

## relationships

Stores graph relationships.

Fields:

- source_entity_id
- relationship_type
- target_entity_id
- confidence
- created_at

Constraint:

unique_relationship

Status:

✅ Working

---

# Provenance

Implemented:

✅ source_file

✅ source_page

✅ confidence

Example:

Fact:

Column Type 7000

Source:

WTCI-000721-L.PDF

Page:

22

Status:

✅ Working

---

# Current Proven Capabilities

The engine can:

✅ Read scanned engineering PDFs

✅ OCR historical drawings

✅ Extract structured facts

✅ Normalize OCR variations

✅ Deduplicate facts

✅ Track source document

✅ Track source page

✅ Build relationships automatically

✅ Store knowledge in PostgreSQL

✅ Maintain provenance

---

# Recently Completed

- Package migration
- OCR support
- Fact normalization
- Fact cleaning
- Fact deduplication
- Source file attribution
- Source page attribution
- fact_sources architecture
- Automatic relationship mining

---

# Current Priority

## 1

Relationship Confidence Scoring

Goal:

Relationships should accumulate evidence.

Example:

Column Type 7000

associated_with

Exterior Wall To EL. 363

evidence_count = 12

confidence = 95

---

## 2

Entity Resolution V2

Goal:

Merge aliases.

Examples:

WTC

World Trade Center

WORLD TRADE CENTER

↓

Single entity

---

## 3

Relationship Search

Goal:

Query graph and return relationships.

Example:

Search:

Column Type 7000

Returns:

Relationships

Sources

Pages

Documents

Confidence

---

## 4

Automated Ingestion

Goal:

Drop PDF into folder.

Engine automatically

## Automated Ingestion

File:

agents/ingestion/automated_ingestion.py

Status:

✅ Working

Purpose:

Processes all PDFs in:

data/incoming_pdfs/

Successful PDFs are moved to:

data/processed_pdfs/

Failed PDFs are moved to:

data/failed_pdfs/

After ingestion, the relationship builder runs automatically.

## Fact Verification v2

File:

agents/verification/fact_verifier.py

Status:

✅ Working

Purpose:

Uses fact_sources counts to update facts with:

- verification_status
- confidence

Rules:

0 sources = claim, confidence 50  
1 source = supported, confidence 70  
2 sources = well_supported, confidence 85  
3+ sources = verified, confidence 95

## Relationship Search v2

File:

agents/search/relationship_search.py

Status:

✅ Working

Purpose:

Searches graph relationships and displays:

- source entity
- relationship type
- target entity
- relationship confidence
- evidence count
- source method
- source fact confidence
- target fact confidence
- verification status
- source PDF files
- source pages
``

## Citation Loader

File:

agents/knowledge/citation_loader.py

Status:

✅ Working

Purpose:

Copies evidence records from fact_sources into citations.

The master engine runner now executes:

1. Automated PDF ingestion
2. Citation loader
3. Fact verification
4. Relationship building
5. Timeline build

