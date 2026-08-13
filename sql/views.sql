-- PostgreSQL 16 Production Operational Views
-- Database: wtc_evidence

-- 1. Full Entity Audit View
CREATE OR REPLACE VIEW wtc_evidence.v_entity_audit AS
SELECT 
    e.entity_id,
    e.canonical_name,
    s.name AS subsystem_name,
    e.building_level,
    e.validation_status,
    e.confidence_score,
    COUNT(DISTINCT ev.drawing_id) AS primary_drawing_count,
    COUNT(DISTINCT r1.relationship_id) AS outgoing_edge_count,
    COUNT(DISTINCT r2.relationship_id) AS incoming_edge_count
FROM wtc_evidence.entities e
JOIN wtc_evidence.subsystems s ON e.subsystem_id = s.subsystem_id
LEFT JOIN wtc_evidence.evidence ev ON e.entity_id = ev.entity_id
LEFT JOIN wtc_evidence.relationships r1 ON e.entity_id = r1.subject_entity_id
LEFT JOIN wtc_evidence.relationships r2 ON e.entity_id = r2.object_entity_id
GROUP BY e.entity_id, e.canonical_name, s.name, e.building_level, e.validation_status, e.confidence_score;

-- 2. Property Graph Directed Edges View
CREATE OR REPLACE VIEW wtc_evidence.v_directed_graph_edges AS
SELECT 
    r.relationship_id,
    r.subject_entity_id,
    e1.canonical_name AS subject_name,
    e1.subsystem_id AS subject_subsystem,
    r.relationship_type,
    r.object_entity_id,
    e2.canonical_name AS object_name,
    e2.subsystem_id AS object_subsystem,
    r.confidence_score
FROM wtc_evidence.relationships r
JOIN wtc_evidence.entities e1 ON r.subject_entity_id = e1.entity_id
JOIN wtc_evidence.entities e2 ON r.object_entity_id = e2.entity_id;

-- 3. Operational Chain Continuity Summary View
CREATE OR REPLACE VIEW wtc_evidence.v_operational_chain_summary AS
SELECT 
    c.chain_id,
    c.chain_name,
    s.name AS subsystem_name,
    c.stage_count,
    c.continuity_status
FROM wtc_evidence.operational_chains c
JOIN wtc_evidence.subsystems s ON c.subsystem_id = s.subsystem_id;
