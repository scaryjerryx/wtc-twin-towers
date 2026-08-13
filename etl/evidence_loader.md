# ETL Evidence Citation Ingestion Pipeline Specification

## Pipeline Overview
The Evidence Ingestion Pipeline parses PDF citation URIs, bounding box coordinates, and drawing sheet numbers, linking physical drawing evidence to digital twin entities.

```text
Drawing Citations ──► Bounding Box Parsing ──► PostgreSQL Evidence Table ──► Web Viewport Overlays
```

## Pipeline Execution Stages
1. **Extraction:** Parses `drawing_sheet.pdf#page=N&rect=X1,Y1,X2,Y2` citations.
2. **Entity Linkage:** Associates evidence record to target `entity_id` and `drawing_id`.
3. **Relational Load:** Inserts record into `wtc_evidence.evidence`.
