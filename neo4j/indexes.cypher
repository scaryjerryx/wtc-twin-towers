// Neo4j Graph Database Indexes
// Database: Neo4j v5

CREATE INDEX idx_entity_subsystem IF NOT EXISTS 
FOR (e:Entity) ON (e.subsystem);

CREATE INDEX idx_entity_level IF NOT EXISTS 
FOR (e:Entity) ON (e.level);

CREATE INDEX idx_entity_status IF NOT EXISTS 
FOR (e:Entity) ON (e.validation_status);

CREATE INDEX idx_drawing_sheet IF NOT EXISTS 
FOR (d:Drawing) ON (d.sheet_number);
