# Historical Timeline Experience

## Date: August 11, 2026

## Purpose

This document defines the Historical Timeline Experience — the time-release system through which the public experiences the World Trade Center as a construction journey rather than a completed timeline.

---

## 1. Core Concept

The public should NOT initially receive the completed World Trade Center.

Instead, the World Trade Center should be experienced as a **construction journey** — the complex being built over time, year by year, as it was historically constructed.

Internally, the complete world may already exist. Publicly, only currently released years are accessible.

---

## 2. Release Schedule

### 2.1 Construction Era (1966-1973)

| Public Day | Historical Year | Content Unlocked |
|------------|----------------|------------------|
| Day 1 | 1966 | Site preparation, foundation excavation, slurry wall construction |
| Day 2 | 1967 | Steel erection begins, Tower A base, Tower B foundation |
| Day 3 | 1968 | Tower A rising (floors 1-30), Tower B steel begins |
| Day 4 | 1969 | Tower A (floors 30-60), Tower B (floors 1-30), facade begins |
| Day 5 | 1970 | Tower A topped out, Tower B (floors 30-60), plaza construction |
| Day 6 | 1971 | Tower B topped out, facade installation, mechanical systems |
| Day 7 | 1972 | Interior completion, elevator installation, tenant fit-out |
| Day 8 | 1973 | Official opening, full complex operational |

### 2.2 Operational Era (1973-1993)

| Public Day | Historical Year | Content Unlocked |
|------------|----------------|------------------|
| Day 9 | 1974 | Early operations, initial tenant occupancy |
| Day 10 | 1975 | Full tenant occupancy, Windows on the World construction |
| Day 11 | 1976 | Windows on the World opens |
| Day 12-28 | 1977-1992 | Operational era, tenant changes, modifications |
| Day 29 | 1993 | Post-1993 bombing repairs and modifications |

### 2.3 Final Era (1993-2001)

| Public Day | Historical Year | Content Unlocked |
|------------|----------------|------------------|
| Day 30-34 | 1994-2000 | Modified operational era |
| Day 35 | 2001 | Final state of the complex |

### 2.4 Post-Day-35

After reaching 2001, the full timeline unlocks as a permanent historical archive. Users may freely explore 1966 through 2001.

---

## 3. Timeline Rules

### 3.1 Access Rules

| Rule | Description |
|------|-------------|
| **Forward Lock** | Users cannot access years beyond the current public release |
| **Backward Travel** | Users can always revisit previously released years |
| **State Comparison** | Users can compare any two released years side by side |
| **Archive Mode** | After Day 35, all years become permanently accessible |

### 3.2 User Permissions

| Action | Allowed? |
|--------|----------|
| View current public year | ✅ Yes |
| View any previously released year | ✅ Yes |
| Compare two released years | ✅ Yes |
| View unreleased future years | ❌ No |
| Access archive (post-Day-35) | ✅ Yes |

### 3.3 Internal vs Public State

| State | Description |
|-------|-------------|
| **Internal Complete** | The full 1966-2001 world model may exist internally |
| **Public Released** | Only years up to the current public day are accessible |
| **Public Locked** | Future years exist but are not publicly accessible |

---

## 4. Construction Visualization

### 4.1 Construction States

Each year shows the complex in its historically accurate construction state:

| Year | Tower A | Tower B | Plaza | Concourse |
|------|---------|---------|-------|-----------|
| 1966 | Not started | Not started | Not started | Excavation |
| 1967 | Foundation | Not started | Not started | Foundation |
| 1968 | Floors 1-30 | Foundation | Not started | Structure |
| 1969 | Floors 30-60 | Floors 1-30 | Not started | Structure |
| 1970 | Topped out | Floors 30-60 | Construction | Structure |
| 1971 | Facade | Topped out | Construction | Fit-out |
| 1972 | Interior | Facade | Construction | Fit-out |
| 1973 | Complete | Complete | Complete | Complete |

### 4.2 Construction Elements

Long-term vision for construction-era visualization:

- **Cranes** — Tower cranes at appropriate positions and heights
- **Steel erection** — Partially completed structural frames
- **Concrete placement** — Floor slab construction sequences
- **Facade installation** — Progressive exterior wall completion
- **Construction staging** — Material storage, temporary structures
- **Construction elevators** — External hoists during construction
- **Worker presence** — Stylized representation (not individual people)

### 4.3 Visual Transitions

When users change years:

- Construction progress animates (buildings rise, facades complete)
- New elements appear as they were historically constructed
- Removed elements disappear as they were historically demolished
- Modified elements transition between states

---

## 5. User Experience

### 5.1 Timeline Interface

The timeline interface includes:

- **Year Display** — Current year prominently shown
- **Timeline Scrubber** — Slider or selector for year navigation
- **Construction Progress** — Visual indicator of completion percentage
- **Event Markers** — Key milestones on the timeline
- **Lock Indicators** — Visual indication of locked future years

### 5.2 Navigation Flow

1. User arrives at the current public year
2. User explores the complex in 3D
3. User opens the timeline panel
4. User selects a different year
5. The world transitions to that year's state
6. User explores the complex as it existed in that year

### 5.3 Discovery Experience

The time-release model creates a discovery experience:

- **Day 1:** Users see only the excavation site
- **Day 8:** Users see the completed complex for the first time
- **Day 35:** Users see the final state

Each day brings anticipation. What will be revealed next?

---

## 6. Historical Accuracy

### 6.1 Evidence Requirements

Each construction state must be supported by evidence:

| Construction Element | Evidence Type |
|---------------------|---------------|
| Steel erection sequence | Construction photos, NCSTAR reports |
| Facade installation progress | Construction photos |
| Concrete placement | Construction photos, engineering reports |
| Crane positions | Construction photos, site plans |
| Interior completion | Architectural drawings, photos |
| Tenant fit-out | Leasing records, architectural drawings |

### 6.2 Uncertainty Handling

Where exact construction dates are unknown:

- Use date ranges (e.g., "1968-1969")
- Mark as "Approximate" with lower confidence
- Show alternative states where evidence conflicts
- Allow users to see uncertainty indicators

### 6.3 Evidence Citation

Each construction state links to supporting evidence:

```
State: Tower A, 1969 (Floors 30-60 under construction)
  → Evidence: Construction photo NCSTAR_1-8_Appendix_D-G_-042.ppm
    → Source: NCSTAR 1-8 Visual Evidence Collection
      → Confidence: Verified (95%)
```

---

## 7. Technical Implementation

### 7.1 State Management

Each element in the World Model has historical states:

```json
{
  "element_id": "tower_a_floor_50",
  "states": [
    {"year": 1966, "status": "not_constructed"},
    {"year": 1967, "status": "not_constructed"},
    {"year": 1968, "status": "not_constructed"},
    {"year": 1969, "status": "under_construction"},
    {"year": 1970, "status": "completed"},
    {"year": 1973, "status": "operational"},
    {"year": 2001, "status": "final"}
  ]
}
```

### 7.2 Year Transitions

When the user changes years:

1. Query World Model for all elements at the selected year
2. Determine which elements appear, disappear, or change
3. Animate transitions for changed elements
4. Update the 3D scene
5. Update the timeline UI

### 7.3 Performance Optimization

- Pre-compute year states for fast switching
- Use level-of-detail for distant elements
- Cache frequently accessed years
- Stream construction animations progressively

---

## 8. Public Release Strategy

### 8.1 Daily Release Model

The 35-day release schedule creates:

- **Anticipation** — Users return daily to see new content
- **Discovery** — Each day reveals new parts of the complex
- **Education** — Users learn construction history chronologically
- **Community** — Shared experience of watching the complex rise

### 8.2 Content Cadence

| Phase | Days | Content Type |
|-------|------|-------------|
| Foundation | Days 1-2 | Site preparation, excavation |
| Steel Erection | Days 2-6 | Towers rising |
| Completion | Days 6-8 | Facade, interiors, opening |
| Operations | Days 9-28 | Tenant occupancy, changes |
| Modifications | Day 29 | Post-1993 repairs |
| Final | Days 30-35 | Final operational era |

### 8.3 Archive Mode

After Day 35:

- All years permanently accessible
- Full timeline scrubber available
- Construction journey replayable
- Historical archive mode for research

---

## 9. Future Extensions

### 9.1 Pre-Construction Era

Future phases may include:

- Pre-1966 site conditions
- Radio Row and existing buildings
- Demolition and site clearance
- Political and planning history

### 9.2 Tenant History Layer

Future phases may include:

- Company occupancy timelines
- Floor-by-floor tenant changes
- Notable tenants and organizations
- Leasing history

### 9.3 Human Stories Layer

Future phases may include:

- Oral histories from construction workers
- Tenant and visitor memories
- Community stories
- Memorial information

However, these are secondary to the physical reconstruction.

---

## 10. Success Criteria

The Historical Timeline Experience is successful when:

1. Users experience the WTC as a construction journey, not a static model
2. Each year's state is historically accurate and evidence-backed
3. Users can travel freely between released years
4. Construction progress is visually clear and educational
5. The time-release model creates anticipation and discovery
6. After Day 35, the full archive is permanently accessible
7. Evidence citations are available for every construction state

---

**Document prepared:** August 11, 2026  
**Status:** ✅ STRATEGIC EXPERIENCE DOCUMENT