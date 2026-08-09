import shutil
from datetime import datetime
from pathlib import Path

from agents.knowledge.pdf_knowledge_pipeline import (
    process_pdf
)

from agents.knowledge.fact_relationship_builder import (
    build_relationships
)


INCOMING_DIR = Path("data/incoming_pdfs")
PROCESSED_DIR = Path("data/processed_pdfs")
FAILED_DIR = Path("data/failed_pdfs")


def timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def safe_destination(directory, original_name):

    destination = directory / original_name

    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix

    return directory / (
        f"{stem}_{timestamp()}{suffix}"
    )


def move_file(source_path, target_dir):

    target_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    destination = safe_destination(
        target_dir,
        source_path.name
    )

    shutil.move(
        str(source_path),
        str(destination)
    )

    return destination


def find_pdfs():

    INCOMING_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    pdfs = []

    for pattern in [
        "*.pdf",
        "*.PDF"
    ]:

        pdfs.extend(
            INCOMING_DIR.glob(pattern)
        )

    return sorted(pdfs)


def process_all_pdfs():

    pdfs = find_pdfs()

    if not pdfs:

        print()
        print("No PDFs found.")
        print(
            f"Drop PDFs into: {INCOMING_DIR}"
        )
        print()

        return

    print()
    print("=" * 60)
    print("AUTOMATED PDF INGESTION STARTED")
    print("=" * 60)
    print()

    print(
        f"PDFs found: {len(pdfs)}"
    )

    success_count = 0
    failed_count = 0

    for pdf_path in pdfs:

        print()
        print("=" * 60)
        print(f"Processing: {pdf_path.name}")
        print("=" * 60)
        print()

        try:

            process_pdf(
                str(pdf_path)
            )

            moved_to = move_file(
                pdf_path,
                PROCESSED_DIR
            )

            print()
            print(
                f"Processed and moved to: {moved_to}"
            )

            success_count += 1

        except Exception as error:

            print()
            print("FAILED")
            print(
                f"File: {pdf_path}"
            )
            print(
                f"Error: {error}"
            )

            move_file(
                pdf_path,
                FAILED_DIR
            )

            failed_count += 1

    print()
    print("=" * 60)
    print("REBUILDING FACT RELATIONSHIPS")
    print("=" * 60)

    build_relationships()

    print()
    print("=" * 60)
    print("AUTOMATED PDF INGESTION COMPLETE")
    print("=" * 60)
    print()

    print(
        f"Successful: {success_count}"
    )

    print(
        f"Failed: {failed_count}"
    )

    print()


if __name__ == "__main__":

    process_all_pdfs()