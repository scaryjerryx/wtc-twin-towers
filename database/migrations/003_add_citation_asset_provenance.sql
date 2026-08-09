-- M18: Citation Provenance Integration
-- Date: 2026-08-09
-- Milestone: M18 – Citation Provenance Integration
-- Summary: Add asset_id and asset_source_id nullable FKs to citations,
--          enabling traceability from knowledge claims back to
--          acquisition pipeline assets and retrieval events.
-- Safety: All statements are idempotent (IF NOT EXISTS).
-- Role: Administrator (DDL).

-- 1. Add asset_id FK to citations (trace back to assets table)
ALTER TABLE citations ADD COLUMN IF NOT EXISTS asset_id integer REFERENCES assets(id);

-- 2. Add asset_source_id FK to citations (trace back to specific retrieval event)
ALTER TABLE citations ADD COLUMN IF NOT EXISTS asset_source_id integer REFERENCES asset_sources(id);

-- Verification:
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'citations'
--   AND column_name IN ('asset_id', 'asset_source_id');