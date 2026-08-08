# World Trade Center Evidence Engine Master Plan

## Purpose

This document defines the enduring roadmap for the World Trade Center Evidence Engine and evidence-backed digital twin.

It covers the complete intended system from automated evidence discovery through acquisition, processing, verification, knowledge modelling, historical reconstruction, and an explorable walkthrough.

This document is not the current task list.

For current status, see:

- `docs/CURRENT_STATE.md`

For the single active task, see:

- `docs/NEXT_TASK.md`

For AI development context, see:

- `docs/AI_HANDOFF.md`

## Mission

Build an automated, transparent, citation-backed evidence engine capable of supporting the most historically accurate digital reconstruction of the original World Trade Center complex.

The completed system must:

1. Discover historical evidence automatically
2. Download and register permitted evidence
3. Detect duplicate URLs and duplicate files
4. Store evidence and metadata
5. Classify and route assets
6. Process documents, images, drawings, video, and audio
7. Extract entities, facts, events, and relationships
8. Preserve source, page, sheet, frame, and timestamp provenance
9. Create research citations
10. Verify claims and preserve contradictions
11. Build a searchable knowledge graph
12. Support an evidence-backed digital twin and walkthrough

Artificial intelligence may enrich evidence processing, but artificial intelligence must not become an uncited source of truth.

## End-to-End Pipeline

Configured Sources and Research Targets
↓
Automated Discovery
↓
Search Candidates
↓
Discoveries
↓
Discovery Queue
↓
Downloader
↓
Validation and Deduplication
↓
R2 Object Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Specialist Processors
↓
Knowledge Extraction
↓
Normalisation and Cleaning
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

Manual placement of files into incoming directories is a development and testing mechanism. It is not the final evidence-acquisition workflow.

## Phase 1: Automated Evidence Discovery

### Goal

Automatically identify relevant historical evidence from configured and permitted sources.

### Existing Foundation

The repository already contains discovery components under:

`agents/discovery/`

These components must be inspected, repaired, tested, and reused.

A competing acquisition subsystem must not be created unless the existing system is formally reviewed and deliberately replaced.

### Inputs

Discovery inputs may include:

- Trusted source registry
- Source URLs
- Search targets
- Search terms
- Historical aliases
- Building and space names
- Drawing identifiers
- Document identifiers
- Date ranges
- Source-specific search patterns
- Existing entities
- Existing facts
- Open research questions

### Outputs

Discovery should produce:

- Source records
- Search definitions
- Search candidates
- Candidate URLs
- Discovery records
- Relevance scores
- Access dates
- Review statuses
- Discovery queue entries

### Requirements

The discovery system must support:

- URL normalisation
- URL deduplication
- Domain restrictions
- Source allowlists
- Rate limiting
- Retry handling
- Failure logging
- Candidate rejection
- Manual promotion where necessary
- Scheduled rechecking of approved sources
- Source-policy awareness
- Rights and usage awareness

### Completion Criteria

Discovery is complete when configured sources can produce relevant, deduplicated discovery records without requiring the user to locate and paste every evidence URL manually.

## Phase 2: Downloading and Asset Registration

### Goal

Convert approved discoveries into stored, registered, and traceable evidence assets.

### Existing Foundation

The repository already contains downloader components under:

`agents/downloader/`

The existing downloader must be connected to the discovery queue, R2 storage, the assets table, and processing queues.

### Required Workflow

Discovery Queue
↓
Downloader
↓
Response Validation
↓
File Hashing
↓
Duplicate Detection
↓
R2 Upload
↓
Asset Registration
↓
Metadata and Processing Queues

### Required Asset Metadata

Each asset should preserve, where available:

- Original URL
- Source organisation
- Discovery record
- Retrieval date
- Access date
- HTTP status
- Content
- Content type
- Original file name
- R2 object key
- File size
- Cryptographic file hash
- Rights or licence information
- Source title
- Source creation or publication date
- Asset type
- Classification confidence
- Processing status
- Failure status
- Retry information

### Deduplication Requirements

The downloader should distinguish between:

- Repeated URL
- Redirected URL
- Identical file hash
- Different scan of the same source
- Different edition
- Different drawing revision
- Cropped or transformed derivative
- Independent evidence

### Completion Criteria

This phase is complete when approved discoveries can become registered, deduplicated R2 assets without manual file transfer.

## Phase 3: Classification and Routing

### Goal

Identify each asset type and route it to the appropriate specialist processor.

### Supported or Planned Asset Types

- Photograph
- Architectural drawing
- Engineering drawing
- Blueprint
- Floor plan
- Map
- PDF document
- Report
- Newspaper
- Publication
- Video
- Audio
- Web capture
- Data file
- Unknown asset

### Classification Inputs

Classification may use:

- File extension
- MIME type
- Embedded metadata
- PDF structure
- OCR samples
- Source context
- Deterministic rules
- AI-assisted classification

### Completion Criteria

Every registered asset receives:

- An asset type
- A classification confidence
- A processing route
- A traceable processing status

## Phase 4: Specialist Evidence Processing

### PDF Processing

Required capabilities include:

- Embedded-text extraction
- OCR fallback
- Page-level extraction
- Page-number attribution
- Document metadata
- Drawing-book detection
- Sheet and drawing references
- Processing-failure recovery

### Image Processing

Required capabilities include:

- Metadata extraction
- Text and signage OCR
- Visual description
- Location suggestions
- Object and feature detection
- Duplicate and derivative detection
- Evidence-linked AI analysis

### Drawing Processing

Required capabilities include:

- Drawing title and number
- Revision and sheet number
- Scale
- Floor and tower
- Elevation
- Sections and details
- Dimensions
- Structural references
- Architectural references
- Design-status interpretation
- As-designed versus as-built distinction

### Video Processing

Required capabilities include:

- Video metadata
- Keyframe extraction
- Scene segmentation
- Frame OCR
- Speech-to-text
- Transcripts
- Timestamp-level citations
- Location and object suggestions
- Duplicate-footage detection

### Audio Processing

Required capabilities include:

- Audio metadata
- Speech-to-text
- Timestamp-level citations
- Entity extraction
- Claim extraction
- Uncertainty preservation

### Completion Criteria

Supported evidence formats produce traceable text, observations, metadata, pages, sheets, frames, and timestamps suitable for knowledge extraction.

## Phase 5: Knowledge Extraction

### Goal

Transform processed evidence into structured and cited knowledge.

### Existing Foundation

Implemented components include:

- Entity extraction
- Engineering fact extraction
- Fact normalisation
- Fact cleaning
- Fact deduplication
- PDF knowledge ingestion
- Source-file provenance
- Source-page provenance
- Citation loading
- Entity alias resolution
- Relationship mining
- Verification scoring

### Knowledge Objects

The engine should represent:

- Entities
- Aliases
- Facts
- Claims
- Dates
- Events
- Locations
- Spaces
- Components
- Systems
- Sources
- Citations
- Relationships
- Contradictions
- Research questions
- Digital-twin elements

### Extraction Types

The system must distinguish between:

- Direct source metadata
- Embedded text
- OCR-derived text
- Deterministic extraction
- AI-assisted extraction
- AI-generated suggestions
- Human-reviewed conclusions

### Canonicalisation

The system must normalise:

- Entity aliases
- Building names
- Tower names
- Floor names
- Space names
- Drawing references
- Elevations
- Dates
- Structural identifiers
- Organisation names

### Completion Criteria

Evidence produces structured knowledge without losing source, page, sheet, frame, timestamp, extraction-method, or confidence provenance.

## Phase 6: Citations and Provenance

### Goal

Make every important claim traceable to supporting evidence.

### Existing Foundation

The current system includes:

- `fact_sources`
- Source-file attribution
- Source-page attribution
- Citation loading
- Fact confidence
- Verification status

### Required Citation Types

- PDF page
- Drawing sheet
- Drawing detail
- Photograph
- Archive record
- Web page
- Image region
- Video timestamp
- Audio timestamp
- Database entry
- Manual research note

### Multiple Sources

A fact may be supported by:

- Multiple pages in one document
- Multiple documents from one organisation
- Multiple derivative copies
- Multiple independent sources
- Conflicting sources

Repeated copies must not automatically be treated as independent evidence.

### Completion Criteria

A researcher can navigate from a fact, relationship, event, or reconstruction element to the smallest useful original evidence location.

## Phase 7: Verification and Contradictions

### Goal

Evaluate evidence strength and preserve unresolved conflicts.

### Existing Foundation

Current operational fact-verification defaults are:

- Zero source records: claim, confidence 50
- One source record: supported, confidence 70
- Two source records: well supported, confidence 85
- Three or more source records: verified, confidence 95

These are operational defaults, not universal historical truth.

### Future Verification Inputs

Future verification must consider:

- Independent source count
- Source priority
- Source authenticity
- Directness
- Date relevance
- OCR quality
- Extraction method
- Document revision
- As-designed versus as-built status
- Contradictions
- Human review

### Contradiction Handling

The engine must preserve:

- Conflicting claims
- Supporting citations
- Relevant dates
- Confidence values
- Review notes
- Preferred interpretations where justified
- Unresolved status where appropriate

### Completion Criteria

Confidence reflects evidence quality, relevance, and independence rather than simple record repetition alone.

## Phase 8: Relationships and Knowledge Graph

### Goal

Connect entities, facts, spaces, documents, events, and evidence.

### Existing Foundation

The current system supports:

- Seed relationships
- Page-co-occurrence relationships
- Relationship confidence
- Evidence counts
- Source methods
- Relationship Search v2

### Relationship Examples

- `part_of`
- `located_in`
- `contains`
- `appears_in`
- `documented_in`
- `associated_with`
- `designed_by`
- `constructed_by`
- `occupied_by`
- `connected_to`
- `replaced_by`
- `changed_at`
- `supported_by`
- `contradicted_by`

### Important Limitation

Page co-occurrence indicates an association signal.

Page co-occurrence does not by itself prove causation, containment, structural dependency, or design intent.

### Completion Criteria

Users can discover meaningful, cited connections rather than only isolated records.

## Phase 9: Search, Timeline, and Research Tools

### Existing Foundation

Implemented tools include:

- Relationship Search v2
- Timeline Builder
- Provenance display
- Engine Health Report
- Query and graph-search foundations

### Planned Capabilities

- Entity search
- Fact search
- Source search
- Citation search
- Full-text search
- Date search
- Floor and space search
- Drawing-number search
- Media search
- Confidence filtering
- Verification filtering
- Contradiction filtering

### Timeline Requirements

Timeline events should preserve:

- Date or date range
- Event description
- Associated entities
- Associated locations
- Supporting sources
- Confidence
- Verification status
- Contradictory dates

Technical identifiers containing four digits must not automatically be treated as calendar years.

### Completion Criteria

Researchers can explore evidence, sources, facts, relationships, dates, confidence, uncertainty, and contradictions through coherent tools.

## Phase 10: Engine Orchestration

### Existing Foundation

Implemented operational components include:

- Automated local PDF-processing test harness
- Master Engine Runner
- Citation loading
- Fact verification
- Relationship building
- Timeline generation
- Engine Health Report

### Intended Production Workflow

Scheduled Source Discovery
↓
Candidate Promotion
↓
Discovery Queue
↓
Download and Asset Registration
↓
Classification and Routing
↓
Specialist Processing
↓
Knowledge Extraction
↓
Citation Loading
↓
Verification
↓
Relationship Building
↓
Search and Timeline Updates
↓
Health Reporting

### Operational Requirements

- Scheduled runs
- Idempotency
- Job status
- Retry handling
- Failure queues
- Structured logging
- Metrics
- Health checks
- Cost monitoring
- API-usage monitoring
- Backups
- Database migrations
- Secrets management
- Recovery procedures

### Completion Criteria

The engine can run unattended, recover from failures, and report its own state.

## Phase 11: AI Enrichment

### Goal

Use artificial intelligence to improve evidence processing without weakening evidence standards.

### Candidate Uses

- Evidence relevance scoring
- Document classification
- Document summarisation
- Fact suggestions
- Entity suggestions
- Relationship suggestions
- Image interpretation
- Drawing interpretation
- Contradiction detection
- Research assistance

### Requirements

- AI output must be labelled
- AI output must retain source citations
- AI suggestions must not overwrite evidence
- Unsupported details must not be invented
- Structured output must be validated
- Provider and model must be recorded
- Prompt or prompt version should be recorded
- Token usage and cost should be monitored
- High-impact claims require human review

### Completion Criteria

AI improves throughput and interpretation while accepted knowledge remains traceable to evidence.

## Phase 12: Digital Twin Knowledge Model

### Goal

Represent the World Trade Center as structured, time-aware, and evidence-backed spatial knowledge.

### Planned Hierarchy

World Trade Center Complex
↓
Site
↓
Building
↓
Tower
↓
Floor
↓
Zone
↓
Space
↓
Architectural or Structural Element
↓
Object, Material, System, or Feature

### Required Records

- Complex
- Site
- Building
- Tower
- Floor
- Space
- Zone
- Structural element
- Architectural element
- Material
- Object
- Building system
- Connection
- Geometry reference
- Time period
- Evidence status
- Supporting citations
- Confidence
- Reconstruction notes

### Time Awareness

The twin must support changes over time, including:

- Construction phases
- Original configurations
- Renovations
- Tenant changes
- Space changes
- Signage changes
- Furniture changes
- Operational changes

### Completion Criteria

Evidence can be attached to specific buildings, floors, spaces, systems, objects, and reconstruction elements.

## Phase 13: Evidence-Backed Reconstruction

### Goal

Create reconstruction assets from verified or clearly labelled evidence.

Every significant reconstruction element should include:

- Evidence status
- Supporting citations
- Applicable historical period
- Confidence
- Assumptions
- Open questions
- Human-review status

Inferred geometry or appearance must remain distinguishable from verified reconstruction.

### Completion Criteria

Selected areas can be reconstructed with clear evidence traceability and uncertainty labels.

## Phase 14: Explorable Walkthrough

### Goal

Provide an experience combining historical exploration, reconstruction, and supporting evidence.

Users should be able to:

- Navigate the complex
- Select buildings and floors
- Enter reconstructed spaces
- Inspect architectural elements and objects
- Open supporting evidence
- Open citations
- Compare historical periods
- Display confidence and uncertainty
- Search entities and facts
- Explore timelines
- View alternative interpretations

### Completion Criteria

The walkthrough presents both the reconstruction and the evidence supporting the reconstruction.

## Cross-Cutting Requirements

Every phase must preserve:

- Provenance
- Citation traceability
- Deduplication
- Source-independence awareness
- Confidence and verification
- Contradictions
- Human review
- Rights metadata
- Security
- Recoverability
- Documentation
- Testing
- Cost awareness

## Development Method

Development proceeds through small, verified milestones:

Inspect
↓
Plan
↓
Implement One Scoped Change
↓
Run Targeted Tests
↓
Review Git Diff
↓
Update Documentation
↓
Commit
↓
Continue

Existing architecture must be inspected before replacement architecture is introduced.

A new system must not duplicate an existing subsystem without an explicit review and migration decision.

## Current Strategic Priority

The immediate strategic priority is to inspect, reconnect, test, and complete the existing automated evidence-gathering pipeline under:

- `agents/discovery/`
- `agents/downloader/`

The exact active implementation task is maintained in:

- `docs/NEXT_TASK.md`