// Neo4j Model Ingestion Templates
// Load Entities & Relationships from JSON/CSV Exports

// 1. Load Entities
LOAD CSV WITH HEADERS FROM 'file:///entities.csv' AS row
MERGE (e:Entity {entity_id: row.entity_id})
ON CREATE SET 
    e.canonical_name = row.canonical_name,
    e.subsystem = row.subsystem_id,
    e.building = row.building,
    e.level = row.building_level,
    e.validation_status = row.validation_status,
    e.confidence_score = toInteger(row.confidence_score);

// 2. Load Relationships Dynamically
LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row
MATCH (source:Entity {entity_id: row.subject_entity_id})
MATCH (target:Entity {entity_id: row.object_entity_id})
CALL apoc.create.relationship(source, row.relationship_type, {confidence_score: toInteger(row.confidence_score)}, target) YIELD rel
RETURN count(rel);
