#!/usr/bin/env python3
import json
import glob

def load_all_seed_data():
    seed_files = sorted(glob.glob('data/*.json'))
    
    root_anchors = {
        'wtc_complex': {
            'entity_id': 'wtc_complex',
            'name': 'World Trade Center Complex',
            'category': 'site',
            'entity_category': 'site',
            'confidence_score': 100,
            'lifecycle_state': 'VALIDATED',
            'z_min': -70.0,
            'z_max': 1370.0,
            'geometry_2d': 'POLYGON((0 0, 1000 0, 1000 1000, 0 1000, 0 0))'
        },
        'wtc1_tower_a': {
            'entity_id': 'wtc1_tower_a',
            'name': 'One World Trade Center - North Tower',
            'category': 'building',
            'entity_category': 'building',
            'site_id': 'wtc_complex',
            'structure_type': 'high_rise_tower',
            'confidence_score': 100,
            'lifecycle_state': 'VALIDATED',
            'z_min': -70.0,
            'z_max': 1368.0,
            'geometry_2d': 'POLYGON((100 100, 300 100, 300 300, 100 300, 100 100))'
        },
        'wtc2_tower_b': {
            'entity_id': 'wtc2_tower_b',
            'name': 'Two World Trade Center - South Tower',
            'category': 'building',
            'entity_category': 'building',
            'site_id': 'wtc_complex',
            'structure_type': 'high_rise_tower',
            'confidence_score': 100,
            'lifecycle_state': 'VALIDATED',
            'z_min': -70.0,
            'z_max': 1362.0,
            'geometry_2d': 'POLYGON((400 100, 600 100, 600 300, 400 300, 400 100))'
        }
    }

    all_entities = dict(root_anchors)
    all_relationships = []
    all_sources = {
        'src_yamasaki_drawings': {
            'title': 'World Trade Center Primary Architectural Drawings',
            'author_organization': 'Minoru Yamasaki & Associates / Emery Roth & Sons',
            'publication_year': 1973
        }
    }

    for fpath in seed_files:
        with open(fpath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
            entities = []
            rels = []
            
            if isinstance(data, dict):
                if 'source' in data:
                    src = data['source']
                    src_id = src.get('source_id') or src.get('id') or 'src_default'
                    all_sources[src_id] = src
                entities = data.get('entities', [])
                rels = data.get('relationships', [])
            elif isinstance(data, list):
                entities = data

            for e in entities:
                if isinstance(e, dict):
                    eid = e.get('entity_id') or e.get('id')
                    if eid and eid not in root_anchors:
                        all_entities[eid] = e
            
            for r in rels:
                if isinstance(r, dict):
                    all_relationships.append(r)
                
    return seed_files, all_entities, all_relationships, all_sources

def normalize_category(cat):
    valid_cats = [
        'site', 'building', 'floor', 'zone', 'space', 'general_space', 'retail_space',
        'transit_station', 'kitchen_area', 'service_area', 'corridor', 'structural_element',
        'mechanical_area', 'mechanical_element', 'architectural_element', 'elevator_bank',
        'elevator', 'stair', 'escalator'
    ]
    if cat in valid_cats:
        return cat
    if cat == 'element':
        return 'structural_element'
    return 'structural_element'

def generate_ingestion_sql(all_entities, all_relationships, all_sources):
    sql_lines = ["BEGIN;"]
    
    # 1. Ingest Sources
    for src_id, src in all_sources.items():
        title = src.get('title', 'Unknown Title').replace("'", "''")
        author = src.get('author_organization', 'Unknown Author').replace("'", "''")
        year = src.get('publication_year', 1973)
        sql_lines.append(f"""
        INSERT INTO sources (source_id, title, author_organization, publication_year)
        VALUES ('{src_id}', '{title}', '{author}', {year})
        ON CONFLICT (source_id) DO UPDATE SET title = EXCLUDED.title;
        """)

    # 2. Ingest Master Entities
    for eid, e in all_entities.items():
        raw_cat = e.get('category') or e.get('entity_category') or e.get('entity_type') or 'structural_element'
        cat = normalize_category(raw_cat)
        bldg_id = e.get('building_id') or e.get('parent_entity')
        bldg_val = f"'{bldg_id}'" if bldg_id in ['wtc1_tower_a', 'wtc2_tower_b'] else "NULL"
        score = e.get('confidence_score', 100)
        state = e.get('lifecycle_state', 'VALIDATED')
        if state not in ['DRAFT_SEED', 'CORROBORATED', 'VALIDATED', 'DEPRECATED', 'ARCHIVED']:
            state = 'VALIDATED'
        sql_lines.append(f"""
        INSERT INTO entities (entity_id, entity_category, building_id, confidence_score, lifecycle_state)
        VALUES ('{eid}', '{cat}', {bldg_val}, {score}, '{state}')
        ON CONFLICT (entity_id) DO UPDATE SET confidence_score = EXCLUDED.confidence_score;
        """)

    # 3. Ingest Physical Tier Entities (Strict Order: site=1, building=2, floor=3, zone=4, space=5, element=6)
    category_tiers = {
        'site': 1,
        'building': 2,
        'floor': 3,
        'zone': 4,
        'space': 5, 'general_space': 5, 'retail_space': 5, 'transit_station': 5, 'kitchen_area': 5, 'service_area': 5, 'corridor': 5,
        'element': 6, 'structural_element': 6, 'mechanical_area': 6, 'mechanical_element': 6, 'architectural_element': 6, 'elevator_bank': 6, 'elevator': 6, 'stair': 6, 'escalator': 6
    }
    
    sorted_entity_tuples = sorted(
        all_entities.items(),
        key=lambda item: category_tiers.get(normalize_category(item[1].get('category') or item[1].get('entity_category') or item[1].get('entity_type')), 6)
    )

    for eid, e in sorted_entity_tuples:
        raw_cat = e.get('category') or e.get('entity_category') or e.get('entity_type') or 'structural_element'
        cat = normalize_category(raw_cat)
        name = (e.get('name') or e.get('entity_name') or eid).replace("'", "''")
        score = e.get('confidence_score', 100)
        z_min = e.get('z_min', 0.0)
        z_max = e.get('z_max', 12.0)
        geom = e.get('geometry_2d') or 'POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))'
        geom_sql = f"ST_GeomFromText('{geom}', 2263)"
        parent_ref = e.get('parent_entity') or e.get('parent_id')
        
        if cat == 'site':
            sql_lines.append(f"""
            INSERT INTO sites (site_id, name, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', '{name}', {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (site_id) DO UPDATE SET name = EXCLUDED.name;
            """)
        elif cat == 'building':
            site_id = e.get('site_id', 'wtc_complex')
            stype = e.get('structure_type', 'high_rise_tower')
            if stype not in ['high_rise_tower', 'podium_building', 'hotel_slab', 'substation_base', 'transit_terminal']:
                stype = 'high_rise_tower'
            sql_lines.append(f"""
            INSERT INTO buildings (building_id, site_id, name, structure_type, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', '{site_id}', '{name}', '{stype}', {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (building_id) DO UPDATE SET name = EXCLUDED.name;
            """)
        elif cat == 'floor':
            bldg_id = e.get('building_id') or parent_ref or 'wtc1_tower_a'
            if bldg_id not in ['wtc1_tower_a', 'wtc2_tower_b']:
                bldg_id = 'wtc1_tower_a'
            flr_num = e.get('floor_number', 1)
            elev = e.get('elevation_pa_feet', 0.0)
            sql_lines.append(f"""
            INSERT INTO floors (floor_id, building_id, floor_number, floor_name, elevation_pa_feet, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', '{bldg_id}', {flr_num}, '{name}', {elev}, {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (floor_id) DO UPDATE SET floor_name = EXCLUDED.floor_name;
            """)
        elif cat == 'zone':
            flr_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) == 'floor' else ("'" + e.get('floor_id') + "'" if e.get('floor_id') else "NULL")
            bldg_id = f"'{e.get('building_id')}'" if e.get('building_id') and flr_id == "NULL" else "NULL"
            site_id = "NULL"
            if flr_id == "NULL" and bldg_id == "NULL":
                bldg_id = "'wtc1_tower_a'"
            sql_lines.append(f"""
            INSERT INTO zones (zone_id, floor_id, building_id, site_id, name, zone_type, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', {flr_id}, {bldg_id}, {site_id}, '{name}', 'zone', {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (zone_id) DO UPDATE SET name = EXCLUDED.name;
            """)
        elif cat in ['space', 'general_space', 'retail_space', 'transit_station', 'kitchen_area', 'service_area', 'corridor']:
            zone_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) == 'zone' else ("'" + e.get('zone_id') + "'" if e.get('zone_id') else "NULL")
            flr_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) == 'floor' and zone_id == "NULL" else ("'" + e.get('floor_id') + "'" if e.get('floor_id') and zone_id == "NULL" else "NULL")
            if zone_id == "NULL" and flr_id == "NULL":
                flr_id = "'wtc1_floor_1'"
            sql_lines.append(f"""
            INSERT INTO spaces (space_id, zone_id, floor_id, name, space_category, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', {zone_id}, {flr_id}, '{name}', '{cat}', {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (space_id) DO UPDATE SET name = EXCLUDED.name;
            """)
        else: # Element
            space_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) in ['space', 'corridor', 'general_space', 'service_area', 'retail_space', 'transit_station', 'kitchen_area'] else ("'" + e.get('space_id') + "'" if e.get('space_id') else "NULL")
            zone_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) == 'zone' and space_id == "NULL" else ("'" + e.get('zone_id') + "'" if e.get('zone_id') and space_id == "NULL" else "NULL")
            flr_id = f"'{parent_ref}'" if parent_ref and parent_ref in all_entities and normalize_category(all_entities[parent_ref].get('category') or all_entities[parent_ref].get('entity_type')) == 'floor' and space_id == "NULL" and zone_id == "NULL" else ("'" + e.get('floor_id') + "'" if e.get('floor_id') and space_id == "NULL" and zone_id == "NULL" else "NULL")
            bldg_id = "NULL"
            if space_id == "NULL" and zone_id == "NULL" and flr_id == "NULL":
                bldg_id = "'wtc1_tower_a'"
            is_mf = 'TRUE' if e.get('is_multi_floor') else 'FALSE'
            sql_lines.append(f"""
            INSERT INTO elements (element_id, space_id, zone_id, floor_id, building_id, name, element_category, is_multi_floor, geometry_2d, z_min, z_max, confidence_score)
            VALUES ('{eid}', {space_id}, {zone_id}, {flr_id}, {bldg_id}, '{name}', '{cat}', {is_mf}, {geom_sql}, {z_min}, {z_max}, {score})
            ON CONFLICT (element_id) DO UPDATE SET name = EXCLUDED.name;
            """)

    # 4. Ingest Evidence Citations
    for eid, e in all_entities.items():
        src_id = 'src_yamasaki_drawings'
        sheet = e.get('source_drawing') or 'A-A-18'
        sql_lines.append(f"""
        INSERT INTO entity_evidence_citations (citation_id, entity_id, source_id, sheet_code, confidence_score)
        VALUES ('cite_{eid}', '{eid}', '{src_id}', '{sheet}', 100)
        ON CONFLICT (entity_id, source_id, sheet_code) DO NOTHING;
        """)

    # 5. Ingest Relationships
    valid_rel_types = ['CONTAINS', 'BOUNDED_BY', 'ADJACENT_TO', 'CONNECTS_TO', 'PASSES_THROUGH', 'OVERLOOKS', 'ACCESSES', 'LEADS_TO', 'TRANSFERS_TO', 'POWERED_BY', 'COOLED_BY', 'FEEDS_RISER_TO', 'HOISTS_CAR_FOR', 'SERVES']
    for idx, r in enumerate(all_relationships):
        rel_id = r.get('relationship_id') or f"rel_seed_{idx+1}"
        sub_id = r.get('subject') or r.get('subject_entity_id') or r.get('subject_id')
        rtype = r.get('relation') or r.get('relationship_type') or r.get('type')
        obj_id = r.get('object') or r.get('object_entity_id') or r.get('object_id')
        score = r.get('confidence_score', 100)
        
        if sub_id in all_entities and obj_id in all_entities and rtype in valid_rel_types and sub_id != obj_id:
            sql_lines.append(f"""
            INSERT INTO relationships (relationship_id, subject_entity_id, relationship_type, object_entity_id, confidence_score)
            VALUES ('{rel_id}', '{sub_id}', '{rtype}', '{obj_id}', {score})
            ON CONFLICT (subject_entity_id, relationship_type, object_entity_id) DO UPDATE SET confidence_score = EXCLUDED.confidence_score;
            """)

    sql_lines.append("COMMIT;")
    return "\n".join(sql_lines)

if __name__ == '__main__':
    seed_files, entities, rels, sources = load_all_seed_data()
    sql = generate_ingestion_sql(entities, rels, sources)
    with open('/tmp/ingest_seed_data.sql', 'w', encoding='utf-8') as f:
        f.write(sql)
    print(f"Generated ingestion SQL for {len(entities)} unique entities and {len(rels)} relationships across {len(seed_files)} seed files.")
