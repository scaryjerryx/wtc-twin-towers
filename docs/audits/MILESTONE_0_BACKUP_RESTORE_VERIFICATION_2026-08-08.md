# Milestone 0 Completion Report — Backup & Restore Verification

Date: 2026-08-08

## 1. Summary

- **Milestone:** 0 (Backup & Restore Verification)
- **Date executed:** 2026-08-08
- **Result:** **PASSED**
- **Purpose:** Verify that the live `wtc_evidence` database can be reliably backed up and restored to an independent scratch database before any schema changes or code repairs begin.

## 2. Backup Artifact

- **Filename:** `wtc_evidence_20260808T165348.dump`
- **Location:** `/opt/wtc/backups/wtc_evidence_20260808T165348.dump`
- **Size:** 61,194 bytes
- **Permissions:** `600`, owner `root:root`
- **Format:** pg_dump custom format (`-Fc`)
- **Created by:** Stage A using `wtc_ai_auditor` read-only role via Docker exec

## 3. State File

- **Filename:** `m0.state`
- **Location:** `/opt/wtc/backups/m0.state`
- **Permissions:** `600`, owner `root:root`
- **Contents:** Timestamp (`TS`), backup path (`BACKUP`), scratch database name (`SCRATCH`) — no credentials stored
- **Validation:** All three embedded timestamps match; variable names syntactically valid; no symlinks permitted

## 4. Scratch Database

- **Name:** `wtc_evidence_m0_scratch_20260808T165348`
- **Created by:** Stage C using `wtc_admin` role
- **Restored from:** `wtc_evidence_20260808T165348.dump`
- **Restore flags:** `--exit-on-error --no-owner --no-privileges`
- **Post-restore grants:** `CONNECT`, `USAGE`, `SELECT` on all tables and sequences granted to `wtc_ai_auditor`

## 5. Backup Archive TOC

- **TOC entries:** 202
- **Validated by:** Stage B — `pg_restore -l` piped into the Docker container without credentials
- **Result:** Non-zero, archive readable and well-formed

## 6. Restored Table Count

- **Expected:** 19 public base tables
- **Actual:** 19
- **Verified by:** Stage C — `information_schema.tables` count after restore

## 7. Row-Count Comparison

- **Method:** Exact `COUNT(*)` per table generated via `query_to_xml(format(...))` to avoid off-by-one issues with statistics-based estimates — executed by Stage D
- **Live database:** queried using `wtc_ai_auditor` read-only role
- **Scratch database:** queried using `wtc_ai_auditor` read-only role
- **Result:** **MATCH** — all 19 tables returned identical exact row counts

## 8. Schema-Object Comparison

- **Method:** Object-type totals compared via `information_schema` and `pg_catalog` — executed by Stage D
- **Categories compared:**
  - Tables: 19
  - Sequences: 19
  - Indexes: 28
  - Primary keys: 19
  - Unique constraints: 8
  - Foreign keys: 6
  - Check constraints: 0
- **Result:** **MATCH** — all seven object-type totals identical between live and scratch

## 9. Live Database Unchanged Confirmation

- All queries against `wtc_evidence` used the `wtc_ai_auditor` read-only role
- No write operations (`INSERT`, `UPDATE`, `DELETE`, `DROP`, `CREATE`) executed against the live database
- `pg_dump` is a read-only operation; `pg_restore` targeted only the scratch database
- **Live database confirmed unchanged**

## 10. Problems Encountered and Corrections

Three problems were identified and resolved during script development:

1. **Privilege query used unqualified relation names (Stage A):** The original `has_table_privilege` query used unqualified table names, which failed on collation objects. Corrected to use schema-qualified `format('%I.%I', t.table_schema, t.table_name)` notation. The corrected query confirmed auditor SELECT access on every public table and sequence.

2. **Missing `-d postgres` in Stage C `createdb` guard query:** The first Stage C run omitted `-d postgres` from the `psql` command that checks for an existing scratch database. PostgreSQL interpreted `wtc_admin` (the username) as the database name to connect to, producing a misleading error. Added `-d postgres` to specify the administrative database explicitly. The corrected Stage C ran successfully.

3. **HTML entity check before execution:** All four stage scripts were checked for HTML entities (such as `&`, `<`, `>`) introduced by copy-paste from a browser interface before they were executed. No entities were found; the scripts were shell-safe as written.

## 11. Verification Outputs

The following outputs were produced during verification and are retained in `/opt/wtc/backups/`:

- `m0_live_rows.txt` — exact row counts from live database
- `m0_scratch_rows.txt` — exact row counts from scratch database
- `m0_rows.diff` — empty diff (no differences)
- `m0_live_objects.txt` — schema-object totals from live database
- `m0_scratch_objects.txt` — schema-object totals from scratch database
- `m0_objects.diff` — empty diff (no differences)

## 12. Repository Impact

No repository files were intentionally modified during Milestone 0.

All artifacts (backup `.dump`, `m0.state`, stage scripts `m0_stage_A.sh` through `m0_stage_D.sh`, and verification outputs) were created under `/opt/wtc/backups/`, which is outside the repository working tree.

Git state was checked with `git status --short` to confirm the repository contains no unintended modifications.

## 13. Verification Checklist

- [x] pg_dump completes without error
- [x] Backup file non-empty (61,194 bytes)
- [x] Backup file permissions 600, root-owned
- [x] State file created with valid syntax
- [x] State file permissions 600, root-owned
- [x] Backup TOC parseable (202 entries)
- [x] Scratch database created
- [x] pg_restore completes without error (exit code 0)
- [x] Restored table count matches expected (19)
- [x] All exact row counts match (19 of 19 tables)
- [x] All schema-object totals match (7 of 7 categories)
- [x] Live database unchanged

## 14. Milestone 0 Result

**PASSED** — The backup-and-restore pipeline is verified working. The live database can be reliably backed up and restored to an independent scratch database. Schema changes and discovery/downloader repairs may proceed.

## 15. Pending: Scratch Database Cleanup

- Scratch database `wtc_evidence_m0_scratch_20260808T165348` remains on the PostgreSQL server
- Cleanup (`DROP DATABASE`) requires separate approval
- The scratch database is isolated from production and has read-only access for `wtc_ai_auditor`