from pathlib import Path

PROJECT_ROOT = Path("/opt/wtc/wtc-twin-towers")

REPLACEMENTS = {
    "from agents.downloader.r2 import upload_file":
        "from agents.downloader.r2 import upload_file",

    "from agents.knowledge.knowledge_extractor import (":
        "from agents.knowledge.knowledge_extractor import (",

    "from agents.knowledge.entity_resolver import (":
        "from agents.knowledge.entity_resolver import (",

    "from agents.processors.pdf_text_extractor import extract_text":
        "from agents.processors.pdf_text_extractor import extract_text",
}

updated = []

for py_file in PROJECT_ROOT.rglob("*.py"):

    text = py_file.read_text(encoding="utf-8")

    original = text

    for old, new in REPLACEMENTS.items():
        text = text.replace(old, new)

    if text != original:
        py_file.write_text(
            text,
            encoding="utf-8"
        )

        updated.append(str(py_file))

print()
print("Updated files:")
print("----------------")

for file in updated:
    print(file)

print()
print(f"Total: {len(updated)} files")
