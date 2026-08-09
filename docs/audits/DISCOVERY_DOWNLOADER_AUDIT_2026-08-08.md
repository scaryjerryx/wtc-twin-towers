# Discovery and Downloader Read-Only Audit

## World Trade Center Evidence Engine

**Date:** August 8, 2026

**Status:** Read-only audit — no files, database records, or schemas were changed

**Scope:** `agents/discovery/` and `agents/downloader/`

---

## 1. Executive Summary

The discovery and downloader layers exist as foundations only. They are **not** an operational end-to-end automated evidence-gathering pipeline.

The repository contains the documented file structure, but the code does not implement the documented flow:

```
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
Validation and Deduplication
↓
R2 Storage
↓
Asset Registration
↓
Metadata and Processing Queues
↓
Classification and Routing
↓
Existing Processing and Knowledge Engine
```

The highest-severity blockers are:

1. `agents/discovery/main.py` uses an unqualified import (`from database import get_db_connection`) that is not package-safe; it may resolve under direct script execution (`python agents/discovery/main.py`) but fails or is unreliable under the preferred package invocation (`python -m agents.discovery.main`).
2. `agents/discovery/find_candidates.py` is a hollow stub that performs no actual discovery.
3. `agents/discovery/discover.py` fabricates `https://example.com/` URLs and inserts them into `discovery_queue`, violating evidence rules.
4. `agents/run_pipeline.py` invokes the downloader in script mode, which is incompatible with the downloader's package-qualified import — the pipeline crashes on first run.
5. The downloader has no HTTP status validation, no content-type validation, no file hashing, no deduplication, no error handling, no retry, and no metadata/processing-queue handoff.
6. No URL normalisation or file-hash deduplication exists anywhere in the acquisition path.
7. The documented `discoveries` table is never written by any code.

The audit confirms the documentation's assessment: these components are marked "Requires Verification" and must be repaired and tested before the pipeline can be marked working.

---

## 2. Audit Scope and Method

### Files Read Completely

**Discovery layer (`agents/discovery/`):**

- `__init__.py`
- `database.py`
- `main.py`
- `build_searches.py`
- `build_real_searches.py`
- `find_candidates.py`
- `promote_searches.py`
- `manual_promote.py`
- `discover.py`
- `queue_discoveries.py`
- `export_candidates.py`
- `export_discoveries.py`
- `requirements.txt`
- `sources.json`

**Downloader layer (`agents/downloader/`):**

- `__init__.py`
- `main.py`
- `r2.py`
- `test_r2.py`

**Supporting inputs read:**

- `research/targets.json`
- `research/sources.json`

**Callers inspected:**

- `agents/run_pipeline.py`
- `agents/metadata/mock_analyze.py`
- `agents/engine/run_engine.py`
- `agents/ingestion/automated_ingestion.py`

**Repository-wide import search:**

A regex search for `discovery|downloader` across all `*.py` files confirmed that no module outside the two audited directories imports discovery or downloader code, with the exception of `agents/run_pipeline.py`, which invokes the downloader via subprocess.

**Non-operations confirmation:**

- No files were edited or created during the audit.
- No PostgreSQL database was accessed or modified.
- No packages were installed.
- No evidence was downloaded.
- Nothing was uploaded to R2.
- No migrations were run.
- Nothing was committed.

---

## 3. Discovery Layer File-by-File Audit

### 3.1 `agents/discovery/__init__.py`

- **Purpose:** Python package marker.
- **Imports/dependencies:** None.
- **Tables read:** None.
- **Tables written:** None.
- **Inputs:** None.
- **Outputs:** None.
- **Files downloaded/created:** None.
- **Invocation:** Implicit at package import.
- **Expected execution order:** N/A.
- **Package-import safety:** Safe (empty file).
- **Status:** Complete; standard empty package marker.
- **Error handling:** N/A.
- **Idempotency/dedup:** N/A.
- **Existing tests:** None.
- **Missing tests:** None required.

### 3.2 `agents/discovery/database.py`

- **Purpose:** Single shared PostgreSQL connection factory.
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv.load_dotenv`.
- **Tables read:** None directly.
- **Tables written:** None directly.
- **Inputs:** Environment variables `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`; host hardcoded to `"localhost"`.
- **Outputs:** `psycopg2` connection object.
- **Files downloaded/created:** None.
- **Invocation:** `get_db_connection()` — callable; currently used by only one file (`agents/discovery/main.py`).
- **Expected execution order:** N/A (helper module).
- **Package-import safety:** Safe as a module, but the only consumer imports it incorrectly (see 3.3).
- **Status:** Complete but underused — 7 other discovery files and `agents/downloader/main.py` duplicate its connection logic inline.
- **Error handling:** None (no timeout, no failure handling, no context manager).
- **Idempotency/dedup:** N/A.
- **Existing tests:** None.
- **Missing tests:** None critical; connection helper is trivial.

### 3.3 `agents/discovery/main.py` — **BROKEN IMPORT**

- **Purpose:** Seed the `sources` table from `agents/discovery/sources.json` (idempotent upsert).
- **Imports/dependencies:** `json`; `from database import get_db_connection` (**script-style, unqualified**).
- **Tables read:** None.
- **Tables written:** `sources` (INSERT … ON CONFLICT DO NOTHING).
- **Inputs:** `agents/discovery/sources.json`.
- **Outputs:** Rows in `sources`.
- **Files downloaded/created:** None.
- **Invocation:** Unspecified. When executed directly as `python agents/discovery/main.py`, the unqualified `from database import get_db_connection` may resolve because Python adds the script's directory (`agents/discovery/`) to `sys.path`. Under the preferred package invocation `python -m agents.discovery.main`, `database` is not resolvable, so the import fails or is unreliable. **The file is not package-safe.**
- **Expected execution order:** Step 1 (source seeding) in the documented flow.
- **Package-import safety:** **Unsafe — package-execution blocker.** Must become `from agents.discovery.database import get_db_connection` for consistent package-safe execution.
- **Status:** **Partial/untested**; seed logic is conceptually correct (`ON CONFLICT DO NOTHING`) but not reliably executable under the preferred package invocation.
- **Error handling:** None; a failed insert aborts the whole run.
- **Idempotency:** Partial — `ON CONFLICT DO NOTHING` prevents duplicate source rows, but only if a unique constraint on `name`/`url` exists (schema audit must confirm).
- **Existing tests:** None.
- **Missing tests:** Source-seeding idempotency test (run twice, confirm no duplicates).

### 3.4 `agents/discovery/build_searches.py` — **LEGACY/DUPLICATED**

- **Purpose:** Insert search URLs into `search_history` for every `(source, target)` pair.
- **Imports/dependencies:** `json`, `os`, `urllib.parse`, `psycopg2`, `dotenv`; inline connection (duplicates `database.py`).
- **Tables read:** None.
- **Tables written:** `search_history` (no dedup clause).
- **Inputs:** `research/targets.json` + `research/sources.json`.
- **Outputs:** `search_history` rows.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script only.
- **Expected execution order:** Search-definition generation.
- **Package-import safety:** No internal imports; runs only as a script. No `__main__` guard.
- **Status:** **Duplicated/legacy candidate.** Writes `search_history`, a table that appears nowhere in the documented flow (`sources → search_candidates → discoveries → discovery_queue`). Later `promote_searches.py` consumes it.
- **Error handling:** None.
- **Idempotency:** **None** — plain INSERT; repeated runs duplicate rows.
- **Existing tests:** None.
- **Missing tests:** Search-definition deduplication test.

### 3.5 `agents/discovery/build_real_searches.py` — **DUPLICATED with 3.4, partially correct target table**

- **Purpose:** Insert search URLs into `search_candidates` for three hardcoded sources (Library of Congress, Internet Archive, Wikimedia Commons) across all `research/targets.json` targets.
- **Imports/dependencies:** `json`, `urllib.parse`, `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** None.
- **Tables written:** `search_candidates` (plain INSERT).
- **Inputs:** `research/targets.json`; three hardcoded source tuples (does **not** read `sources.json`).
- **Outputs:** `search_candidates` rows.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Search-candidate creation.
- **Package-import safety:** No internal imports.
- **Status:** **Partial/duplicated** — overlapping responsibility with `build_searches.py`, but writes the correct documented table (`search_candidates`). Hardcoded source URLs contradict the "configured sources" model.
- **Error handling:** None.
- **Idempotency:** **None** — plain INSERT; repeated runs duplicate candidates. A candidate uniqueness constraint is required (schema audit).
- **Existing tests:** None.
- **Missing tests:** Candidate-creation deduplication test.

### 3.6 `agents/discovery/find_candidates.py` — **HOLLOW STUB**

- **Purpose:** Intended to discover candidate URLs by querying sources; **actual body only prints `"Searching: {target} from {source}"`** — no HTTP, no parsing, no database access.
- **Imports/dependencies:** `json`.
- **Tables read:** None.
- **Tables written:** None.
- **Inputs:** `research/targets.json` + `research/sources.json` (read but only for names).
- **Outputs:** None.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** After candidate generation, before promotion (documented).
- **Package-import safety:** N/A (no imports).
- **Status:** **Incomplete/obsolete stub** — performs no actual discovery. This is the largest functional gap in the discovery layer.
- **Error handling:** None.
- **Idempotency:** N/A.
- **Existing tests:** None.
- **Missing tests:** A real discovery test against one controlled source.

### 3.7 `agents/discovery/promote_searches.py` — **WRONG TABLE + DUPLICATED**

- **Purpose:** Copy `search_history` rows into `discovered_urls` (deduplicated on `discovered_url`).
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** `search_history`.
- **Tables written:** `discovered_urls`.
- **Inputs:** `search_history`.
- **Outputs:** `discovered_urls`.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Candidate promotion.
- **Package-import safety:** No internal imports.
- **Status:** **Duplicated with `manual_promote.py` and off-flow.** Documentation describes promotion as `search_candidates → discoveries`; this moves `search_history → discovered_urls` and never touches `discoveries`. It also treats a generated search URL as a "discovered URL", which is not a real evidence URL.
- **Error handling:** None.
- **Idempotency:** `ON CONFLICT (discovered_url) DO NOTHING` — partial, but depends on a unique constraint on `discovered_url`.
- **Existing tests:** None.
- **Missing tests:** Promotion deduplication and provenance-preservation test.

### 3.8 `agents/discovery/manual_promote.py` — **DUPLICATED + TEST-EVIDENCE CONCERN**

- **Purpose:** Manually insert a single hardcoded "discovery" (`Delete_key1.jpg` from Wikimedia Commons) into `discovered_urls`.
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** None.
- **Tables written:** `discovered_urls`.
- **Inputs:** Hardcoded `REAL_DISCOVERIES` list (1 item, a generic "delete key" test image URL).
- **Outputs:** `discovered_urls` row.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Manual promotion fallback.
- **Package-import safety:** No internal imports.
- **Status:** **Duplicated with `promote_searches.py`; test-only content.** The hardcoded URL is a placeholder test image — inconsistent with evidence standards (a real, permitted URL is required).
- **Error handling:** None.
- **Idempotency:** `ON CONFLICT (discovered_url) DO NOTHING` — partial.
- **Existing tests:** None.
- **Missing tests:** Manual-promotion deduplication test.

### 3.9 `agents/discovery/discover.py` — **BLOCKER: FABRICATES EVIDENCE URLs**

- **Purpose:** Intended to queue discoveries; **actual body fabricates `https://example.com/{target}` URLs** and inserts them into `discovery_queue` with `source_name = "Discovery Agent"`.
- **Imports/dependencies:** `json`, `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** None.
- **Tables written:** `discovery_queue`.
- **Inputs:** `research/targets.json` target names.
- **Outputs:** `discovery_queue` rows with **fake `target_url`s**.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Discovery creation (after promotion) — but it skips the entire `search_candidates`/`discoveries` stage.
- **Package-import safety:** No internal imports.
- **Status:** **Obsolete/unsafe.** Directly violates evidence rules ("Do not invent missing URLs / Source identifiers") and the documented flow. It bypasses candidates and discoveries entirely.
- **Error handling:** None.
- **Idempotency:** `ON CONFLICT (target_url) DO NOTHING` — partial.
- **Existing tests:** None.
- **Missing tests:** Discovery-creation provenance test.

### 3.10 `agents/discovery/queue_discoveries.py` — **SUBTLY NON-IDEMPOTENT**

- **Purpose:** Move `discovered_urls` rows with `queued = FALSE` into `discovery_queue`, then flag them queued.
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** `discovered_urls`.
- **Tables written:** `discovery_queue` + `discovered_urls (queued)`.
- **Inputs:** `discovered_urls WHERE queued = FALSE`.
- **Outputs:** `discovery_queue` rows; `queued` flag updates.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** After discovery creation, before downloader.
- **Package-import safety:** No internal imports.
- **Status:** **Partial.** Correct concept (dedup + flag), but:
  - If the queue INSERT is skipped by `ON CONFLICT DO NOTHING`, the row is still marked `queued = TRUE` — **silent data-loss path** (the URL is neither queued nor retried).
  - No transaction around the two statements (risk of partial state on crash).
- **Error handling:** None.
- **Idempotency:** Partially broken (see above).
- **Existing tests:** None.
- **Missing tests:** Queue-transition idempotency test (repeated runs remain safe).

### 3.11 `agents/discovery/export_candidates.py`

- **Purpose:** Diagnostic report — print all `search_candidates` rows.
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** `search_candidates`.
- **Tables written:** None.
- **Inputs:** None.
- **Outputs:** Console lines.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Diagnostic only.
- **Package-import safety:** No internal imports.
- **Status:** Complete but read-only diagnostic; references `ORDER BY id` (id column must exist — schema audit).
- **Error handling:** None.
- **Idempotency:** N/A (read-only).
- **Existing tests:** None.
- **Missing tests:** None critical.

### 3.12 `agents/discovery/export_discoveries.py`

- **Purpose:** Diagnostic report — print all `discovered_urls` rows.
- **Imports/dependencies:** `os`, `psycopg2`, `dotenv`; inline connection.
- **Tables read:** `discovered_urls`.
- **Tables written:** None.
- **Inputs:** None.
- **Outputs:** Console lines.
- **Files downloaded/created:** None.
- **Invocation:** Standalone script.
- **Expected execution order:** Diagnostic only.
- **Package-import safety:** No internal imports.
- **Status:** Complete but read-only diagnostic; duplicates the diagnostic responsibility of `export_candidates.py` in style.
- **Error handling:** None.
- **Idempotency:** N/A (read-only).
- **Existing tests:** None.
- **Missing tests:** None critical.

### 3.13 `agents/discovery/requirements.txt`

- **Declared dependencies:** `psycopg2-binary`, `python-dotenv`, `requests`.
- **Note:** `requests` is declared but **never used** in the discovery layer (no HTTP client exists anywhere). `urllib.parse`, `json`, and `os` are standard library.

### 3.14 `agents/discovery/sources.json`

- **Content:** 7 sources: Library of Congress, Internet Archive, Wikimedia Commons, NIST, Port Authority, Flickr Commons, **National Archives**.
- **Mismatch vs `docs/SOURCE_REGISTRY.md`:**
  - National Archives has no registry entry.
  - Names differ from canonical registry names (`NIST` vs `National Institute of Standards and Technology`; `Port Authority` vs `Port Authority of New York and New Jersey`).
  - No status, rights, rate-limit, or automation fields are represented despite the registry defining them as required.
- **Mismatch vs `research/sources.json`:** the other source config contains only 4 sources (Library of Congress, Internet Archive, Wikimedia Commons, NIST) and is what most discovery scripts actually read. **Two competing source configs exist.**

---

## 4. Downloader Layer File-by-File Audit

### 4.1 `agents/downloader/__init__.py`

- **Purpose:** Python package marker.
- **Imports/dependencies:** None.
- **Tables read/written:** None.
- **Inputs/outputs:** None.
- **Files downloaded/created:** None.
- **Invocation:** Implicit at package import.
- **Package-import safety:** Safe (empty).
- **Status:** Complete; standard empty package marker.
- **Error handling:** N/A.
- **Idempotency/dedup:** N/A.
- **Existing tests:** None.
- **Missing tests:** None.

### 4.2 `agents/downloader/main.py`

- **Purpose:** Consume one `pending` `discovery_queue` row, `requests.get` the URL, save bytes to `storage/raw/{queue_id}.jpg`, upload to R2 as `images/{queue_id}.jpg`, insert an `assets` row, mark queue `completed`.
- **Imports/dependencies:** `os`, `requests`, `psycopg2`, `dotenv`; **package-safe** `from agents.downloader.r2 import upload_file`.
- **Tables read:** `discovery_queue`.
- **Tables written:** `discovery_queue (status)`, `assets`.
- **Inputs:** 1 pending queue item.
- **Outputs:** asset row; R2 object; local `.jpg` file.
- **Files downloaded/created:** `storage/raw/{queue_id}.jpg`.
- **Invocation:** `python agents/run_pipeline.py` → `python agents/downloader/main.py`.
- **Execution blocker:** `run_pipeline.py` invokes it as a **script path** (`"python", "agents/downloader/main.py"`), but the file contains a **package-qualified import** (`agents.downloader.r2`). Under script execution, `sys.path[0]` is `agents/downloader/`, so `agents` is not importable → **ImportError at runtime.** Must be invoked as `python -m agents.downloader.main`.
- **Package-import safety:** Mixed — the import itself is package-safe, but the documented/only caller executes it in script mode. **Inconsistent invocation contract.**
- **Status:** **Partial/untested.**
- **Error handling:** **None.**
  - No `response.raise_for_status()` / HTTP status check.
  - No content-type validation (`.jpg` hardcoded regardless of actual content; `asset_type` always `"image"`).
  - No `requests` timeout.
  - No exception handling/try-except; a network failure or R2 error aborts with no queue retry/failure status.
- **Idempotency/dedup:** **None.**
  - No URL normalisation.
  - No duplicate-URL guard (relies entirely on queue `status`, which starts `'pending'`).
  - **No file hashing / hash dedup** — same file from a second URL is stored twice.
  - No retry/failure queue.
- **Missing handoff:** Does **not** create a `metadata_queue` or any processing queue entry — `agents/metadata/mock_analyze.py` therefore has nothing to consume after a successful download, breaking the `run_pipeline` chain.
- **Existing tests:** None.
- **Missing tests:** HTTP validation, content-type validation, file-hash dedup, R2 upload verification, asset-record verification, queue-transition verification.

### 4.3 `agents/downloader/r2.py`

- **Purpose:** S3-compatible R2 client + `upload_file(local_file, remote_file)`.
- **Imports/dependencies:** `os`, `boto3`, `dotenv`.
- **Tables read/written:** None.
- **Inputs:** Local file path, remote object key.
- **Outputs:** R2 object.
- **Files downloaded/created:** Uploads arbitrary local file to R2 bucket.
- **Invocation:** Imported (package-safe) by `main.py` and `test_r2.py`.
- **Expected execution order:** After download, before asset registration.
- **Package-import safety:** Safe.
- **Status:** Foundationally complete but minimal:
  - Client created at **module import time** (hard to mock/test; no dependency injection).
  - No error handling, no retry, no object-metadata preservation (content-type, hash, rights).
  - No verification/HEAD after upload.
- **Existing tests:** None automated (see 4.4).
- **Missing tests:** Mocked R2 upload test, object-key preservation test, metadata-preservation test.

### 4.4 `agents/downloader/test_r2.py`

- **Purpose:** Exercise `upload_file`.
- **Content:** Imports `upload_file` then **actually calls it with `storage/raw/3.jpg → test/3.jpg`**.
- **Status:** **Not an automated test.** Executing it performs a **live R2 upload** — unsafe to run in CI/tests, depends on real credentials, and uploads a tracked evidence image. Must be replaced with a mocked unit test.
- **Existing tests:** None (this file is the pseudo-test).
- **Missing tests:** A real mocked unit test for `upload_file`.

---

## 5. Supporting Callers Inspected

### 5.1 `agents/run_pipeline.py`

- **Purpose:** Orchestrate downloader + metadata analysis via subprocess.
- **Content:** Runs `python agents/downloader/main.py`, then `python agents/metadata/mock_analyze.py`.
- **Findings:**
  - Runs the downloader in **wrong invocation mode** (script path incompatible with package import — see 4.2).
  - Does **not** run any discovery stage, so the documented flow is unreachable through this entry point.
  - After the downloader, `metadata_queue` is never populated → `mock_analyze.py` will always find "No pending metadata items" unless rows were manually inserted.

### 5.2 `agents/metadata/mock_analyze.py`

- **Purpose:** Consume `metadata_queue` (`status='pending'`), write a mock row into `ai_analysis` (`confidence_score=50`, `analysis_json='{"agent":"mock"}'`), mark queue + asset `metadata_status='completed'`.
- **Findings:**
  - Demonstrates the expected downstream handoff table, but the downloader **never enqueues** into it.
  - Uses inline connection logic (duplicates `database.py`).

### 5.3 `agents/engine/run_engine.py`

- **Purpose:** Master Engine Runner.
- **Content:** Runs the local-PDF test harness: ingestion → citations → verification → relationships → timeline.
- **Findings:**
  - Uses correct package-qualified imports.
  - No discovery/downloader integration — consistent with documentation (must not be changed during this audit).

### 5.4 `agents/ingestion/automated_ingestion.py`

- **Purpose:** Local PDF processing test harness.
- **Content:** Reads `data/incoming_pdfs`, processes via `pdf_knowledge_pipeline`, moves to processed/failed dirs, rebuilds relationships.
- **Findings:**
  - Correctly identified as the development test harness.
  - Package-safe imports.
  - Not part of the acquisition flow.

---

## 6. Cross-Cutting Findings

### 6.1 Duplicate Responsibilities

| Responsibility | Files | Notes |
|---|---|---|
| Search generation | `build_searches.py` (→ `search_history`), `build_real_searches.py` (→ `search_candidates`) | Two parallel, incompatible search-generation paths |
| Promotion | `promote_searches.py` (→ `discovered_urls`), `manual_promote.py` (→ `discovered_urls`) | Same table, two scripts |
| Diagnostics | `export_candidates.py`, `export_discoveries.py` | Near-identical pattern |
| DB connection | `database.py` + inline connections in 8 other files | 7 discovery + 1 downloader |

### 6.2 Old Script-Style Imports

- `agents/discovery/main.py`: `from database import get_db_connection` — the unqualified import may work during direct script execution (`python agents/discovery/main.py`), but it is **not package-safe** and is **incompatible with the preferred module invocation** (`python -m agents.discovery.main`). It should use `from agents.discovery.database import get_db_connection`.
- All other discovery scripts have no internal imports and run as bare scripts with inline connections (not package-safe, no `__main__` guards).
- `agents/run_pipeline.py` invokes the downloader via script path incompatible with the downloader's package import — **execution blocker**.

### 6.3 Missing Queue Transitions

- No `sources → search_candidates` transition using the documented `sources` table and configured source records (only hardcoded or secondary JSON).
- No `search_candidates → discoveries` promotion (promote scripts target `discovered_urls`; `discoveries` table unused by all code).
- No `discoveries → discovery_queue` queueing (queue is written directly by `discover.py` — with fake URLs — or by `queue_discoveries.py` from `discovered_urls`).
- Downloader → `metadata_queue` / processing queue: **missing entirely.**

### 6.4 Missing URL Normalisation

- None anywhere. No `urllib` canonicalisation of candidate/discovery URLs; duplicate URLs can slip through as distinct strings.

### 6.5 Missing File-Hash Deduplication

- None anywhere. Downloader stores bytes with no `sha256` calculation; the same file downloaded from two URLs creates two assets.

### 6.6 Missing R2 Integration

- R2 foundation exists (`r2.py`) and is connected to the downloader (the **only** fully connected acquisition sub-step), but:
  - No error/retry handling.
  - No content-type / metadata on the S3 object.
  - Client tied to module import (untestable).
  - Callback/test file performs live uploads.

### 6.7 Missing Asset Registration

- `assets` insert exists in the downloader but is **minimal**: no file hash, no acquisition date, no source id, no classification confidence, no content type, no processing status, no R2-object metadata. Duplicate-URL reruns would create duplicate asset rows (no dedup guard).

### 6.8 Missing Metadata/Processing-Queue Handoff

- Downloader never enqueues into `metadata_queue` or any processing queue → `mock_analyze.py` and the router (`agents/router/route_asset.py`) have no operational input.

### 6.9 Mismatches with `docs/ARCHITECTURE.md` / `docs/NEXT_TASK.md`

1. Documented tables `sources`, `search_candidates`, `discoveries`, `discovery_queue`, `assets`, `metadata_queue`; code writes also to **`search_history`** and **`discovered_urls`** — two tables absent from the documented flow (must be confirmed against the live schema in Phase 2).
2. Documented promotion `candidate → discovery`; code has no `discoveries` usage at all.
3. Documented downloader responsibilities (response/content validation, hashing, dedup, retries, failure handling, queue creation) are **not implemented**.
4. `test_r2.py` listed as a "component" is a live-upload smoke script, not a test.
5. `run_pipeline.py` is an **undocumented orchestrator** whose invocation mode is broken for its own child module.

---

## 7. Confirmed Blocker Summary

| # | Blocker | Severity |
|---|---------|----------|
| B1 | `discovery/main.py` unqualified import — not package-safe; fails under `python -m agents.discovery.main` | High |
| B2 | No real discovery implementation (`find_candidates.py` is a stub; no source querying, no HTTP, no candidate URL generation from real sources) | High |
| B3 | `discover.py` fabricates `example.com` URLs — evidence-safety violation, poisons queue | High |
| B4 | `run_pipeline.py` invokes downloader in script mode, incompatible with its package import — crash on first run | High |
| B5 | Downloader lacks HTTP status, content-type, timeout, error handling, retry, failure queue | High |
| B6 | No URL normalisation or deduplication anywhere | High |
| B7 | No file-hash dedup anywhere | High |
| B8 | No metadata/processing-queue handoff from downloader | High |
| B9 | `queue_discoveries.py` marks queued even when insert was skipped (silent loss) | Medium |
| B10 | Two competing source configs (`agents/discovery/sources.json` vs `research/sources.json`) and two competing search builders | Medium |
| B11 | `discoveries` table documented but never written by any code | Medium |
| B12 | `test_r2.py` performs live uploads; no mock tests exist for any discovery/downloader file | Medium |
| B13 | No activation/approval state on sources; no rights/rate-limit metadata in code | Medium (governance) |

---

## 8. Complete Questions for the Schema Audit (Phase 2)

1. **`discoveries` table**: Does a `discoveries` table exist in `wtc_evidence`? If yes, what columns/constraints? If not, is the documented `discoveries` stage meant to be folded into `discovered_urls` or created anew?
2. **`discovered_urls` and `search_history`**: Are these real tables in the schema, and are they considered the operative discovery tables, or legacy leftovers to be migrated away?
3. **Source uniqueness**: Does `sources` enforce a unique constraint on `name` and/or `url`? (The `ON CONFLICT DO NOTHING` logic depends on it.)
4. **Candidate uniqueness**: Does `search_candidates` have a unique constraint on `(source, search_url)` or `search_url`? Without one, `build_real_searches.py` is non-idempotent.
5. **Discovery-queue uniqueness and statuses**: Does `discovery_queue` enforce unique `target_url`? What are the valid `status` values (`pending/completed/failed/retry`?), and are there `attempt_count`, `last_error`, `next_retry` columns?
6. **`assets` schema**: What are the exact columns (hash, content_type, source_id, r2_key, acquisition/processing status fields)? Is there a unique file-hash constraint?
7. **`metadata_queue` schema**: Columns and status values, and whether it links to `assets` via `asset_id` (as `mock_analyze.py` assumes).
8. **`ai_analysis` schema**: Exact columns (the mock inserts `tower/floor/area/estimated_year/confidence_score/analysis_json` — do these exist, and what is nullable/default?).
9. **Source governance fields**: Do `sources` columns support `status`, `approved`, `rate_limit`, `rights`, `last_reviewed` — or must the governance data stay only in `SOURCE_REGISTRY.md`?
10. **`discoveries` vs `discovered_urls` resolution**: Which table must be the canonical discovery record so the documented flow `candidates → discoveries → discovery_queue` can be implemented without inventing new tables?
11. **Foreign keys**: Do queue/asset tables reference `sources` and `discoveries` by id (referential integrity), or are they denormalised with `source_name` text columns as the current code implies?

---

## 9. Confirmation of Non-Operations

This audit was performed in read-only mode. The following were **not** performed:

- No PostgreSQL database was accessed, inspected, or modified.
- No database records or schemas were changed.
- No migrations were run.
- No evidence was downloaded.
- Nothing was uploaded to R2.
- No packages were installed.
- No source code was edited.
- No documentation other than this audit report was modified.
- Nothing was committed.

---

## 10. Next Step

Awaiting approval to proceed to Phase 2: the read-only database-schema audit of `sources`, `search_candidates`, `discoveries`, `discovery_queue`, `assets`, `metadata_queue`, and any processing or failure queues used by the existing code, as defined in `docs/NEXT_TASK.md`.