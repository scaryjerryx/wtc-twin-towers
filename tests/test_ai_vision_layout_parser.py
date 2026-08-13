#!/usr/bin/env python3
"""
Unit Tests for Stage 3 AI Vision Layout Parser Script
Phase 4 Automated PDF Parsing Pipeline

Governing Contract: docs/PHASE_4_STAGE_3_LAYOUT_CONTRACT.md (v1.0.0)
"""

import unittest
import shutil
import json
import tempfile
from pathlib import Path
from scripts.ai_vision_layout_parser import AIVisionLayoutParser, CONTRACT_VERSION


class TestAIVisionLayoutParser(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.processed_dir = self.test_dir / "processed"
        self.failed_dir = self.test_dir / "failed"

        self.parser = AIVisionLayoutParser(
            processed_dir=self.processed_dir,
            failed_dir=self.failed_dir
        )

        # Mock valid Stage 2 contract payload
        self.mock_stage2_contract = {
            "contract_version": "1.0.0",
            "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "source_sheet_code": "A-A-18",
            "extraction_timestamp": "2026-08-12T22:35:00Z",
            "coordinate_system": {
                "srid": 2263,
                "projection_name": "NAD83 / New York Long Island (ftUS)",
                "drawing_scale": "1/8\" = 1'-0\"",
                "unit": "us_survey_feet"
            },
            "vector_objects": {
                "polylines": [
                    {
                        "polyline_id": "line_grid_1",
                        "cad_layer": "GRID_LINES",
                        "vertex_count": 2,
                        "wkt_geometry": "LINESTRING(982100.00 198200.00, 982100.00 199000.00)"
                    }
                ],
                "polygons": [
                    {
                        "polygon_id": "poly_fan_room_101",
                        "cad_layer": "WALLS",
                        "vertex_count": 5,
                        "wkt_geometry": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))",
                        "area_sq_ft": 40000.0,
                        "is_valid": True
                    }
                ],
                "text_annotations": [
                    {
                        "text_id": "txt_fan_room_101",
                        "text_content": "SUB-GRADE FAN ROOM 101",
                        "cad_layer": "ANNO",
                        "bounding_box_wkt": "POLYGON((982150 198250, 982250 198250, 982250 198280, 982150 198280, 982150 198250))",
                        "associated_polygon_id": "poly_fan_room_101"
                    }
                ]
            },
            "geometry_validation": {
                "total_geometries": 1,
                "valid_geometries": 1,
                "repaired_geometries": 0,
                "invalid_geometries": 0,
                "pass_rate_percentage": 100.0
            },
            "confidence_score": 98,
            "validation_status": "VALIDATED",
            "quarantine_status": False,
            "processing_errors": []
        }

        self.stage2_file_path = self.processed_dir / "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855_stage2.json"
        with open(self.stage2_file_path, "w", encoding="utf-8") as f:
            json.dump(self.mock_stage2_contract, f, indent=2)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_composite_confidence_formula(self):
        # 0.4 * 100 + 0.4 * 90 + 0.2 * 80 = 40 + 36 + 16 = 92
        score = self.parser.calculate_composite_confidence(100, 90, 80)
        self.assertEqual(score, 92)

    def test_ocr_vector_text_reconciliation(self):
        # Matching text
        final_txt, alias = self.parser.reconcile_ocr_vector_text("BOOSTER PUMP", "BOOSTER PUMP")
        self.assertEqual(final_txt, "BOOSTER PUMP")
        self.assertIsNone(alias)

        # Conflicting text: Vector PREVAILS, OCR saved as alias
        final_txt2, alias2 = self.parser.reconcile_ocr_vector_text("BOOSTER PUMP", "BOOSTER PUMP ROOM 2")
        self.assertEqual(final_txt2, "BOOSTER PUMP")
        self.assertEqual(alias2, "BOOSTER PUMP ROOM 2")

    def test_stage3_layout_contract_generation(self):
        result = self.parser.process_stage2_contract(self.stage2_file_path)

        self.assertEqual(result["contract_version"], CONTRACT_VERSION)
        self.assertEqual(result["source_file_hash"], self.mock_stage2_contract["source_file_hash"])
        self.assertEqual(result["source_sheet_code"], "A-A-18")
        self.assertEqual(result["validation_status"], "VALIDATED")
        self.assertFalse(result["quarantine_status"])
        self.assertGreaterEqual(result["confidence_summary"]["min_confidence"], 80)
        self.assertEqual(len(result["detected_entities"]), 1)

        # Verify output stage3 JSON file exists
        stage3_json = self.processed_dir / f"{self.mock_stage2_contract['source_file_hash']}_stage3.json"
        self.assertTrue(stage3_json.exists())

    def test_quarantined_stage2_rejection(self):
        bad_stage2 = dict(self.mock_stage2_contract)
        bad_stage2["quarantine_status"] = True
        bad_stage2["validation_status"] = "FAILED"
        bad_stage2_path = self.processed_dir / "bad_stage2.json"
        with open(bad_stage2_path, "w", encoding="utf-8") as f:
            json.dump(bad_stage2, f, indent=2)

        with self.assertRaises(ValueError):
            self.parser.process_stage2_contract(bad_stage2_path)


if __name__ == "__main__":
    unittest.main()
