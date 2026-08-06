import json

with open("research/targets.json", "r") as f:
    targets = json.load(f)

with open("research/sources.json", "r") as f:
    sources = json.load(f)

for source in sources:
    for target in targets:

        print(
            f"Searching: {target} "
            f"from {source['name']}"
        )