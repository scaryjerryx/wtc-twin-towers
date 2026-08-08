# Evidence Standards

## Purpose

These standards govern how the World Trade Center Evidence Engine
discovers, records, evaluates, cites, verifies, and uses historical
evidence.

The standards apply to:

- Automated discovery
- Manual research
- Downloaded files
- Archive records
- OCR output
- Extracted facts
- AI-assisted analysis
- Knowledge-graph relationships
- Timeline events
- Digital-twin reconstruction elements

Evidence must remain traceable to its origin.

## Core Principles

### Evidence Before Assumption

The engine must prefer documented evidence over unsupported assumptions.

When evidence is unavailable, incomplete, ambiguous, or conflicting, the
system must record that uncertainty rather than present an inference as a
verified fact.

### Provenance Must Be Preserved

Every stored fact, relationship, event, or reconstruction claim should
retain enough provenance to identify where the supporting information
came from.

### Sources Must Not Be Treated as Equally Reliable

Source type, authenticity, independence, date, context, and relevance
must all be considered.

A high-priority source may still be ambiguous or inaccurate for a
particular claim.

### Design Intent Is Not Always As-Built Evidence

Architectural and engineering drawings may show:

- Proposed design
- Issued design
- Revised design
- Construction intent
- As-built conditions

The engine must not automatically treat every drawing as proof of what
was ultimately constructed.

### Date and Context Matter

The World Trade Center changed over time.

Evidence must be associated with a date, date range, construction phase,
operational period, or uncertainty where possible.

A photograph or document may accurately describe one period while being
incorrect for another.

## Evidence Priority Guide

The following priorities guide evaluation but do not automatically
determine truth.

### Priority 1: Primary Design and Construction Records

Examples:

- Original architectural drawings
- Structural engineering drawings
- Mechanical and electrical drawings
- Specifications
- Shop drawings
- As-built drawings
- Change orders
- Construction records
- Official project correspondence

Best suited for:

- Design intent
- Dimensions
- Materials
- Structural systems
- Building systems
- Construction decisions

Important limitation:

Design documents may not represent final as-built conditions unless the
document status is known.

### Priority 2: Official Operational and Institutional Records

Examples:

- Port Authority publications
- Tenant records
- Official floor directories
- Operations manuals
- Inspection records
- Maintenance documentation
- Government archives
- Official reports

Best suited for:

- Building use
- Tenant occupancy
- Operational changes
- Official terminology
- Dates and institutional decisions

### Priority 3: Construction and Survey Photography

Examples:

- Construction photographs
- Progress photographs
- Survey photographs
- Inspection photographs
- Official photographic documentation

Best suited for:

- As-built appearance
- Construction sequence
- Installed components
- Materials
- Spatial relationships

### Priority 4: Contemporary Photographs and Film

Examples:

- Dated interior photographs
- Exterior photographs
- Professional photography
- News footage
- Documentary footage
- Visitor photographs
- Tenant photographs

Best suited for:

- Appearance at a particular date
- Furniture and objects
- Signage
- Lighting
- Finishes
- Layout and spatial use

### Priority 5: Contemporary Publications

Examples:

- Books
- Brochures
- Newspapers
- Magazines
- Trade publications
- Engineering journals
- Architectural journals
- Maps
- Guidebooks

Best suited for:

- Historical context
- Contemporary descriptions
- Published dates
- Public interpretation
- Technical reporting

### Priority 6: Later Research and Secondary Sources

Examples:

- Historical studies
- Museum publications
- Research websites
- Later documentaries
- Academic analysis
- Curated databases

Best suited for:

- Locating primary evidence
- Providing context
- Comparing interpretations
- Identifying open research questions

### Priority 7: Eyewitness and Personal Accounts

Examples:

- Interviews
- Memoirs
- Personal recollections
- Oral histories
- Forum discussions
- Correspondence

Best suited for:

- Leads
- Personal experience
- Use of spaces
- Events not otherwise documented
- Identifying terminology or locations for further research

Important limitation:

Memory may be incomplete, date-dependent, or influenced by later
information. Eyewitness claims should be corroborated where possible.

## Required Provenance

Evidence records should include the following fields where applicable:

- Source organisation
- Source title
- Source type
- Author, creator, photographer, or issuing organisation
- Original URL
- Archive collection and reference number
- Publication or creation date
- Date range
- Acquisition date
- Access date
- Local file location
- Object-storage location
- File name
- File format
- File hash
- Page number
- Drawing or sheet number
- Image identifier
- Frame number
- Video or audio timestamp
- Description
- Extracted text or observation
- Extraction method
- Associated entities
- Associated facts
- Confidence
- Verification status
- Rights or usage notes
- Research notes

Not every source will provide every field. Missing values should remain
unknown rather than being invented.

## File Integrity and Deduplication

Downloaded evidence should be assigned a cryptographic file hash where
possible.

The system should distinguish between:

- Duplicate URL
- Duplicate file
- Different scan of the same source
- Different edition or revision
- Derivative copy
- Cropped or edited copy
- Independent source

Multiple URLs hosting the same file must not be counted as independent
support for a fact.

## Citation Requirements

A citation should identify the smallest useful evidence location.

Examples:

- PDF file and page
- Drawing book and sheet number
- Photograph identifier
- Archive reference
- Video file and timestamp
- Audio file and timestamp
- Web page and access date

A fact should not be marked verified solely because the same uncited
statement appears repeatedly.

## Confidence and Verification

Confidence should reflect evidence quality and support, not model
certainty alone.

The current fact-verification implementation uses source-count rules:

- 0 source records: claim, confidence 50
- 1 source record: supported, confidence 70
- 2 source records: well_supported, confidence 85
- 3 or more source records: verified, confidence 95

These values are operational defaults, not universal historical truth.

Future verification must also account for:

- Source independence
- Source priority
- Source authenticity
- Directness of evidence
- Date relevance
- Contradictions
- Duplicate or derivative evidence
- Human review

Several pages from the same document may strengthen localisation but do
not necessarily represent several independent sources.

## Contradictory Evidence

Contradictory claims must not be silently overwritten.

The system should preserve:

- Each claim
- Each supporting source
- Each source date
- Each confidence level
- The nature of the contradiction
- Human review notes
- The currently preferred interpretation, if one exists

A disputed claim should remain marked as disputed until the conflict is
resolved or adequately explained.

## OCR Standards

OCR output is an interpretation of a source image, not the source itself.

The system must preserve a link from OCR-derived text and facts back to:

- The original file
- The page or image
- The OCR method
- The extraction confidence where available

OCR errors must be normalised or rejected before facts enter the
knowledge graph.

Technical identifiers such as column types, drawing numbers, elevations,
dates, and section references require additional validation because OCR
may confuse letters, numbers, punctuation, and spacing.

## Artificial Intelligence Standards

AI models may assist with:

- Relevance assessment
- Classification
- OCR interpretation
- Entity extraction
- Fact extraction
- Document summaries
- Relationship suggestions
- Image interpretation
- Drawing interpretation
- Contradiction detection
- Research assistance

AI-generated output must be labelled according to its role.

The system must distinguish between:

- Directly extracted evidence
- Deterministic rule output
- AI-assisted extraction
- AI-generated suggestion
- Human-reviewed conclusion

AI-generated text must not be treated as independent supporting evidence.

AI-derived facts and relationships must retain citations to the original
evidence used as input.

AI must not create missing dates, dimensions, names, locations, or
relationships merely to complete a record.

## Reconstruction Evidence Status

Every digital-twin element should carry an evidence status.

Recommended statuses:

### Verified

Direct and sufficiently strong evidence supports the element.

### Well Supported

Multiple supporting observations or strong evidence support the element,
but some uncertainty remains.

### Supported

At least one relevant source supports the element.

### Provisional

Evidence exists, but important details remain unresolved.

### Inferred

The element is based on reasoned interpretation rather than direct
evidence.

### Disputed

Available evidence supports conflicting interpretations.

### Unknown

There is insufficient evidence for a responsible reconstruction.

## Human Review

Human review is required before:

- A disputed claim is resolved
- An inferred reconstruction is presented as verified
- An AI-generated relationship is promoted to authoritative knowledge
- Conflicting measurements are consolidated
- A source is declared authentic when authenticity is uncertain
- A high-impact digital-twin element is finalised without direct evidence

Human review decisions should be documented and retain links to the
evidence considered.

## Rights and Responsible Use

The system should record copyright, licence, public-domain status, access
restrictions, and permitted uses where known.

Automated discovery does not automatically grant permission to download,
republish, modify, or distribute a source.

The acquisition system should respect:

- Source terms
- Access controls
- Copyright
- Archive restrictions
- Rate limits
- Robots and crawling policies where applicable

## Minimum Acceptance Standard

Evidence may enter the discovery and review queues with incomplete
metadata.

Evidence should not be promoted to verified reconstruction support
unless the system can identify:

1. What the source is
2. Where the relevant evidence appears
3. What claim the evidence supports
4. How the evidence was interpreted
5. The confidence and verification status
6. Any important uncertainty or contradiction
