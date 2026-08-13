-- PostgreSQL 16 + PostGIS 3.6.4 Production Schema DDL
-- Database: wtc_evidence

CREATE SCHEMA IF NOT EXISTS wtc_evidence;
CREATE EXTENSION IF NOT EXISTS postgis SCHEMA wtc_evidence;

-- 1. Subsystems Lookup Table
CREATE TABLE wtc_evidence.subsystems (
    subsystem_id VARCHAR(64) PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    description TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 2. Drawings Table
CREATE TABLE wtc_evidence.drawings (
    drawing_id VARCHAR(64) PRIMARY KEY,
    sheet_number VARCHAR(32) NOT NULL UNIQUE,
    title VARCHAR(256) NOT NULL,
    corpus_collection VARCHAR(128) NOT NULL,
    scale_ratio VARCHAR(32),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 3. Sessions Table
CREATE TABLE wtc_evidence.sessions (
    session_id VARCHAR(64) PRIMARY KEY,
    session_number INT NOT NULL UNIQUE,
    title VARCHAR(256) NOT NULL,
    execution_date DATE NOT NULL,
    summary_report_path VARCHAR(512) NOT NULL
);

-- 4. Entities Table
CREATE TABLE wtc_evidence.entities (
    entity_id VARCHAR(128) PRIMARY KEY,
    canonical_name VARCHAR(256) NOT NULL,
    subsystem_id VARCHAR(64) NOT NULL REFERENCES wtc_evidence.subsystems(subsystem_id),
    building VARCHAR(64) NOT NULL DEFAULT 'WTC 1 (Tower A)',
    building_level VARCHAR(64) NOT NULL,
    validation_status VARCHAR(32) NOT NULL DEFAULT 'VALIDATED',
    confidence_score INT NOT NULL DEFAULT 100,
    geom wtc_evidence.geometry(Geometry, 2263),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 5. Evidence Table
CREATE TABLE wtc_evidence.evidence (
    evidence_id VARCHAR(128) PRIMARY KEY,
    entity_id VARCHAR(128) NOT NULL REFERENCES wtc_evidence.entities(entity_id),
    drawing_id VARCHAR(64) NOT NULL REFERENCES wtc_evidence.drawings(drawing_id),
    page_number INT DEFAULT 1,
    bounding_box_rect VARCHAR(128) NOT NULL,
    citation_uri VARCHAR(512) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 6. Validations Table
CREATE TABLE wtc_evidence.validations (
    validation_id VARCHAR(128) PRIMARY KEY,
    entity_id VARCHAR(128) NOT NULL REFERENCES wtc_evidence.entities(entity_id),
    session_id VARCHAR(64) NOT NULL REFERENCES wtc_evidence.sessions(session_id),
    confidence_score INT NOT NULL DEFAULT 100,
    validation_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

-- 7. Relationships Table
CREATE TABLE wtc_evidence.relationships (
    relationship_id SERIAL PRIMARY KEY,
    subject_entity_id VARCHAR(128) NOT NULL REFERENCES wtc_evidence.entities(entity_id),
    relationship_type VARCHAR(64) NOT NULL,
    object_entity_id VARCHAR(128) NOT NULL REFERENCES wtc_evidence.entities(entity_id),
    confidence_score INT NOT NULL DEFAULT 100
);

-- 8. Operational Chains Table
CREATE TABLE wtc_evidence.operational_chains (
    chain_id VARCHAR(64) PRIMARY KEY,
    chain_name VARCHAR(128) NOT NULL,
    subsystem_id VARCHAR(64) NOT NULL REFERENCES wtc_evidence.subsystems(subsystem_id),
    stage_count INT NOT NULL,
    continuity_status VARCHAR(32) NOT NULL DEFAULT 'COMPLETE'
);

-- 9. Audit Records Table
CREATE TABLE wtc_evidence.audit_records (
    audit_id VARCHAR(64) PRIMARY KEY,
    program_name VARCHAR(128) NOT NULL,
    execution_date DATE NOT NULL,
    total_validated_entities INT NOT NULL,
    total_validated_relationships INT NOT NULL,
    validation_rate_pct NUMERIC(5,2) NOT NULL DEFAULT 100.00,
    contradiction_count INT NOT NULL DEFAULT 0,
    classification VARCHAR(64) NOT NULL
);
