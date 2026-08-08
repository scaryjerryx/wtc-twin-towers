# Evidence Source Registry

## Purpose

This document records known and potential evidence sources for the World Trade Center Evidence Engine.

The registry supports:

- Automated evidence discovery
- Source-specific search generation
- Manual research
- Source evaluation
- Acquisition planning
- Rights and access review
- Provenance
- Citation creation

This document is a source-planning registry.

The PostgreSQL `sources` table remains the machine-readable source registry used by the discovery engine.

A source appearing in this document must not automatically be treated as approved for unrestricted crawling, downloading, reuse, or publication.

## Source Status Definitions

Each source should use one of the following statuses:

- **Approved**: Reviewed and permitted for the stated acquisition method
- **Approved with Restrictions**: Usable only under recorded conditions
- **Under Review**: Potentially useful, but access, rights, or technical behaviour requires review
- **Manual Research Only**: Suitable for human research but not automated acquisition
- **Blocked**: Must not be accessed automatically
- **Inactive**: Previously considered but not currently used
- **Unknown**: Not yet assessed

## Trust and Evidence Roles

Source organisations and platforms must not be assigned universal trust.

A source may be authoritative for one type of claim and weak for another.

For example:

- An archive catalogue may be authoritative for collection identifiers
- An engineering drawing may document design intent
- A construction photograph may document installed conditions
- A contemporary photograph may document appearance at a specific date
- A secondary publication may provide useful context but require citation verification
- A user-uploaded image may provide a research lead but require authenticity review

Every acquired item must be evaluated according to `docs/EVIDENCE_STANDARDS.md`.

## Required Source Fields

Each source entry should preserve, where available:

- Source name
- Canonical name
- Organisation
- Source category
- Base URL
- Search URL or access point
- Geographic scope
- Historical scope
- Expected evidence types
- Access method
- Authentication requirements
- API availability
- Robots or crawling-policy status
- Rate-limit requirements
- Copyright or rights notes
- Download permissions
- Reuse permissions
- Citation requirements
- Automation status
- Review status
- Last review date
- Technical notes
- Research notes

Missing information must remain unknown.

## Automation Rules

Before a source is enabled for automated discovery or downloading:

1. Confirm the source URL
2. Confirm the source is relevant
3. Review access requirements
4. Review terms and rights restrictions
5. Review robots or crawling policies where applicable
6. Establish a conservative request rate
7. Confirm whether an API, export, or search endpoint is available
8. Define permitted evidence types
9. Define URL normalisation rules
10. Define duplicate handling
11. Test with one controlled search
12. Test with one controlled download where permitted
13. Record the result
14. Require approval before scaling

Automated discovery does not automatically grant permission to download or republish evidence.

## Machine-Readable Registry

The current repository contains:

- `agents/discovery/sources.json`

The discovery audit must determine:

- Whether every JSON source has a corresponding entry in this document
- Whether every documented source has a machine-readable entry
- Whether names and URLs agree
- Whether duplicate source records exist
- Whether source identifiers remain stable
- Whether the database enforces source uniqueness
- Whether enabled and disabled statuses are supported
- Whether source restrictions can be represented

Do not rewrite `sources.json` until the existing discovery system has been audited.

# Priority Source Registry

## Library of Congress

### Registry Information

Canonical name:

`Library of Congress`

Organisation:

Library of Congress

Source category:

Government archive and national library

Status:

**Under Review**

Expected evidence types:

- Photographs
- Architectural records
- Maps
- Publications
- Newspapers
- Prints
- Drawings
- Catalogue records
- Historical metadata

Potential evidence value:

- Original or contemporary photographic records
- Published material
- Collection metadata
- Archive identifiers
- Historical maps and prints

Preferred access method:

- Official search interface
- Official API or structured data where available
- Controlled manual research
- Permitted direct file access

Required review:

- Confirm relevant World Trade Center collections
- Confirm API or search endpoints
- Confirm item-level rights statements
- Confirm download permissions
- Establish rate limits
- Record citation format
- Test one controlled discovery path

Automation status:

**Not yet approved for production harvesting**

## Internet Archive

### Registry Information

Canonical name:

`Internet Archive`

Organisation:

Internet Archive

Source category:

Digital archive platform

Status:

**Under Review**

Expected evidence types:

- Books
- Reports
- Scanned documents
- Audio
- Video
- Web captures
- Publications
- Metadata records

Potential evidence value:

- Digitised historical publications
- Archived reports
- Historical audio and video
- Captured websites
- Searchable metadata

Important limitations:

- Items may have different uploaders and rights conditions
- Metadata quality may vary
- Duplicate or derivative copies may exist
- An archived copy is not automatically an independent source
- Uploaded material may require authenticity review

Required review:

- Confirm permitted API or metadata access
- Confirm item-level rights information
- Define duplicate handling
- Define collection and identifier preservation
- Establish conservative rate limits
- Test one controlled discovery and download path

Automation status:

**Not yet approved for production harvesting**

## NIST Archives and Publications

### Registry Information

Canonical name:

`National Institute of Standards and Technology`

Known abbreviation:

`NIST`

Source category:

Government technical documentation

Status:

**Under Review**

Expected evidence types:

- Technical reports
- Engineering analysis
- Investigation records
- Supporting documents
- Photographs
- Data files
- Publication metadata

Potential evidence value:

- Structural and engineering context
- Technical terminology
- Official report identifiers
- Referenced source material
- Building-system information

Important limitations:

- Later investigative material must be distinguished from original design and construction records
- A report may describe conditions for a specific research purpose
- Referenced source documents may be more direct evidence than the report itself

Required review:

- Identify relevant official repositories
- Confirm file-access patterns
- Record report and document identifiers
- Confirm reuse conditions
- Test one controlled document-discovery path

Automation status:

**Not yet approved for production harvesting**

## Port Authority of New York and New Jersey

### Registry Information

Canonical name:

`Port Authority of New York and New Jersey`

Known abbreviations:

- `Port Authority`
- `PANYNJ`

Source category:

Official institutional source

Status:

**Under Review**

Expected evidence types:

- Official publications
- Planning records
- Construction records
- Reports
- Operational documents
- Photographs
- Maps
- Tenant information
- Public information material

Potential evidence value:

- Official terminology
- Project dates
- Building operations
- Complex organisation
- Tenant and space information
- Planning and construction context

Required review:

- Identify public archive and publication access points
- Identify collection references
- Confirm automated-access permissions
- Confirm citation requirements
- Record rights restrictions
- Test a controlled search

Automation status:

**Not yet approved for production harvesting**

## Wikimedia Commons

### Registry Information

Canonical name:

`Wikimedia Commons`

Organisation:

Wikimedia Foundation and contributing communities

Source category:

Media repository

Status:

**Under Review**

Expected evidence types:

- Photographs
- Diagrams
- Maps
- Scanned publications
- Video
- Audio
- Structured metadata

Potential evidence value:

- Historical exterior photographs
- Interior photographs
- Construction photographs
- Maps
- Media metadata
- Licence information
- Source links

Important limitations:

- File descriptions and categories may contain errors
- Original-source links must be preserved
- User uploads require authenticity review
- Multiple files may be derivatives of the same original
- Licence and attribution requirements vary by file

Required review:

- Confirm API usage
- Preserve original file page and uploader metadata
- Preserve licence and attribution
- Preserve original-source claims
- Define derivative-file detection
- Test one controlled API search

Automation status:

**Not yet approved for production harvesting**

## Flickr Commons

### Registry Information

Canonical name:

`Flickr Commons`

Source category:

Institutional photographic collections hosted on Flickr

Status:

**Under Review**

Expected evidence types:

- Historical photographs
- Collection metadata
- Institutional descriptions
- Dates
- Tags
- Album and collection context

Potential evidence value:

- Construction photographs
- Contemporary photographs
- Institutional photo collections
- Visual evidence of spaces and materials

Important limitations:

- Flickr Commons institutional records must be distinguished from ordinary user uploads
- Collection descriptions may be incomplete
- Image rights and reuse conditions must be recorded
- Original institutional identifiers should be preserved

Required review:

- Identify participating institutions with relevant collections
- Confirm API access
- Preserve institution and collection identifiers
- Confirm image-download policy
- Confirm rights statements
- Test one controlled discovery process

Automation status:

**Not yet approved for production harvesting**

## Engineering and Architectural Journals

### Registry Information

Canonical category:

`Engineering and Architectural Journals`

Source category:

Professional and technical publications

Status:

**Manual Research Only until individual sources are reviewed**

Expected evidence types:

- Engineering articles
- Architectural articles
- Construction reports
- Technical diagrams
- Project descriptions
- Structural analysis
- Material specifications
- Professional commentary

Potential evidence value:

- Contemporary design descriptions
- Engineering terminology
- Construction methods
- Structural systems
- Drawings and diagrams
- Project-team attribution

Important limitations:

- Access and copyright conditions vary by publication
- Paywalled material must not be bypassed
- Articles may describe design intent rather than as-built conditions
- Secondary summaries should be traced to primary records where possible

Required review:

Each journal or database must receive its own source entry before automation.

Automation status:

**Not approved as a general automated source category**

## Construction Archives

### Registry Information

Canonical category:

`Construction Archives`

Source category:

Archive category requiring source-specific registration

Status:

**Manual Research Only until individual archives are identified**

Expected evidence types:

- Construction photographs
- Contractor records
- Shop drawings
- Progress reports
- Material records
- Correspondence
- Inspection records
- Project schedules

Potential evidence value:

- Construction sequence
- Installed conditions
- Contractor roles
- Materials
- Revisions
- As-built evidence

Important limitations:

`Construction Archives` is not a single source.

Every archive, collection, company record, or institutional repository must be registered separately with a stable source identifier.

Automation status:

**Not approved as a general source**

# Additional Source Categories Requiring Research

Potential future source categories include:

- Municipal archives
- State archives
- Federal archives
- University collections
- Museum collections
- Architectural firm archives
- Engineering firm archives
- Contractor archives
- Historical societies
- Library special collections
- Newspaper archives
- Television archives
- Documentary collections
- Oral-history collections
- Trade publications
- Patent and product catalogues
- Transit-agency records
- Tenant publications
- Public brochures and guidebooks
- Personal photographic collections

Each specific source must be reviewed and registered before automated acquisition.

# Rejected or Blocked Sources

No sources are currently documented as permanently blocked.

If a source is blocked, record:

- Source name
- URL
- Date blocked
- Reason
- Access or rights concern
- Technical concern
- Review decision
- Conditions for reconsideration

# Source Entry Template

Use the following template for each future source:

## Source Name

Canonical name:

`Canonical source name`

Organisation:

`Organisation name`

Source category:

`Government archive, institutional archive, media repository, publication, or other category`

Database source identifier:

`Identifier or not yet assigned`

Base URL:

`URL`

Search or API endpoint:

`URL or unknown`

Status:

`Approved, approved with restrictions, under review, manual research only, blocked, inactive, or unknown`

Expected evidence types:

- `Evidence type`

Historical scope:

`Scope or unknown`

Geographic scope:

`Scope or unknown`

Access method:

`API, search page, catalogue, manual research, or other`

Authentication:

`Required, not required, or unknown`

Rights and licence notes:

`Record item-level and source-level restrictions`

Robots or crawling-policy review:

`Reviewed date and result`

Rate limit:

`Requests per time period or not yet assigned`

URL-normalisation rules:

`Rules or not yet defined`

Automation status:

`Enabled, disabled, test only, or not approved`

Last review date:

`YYYY-MM-DD`

Reviewed by:

`Reviewer or process`

Technical notes:

`Endpoints, identifiers, file patterns, redirects, or limitations`

Research notes:

`Relevant collections, search terms, and open questions`

# Current Registry Status

All currently listed sources remain under review or manual-research-only status.

No source should be enabled for uncontrolled automated harvesting based solely on its presence in this document.

The immediate discovery audit must compare this registry against:

- `agents/discovery/sources.json`
- The PostgreSQL `sources` table
- Existing discovery code
- Existing search-generation code
- Existing candidate records

Differences must be documented before source records are changed.

# Completion Criteria

The source registry is operationally complete when:

1. Every enabled discovery source has a documented registry entry
2. Every registry entry has a stable database identifier
3. Names and URLs agree across Markdown, JSON, and PostgreSQL
4. Access methods are documented
5. Rights and restrictions are documented
6. Rate limits are documented
7. Automation status is explicit
8. Source-specific tests exist
9. Duplicate source records are prevented
10. Source provenance is preserved through discovery, downloading, assets, facts, and citations