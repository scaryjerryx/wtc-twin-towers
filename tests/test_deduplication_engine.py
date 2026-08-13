#!/usr/bin/env python3
"""
Unit Tests for Stage 5 PostGIS Deduplication Engine Script
Phase 4 Automated PDF Parsing Pipeline

Governing Contract: docs/PHASE_4_STAGE_5_DEDUPLICATION_CONTRACT.md (v1.0.0)
"""

import unittest
import shutil
import json
import tempfile
from pathlib import Path
from scripts.deduplication_engine import DeduplicationEngine, CONTRACT_VERSION


class TestDeduplicationEngine(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.processed_dir = self.test_dir / "processed"
        self.failed_dir = self.test_dir / "failed"

        self.engine = DeduplicationEngine(
            processed_dir=self.processed_dir,
            failed_dir=self.failed_dir
        )

        # Mock valid Stage 3 layout contract payload
        self.mock_stage3_contract = {
            "contract_version": "1.0.0",
            "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "source_sheet_code": "A-A-18",
            "parsing_timestamp": "2026-08-12T22:37:00Z",
            "detected_entities": [
                {
                    "entity_id": "wtc1_f1_fan_room_101",
                    "entity_name": "Sub-grade Fan Room 101",
                    "category": "service_area",
                    "bounding_box": {"x_min": 982100.0, "y_min": 198200.0, "x_max": 982300.0, "y_max": 198400.0},
                    "wkt_geometry": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))",
                    "confidence_score": 95,
                    "evidence_citation": {
                        "source_id": "src_yamasaki_drawings",
                        "sheet_code": "A-A-18"
                    }
                }
            ],
            "ocr_results": [],
            "symbol_detections": [],
            "confidence_summary": {
                "average_confidence": 95.0,
                "min_confidence": 95,
                "max_confidence": 95,
                "low_confidence_count": 0
            },
            "human_review_status": {
                "requires_human_review": False,
                "review_reason": None,
                "flagged_entity_ids": []
            },
            "validation_status": "VALIDATED",
            "quarantine_status": False,
            "processing_errors": []
        }

        self.stage3_file_path = self.processed_dir / "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855_stage3.json"
        with open(self.stage3_file_path, "w", encoding="utf-8") as f:
            json.dump(self.mock_stage3_contract, f, indent=2)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_iou_calculation(self):
        bbox1 = {"x_min": 0, "y_min": 0, "x_max": 10, "y_max": 10}
        bbox2 = {"x_min": 0, "y_min": 0, "x_max": 10, "y_max": 10}
        self.assertEqual(self.engine.calculate_iou(bbox1, bbox2), 1.0)

        bbox3 = {"x_min": 20, "y_min": 20, "x_max": 30, "y_max": 30}
        self.assertEqual(self.engine.calculate_iou(bbox1, bbox3), 0.0)

    def test_levenshtein_similarity(self):
        self.assertEqual(self.engine.levenshtein_similarity("Fan Room 101", "Fan Room 101"), 1.0)
        self.assertGreaterEqual(self.engine.levenshtein_similarity("Fan Room 101", "Fan Room 102"), 0.8)

    def test_stage5_deduplication_contract_generation(self):
        result = self.engine.process_stage3_contract(self.stage3_file_path)

        self.assertEqual(result["contract_version"], CONTRACT_VERSION)
        self.assertEqual(result["source_file_hash"], self.mock_stage3_contract["source_file_hash"])
        self.assertEqual(result["source_sheet_code"], "A-A-18")
        self.assertEqual(result["validation_status"], "VALIDATED")
        self.assertFalse(result["quarantine_status"])
        self.assertGreaterEqual(result["confidence_reconciliation"]["min_reconciled_confidence"], 80)
        self.assertEqual(len(result["deduplicated_entities"]), 1)

        # Check resolution action & lifecycle state promotion
        ent = result["deduplicated_entities"][0]
        self.assertEqual(ent["resolution_action"], "CORROBORATE_CITATION")
        self.assertEqual(ent["lifecycle_state"], "CORROBORATED")

        # Verify output stage5 JSON file exists
        stage5_json = self.processed_dir / f"{self.mock_stage3_contract['source_file_hash']}_stage5.json"
        self.assertTrue(stage5_json.exists())

    def test_quarantined_stage3_rejection(self):
        bad_stage3 = dict(self.mock_stage3_contract)
        bad_stage3["quarantine_status"] = True
        bad_stage3["validation_status"] = "FAILED"
        bad_stage3_path = self.processed_dir / "bad_stage3.json"
        with open(bad_stage3_path, "w", encoding="utf-8") as f:
            json.dump(bad_stage3, f, indent=2)

        with self.assertRaises(ValueError):
            self.engine.process_stage3_contract(bad_stage3_path)


if __name__ == "__main__":
    unittest.main()
