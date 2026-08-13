#!/usr/bin/env python3
"""
Unit Tests for Stage 6 Transactional Database Ingestion Engine Script
Phase 4 Automated PDF Parsing Pipeline

Governing Contract: docs/PHASE_4_STAGE_6_INGESTION_CONTRACT.md (v1.0.0)
"""

import unittest
import shutil
import json
import tempfile
from pathlib import Path
from scripts.database_ingestion_engine import DatabaseIngestionEngine, CONTRACT_VERSION


class TestDatabaseIngestionEngine(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.processed_dir = self.test_dir / "processed"
        self.failed_dir = self.test_dir / "failed"

        self.engine = DatabaseIngestionEngine(
            processed_dir=self.processed_dir,
            failed_dir=self.failed_dir
        )

        # Mock valid Stage 5 deduplication contract payload
        self.mock_stage5_contract = {
            "contract_version": "1.0.0",
            "source_file_hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "source_sheet_code": "A-A-18",
            "resolution_timestamp": "2026-08-12T22:40:00Z",
            "deduplicated_entities": [
                {
                    "entity_id": "wtc1_f1_fan_room_101",
                    "resolution_action": "INSERT_NEW",
                    "category": "service_area",
                    "name": "Sub-grade Fan Room 101",
                    "wkt_geometry": "POLYGON((982100 198200, 982300 198200, 982300 198400, 982100 198400, 982100 198200))",
                    "confidence_score": 95,
                    "lifecycle_state": "CORROBORATED"
                }
            ],
            "deduplicated_relationships": [
                {
                    "relationship_id": "rel_aa18_10",
                    "subject_entity_id": "wtc1_f1_fan_room_101",
                    "relationship_type": "CONTAINS",
                    "object_entity_id": "wtc1_f1_chiller_unit_1",
                    "confidence_score": 95
                }
            ],
            "evidence_reconciliation": {
                "total_citations_linked": 1,
                "new_sources_registered": 0,
                "corroborated_citations": 1
            },
            "confidence_reconciliation": {
                "average_reconciled_confidence": 95.0,
                "min_reconciled_confidence": 95,
                "max_reconciled_confidence": 95
            },
            "conflict_resolution_log": [],
            "human_review_status": {
                "requires_human_review": False,
                "review_reason": None,
                "flagged_entity_ids": []
            },
            "validation_status": "VALIDATED",
            "quarantine_status": False,
            "processing_errors": [],
            "audit_metadata": {
                "pipeline_stage": "Stage_5_PostGIS_Deduplication",
                "processor_id": "dedup_engine_v1",
                "execution_duration_ms": 120
            }
        }

        self.stage5_file_path = self.processed_dir / "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855_stage5.json"
        with open(self.stage5_file_path, "w", encoding="utf-8") as f:
            json.dump(self.mock_stage5_contract, f, indent=2)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_stage6_ingestion_contract_generation(self):
        result = self.engine.process_stage5_contract(self.stage5_file_path)

        self.assertEqual(result["contract_version"], CONTRACT_VERSION)
        self.assertEqual(result["source_file_hash"], self.mock_stage5_contract["source_file_hash"])
        self.assertEqual(result["source_sheet_code"], "A-A-18")
        self.assertEqual(result["transaction_status"], "COMMITTED")
        self.assertFalse(result["rollback_status"]["executed_rollback"])
        self.assertTrue(result["validation_results"]["single_parent_check_passed"])
        self.assertTrue(result["validation_results"]["foreign_keys_passed"])
        self.assertEqual(result["validation_results"]["orphan_records_detected"], 0)

        # Verify output stage6 JSON file exists
        stage6_json = self.processed_dir / f"{self.mock_stage5_contract['source_file_hash']}_stage6.json"
        self.assertTrue(stage6_json.exists())

    def test_human_review_gate_enforcement(self):
        unreviewed_stage5 = dict(self.mock_stage5_contract)
        unreviewed_stage5["human_review_status"] = {
            "requires_human_review": True,
            "review_reason": "BOUNDARY_OVERLAP",
            "review_signoff_timestamp": None  # Missing signoff timestamp
        }

        result = self.engine.execute_transactional_ingestion(unreviewed_stage5)

        self.assertEqual(result["transaction_status"], "ROLLED_BACK")
        self.assertTrue(result["rollback_status"]["executed_rollback"])
        self.assertTrue(result["quarantine_audit"]["quarantined"])
        self.assertEqual(result["processing_errors"][0]["error_code"], "ERR_HUMAN_REVIEW_MISSING")

    def test_quarantined_stage5_rejection(self):
        bad_stage5 = dict(self.mock_stage5_contract)
        bad_stage5["quarantine_status"] = True
        bad_stage5["validation_status"] = "FAILED"
        bad_stage5_path = self.processed_dir / "bad_stage5.json"
        with open(bad_stage5_path, "w", encoding="utf-8") as f:
            json.dump(bad_stage5, f, indent=2)

        with self.assertRaises(ValueError):
            self.engine.process_stage5_contract(bad_stage5_path)


if __name__ == "__main__":
    unittest.main()
