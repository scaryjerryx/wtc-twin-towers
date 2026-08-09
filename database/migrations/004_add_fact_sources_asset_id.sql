-- M22: Add asset_id to fact_sources for independent-source verification
-- Idempotent: safe to re-run

BEGIN;

-- Add nullable FK column
ALTER TABLE fact_sources
ADD COLUMN IF NOT EXISTS asset_id INTEGER
REFERENCES assets(id);

-- Backfill asset_id from source_file patterns:
--   acquisition_asset_{id}
--   acquisition_asset_{id}_ocr
UPDATE fact_sources
SET asset_id = (
    SELECT (regexp_matches(
        fact_sources.source_file,
        '^acquisition_asset_(\d+)(?:_ocr)?$'
    ))[1]::integer
)
WHERE
    fact_sources.source_file ~ '^acquisition_asset_\d+'
    AND fact_sources.asset_id IS NULL;

COMMIT;