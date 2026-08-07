# WTC Knowledge Engine

## Completed

### OCR

- PyPDF2 extraction
- OCR fallback via Tesseract
- pdf2image support
- Scanned PDF support

### Knowledge

- Entity extraction
- Fact extraction
- Fact normalization
- Fact cleaning
- Fact deduplication

### Database

Tables:

- entities
- facts
- relationships
- fact_sources

Constraints:

- unique_fact
- unique_relationship
- unique_fact_source

### Provenance

Facts track:

- source_file

Sources track:

- source_page
- confidence

### Pipelines

knowledge_pipeline.py
pdf_knowledge_pipeline.py

### Relationship Mining

fact_relationship_builder.py

Generated relationships:

- appears_in
- associated_with