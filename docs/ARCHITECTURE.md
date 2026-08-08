# World Trade Center Evidence Engine Architecture

## Purpose

This document describes the current technical architecture of the World Trade Center Evidence Engine.

It identifies:

- Existing subsystems
- Current data flows
- Database responsibilities
- Working components
- Components requiring verification
- Current integration boundaries

For the enduring roadmap, see:

- `docs/MASTER_PLAN.md`

For current implementation status, see:

- `docs/CURRENT_STATE.md`

For the single active task, see:

- `docs/NEXT_TASK.md`

For evidence rules, see:

- `docs/EVIDENCE_STANDARDS.md`

## Architectural Principles

The architecture must follow these principles:

1. Evidence must remain traceable to its original source.
2. Automated gathering must reuse the existing discovery and downloader systems.
3. Manual incoming directories are development test harnesses, not the final acquisition workflow.
4. Duplicate URLs, files, facts, citations, and relationships must be controlled.
5. Deterministic extraction must remain distinguishable from AI-assisted interpretation.
6. AI output must not become an uncited source of truth.
7. Existing subsystems must be inspected before replacement systems are introduced.
8. Database changes require explicit review and migration planning.
9. Processing stages should be idempotent where practical.
10. Every working milestone must be tested, documented, reviewed, committed, and pushed.

## High-Level Data Flow

Configured Sources
↓
Discovery Layer
↓
Search Requests (`search_candidates`, `record_type = 'search_request'`)
↓
Evidence Candidates (`search_candidates`, `record_type = 'evidence_candidate'`)
↓
Discoveries
↓
Discovery Queue
↓
Downloader
↓
R2 Object Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification
↓
Routing
↓
Specialist Processors
↓
Knowledge Extraction
↓
Fact Normalisation and Cleaning
↓
Sources and Citations
↓
Verification
↓
Relationship Mining
↓
Search and Timeline
↓
Digital Twin Knowledge Model
↓
Evidence-Backed Reconstruction

## Current Integration Boundary

The processing and knowledge layers have been tested using a scanned engineering PDF.

The external evidence-gathering path is not yet confirmed as working end to end.

The current integration task is:

Configured Sources
↓
Existing Discovery Layer
↓
Existing Downloader Layer
↓
R2 and Asset Registration
↓
Processing Queues
↓
Existing Processing and Knowledge Engine

No competing `agents/acquisition/` system should be created.

# Discovery Layer

## Location

`agents/discovery/`

## Purpose

Discover potentially relevant evidence from configured historical and archive sources.

## Known Components

The repository contains components such as:

- `agents/discovery/main.py`
- `agents/discovery/database.py`
- `agents/discovery/discover.py`
- `agents/discovery/build_searches.py`
- `agents/discovery/build_real_searches.py`
- `agents/discovery/find_candidates.py`
- `agents/discovery/promote_searches.py`
- `agents/discovery/manual_promote.py`
- `agents/discovery/queue_discoveries.py`
- `agents/discovery/export_candidates.py`
- `agents/discovery/export_discoveries.py`
- `agents/discovery/sources.json`

The exact responsibility and current validity of every file must be confirmed by repository inspection.

## Intended Flow

`sources.json`
↓
Sources Table
↓
Search Requests (`record_type = 'search_request'`)
↓
Evidence Candidates (`record_type = 'evidence_candidate'`)
↓
Candidate Review or Promotion
↓
Discoveries
↓
Discovery Queue

## Search-Candidate Representation

`search_candidates` distinguishes two record types via a `record_type` field:

- `search_request` — a generated query URL for one source and target
- `evidence_candidate` — a returned evidence URL produced by executing a search request

A search request is not the same thing as a returned evidence URL.

Legacy tables `discovered_urls` and `search_history` are preserved as read-only legacy data and are excluded from the new operational path.

## Intended Responsibilities

- Store trusted evidence sources
- Generate source-specific searches
- Record candidate URLs
- Normalise URLs
- Prevent duplicate candidates
- Assess relevance
- Promote approved candidates
- Reject unsuitable candidates
- Queue discoveries for downloading
- Preserve discovery provenance
- Export diagnostic reports

## Current Status

**Under audit**

The files exist, but the complete discovery workflow must be verified before the layer is marked working.

# Downloader Layer

## Location

`agents/downloader/`

## Known Components

- `agents/downloader/main.py`
- `agents/downloader/r2.py`
- `agents/downloader/test_r2.py`

## Purpose

Convert queued discoveries into stored and registered evidence assets.

## Intended Flow

Discovery Queue
↓
Download Request
↓
Response and Content Validation
↓
File Hashing
↓
Duplicate Detection
↓
R2 Upload
↓
Asset Record
↓
Metadata and Processing Queue

## Intended Responsibilities

- Read pending discovery records
- Download permitted files
- Validate HTTP responses
- Validate content types
- Preserve original URLs
- Calculate cryptographic hashes
- Prevent duplicate storage
- Upload files to R2
- Create asset records
- Create processing jobs
- Record failures
- Retry recoverable failures
- Preserve acquisition provenance

## Current Status

**Under audit**

R2 and downloader code exist, but their complete integration with discovery, assets, queues, and processors must be verified.

# Storage Layer

## R2 Object Storage

R2 is intended to store acquired evidence files.

Each stored object should be associated with:

- Object key
- Original file name
- Original URL
- Source organisation
- MIME type
- File size
- File hash
- Acquisition date
- Rights information
- Asset identifier
- Processing status

## PostgreSQL

Primary database:

`wtc_evidence`

PostgreSQL stores:

- Discovery records
- Operational queues
- Asset metadata
- Analysis output
- Entities
- Facts
- Provenance
- Citations
- Relationships
- Verification status
- Aliases

# Asset and Queue Layer

## Assets

The asset registry represents acquired evidence.

Expected fields include:

- Asset identifier
- Original URL
- Source identifier
- R2 object key
- File name
- File type
- File hash
- Classification
- Acquisition status
- Processing status
- Creation timestamp
- Update timestamp

## Asset Sources (Retrieval Events)

`asset_sources` records retrieval-event provenance for assets.

One `asset_sources` row = one retrieval event.

Expected fields include:

- `asset_id`
- `source_id`
- `original_url`
- `normalised_url`
- `final_effective_url`
- `retrieved_at`
- `created_at`

A second row represents a separate retrieval event or a separately discovered source reference. Two rows are not expected merely because `original_url` and `final_effective_url` differ.

## Queues

Known or intended queues include:

- Discovery queue
- Metadata queue
- Processing queues
- Failure queues
- Retry queues

Queue records should support:

- Status
- Attempt count
- Last error
- Last attempt
- Next retry
- Creation timestamp
- Update timestamp

## Current Status

**Requires verification**

Asset and queue components are documented as existing, but the complete acquisition-to-processing flow must be tested.

# Classification Layer

## Location

`agents/classification/`

## Known Component

`agents/classification/asset_classifier.py`

## Purpose

Determine the evidence type and assign a classification confidence.

## Expected Types

- Photograph
- Blueprint
- Floor plan
- Architectural drawing
- Engineering drawing
- PDF
- Report
- Document
- Newspaper
- Map
- Video
- Audio
- Unknown

## Inputs

Classification may use:

- File extension
- MIME type
- Embedded metadata
- PDF structure
- OCR sample
- Source context
- Deterministic rules
- AI-assisted classification

## Current Status

**Requires verification**

# Routing Layer

## Location

`agents/router/`

## Known Component

`agents/router/route_asset.py`

## Purpose

Route classified assets to specialist processors.

## Intended Routing

Photograph
→ Photo Processor

PDF
→ PDF Processor

Blueprint or Drawing
→ Blueprint Processor

Video
→ Video Processor

Audio
→ Audio Processor

## Current Status

**Requires verification**

Imports, package structure, queue integration, and processor availability must be inspected.

# Processing Layer

## Location

`agents/processors/`

## PDF Text Extractor

File:

`agents/processors/pdf_text_extractor.py`

Implemented responsibilities:

- Embedded text extraction with PyPDF2
- Detection of insufficient embedded text
- OCR fallback using Tesseract
- PDF rendering using pdf2image
- Whole-document extraction
- Page-level extraction
- Page-number preservation

Status:

**Working**

## PDF Analyzer

File:

`agents/processors/pdf_analyzer.py`

Responsibilities:

- Extract PDF text
- Extract entities
- Extract facts
- Clean facts
- Print analysis results

Status:

**Working**

## PDF Processor

File:

`agents/processors/pdf_processor.py`

Intended responsibilities:

- Receive routed PDF assets
- Coordinate extraction
- Trigger OCR
- Preserve asset identity
- Pass results into knowledge processing

Status:

**Requires integration verification**

## Photo Processor

Expected responsibilities:

- Image metadata extraction
- Text and signage OCR
- Visual description
- Location suggestions
- Object and feature detection
- Evidence-linked analysis

Status:

**Requires repository verification**

## Blueprint Processor

Expected responsibilities:

- Drawing-title recognition
- Drawing-number recognition
- Revision recognition
- Sheet recognition
- Floor and tower detection
- Elevation extraction
- Section and detail extraction
- Structural and architectural feature extraction

Status:

**Requires repository verification**

## Video and Audio Processors

Expected responsibilities:

- Media metadata
- Keyframe extraction
- Scene segmentation
- Frame OCR
- Speech-to-text
- Transcripts
- Timestamp-level provenance

Status:

**Requires repository verification**

# Metadata and AI Analysis Layer

## Location

`agents/metadata/`

## Intended Components

- `agents/metadata/vision_analyze.py`
- `agents/metadata/vision_client.py`
- `agents/metadata/r2_download.py`

## Intended Responsibilities

- Read metadata jobs
- Retrieve assets from R2
- Send supported evidence to an analysis provider
- Store descriptions, tags, observations, and confidence
- Preserve provider and model information
- Preserve source-asset identity
## AI Provider Boundary

AI provider access should remain behind a client abstraction.

Possible providers include:

- OpenRouter
- DeepSeek
- Kimi
- Anthropic
- OpenAI
- Microsoft-hosted models
- Local models

AI analysis records should preserve:

- Provider
- Model
- Prompt or prompt version
- Input asset
- Output
- Confidence
- Review status
- Token usage
- Cost information

## Current Status

**Requires audit**

The existing metadata and vision pipeline must be inspected before AI integration is expanded.

# Knowledge Layer

## Location

`agents/knowledge/`

## Knowledge Extractor

File:

`agents/knowledge/knowledge_extractor.py`

Responsibilities:

- Extract known entities
- Extract engineering facts
- Extract drawing-book references
- Extract column types
- Extract spandrel types
- Extract strut types
- Extract section references
- Extract exterior-wall references
- Extract explicit year references

Status:

**Working for current test documents**

The extractor is currently rule-based and WTC-specific. Future expansion must preserve deterministic extraction while allowing validated AI-assisted suggestions.

## Fact Normalizer

File:

`agents/knowledge/fact_normalizer.py`

Responsibilities:

- Convert OCR variants into canonical facts
- Normalise drawing-book references
- Normalise exterior-wall references
- Normalise component types

Status:

**Working**

## Fact Cleaner

File:

`agents/knowledge/fact_cleaner.py`

Responsibilities:

- Reject invalid OCR-derived facts
- Validate known component identifiers
- Filter invalid section references
- Filter implausible year values
- Deduplicate cleaned output

Status:

**Working**

## PDF Knowledge Pipeline

File:

`agents/knowledge/pdf_knowledge_pipeline.py`

Responsibilities:

- Extract PDF pages
- Process pages independently
- Extract entities and facts
- Clean facts
- Insert or resolve facts
- Store source-file provenance
- Store source-page provenance

Status:

**Working**

## General Knowledge Pipeline

File:

`agents/knowledge/knowledge_pipeline.py`

Responsibilities:

- Read existing analysis descriptions
- Extract entities and facts
- Clean extracted facts
- Store knowledge records

Status:

**Working for its current input source**

The general knowledge pipeline is separate from the PDF-specific knowledge pipeline.

## Entity Resolution

File:

`agents/knowledge/entity_resolution.py`

Responsibilities:

- Maintain entity aliases
- Resolve aliases to canonical names
- Create canonical entities
- Merge alias relationships
- Reassign linked facts
- Prevent duplicate canonical entities

Database support:

`entity_aliases`

Status:

**Working**

## Fact Relationship Builder

File:

`agents/knowledge/fact_relationship_builder.py`

Responsibilities:

- Group facts using page-level provenance
- Mine page-co-occurrence relationships
- Create missing fact entities
- Insert or update relationships
- Calculate evidence counts
- Calculate relationship confidence
- Record the source method

Current relationship types include:

- `appears_in`
- `associated_with`

Current source method:

- `page_cooccurrence`

Status:

**Working**

Page co-occurrence represents an association signal. Page co-occurrence does not prove causation, containment, structural dependency, or design intent.

## Citation Loader

File:

`agents/knowledge/citation_loader.py`

Responsibilities:

- Read evidence from `fact_sources`
- Create citation records
- Preserve source-file information
- Preserve source-page information
- Prevent duplicate citations

Status:

**Working**

# Verification Layer

## Location

`agents/verification/`

## Fact Verifier

File:

`agents/verification/fact_verifier.py`

Responsibilities:

- Count evidence records supporting each fact
- Update verification status
- Update operational confidence

Current operational rules:

- Zero sources: claim, confidence 50
- One source: supported, confidence 70
- Two sources: well supported, confidence 85
- Three or more sources: verified, confidence 95

Status:

**Working**

## Verification Limitation

Source-record count is not necessarily independent-source count.

Several pages from one document may increase the current source count without representing several independent pieces of evidence.

Future verification must account for:

- Independent source count
- Duplicate documents
- Derivative copies
- Source priority
- Source authenticity
- Directness
- Date relevance
- Contradictions
- Human review

# Search Layer

## Location

`agents/search/`

## Relationship Search v2

File:

`agents/search/relationship_search.py`

Responsibilities:

- Search source and target entities
- Display relationship type
- Display relationship confidence
- Display evidence count
- Display source method
- Display fact confidence
- Display verification status
- Display supporting source files
- Display supporting source pages

Status:

**Working**

## Additional Search Components

Known files include:

- `agents/search/query_engine.py`
- `agents/search/graph_search.py`

Status:

**Requires verification**

# Timeline Layer

## Location

`agents/timeline/`

## Timeline Builder

File:

`agents/timeline/timeline_builder.py`

Responsibilities:

- Load explicit year facts
- Reject technical identifiers that resemble calendar years
- Display fact confidence
- Display verification status
- Display available source provenance

Status:

**Working**

Current limitation:

Timeline extraction depends on explicit date-oriented fact patterns and is not yet a complete historical event model.

# Local Processing Test Harness

## Location

`agents/ingestion/`

## Automated Ingestion

File:

`agents/ingestion/automated_ingestion.py`

Responsibilities:

- Read PDFs from `data/incoming_pdfs/`
- Process each PDF
- Move successful files to `data/processed_pdfs/`
- Move failed files to `data/failed_pdfs/`
- Rebuild fact relationships

Status:

**Working development test harness**

This is not the final automated evidence-acquisition system.

The completed acquisition workflow must use the discovery and downloader layers.

# Engine Orchestration Layer

## Location

`agents/engine/`

## Master Engine Runner

File:

`agents/engine/run_engine.py`

Current workflow:

1. Automated local PDF processing
2. Citation loading
3. Fact verification
4. Relationship building
5. Timeline generation

Status:

**Working for the current processing pipeline**

Future integration should include:

- Automated discovery
- Candidate promotion
- Discovery queue processing
- Downloading
- File validation
- File deduplication
- R2 storage
- Asset registration
- Classification
- Routing
- Specialist processing
- Health reporting

These additions must happen only after the existing discovery and downloader systems are audited and tested.

## Engine Health Report

File:

`agents/engine/health_report.py`

Responsibilities:

- Count entities
- Count facts
- Count fact sources
- Count citations
- Count relationships
- Count entity aliases
- Report fact-verification statuses
- Report facts without sources
- Report relationships without source methods
- Report top source files
- Report top relationships

Status:

**Working**

# Database Architecture

## Primary Database

`wtc_evidence`

## Known Core Tables

Known knowledge and operational tables include:

- `sources`
- `assets`
- `asset_sources`
- `metadata_queue`
- `ai_analysis`
- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`

Discovery-related tables include:

- `search_candidates` — records both `search_request` and `evidence_candidate` record types via a `record_type` field
- `discoveries` — the canonical discovery record for all new rows
- `discovery_queue`

Legacy discovery tables (read-only, outside the new operational path):

- `discovered_urls`
- `search_history`

The exact discovery and operational schemas will be confirmed during the migrations defined in the repair plan.

## Entities

Purpose:

Store canonical entities.

Examples:

- World Trade Center
- North Tower
- South Tower
- Drawing Book 1
- Column Type 7000

## Entity Aliases

Purpose:

Map alternate terminology to canonical entity names.

Examples:

- `WTC` maps to `World Trade Center`
- `WTC 1` maps to `North Tower`
- `WTC 2` maps to `South Tower`

## Facts

Purpose:

Store unique canonical fact text and verification metadata.

Known fields include:

- `id`
- `entity_id`
- `fact_text`
- `confidence`
- `verification_status`
- `source_file`
- `source_page`

The legacy `source_file` and `source_page` fields may remain for compatibility.

The `fact_sources` table is the authoritative scalable provenance model.

Important constraint:

`unique_fact`

## Fact Sources

Purpose:

Store multiple evidence locations for one canonical fact.

Known fields include:

- `id`
- `fact_id`
- `source_file`
- `source_page`
- `confidence`

Important constraint:

`unique_fact_source`

## Citations

Purpose:

Provide the research-facing evidence citation layer.

Known fields include:

- `id`
- `fact_id`
- `source_file`
- `source_page`
- `confidence`
- `citation_type`
- `created_at`

The citation schema should later support additional evidence types such as URLs, photographs, drawing sheets, frames, and timestamps.

## Relationships

Purpose:

Store graph relationships between entities.

Known fields include:

- `id`
- `source_entity_id`
- `relationship_type`
- `target_entity_id`
- `confidence`
- `evidence_count`
- `source_method`
- `created_at`

Important constraint:

`unique_relationship`

## Current Provenance Model

Facts
↓
Fact Sources
↓
Citations

Future provenance must also support:

- Original URLs
- Archive references
- R2 object keys
- Drawing sheets
- Drawing details
- Image identifiers and regions
- Video frames and timestamps
- Audio timestamps
- AI-analysis records
- Human-review records

# Python Package Architecture

The `agents` directory is a Python package.

Package directories should contain:

`__init__.py`

Internal imports should use package-qualified imports.

Example:

`from agents.knowledge.fact_cleaner import clean_facts`

Package-dependent modules should be executed from the repository root using module mode.

Example:

`python -m agents.knowledge.pdf_knowledge_pipeline`

Direct execution of package-dependent modules should generally be avoided.

# Dependency Architecture

## Python Dependencies

Python packages are maintained in the root:

`requirements.txt`

Known dependencies include:

- PyPDF2
- pdf2image
- pytesseract
- psycopg2-binary
- python-dotenv
- requests
- boto3
- beautifulsoup4

The root requirements file remains authoritative and should be reviewed before deployment.

## System Dependencies

Known system dependencies include:

- Tesseract OCR
- Poppler utilities
- PostgreSQL client
- Python virtual-environment support

System dependencies cannot be represented fully in `requirements.txt`.

Server bootstrap and deployment documentation must install system dependencies explicitly.

# Development AI Workflow

## Current Development Assistant

The current repository-aware development workflow uses:

- Cline
- OpenRouter
- DeepSeek V4 Flash
- Plan mode before Act mode
- Approval before file edits and terminal commands
- Cline checkpoints enabled

## Project Memory

Repository documentation and Git history are the authoritative project memory.

Model conversation history is not authoritative project memory.

Before significant development work, Cline should read:

- `docs/MISSION.md`
- `docs/EVIDENCE_STANDARDS.md`
- `docs/MASTER_PLAN.md`
- `docs/ARCHITECTURE.md`
- `docs/CURRENT_STATE.md`
- `docs/NEXT_TASK.md`
- `docs/AI_HANDOFF.md`
- `.clinerules`

## Safe Development Flow

Read
↓
Audit
↓
Plan
↓
Approve
↓
Implement One Scoped Change
↓
Compile or Test
↓
Review Git Diff
↓
Update Documentation
↓
Commit

Cline must not:

- Duplicate existing systems
- Change database schemas without explicit approval
- Delete evidence
- Commit secrets or API keys
- Commit downloaded evidence files
- Commit unreviewed changes
- Treat AI output as historical evidence
- Jump to unrelated roadmap phases
- Replace working files without first reading them completely
- run destructive commands without explicit approval

# Current Architecture Task

Inspect all relevant files under:

- `agents/discovery/`
- `agents/downloader/`

The audit must identify:

- File purpose
- Imports and dependencies
- Database tables used
- Inputs
- Outputs
- Invocation method
- Completion status
- Duplicate responsibilities
- Broken package imports
- Missing queue transitions
- Missing R2 integration
- Missing asset registration
- Missing processing handoff
- Required tests

The audit must also inspect the relevant database schemas for:

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `metadata_queue`

No files or database records should be changed during the initial audit.

After the audit, repairs must be implemented as small, tested milestones.

The authoritative task definition is maintained in:

- `docs/NEXT_TASK.md`