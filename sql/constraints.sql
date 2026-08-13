-- PostgreSQL 16 Production Check & Unique Constraints
-- Database: wtc_evidence

-- Entity Validation Status & Confidence Score Check Constraints
ALTER TABLE wtc_evidence.entities 
    ADD CONSTRAINT check_entity_validation_status CHECK (validation_status IN ('VALIDATED')),
    ADD CONSTRAINT check_entity_confidence_score CHECK (confidence_score = 100);

-- Validation Score Check Constraint
ALTER TABLE wtc_evidence.validations
    ADD CONSTRAINT check_validation_confidence_score CHECK (confidence_score = 100);

-- Relationship Score Check Constraint & Directed Edge Unique Constraint
ALTER TABLE wtc_evidence.relationships
    ADD CONSTRAINT check_relationship_confidence_score CHECK (confidence_score = 100),
    ADD CONSTRAINT unique_directed_edge UNIQUE (subject_entity_id, relationship_type, object_entity_id);
