import re


def canonicalize_fact(fact):

    fact = fact.strip()

    #
    # Drawing Book
    #
    match = re.search(
        r"DRAWING BOOK\s+(\d+)",
        fact,
        re.IGNORECASE
    )

    if match:

        return (
            f"Drawing Book "
            f"{match.group(1)}"
        )

    #
    # Exterior Wall
    #
    match = re.search(
        r"EXTERIOR WALL TO EL\.?\s*(\d+)",
        fact,
        re.IGNORECASE
    )

    if match:

        return (
            f"Exterior Wall To EL. "
            f"{match.group(1)}"
        )

    #
    # Column Type
    #
    match = re.search(
        r"COLUMN TYPE\s+(\d+)",
        fact,
        re.IGNORECASE
    )

    if match:

        return (
            f"Column Type "
            f"{match.group(1)}"
        )

    #
    # Strut Type
    #
    match = re.search(
        r"STRUT TYPE\s+([A-Z])",
        fact,
        re.IGNORECASE
    )

    if match:

        return (
            f"Strut Type "
            f"{match.group(1).upper()}"
        )

    #
    # Spandrel Type
    #
    match = re.search(
        r"SPANDREL TYPE\s+([A-Z])",
        fact,
        re.IGNORECASE
    )

    if match:

        return (
            f"Spandrel Type "
            f"{match.group(1).upper()}"
        )

    return fact