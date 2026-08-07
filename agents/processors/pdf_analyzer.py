from agents.processors.pdf_text_extractor import extract_text

from agents.knowledge.knowledge_extractor import (
    extract_entities,
    extract_facts
)


def analyze_pdf(pdf_path):

    text = extract_text(pdf_path)

    entities = extract_entities(text)

    facts = extract_facts(text)

    return {
        "text_length": len(text),
        "entities": entities,
        "facts": facts,
        "status": "analyzed"
    }


if __name__ == "__main__":

    pdf_file = input(
        "PDF Path: "
    )

    result = analyze_pdf(
        pdf_file
    )

    print()
    print("PDF Analysis")
    print("------------")

    print(
        f"Text Length: "
        f"{result['text_length']}"
    )

    print()

    print("Entities:")

    for entity in result["entities"]:

        print(
            f" - {entity}"
        )

    print()

    print("Facts:")

    for fact in result["facts"]:

        print(
            f" - {fact}"
        )
