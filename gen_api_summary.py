#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent

SUMMARY_PATH = ROOT / "SUMMARY.md"
API_PATH = ROOT / "api"
TYPES_PATH = API_PATH / "types"
ENUMS_PATH = API_PATH / "enums"

GAME_API_MARKER = "## Game API"


def display_name(file: Path) -> str:
    """
    Returns a readable page name.

    Prefer the first Markdown heading when available. Otherwise,
    fall back to the filename.
    """
    try:
        for line in file.read_text(encoding="utf-8").splitlines():
            stripped = line.strip()

            if stripped.startswith("# "):
                return stripped[2:].strip()
    except OSError:
        pass

    return file.stem.replace("-", " ").replace("_", " ").title()


def sort_key(value: str) -> str:
    return value.casefold()


def scan_types():
    """
    Returns:
        root_pages:
            Types stored directly in api/types/

        grouped_pages:
            Types stored inside api/types/<folder>/
    """
    root_pages = []
    grouped_pages = defaultdict(list)

    if not TYPES_PATH.exists():
        return root_pages, grouped_pages

    for file in TYPES_PATH.rglob("*.md"):
        if file.name.casefold() in {"readme.md", "index.md"}:
            continue

        relative = file.relative_to(TYPES_PATH)
        target = f"api/types/{relative.as_posix()}"
        page = (display_name(file), target)

        if len(relative.parts) == 1:
            root_pages.append(page)
        else:
            category_path = relative.parent.as_posix()
            grouped_pages[category_path].append(page)

    root_pages.sort(key=lambda item: sort_key(item[0]))

    for pages in grouped_pages.values():
        pages.sort(key=lambda item: sort_key(item[0]))

    grouped_pages = dict(
        sorted(
            grouped_pages.items(),
            key=lambda item: sort_key(item[0]),
        )
    )

    return root_pages, grouped_pages


def scan_enums():
    enums = []

    if not ENUMS_PATH.exists():
        return enums

    for file in ENUMS_PATH.rglob("*.md"):
        if file.name.casefold() in {"readme.md", "index.md"}:
            continue

        relative = file.relative_to(ENUMS_PATH)

        enums.append(
            (
                display_name(file),
                f"api/enums/{relative.as_posix()}",
            )
        )

    enums.sort(key=lambda item: sort_key(item[0]))
    return enums


def category_name(category_path: str) -> str:
    return (
        Path(category_path)
        .name
        .replace("-", " ")
        .replace("_", " ")
        .title()
    )


def build_game_api_section() -> str:
    root_types, grouped_types = scan_types()
    enums = scan_enums()

    lines = [
        GAME_API_MARKER,
        "",
        "* [Overview](api/README.md)",
        "* [Types](api/types/README.md)",
    ]

    # Root files appear directly under Types.
    for name, target in root_types:
        lines.append(f"  * [{name}]({target})")

    # Only real folders create category levels.
    for category, pages in grouped_types.items():
        lines.append(f"  * {category_name(category)}")

        for name, target in pages:
            lines.append(f"    * [{name}]({target})")

    lines.append("* [Enums](api/enums/README.md)")

    for name, target in enums:
        lines.append(f"  * [{name}]({target})")

    return "\n".join(lines).rstrip() + "\n"


def main():
    if not SUMMARY_PATH.exists():
        raise FileNotFoundError(
            f"Could not find {SUMMARY_PATH}"
        )

    summary = SUMMARY_PATH.read_text(encoding="utf-8")
    marker_index = summary.find(GAME_API_MARKER)

    if marker_index == -1:
        raise RuntimeError(
            f'Could not find "{GAME_API_MARKER}" in SUMMARY.md'
        )

    preserved_content = summary[:marker_index].rstrip()
    generated_section = build_game_api_section()

    updated_summary = (
        f"{preserved_content}\n\n{generated_section}"
    )

    SUMMARY_PATH.write_text(
        updated_summary,
        encoding="utf-8",
    )

    print("SUMMARY.md Game API section regenerated.")


if __name__ == "__main__":
    main()