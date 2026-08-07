from agents.ingestion.automated_ingestion import (
    process_all_pdfs
)

from agents.verification.fact_verifier import (
    verify_facts
)

from agents.knowledge.fact_relationship_builder import (
    build_relationships
)

from agents.timeline.timeline_builder import (
    build_timeline
)


def run_engine():

    print()
    print("=" * 80)
    print("WTC KNOWLEDGE ENGINE STARTED")
    print("=" * 80)
    print()

    print()
    print("=" * 80)
    print("STEP 1: AUTOMATED PDF INGESTION")
    print("=" * 80)
    print()

    process_all_pdfs()

    print()
    print("=" * 80)
    print("STEP 2: FACT VERIFICATION")
    print("=" * 80)
    print()

    verify_facts()

    print()
    print("=" * 80)
    print("STEP 3: RELATIONSHIP BUILDING")
    print("=" * 80)
    print()

    build_relationships()

    print()
    print("=" * 80)
    print("STEP 4: TIMELINE BUILD")
    print("=" * 80)
    print()

    build_timeline()

    print()
    print("=" * 80)
    print("WTC KNOWLEDGE ENGINE COMPLETE")
    print("=" * 80)
    print()


if __name__ == "__main__":

    run_engine()
