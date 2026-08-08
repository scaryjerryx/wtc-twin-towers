# Known Facts and Baseline Claims

## Purpose

This document records selected human-reviewed baseline claims and canonical terminology used by the World Trade Center Evidence Engine.

This document is not a replacement for the PostgreSQL facts, citations, and provenance tables.

The database remains the machine-readable source of truth for extracted evidence.

Entries in this document must be classified as one of the following:

- Verified fact
- Well-supported claim
- Supported claim
- Unverified seed claim
- Disputed claim
- Open research question

A statement must not be classified as verified unless supporting evidence and citations have been recorded.

## Evidence Requirements

Every verified or supported entry should include, where available:

- Canonical statement
- Status
- Confidence
- Applicable historical period
- Supporting source
- Source identifier
- File or archive reference
- Page, sheet, image, frame, or timestamp
- Review date
- Review notes

Missing information must remain unknown.

Missing dates, names, dimensions, roles, and relationships must not be invented.

## Relationship to the Database

This document contains only selected baseline knowledge needed for:

- Canonical terminology
- Entity-alias seeding
- Development tests
- Human-reviewed reference points
- Open research questions
- Disputed-claim tracking

The complete evidence record belongs in:

- `entities`
- `entity_aliases`
- `facts`
- `fact_sources`
- `citations`
- `relationships`

## Canonical Terminology

### North Tower

Canonical name:

`North Tower`

Known aliases:

- `WTC 1`
- `WTC1`
- `World Trade Center 1`
- `Tower 1`
- `1 World Trade Center`

Status:

**Unverified seed claim pending citation review**

Canonical seed statement:

The North Tower is also identified as WTC 1 and 1 World Trade Center.

Supporting evidence:

Not yet recorded in this document.

Required review:

- Confirm terminology against an authoritative source
- Record the applicable historical period
- Add a citation
- Confirm the canonical format used by the database

### South Tower

Canonical name:

`South Tower`

Known aliases:

- `WTC 2`
- `WTC2`
- `World Trade Center 2`
- `Tower 2`
- `2 World Trade Center`

Status:

**Unverified seed claim pending citation review**

Canonical seed statement:

The South Tower is also identified as WTC 2 and 2 World Trade Center.

Supporting evidence:

Not yet recorded in this document.

Required review:

- Confirm terminology against an authoritative source
- Record the applicable historical period
- Add a citation
- Confirm the canonical format used by the database

## Architectural Attribution

### Minoru Yamasaki Attribution

Seed claim:

Minoru Yamasaki is identified as an architect associated with the original World Trade Center project.

Status:

**Unverified seed claim pending role and citation review**

Confidence:

Not assigned

Supporting evidence:

Not yet recorded in this document.

Required clarification:

- Confirm the precise professional role
- Identify the architectural firm
- Identify associated architects and organisations
- Distinguish individual attribution from firm attribution
- Record an authoritative source
- Add a citation

The engine must not reduce a complex project team to one person without preserving the roles of relevant firms, engineers, authorities, contractors, consultants, and associated architects.

## Completion and Opening Dates

### 1973 Completion Claim

Original seed claim:

`Completed: 1973`

Status:

**Ambiguous and unverified**

Reason:

The original statement does not identify what was completed or what historical milestone the year represents.

Possible interpretations requiring separate research include:

- Completion of one tower
- Completion of both towers
- Completion of major construction
- Formal dedication
- Public opening
- Completion of the wider complex
- Completion of a particular project phase

Required action:

Do not promote this statement to a verified fact until:

1. The event is precisely defined
2. The relevant building or project scope is identified
3. The date is supported by authoritative evidence
4. The evidence is cited
5. Conflicting dates are preserved and explained

## Floor Count

### 110 Floors Per Tower Claim

Seed claim:

The North Tower and South Tower each had 110 floors.

Status:

**Unverified seed claim pending citation review**

Confidence:

Not assigned

Supporting evidence:

Not yet recorded in this document.

Required clarification:

- Confirm whether the count refers to occupied floors, numbered floors, structural levels, or another convention
- Confirm whether mechanical and basement levels are included
- Record an authoritative citation
- Preserve any source-specific counting differences

## Verified Facts

No facts are currently classified as verified in this document.

A fact may be moved into this section only after supporting evidence and citations have been recorded and reviewed.

## Well-Supported Claims

No claims are currently classified as well supported in this document.

## Supported Claims

No claims are currently classified as supported in this document.

## Unverified Seed Claims

Current unverified seed claims include:

1. North Tower is associated with WTC 1 and 1 World Trade Center
2. South Tower is associated with WTC 2 and 2 World Trade Center
3. Minoru Yamasaki is associated architecturally with the original World Trade Center project
4. The year 1973 represents an important completion or opening milestone
5. The North Tower and South Tower each had 110 floors

These statements must not be treated as verified solely because they appear in this file.

## Disputed Claims

No disputed claims are currently recorded.

When a disputed claim is added, preserve:

- Every version of the claim
- Supporting evidence for each version
- Relevant dates
- Source priority
- Confidence
- Human-review notes
- Current preferred interpretation, if justified
- Unresolved status where appropriate

## Open Research Questions

Current research questions include:

1. What authoritative terminology should be used for WTC 1 and WTC 2 across different historical periods?
2. What was the precise architectural role of Minoru Yamasaki and the associated architectural organisations?
3. Which specific event or project milestone is represented by the year 1973?
4. How should the tower floor count be defined and cited?
5. Which source should serve as the canonical reference for building aliases?
6. Which historical facts should be selected as the initial verified baseline for the engine?
7. How should date-dependent changes to buildings and spaces be represented?

## Entry Template

Use the following format for future entries:

### Fact or Claim Title

Canonical statement:

`Write the precise statement here.`

Status:

`Verified, well supported, supported, unverified seed claim, disputed, or open question`

Confidence:

`Numeric confidence or not assigned`

Applicable period:

`Date, date range, historical phase, or unknown`

Entities:

- `Canonical entity name`

Supporting evidence:

1. Source organisation:
2. Source title:
3. Source identifier:
4. Original URL or archive reference:
5. Local file or R2 object:
6. Page, sheet, image, frame, or timestamp:
7. Citation type:
8. Evidence description:

Contradictory evidence:

`Record conflicting evidence or state none known.`

Review date:

`YYYY-MM-DD`

Reviewed by:

`Reviewer or review process`

Notes:

`Interpretation, limitations, and remaining questions.`

## Promotion Rules

An entry may be promoted from an unverified seed claim only when:

1. The statement is precise
2. The relevant entities are identified
3. The applicable historical period is identified
4. Supporting evidence is recorded
5. A useful citation location is recorded
6. Duplicate or derivative sources are identified
7. Contradictions are preserved
8. Confidence is assigned
9. The verification status is justified
10. Human review is completed where required

## AI Use

AI may help locate, organise, compare, or summarise evidence relating to these claims.

AI output is not independent historical evidence.

An AI-generated answer must not promote an entry to verified status without cited supporting evidence and appropriate review.