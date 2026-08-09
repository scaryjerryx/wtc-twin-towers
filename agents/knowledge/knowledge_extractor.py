import re


KNOWN_ENTITIES = [
    "World Trade Center",
    "North Tower",
    "South Tower",
    "Windows on the World",
    "Observation Deck",
    "Austin J Tobin Plaza"
]


def extract_entities(text):

    entities = []

    text_upper = text.upper()

    for entity in KNOWN_ENTITIES:

        if entity.upper() in text_upper:
            entities.append(entity)

    return sorted(
        list(set(entities))
    )


def extract_facts(text):

    facts = []

    #
    # Years
    #
    years = re.findall(
        r"\b(19\d{2}|20\d{2})\b",
        text
    )

    for year in sorted(set(years)):

        year_num = int(year)

        if 1960 <= year_num <= 2001:
            facts.append(
                f"Referenced year {year}"
            )

    #
    # Drawing Books
    #
    drawing_books = re.findall(
        r"Drawing Book\s+\d+",
        text,
        re.IGNORECASE
    )

    for item in drawing_books:

        facts.append(
            item.strip()
        )

    #
    # Column Types
    #
    column_types = re.findall(
        r"Column Type\s+\d+",
        text,
        re.IGNORECASE
    )

    for item in column_types:

        facts.append(
            item.strip()
        )

    #
    # Spandrel Types
    #
    spandrel_types = re.findall(
        r"Spandrel Type\s+[A-Z]",
        text,
        re.IGNORECASE
    )

    for item in spandrel_types:

        facts.append(
            item.strip()
        )

    #
    # Strut Types
    #
    strut_types = re.findall(
        r"Strut Type\s+[A-Z]",
        text,
        re.IGNORECASE
    )

    for item in strut_types:

        facts.append(
            item.strip()
        )

    #
    # Sections
    #
    sections = re.findall(
        r"Section\s+[A-Z]-[A-Z]",
        text,
        re.IGNORECASE
    )

    for item in sections:

        facts.append(
            item.strip()
        )

    #
    # Exterior Wall elevations
    #
    wall_refs = re.findall(
        r"Exterior Wall To EL\.\s*\d+",
        text,
        re.IGNORECASE
    )

    for item in wall_refs:

        facts.append(
            item.strip()
        )

    facts = sorted(
        list(set(facts))
    )

    return facts


if __name__ == "__main__":

    sample = """
    The World Trade Center.

    Drawing Book 1

    Exterior Wall To EL. 363

    Column Type 7000

    Spandrel Type C

    Strut Type F

    Section A-A

    Opened in 1976.
    """

    print()

    print(
        extract_entities(sample)
    )

    print()

    print(
        extract_facts(sample)
    )