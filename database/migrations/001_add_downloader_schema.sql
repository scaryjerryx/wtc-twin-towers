-- M11: Downloader Schema Additions
-- Date: 2026-08-09
-- Milestone: M11 – Downloader Schema Additions
-- Summary: Add assets.file_hash (unique), assets.content_type,
--          and create asset_sources table for retrieval-event provenance.
-- Safety: All statements are idempotent (IF NOT EXISTS).
-- Role: Administrator (DDL).

-- 1. Add file_hash and content_type columns to assets
ALTER TABLE assets ADD COLUMN IF NOT EXISTS file_hash text;
ALTER TABLE assets ADD COLUMN IF NOT EXISTS content_type text;

-- 2. Unique index on file_hash (the only index on this column)
CREATE UNIQUE INDEX IF NOT EXISTS unique_asset_file_hash ON assets(file_hash);

-- 3. Create asset_sources table (one row = one retrieval event, per approved decision A4)
CREATE TABLE IF NOT EXISTS asset_sources (
    id SERIAL PRIMARY KEY,
    asset_id integer NOT NULL REFERENCES assets(id),
    source_id integer REFERENCES sources(id),
    original_url text NOT NULL,
    normalised_url text,
    final_effective_url text,
    retrieved_at timestamptz NOT NULL DEFAULT now(),
    created_at timestamptz NOT NULL DEFAULT now()
);

-- Verification queries:
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'assets'
--   AND column_name IN ('file_hash', 'content_type');
--
-- SELECT indexname FROM pg_indexes
-- WHERE schemaname = 'public' AND tablename = 'assets'
--   AND indexname = 'unique_asset_file_hash';
--
-- SELECT column_name, data_type, is_nullable
-- FROM information_schema.columns
-- WHERE table_name = 'asset_sources'
-- ORDER BY ordinal_position;