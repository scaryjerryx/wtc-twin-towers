#!/usr/bin/env python3
"""
Unit Tests for Stage 1 PDF Acquisition and Preprocessor Script
Phase 4 Automated PDF Parsing Pipeline

Governing Contract: docs/PHASE_4_STAGE_1_DATA_CONTRACT.md (v1.0.0)
"""

import unittest
import shutil
import json
import tempfile
from pathlib import Path
from scripts.pdf_acquisition_preprocessor import Stage1Preprocessor, CONTRACT_VERSION, SHEET_CODE_REGEX


class TestStage1Preprocessor(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path(tempfile.mkdtemp())
        self.incoming_dir = self.test_dir / "incoming"
        self.processed_dir = self.test_dir / "processed"
        self.failed_dir = self.test_dir / "failed"

        self.processor = Stage1Preprocessor(
            incoming_dir=self.incoming_dir,
            processed_dir=self.processed_dir,
            failed_dir=self.failed_dir
        )

        # Create valid test PDF binary content
        self.valid_pdf_path = self.incoming_dir / "drawing_aa18.pdf"
        pdf_content = (
            b"%PDF-1.7\n"
            b"1 0 obj << /Type /Catalog /Pages 2 0 R >> endobj\n"
            b"2 0 obj << /Type /Pages /Kinds [3 0 R] /Count 1 >> endobj\n"
            b"3 0 obj << /Type /Page (A-A-18 DRAWING B1 & B2) >> endobj\n"
            b"xref\n0 4\n0000000000 65535 f\n"
            b"trailer << /Size 4 >>\nstartxref\n180\n%%EOF"
        )
        with open(self.valid_pdf_path, "wb") as f:
            f.write(pdf_content)

        # Create corrupted test PDF
        self.corrupt_pdf_path = self.incoming_dir / "corrupt_drawing.pdf"
        with open(self.corrupt_pdf_path, "wb") as f:
            f.write(b"NOT_A_PDF_HEADER_BINARY_DATA")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_compute_sha256(self):
        hash_val = self.processor.compute_sha256(self.valid_pdf_path)
        self.assertEqual(len(hash_val), 64)
        self.assertTrue(all(c in '0123456789abcdef' for c in hash_val))

    def test_valid_pdf_processing(self):
        result = self.processor.process_file(self.valid_pdf_path)
        
        self.assertEqual(result["contract_version"], CONTRACT_VERSION)
        self.assertEqual(result["validation_status"], "VALIDATED")
        self.assertFalse(result["quarantine_status"])
        self.assertEqual(result["file_name"], "drawing_aa18.pdf")
        self.assertTrue(SHEET_CODE_REGEX.match(result["sheet_code"]))
        self.assertEqual(result["metadata"]["pdf_version"], "1.7")
        self.assertTrue(result["title_block_data"]["title_block_found"])
        self.assertEqual(len(result["processing_errors"]), 0)

        # Check processed JSON file created
        json_path = self.processed_dir / f"{result['file_hash']}_stage1.json"
        self.assertTrue(json_path.exists())

    def test_corrupted_pdf_quarantine_workflow(self):
        result = self.processor.process_file(self.corrupt_pdf_path)

        self.assertTrue(result["human_review_required"])
        self.assertEqual(result["quarantine_reason"], "ERR_PDF_CORRUPTED")
        self.assertTrue(len(result["processing_errors"]) > 0)
        self.assertEqual(result["processing_errors"][0]["error_code"], "ERR_PDF_CORRUPTED")

        # Check quarantine files created in failed_dir
        quarantine_files = list(self.failed_dir.glob("*.json"))
        self.assertTrue(len(quarantine_files) > 0)

    def test_sheet_code_extraction(self):
        code1 = self.processor.extract_sheet_code("drawing_aa18.pdf", "")
        self.assertEqual(code1, "A-A-18")

        code2 = self.processor.extract_sheet_code("drawing_aa121.pdf", "")
        self.assertEqual(code2, "A-A-121")


if __name__ == "__main__":
    unittest.main()
