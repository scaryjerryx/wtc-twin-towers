import re


def extract_entities(text):

    entities = []

    patterns = [
        r"World Trade Center",
        r"North Tower",
        r"South Tower",
        r"Windows on the World",
        r"Austin J\. Tobin Plaza",
        r"Observation Deck"
    ]

    for pattern in patterns:

        matches = re.findall(
            pattern,
            text,
            flags=re.IGNORECASE
        )

        if matches:

            entities.append(
                matches[0]
            )

    return list(set(entities))


def extract_facts(text):

    facts = []

    years = re.findall(
        r"\b(19\d{2}|20\d{2})\b",
        text
    )

    for year in years:

        facts.append(
            f"Referenced year {year}"
        )

    return facts


if __name__ == "__main__":

    sample = """
    Windows on the World opened in 1976.
    Located at the World Trade Center.
    """

    print(
        extract_entities(sample)
    )

    print(
        extract_facts(sample)
    )