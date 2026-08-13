-- PostgreSQL 16 + PostGIS 3.6.4 Production Indexes
-- Database: wtc_evidence

-- Spatial Index
CREATE INDEX IF NOT EXISTS idx_entities_geom ON wtc_evidence.entities USING GIST(geom);

-- B-Tree Bounding & Lookup Indexes
CREATE INDEX IF NOT EXISTS idx_entities_subsystem ON wtc_evidence.entities(subsystem_id);
CREATE INDEX IF NOT EXISTS idx_entities_level ON wtc_evidence.entities(building_level);
CREATE INDEX IF NOT EXISTS idx_entities_status ON wtc_evidence.entities(validation_status);

CREATE INDEX IF NOT EXISTS idx_rel_subject ON wtc_evidence.relationships(subject_entity_id);
CREATE INDEX IF NOT EXISTS idx_rel_object ON wtc_evidence.relationships(object_entity_id);
CREATE INDEX IF NOT EXISTS idx_rel_type ON wtc_evidence.relationships(relationship_type);

CREATE INDEX IF NOT EXISTS idx_evidence_entity ON wtc_evidence.evidence(entity_id);
CREATE INDEX IF NOT EXISTS idx_evidence_drawing ON wtc_evidence.evidence(drawing_id);

CREATE INDEX IF NOT EXISTS idx_validations_entity ON wtc_evidence.validations(entity_id);
CREATE INDEX IF NOT EXISTS idx_validations_session ON wtc_evidence.validations(session_id);
