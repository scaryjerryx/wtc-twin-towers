#!/usr/bin/env python3
"""
Unit Tests for Stage 2 Vector Extraction Engine Script
Phase 4 Automated PDF Parsing Pipeline

Governing Contract: docs/PHASE_4_STAGE_2_VECTOR_CONTRACT.md (v1.0.0)
"""

import unittest
import shutil
import json
import tempfile
from pathlib import Path
from scripts.vector_extraction_engine import VectorExtractionEngine, CONTRACT_VERSION, TARGET_SRID


class TestVectorExtractionEngine(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.processed_dir = self.test_dir / "processed"
        self.failed_dir = self.test_dir / "failed"

        self.engine = VectorExtractionEngine(
            processed_dir=self.processed_dir,
            failed_dir=self.failed_dir
        )

        # Mock valid Stage 1 contract payload
        self.mock_stage1_contract = {
            "contract_version": "1.0.0",
            "file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "file_name": "drawing_aa18.pdf",
            "file_path": "data/incoming_pdfs/drawing_aa18.pdf",
            "file_size_bytes": 2457600,
            "page_count": 1,
            "sheet_code": "A-A-18",
            "extraction_timestamp": "2026-08-12T22:35:00Z",
            "validation_status": "VALIDATED",
            "quarantine_status": False,
            "metadata": {
                "pdf_version": "1.7",
                "author": "Yamasaki",
                "creator": "AutoCAD",
                "producer": "PDFium",
                "creation_date": "1973-05-14T00:00:00Z"
            },
            "title_block_data": {
                "title_block_found": True,
                "drawing_title": "SUB-GRADE FLOOR PLAN B1 & B2",
                "sheet_number": "A-A-18",
                "scale": "1/8\" = 1'-0\"",
                "revision": "Rev 4"
            },
            "processing_errors": []
        }

        self.stage1_file_path = self.processed_dir / "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855_stage1.json"
        with open(self.stage1_file_path, "w", encoding="utf-8") as f:
            json.dump(self.mock_stage1_contract, f, indent=2)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_coordinate_transformation(self):
        x, y = self.engine.pdf_pt_to_epsg2263(10, 20, scale_factor=8.0)
        self.assertEqual(x, 982180.0)
        self.assertEqual(y, 198360.0)

    def test_polygon_wkt_validation(self):
        valid_wkt = "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))"
        is_valid, area, v_count = self.engine.validate_polygon_wkt(valid_wkt)
        self.assertTrue(is_valid)
        self.assertEqual(v_count, 5)
        self.assertEqual(area, 40000.0)

        invalid_wkt = "POLYGON((982100 198200, 982300 198200))"
        is_valid_bad, area_bad, _ = self.engine.validate_polygon_wkt(invalid_wkt)
        self.assertFalse(is_valid_bad)

    def test_stage2_vector_contract_generation(self):
        result = self.engine.process_stage1_contract(self.stage1_file_path)

        self.assertEqual(result["contract_version"], CONTRACT_VERSION)
        self.assertEqual(result["source_file_hash"], self.mock_stage1_contract["file_hash"])
        self.assertEqual(result["source_sheet_code"], "A-A-18")
        self.assertEqual(result["coordinate_system"]["srid"], TARGET_SRID)
        self.assertEqual(result["validation_status"], "VALIDATED")
        self.assertFalse(result["quarantine_status"])
        self.assertGreaterEqual(result["confidence_score"], 80)
        self.assertGreaterEqual(result["geometry_validation"]["pass_rate_percentage"], 95.0)

        # Verify output stage2 JSON file exists
        stage2_json = self.processed_dir / f"{self.mock_stage1_contract['file_hash']}_stage2.json"
        self.assertTrue(stage2_json.exists())

    def test_quarantined_stage1_rejection(self):
        bad_stage1 = dict(self.mock_stage1_contract)
        bad_stage1["quarantine_status"] = True
        bad_stage1["validation_status"] = "FAILED"
        bad_stage1_path = self.processed_dir / "bad_stage1.json"
        with open(bad_stage1_path, "w", encoding="utf-8") as f:
            json.dump(bad_stage1, f, indent=2)

        with self.assertRaises(ValueError):
            self.engine.process_stage1_contract(bad_stage1_path)


if __name__ == "__main__":
    unittest.main()
