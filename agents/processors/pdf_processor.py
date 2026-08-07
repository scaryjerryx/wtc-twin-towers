from pathlib import Path


def process_pdf(asset_path):

    file_size = Path(asset_path).stat().st_size

    return {
        "asset_type": "pdf",
        "description": (
            f"PDF detected. "
            f"Size: {file_size} bytes."
        ),
        "confidence": 75,
        "status": "ready_for_text_extraction"
    }