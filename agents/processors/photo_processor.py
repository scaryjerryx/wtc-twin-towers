import os
import sys

from agents.discovery.database import get_db_connection
from agents.knowledge.knowledge_extractor import (
    extract_entities,
    extract_facts
)
from agents.knowledge.fact_cleaner import (
    clean_facts
)


def ocr_image(image_path):
    """
    Run Tesseract OCR on an image file.

    Returns extracted text or empty string on failure.
    """
    try:
        import pytesseract
        from PIL import Image

        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)

        return text.strip()

    except Exception as exc:

        print(
            f"OCR failed for {image_path}: {exc}"
        )

        return ""


def query_ai_description(asset_path):
    """
    Look up the most recent ai_analysis row for this asset
    by matching against the local path or R2 key.

    Returns the image_description text or empty string.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    file_name = os.path.basename(asset_path)

    cur.execute(
        """
        SELECT ai.image_description
        FROM ai_analysis ai
        JOIN assets a
          ON a.id = ai.asset_id
        WHERE
          a.local_path ILIKE %s
          OR a.r2_key ILIKE %s
        ORDER BY ai.id DESC
        LIMIT 1
        """,
        (
            f"%{file_name}%",
            f"%{file_name}%",
        ),
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    if row and row[0]:
        return row[0].strip()

    return ""


def store_fact(cur, fact_text, source_file, confidence=50):
    """
    Insert a fact with idempotency, return the fact id.
    """
    cur.execute(
        """
        INSERT INTO facts
        (
            entity_id,
            fact_text,
            confidence
        )
        VALUES
        (
            NULL,
            %s,
            %s
        )
        ON CONFLICT (fact_text)
        DO NOTHING
        """,
        (
            fact_text,
            confidence,
        ),
    )

    cur.execute(
        """
        SELECT id
        FROM facts
        WHERE fact_text = %s
        """,
        (
            fact_text,
        ),
    )

    row = cur.fetchone()

    if row is None:
        return None

    fact_id = row[0]

    cur.execute(
        """
        INSERT INTO fact_sources
        (
            fact_id,
            source_file,
            source_page,
            confidence
        )
        VALUES
        (
            %s,
            %s,
            NULL,
            %s
        )
        ON CONFLICT
        (
            fact_id,
            source_file,
            source_page
        )
        DO NOTHING
        """,
        (
            fact_id,
            source_file,
            confidence,
        ),
    )

    return fact_id


def lookup_asset_id(asset_path):
    """
    Look up the asset ID from the database by local path or R2 key match.
    Returns None if not found.
    """
    conn = get_db_connection()
    cur = conn.cursor()

    file_name = os.path.basename(asset_path)

    cur.execute(
        """
        SELECT id FROM assets
        WHERE
            local_path ILIKE %s
            OR r2_key ILIKE %s
        ORDER BY id DESC
        LIMIT 1
        """,
        (
            f"%{file_name}%",
            f"%{file_name}%",
        ),
    )

    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return row[0]

    return None


def process_photo(asset_path):
    """
    Process a WTC photograph:

    1. Run Tesseract OCR on the image
    2. Look up any AI-generated description (ai_analysis)
    3. Concatenate OCR text + AI description
    4. Extract entities and facts
    5. Store entities and facts with provenance
    6. Return processing summary
    """

    file_name = os.path.basename(asset_path)

    # Look up asset ID for provenance
    asset_id = lookup_asset_id(asset_path)

    if asset_id:
        source_file = f"acquisition_asset_{asset_id}_ocr"
    else:
        # Fallback: use filename if not yet in database
        source_file = f"photo_ocr_{file_name}"

    print()
    print("=" * 60)
    print(f"PHOTO PROCESSOR: {file_name}")
    print("=" * 60)
    print()

    #
    # Step 1: OCR
    #
    print("Running Tesseract OCR ...")
    ocr_text = ocr_image(asset_path)

    if ocr_text:
        print(f"OCR extracted {len(ocr_text)} characters")
    else:
        print("No OCR text extracted")

    #
    # Step 2: AI description
    #
    print("Looking up AI description ...")
    ai_description = query_ai_description(asset_path)

    if ai_description:
        print(
            f"AI description found "
            f"({len(ai_description)} characters)"
        )
    else:
        print("No AI description found")

    #
    # Step 3: Concatenate
    #
    combined_text = ""

    if ocr_text:
        combined_text += ocr_text + "\n"

    if ai_description:
        combined_text += ai_description

    if not combined_text.strip():

        print("No text to process - returning early")
        print()

        return {
            "asset_type": "photo",
            "description": "No extractable text found",
            "entities": [],
            "facts": [],
            "confidence": 0,
        }

    #
    # Step 4: Extract entities and facts
    #
    entities = extract_entities(combined_text)
    raw_facts = extract_facts(combined_text)
    facts = clean_facts(raw_facts)

    print()
    print("Entities found:")
    for entity in sorted(entities):
        print(f"  - {entity}")

    print()
    print("Facts found:")
    for fact in sorted(facts):
        print(f"  - {fact}")

    #
    # Step 5: Store in database
    #
    conn = get_db_connection()
    cur = conn.cursor()

    for entity in entities:

        cur.execute(
            """
            INSERT INTO entities
            (
                name,
                entity_type
            )
            VALUES
            (%s, %s)
            ON CONFLICT (name)
            DO NOTHING
            """,
            (
                entity,
                "photo",
            ),
        )

    fact_ids = []

    for fact in facts:

        fact_id = store_fact(
            cur,
            fact,
            source_file,
            confidence=60,
        )

        if fact_id is not None:
            fact_ids.append(fact_id)

    conn.commit()
    cur.close()
    conn.close()

    print()
    print("=" * 60)
    print("PHOTO PROCESSING COMPLETE")
    print("=" * 60)
    print()
    print(f"  Asset:        {file_name}")
    print(f"  Entities:     {len(entities)}")
    print(f"  Facts stored: {len(fact_ids)}")
    print()

    return {
        "asset_type": "photo",
        "description": ai_description
        if ai_description
        else "Photo processed via OCR",
        "entities": sorted(entities),
        "facts": sorted(facts),
        "confidence": 60 if facts else 30,
    }


if __name__ == "__main__":

    if len(sys.argv) < 2:

        print(
            "Usage: "
            "python -m agents.processors.photo_processor "
            "<image_path>"
        )

        sys.exit(1)

    result = process_photo(sys.argv[1])

    print()
    print("Result:")
    print(result)