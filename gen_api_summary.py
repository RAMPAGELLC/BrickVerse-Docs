#!/usr/bin/env python3

"""
Regenerates the Game API section inside SUMMARY.md.

Scans:
    api/types/
    api/enums/

and replaces everything beginning at:

    ## Game API

with a freshly generated navigation.

README.md files become folder landing pages.
"""

from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent

SUMMARY = ROOT / "SUMMARY.md"
API = ROOT / "api"
TYPES = API / "types"
ENUMS = API / "enums"


def slug(name: str):
    return name.lower()


def scan_types():
    categories = defaultdict(list)

    if not TYPES.exists():
        return categories

    for file in TYPES.rglob("*.md"):
        if file.name.lower() == "readme.md":
            continue

        rel = file.relative_to(TYPES)

        if len(rel.parts) == 1:
            category = "General"
            name = file.stem
            path = f"api/types/{file.name}"
        else:
            category = rel.parts[0]
            name = file.stem
            path = "api/types/" + rel.as_posix()

        categories[category].append((name, path))

    for cat in categories:
        categories[cat].sort(key=lambda x: slug(x[0]))

    return dict(sorted(categories.items()))


def scan_enums():
    enums = []

    if not ENUMS.exists():
        return enums

    for file in ENUMS.rglob("*.md"):
        if file.name.lower() == "readme.md":
            continue

        enums.append((file.stem, "api/enums/" + file.relative_to(ENUMS).as_posix()))

    enums.sort(key=lambda x: slug(x[0]))
    return enums


def build_section():
    lines = []

    lines.append("## Game API")
    lines.append("")
    lines.append("* [Overview](api/README.md)")
    lines.append("")
    lines.append("* [Types](api/types/README.md)")

    categories = scan_types()

    for category, pages in categories.items():
        lines.append(f"  * **{category}**")

        for name, path in pages:
            lines.append(f"    * [{name}]({path})")

    lines.append("")
    lines.append("* [Enums](api/enums/README.md)")

    for name, path in scan_enums():
        lines.append(f"  * [{name}]({path})")

    return "\n".join(lines) + "\n"


def main():
    if not SUMMARY.exists():
        raise FileNotFoundError("SUMMARY.md not found.")

    summary = SUMMARY.read_text(encoding="utf-8")

    marker = "## Game API"

    idx = summary.find(marker)

    if idx == -1:
        raise RuntimeError("Couldn't locate '## Game API' in SUMMARY.md")

    summary = summary[:idx].rstrip() + "\n\n" + build_section()

    SUMMARY.write_text(summary, encoding="utf-8")

    print("SUMMARY.md regenerated successfully.")


if __name__ == "__main__":
    main()