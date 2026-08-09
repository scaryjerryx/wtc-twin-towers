-- M23: Create timeline_events table for persistent event storage
-- Idempotent: safe to re-run

BEGIN;

CREATE TABLE IF NOT EXISTS timeline_events (
    id SERIAL PRIMARY KEY,
    event_year INTEGER NOT NULL,
    event_type TEXT NOT NULL DEFAULT 'reference',
    description TEXT,
    date_text TEXT NULL,
    fact_id INTEGER REFERENCES facts(id),
    entity_id INTEGER REFERENCES entities(id),
    asset_id INTEGER REFERENCES assets(id),
    confidence INTEGER DEFAULT 50,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE UNIQUE INDEX IF NOT EXISTS unique_timeline_event
ON timeline_events (fact_id, event_year, event_type);

COMMIT;