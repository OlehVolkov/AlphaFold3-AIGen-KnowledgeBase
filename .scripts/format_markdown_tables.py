#!/usr/bin/env python3
"""
Normalize markdown tables across the repository.

What this script does:
- finds simple pipe-based markdown tables outside fenced code blocks
- rewrites them into a consistent aligned format accepted by markdownlint MD060
- keeps the rest of each file unchanged

What to review first when adapting to another repository:
- table detection assumes ordinary markdown pipe tables, not HTML tables
- cell splitting assumes literal `|` is a column separator; repositories with many
  escaped pipes or unusual inline syntax inside tables may need a stricter parser
- file discovery currently walks the whole repository and skips only common hidden
  or generated directories listed in SKIP_DIRS
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse


SKIP_DIRS = {".git", ".obsidian", ".smart-env", ".venv", "__pycache__", "node_modules"}


@dataclass
class TableBlock:
    start: int
    end: int
    lines: list[str]


def is_fence(line: str) -> bool:
    stripped = line.lstrip()
    return stripped.startswith("```") or stripped.startswith("~~~")


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    cells: list[str] = []
    current: list[str] = []
    escaped = False
    for char in stripped:
        if escaped:
            current.append(char)
            escaped = False
            continue
        if char == "\\":
            current.append(char)
            escaped = True
            continue
        if char == "|":
            cells.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    cells.append("".join(current).strip())
    return cells


def is_table_row(line: str) -> bool:
    stripped = line.strip()
    if "|" not in stripped:
        return False
    if stripped.startswith(">"):
        return False
    return True


def is_separator_row(line: str) -> bool:
    cells = split_row(line)
    if not cells:
        return False
    for cell in cells:
        compact = cell.replace(" ", "")
        if not compact:
            return False
        if not set(compact) <= {"-", ":"}:
            return False
        if compact.replace(":", "").count("-") < 3:
            return False
    return True


def find_tables(lines: list[str]) -> list[TableBlock]:
    tables: list[TableBlock] = []
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if is_fence(line):
            in_fence = not in_fence
            i += 1
            continue
        if in_fence:
            i += 1
            continue
        if i + 1 < len(lines) and is_table_row(lines[i]) and is_separator_row(lines[i + 1]):
            start = i
            j = i + 2
            while j < len(lines) and is_table_row(lines[j]) and lines[j].strip():
                j += 1
            tables.append(TableBlock(start=start, end=j, lines=lines[start:j]))
            i = j
            continue
        i += 1
    return tables


def normalize_alignment_cell(cell: str) -> str:
    compact = cell.replace(" ", "")
    left = compact.startswith(":")
    right = compact.endswith(":")
    if left and right:
        return ":---:"
    if left:
        return ":---"
    if right:
        return "---:"
    return "---"


def format_table(lines: list[str]) -> list[str]:
    rows = [split_row(line) for line in lines]
    width = max(len(row) for row in rows)
    padded_rows = [row + [""] * (width - len(row)) for row in rows]
    header = padded_rows[0]
    separator = [normalize_alignment_cell(cell) for cell in padded_rows[1]]
    data_rows = padded_rows[2:]

    def render_row(row: list[str]) -> str:
        rendered = ["|"]
        for cell in row:
            rendered.append(f" {cell} |" if cell else " |")
        return "".join(rendered)

    output = [render_row(header), render_row(separator)]
    output.extend(render_row(row) for row in data_rows)
    return output


def normalize_tables_in_text(text: str) -> tuple[str, int]:
    lines = text.splitlines()
    tables = find_tables(lines)
    if not tables:
        return text, 0

    new_lines: list[str] = []
    cursor = 0
    changed = 0
    for table in tables:
        new_lines.extend(lines[cursor : table.start])
        formatted = format_table(table.lines)
        if formatted != table.lines:
            changed += 1
        new_lines.extend(formatted)
        cursor = table.end
    new_lines.extend(lines[cursor:])

    normalized = "\n".join(new_lines)
    if text.endswith("\n"):
        normalized += "\n"
    return normalized, changed


def iter_markdown_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize markdown tables in repository files.")
    parser.add_argument("paths", nargs="*", default=["."], help="Files or directories to process.")
    args = parser.parse_args()

    targets: list[Path] = []
    for raw in args.paths:
        path = Path(raw)
        if path.is_dir():
            targets.extend(iter_markdown_files(path))
        elif path.suffix.lower() == ".md" and path.exists():
            targets.append(path)

    seen: set[Path] = set()
    changed_files = 0
    changed_tables = 0
    for path in targets:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        original = path.read_text(encoding="utf-8")
        normalized, count = normalize_tables_in_text(original)
        if count:
            path.write_text(normalized, encoding="utf-8", newline="\n")
            changed_files += 1
            changed_tables += count

    print(f"changed_files={changed_files} changed_tables={changed_tables}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
