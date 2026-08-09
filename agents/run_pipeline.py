"""M15 — Acquisition Pipeline Orchestrator.

Executes the automated stages of the evidence acquisition pipeline
in order.  Manual promotion (manual_promote.py) is a human-in-the-loop
step and is not included.

All stages are idempotent — safe to run repeatedly.

Usage:
    python -m agents.run_pipeline
"""

from __future__ import annotations

import subprocess
import sys


STAGES: list[tuple[str, str]] = [
    (
        "Source Seeding",
        "agents.discovery.main",
    ),
    (
        "Search Request Generation",
        "agents.discovery.build_searches",
    ),
    (
        "Candidate Discovery",
        "agents.discovery.find_candidates",
    ),
    (
        "Discovery Queue",
        "agents.discovery.queue_discoveries",
    ),
    (
        "Downloader",
        "agents.downloader.main",
    ),
    (
        "Metadata Processing",
        "agents.metadata.mock_analyze",
    ),
]


def main() -> None:
    python = sys.executable

    print("=" * 60)
    print("WTC ACQUISITION PIPELINE STARTED")
    print("=" * 60)

    for label, module in STAGES:
        print()
        print("-" * 60)
        print(f"STAGE: {label}")
        print("-" * 60)
        print()

        result = subprocess.run(
            [python, "-m", module],
            capture_output=False,
        )

        if result.returncode != 0:
            print(f"\nPipeline stopped: {label} failed (exit code {result.returncode})")
            sys.exit(result.returncode)

        print()

    print()
    print("=" * 60)
    print("WTC ACQUISITION PIPELINE COMPLETE")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()