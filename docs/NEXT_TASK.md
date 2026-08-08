# Next Task

## Reconnect Existing Automated Evidence Gathering

### Status

🔄 **In Progress**

## Objective

Audit, reconnect, repair, and test the existing automated evidence-discovery and downloader pipeline.

The completed workflow must automatically discover evidence, create discovery records, download permitted files, prevent duplicate storage, upload evidence to R2, register assets, create processing jobs, and hand those assets into the existing processing and knowledge engine.

## Existing Systems to Reuse

The repository already contains the relevant foundations under:

- `agents/discovery/`
- `agents/downloader/`

These systems must be inspected before any implementation changes are made.

Do not create a competing `agents/acquisition/` subsystem.

Do not replace the existing discovery or downloader architecture without a documented audit and explicit migration decision.

## Intended End-to-End Flow

Configured Sources
↓
Sources Table
↓
Search Definitions
↓
Search Candidates
↓
Candidate Review and Promotion
↓
Discoveries
↓
Discovery Queue
↓
Downloader
↓
HTTP Response and Content Validation
↓
URL and File-Hash Deduplication
↓
R2 Object Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Existing Specialist Processors
↓
Existing Knowledge Engine

## Phase 1: Read-Only Repository Audit

Inspect every relevant file under:

- `agents/discovery/`
- `agents/downloader/`

The audit must record, for every file:

- File path
- Purpose
- Imports
- Dependencies
- Database tables used
- Input records
- Output records
- Files created or downloaded
- Invocation method
- Expected execution order
- Package-import safety
- Completion status
- Duplicate responsibilities
- Missing error handling
- Missing tests
- Known blockers

The audit must not modify files or database records.

## Phase 2: Database Schema Audit

Inspect the current PostgreSQL schemas for:

- `sources`
- `search_candidates`
- `discoveries`
- `discovery_queue`
- `assets`
- `metadata_queue`
- Any processing or failure queues used by the existing code

For each table, record:

- Columns
- Data types
- Primary key
- Foreign keys
- Unique constraints
- Default values
- Status fields
- Required fields
- Indexes
- Tables or scripts that read from it
- Tables or scripts that write to it

Do not perform schema migrations during the initial audit.

## Phase 3: Minimal Repair Plan

After the repository and schema audits, produce the smallest ordered repair plan required to create a working end-to-end acquisition path.

The repair plan must:

1. Reuse existing files where practical
2. Avoid duplicate systems
3. Identify obsolete files
4. Identify broken imports
5. Identify missing queue transitions
6. Identify missing deduplication
7. Identify missing R2 integration
8. Identify missing asset registration
9. Identify missing processing handoff
10. Define a targeted test for each repair

Stop after presenting the audit and repair plan.

Wait for approval before editing code or changing the database.

## Implementation Order

After the audit and plan are approved, implementation should proceed through these milestones:

### Milestone 1: Source Seeding

Confirm that configured sources can be loaded into the `sources` table safely and idempotently.

Required test:

- Run source seeding twice
- Confirm that duplicate source records are not created

### Milestone 2: Search Candidate Creation

Confirm that source-specific searches can create normalised, deduplicated search candidates.

Required test:

- Generate candidates from one approved test source
- Confirm candidate URLs and source provenance are stored
- Confirm repeated runs do not create duplicate candidates

### Milestone 3: Discovery Promotion

Confirm that an approved candidate can become a discovery record.

Required test:

- Promote one test candidate
- Confirm the discovery retains the candidate and source relationship
- Confirm duplicate discovery records are prevented

### Milestone 4: Discovery Queue

Confirm that an approved discovery can enter the downloader queue.

Required test:

- Queue one discovery
- Confirm its initial status
- Confirm repeated queue operations remain idempotent

### Milestone 5: Download and Validation

Confirm that the downloader can retrieve one permitted test file.

Required test:

- Validate HTTP status
- Validate content type
- Preserve the original URL
- Preserve the source record
- Record failures without losing the discovery

### Milestone 6: Deduplication

Add or verify:

- URL normalisation
- URL deduplication
- Cryptographic file hashing
- File-hash deduplication

Required test:

- Process the same URL twice
- Process the same file from two permitted URLs
- Confirm duplicate storage is prevented
- Confirm all source references are preserved

### Milestone 7: R2 Storage

Confirm that one downloaded file can be uploaded to R2.

Required test:

- Upload one test file
- Confirm the R2 object exists
- Confirm the object key is preserved
- Confirm the original URL and file hash remain associated with the object

### Milestone 8: Asset Registration

Confirm that the stored R2 object creates a valid asset record.

Required test:

- Confirm asset identifier
- Confirm R2 object key
- Confirm source URL
- Confirm source identifier
- Confirm file name
- Confirm content type
- Confirm file hash
- Confirm acquisition status
- Confirm processing status

### Milestone 9: Processing Queue

Confirm that the new asset creates the required metadata or processing job.

Required test:

- Confirm the asset is queued only once
- Confirm the queue status is correct
- Confirm processor routing can locate the asset

### Milestone 10: Existing Engine Handoff

Confirm that the registered and queued asset reaches the existing processing and knowledge engine.

Required test:

- Route one supported PDF asset
- Extract text or OCR
- Create provenance records
- Load citations
- Verify facts
- Build relationships
- Confirm the full path is traceable back to the discovery URL

### Milestone 11: Master Engine Integration

Only after the previous milestones pass, update the Master Engine Runner to include the repaired evidence-gathering workflow.

Expected future order:

1. Source and discovery processing
2. Candidate promotion
3. Discovery queue processing
4. Download and asset registration
5. Classification and routing
6. Specialist processing
7. Citation loading
8. Fact verification
9. Relationship building
10. Timeline updates
11. Health reporting

## Completion Criteria

This task is complete when:

1. Existing discovery and downloader files have been audited
2. Relevant database schemas have been documented
3. Broken package imports have been repaired
4. One approved source can create search candidates
5. One candidate can become a discovery
6. One discovery can enter the downloader queue
7. One permitted file can be downloaded
8. HTTP response and content type are validated
9. URL duplicates are prevented
10. File-hash duplicates are prevented
11. The file is stored in R2
12. A valid asset record is created
13. A processing job is created
14. The asset reaches the existing processing engine
15. Provenance remains traceable to the original discovery URL
16. Targeted tests pass
17. Documentation is updated
18. The Git diff is reviewed
19. A working checkpoint is committed and pushed

## Non-Goals

Do not begin any of the following during this task:

- A new acquisition subsystem
- Digital Twin schema development
- Reconstruction geometry
- Walkthrough development
- Broad AI enrichment
- Unrelated search redesign
- Unrelated database refactoring
- Automatic production scheduling
- Large-scale crawling
- Downloading an uncontrolled archive collection

The purpose of this task is to make one controlled evidence path work end to end before scaling it.

## Safety Rules

- Inspect before editing
- Work on one milestone at a time
- Read complete files before replacing them
- Prefer targeted changes over broad rewrites
- Require approval for database changes
- Do not delete evidence
- Do not commit secrets or API keys
- Do not commit downloaded evidence files
- Do not run destructive commands without explicit approval
- Run targeted tests after each change
- Review `git diff` after each change
- Update documentation only after tests pass
- Do not commit automatically
- Stop when the approved milestone is complete