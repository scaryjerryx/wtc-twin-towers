from PyPDF2 import PdfReader

from pdf2image import convert_from_path

import pytesseract


def extract_with_pypdf2(pdf_path):

    reader = PdfReader(pdf_path)

    all_text = []

    for page in reader.pages:

        text = page.extract_text()

        if text:
            all_text.append(text)

    return "\n".join(all_text)


def extract_with_ocr(pdf_path):

    pages = convert_from_path(
        pdf_path,
        dpi=300
    )

    all_text = []

    for page_number, image in enumerate(pages, start=1):

        print(
            f"OCR page {page_number}/{len(pages)}"
        )

        text = pytesseract.image_to_string(
            image
        )

        if text:
            all_text.append(text)

    return "\n".join(all_text)


def extract_text(pdf_path):

    text = extract_with_pypdf2(
        pdf_path
    )

    if len(text.strip()) > 100:

        print(
            "Using embedded PDF text"
        )

        return text

    print(
        "No embedded text found. "
        "Switching to OCR..."
    )

    return extract_with_ocr(
        pdf_path
    )