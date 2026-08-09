-- M12: Asset Sources Unique Constraint
-- Date: 2026-08-09
-- Milestone: M12 – Asset Registration & Provenance
-- Summary: Add unique index on asset_sources for idempotent registration.
--          Key: (asset_id, COALESCE(source_id, -1), original_url)
--          COALESCE handles nullable source_id (NULLs are not equal in unique constraints).
-- Safety: Idempotent (IF NOT EXISTS).
-- Role: Administrator (DDL).

CREATE UNIQUE INDEX IF NOT EXISTS unique_asset_source_retrieval
ON asset_sources(asset_id, COALESCE(source_id, -1), original_url);

-- Verification:
-- SELECT indexname FROM pg_indexes
-- WHERE schemaname = 'public' AND tablename = 'asset_sources'
--   AND indexname = 'unique_asset_source_retrieval';