// Neo4j Graph Database Constraints
// Database: Neo4j v5

CREATE CONSTRAINT nkf_entity_id IF NOT EXISTS 
FOR (e:Entity) REQUIRE e.entity_id IS UNIQUE;

CREATE CONSTRAINT nkf_drawing_id IF NOT EXISTS 
FOR (d:Drawing) REQUIRE d.drawing_id IS UNIQUE;

CREATE CONSTRAINT nkf_session_id IF NOT EXISTS 
FOR (s:Session) REQUIRE s.session_id IS UNIQUE;

CREATE CONSTRAINT nkf_subsystem_id IF NOT EXISTS 
FOR (sub:Subsystem) REQUIRE sub.subsystem_id IS UNIQUE;
