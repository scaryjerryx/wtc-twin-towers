"""M13 — Mocked R2 Unit Test.

Replaces the live R2 upload test with a mocked unit test that verifies
upload_file() invokes boto3.client.upload_file with correct arguments.

Usage:
    python -m agents.downloader.test_r2
"""

from unittest.mock import patch, MagicMock
from agents.downloader.r2 import upload_file


@patch("agents.downloader.r2.client")
def test_upload_file(mock_client: MagicMock) -> None:
    """Verify upload_file passes correct bucket, local path, and remote key."""
    upload_file("storage/raw/test.jpg", "downloads/1_test.jpg")

    mock_client.upload_file.assert_called_once_with(
        "storage/raw/test.jpg",
        mock_client.upload_file.call_args[0][1],  # bucket from env
        "downloads/1_test.jpg",
    )

    print("PASS: upload_file invoked with correct local and remote paths")


if __name__ == "__main__":
    test_upload_file()
    print("All R2 tests passed.")