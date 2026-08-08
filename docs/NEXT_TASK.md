NEXT TASK:
Build entity_resolver.py

PURPOSE:

Link extracted facts to actual entities.

CURRENT:

Facts are stored with:
entity_id = NULL

TARGET:

World Trade Center
    ↓
Referenced year 1976

Windows on the World
    ↓
Opened in 1976

RESULT:

Knowledge graph begins forming from evidence.

NEXT TASK:
Build automated evidence harvester.

Goal:
Automatically discover, download, classify, and queue evidence files.

Inputs:
- targets.json
- known archive URLs
- search terms
- source domains

Outputs:
- discovered_urls
- discovery_queue
- downloaded assets
- R2 objects
- assets table records
- processing queue entries

NEXT TASK:
Reconnect automated evidence discovery and downloader to the master engine runner.

Goal:
Use the existing agents/discovery and agents/downloader systems instead of creating a duplicate acquisition layer.

Flow:
sources.json
    ↓
discovery candidates
    ↓
promoted discoveries
    ↓
discovery_queue
    ↓
downloader
    ↓
R2 / assets
    ↓
processing queues
    ↓
knowledge engine

# NEXT TASK

## Reconnect Existing Automated Evidence Gathering

Do not create a new acquisition system.

Use existing folders:

- agents/discovery/
- agents/downloader/

Goal:

Understand and complete the existing automated evidence gathering pipeline.

Expected flow:

sources.json
    ↓
sources table
    ↓
search candidates
    ↓
discoveries
    ↓
discovery queue
    ↓
downloader
    ↓
R2 / assets table
    ↓
processing queues
    ↓
knowledge engine

Rules:

- Inspect before editing.
- One file at a time.
- No duplicate acquisition system.
- Full replacement files only when needed.
- Commit after every working milestone.