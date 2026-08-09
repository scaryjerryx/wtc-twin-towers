import re

from agents.knowledge.fact_normalizer import (
    canonicalize_fact
)


VALID_COLUMN_TYPES = {
    "1000",
    "2000",
    "3000",
    "4000",
    "5000",
    "6000",
    "7000",
    "8000"
}

VALID_STRUT_TYPES = {
    "D",
    "E",
    "F",
    "H"
}

VALID_SPANDREL_TYPES = {
    "C",
    "D"
}


def clean_facts(facts):

    cleaned = []

    for fact in facts:

        fact = canonicalize_fact(
            fact
        )

        #
        # Years
        #
        if fact.startswith(
            "Referenced year"
        ):

            match = re.search(
                r"(\d{4})",
                fact
            )

            if match:

                year = int(
                    match.group(1)
                )

                if 1965 <= year <= 1975:

                    cleaned.append(
                        fact
                    )

            continue

        #
        # Column Types
        #
        if "COLUMN TYPE" in fact.upper():

            match = re.search(
                r"(\d+)",
                fact
            )

            if match:

                value = match.group(1)

                if value in VALID_COLUMN_TYPES:

                    cleaned.append(
                        f"Column Type {value}"
                    )

            continue

        #
        # Strut Types
        #
        if "STRUT TYPE" in fact.upper():

            match = re.search(
                r"STRUT TYPE\s+([A-Z])",
                fact.upper()
            )

            if match:

                value = match.group(1)

                if value in VALID_STRUT_TYPES:

                    cleaned.append(
                        f"Strut Type {value}"
                    )

            continue

        #
        # Spandrel Types
        #
        if "SPANDREL TYPE" in fact.upper():

            match = re.search(
                r"SPANDREL TYPE\s+([A-Z])",
                fact.upper()
            )

            if match:

                value = match.group(1)

                if value in VALID_SPANDREL_TYPES:

                    cleaned.append(
                        f"Spandrel Type {value}"
                    )

            continue

        #
        # Sections
        #
        if fact.upper().startswith(
            "SECTION"
        ):

            if fact.upper() in {
                "SECTION A-A",
                "SECTION B-B",
                "SECTION C-C"
            }:

                cleaned.append(
                    fact.upper()
                )

            continue

        #
        # Drawing Books
        #
        if fact.startswith(
            "Drawing Book"
        ):

            cleaned.append(
                fact
            )

            continue

        #
        # Exterior Walls
        #
        if fact.startswith(
            "Exterior Wall"
        ):

            cleaned.append(
                fact
            )

            continue

    return sorted(
        list(set(cleaned))
    )