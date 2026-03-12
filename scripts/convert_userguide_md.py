from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup


ROOT = Path(__file__).resolve().parent.parent
SOURCE_PATH = ROOT / "UserGuide.md"
DOCS_DIR = ROOT / "docs"
MANIFEST_PATH = DOCS_DIR / "manifest.json"


@dataclass
class Section:
    level: int
    title: str
    anchor: str


@dataclass
class Chapter:
    title: str
    slug: str
    filename: str
    content: list[str] = field(default_factory=list)
    sections: list[Section] = field(default_factory=list)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^\d+(?:\.\d+)*\s*", "", value)
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "section"


def clean_line(line: str) -> str:
    line = line.rstrip()
    line = html.unescape(line)
    line = line.replace("\u00a0", " ")
    line = line.replace("…", "...")
    line = fix_mojibake(line)
    return line


def fix_mojibake(text: str) -> str:
    replacements = {
        "вЂ™": "'",
        "вЂ“": "-",
        "вЂ”": "-",
        "вЂњ": '"',
        "вЂќ": '"',
        "вЂ¦": "...",
        "в†’": "->",
        "â†’": "->",
        "â€“": "-",
        "â€”": "-",
        "â€˜": "'",
        "â€™": "'",
        "â€œ": '"',
        "â€�": '"',
        "â€¦": "...",
    }
    for bad, good in replacements.items():
        text = text.replace(bad, good)
    return text


def strip_contents_block(lines: list[str]) -> list[str]:
    start = None
    end = None
    for index, line in enumerate(lines):
        if line.strip() == "# Contents":
            start = index
            continue
        if start is not None and re.match(r"^#\s+1\s+", line):
            end = index
            break
    if start is None:
        return lines
    return lines[:start] + lines[end:]


def split_preface(lines: list[str]) -> tuple[list[str], list[str]]:
    first_heading = next((i for i, line in enumerate(lines) if re.match(r"^#\s+\d+\s+", line)), len(lines))
    preface = [line for line in lines[:first_heading] if line.strip()]
    rest = lines[first_heading:]
    return preface, rest


def new_chapter(title: str, index: int) -> Chapter:
    slug = slugify(title)
    return Chapter(
        title=title.strip(),
        slug=slug,
        filename=f"{index:02d}-{slug}.md",
    )


def write_chapter(chapter: Chapter) -> None:
    body = "\n".join(normalize_chapter_lines(chapter.content)).strip() + "\n"
    (DOCS_DIR / chapter.filename).write_text(body, encoding="utf-8")


def build_manifest(chapters: list[Chapter]) -> None:
    payload = {
        "title": "MoShell UserGuide Content",
        "source": str(SOURCE_PATH.name),
        "chapters": [
            {
                "title": chapter.title,
                "slug": chapter.slug,
                "file": chapter.filename,
                "sections": [
                    {
                        "level": section.level,
                        "title": section.title,
                        "anchor": section.anchor,
                    }
                    for section in chapter.sections
                ],
            }
            for chapter in chapters
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def is_ascii_art_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return any(
        (
            stripped.count("\\*") >= 4,
            stripped == "|",
            stripped.startswith("MO-->"),
            stripped.startswith("- +"),
            stripped.startswith("- |"),
            "++++++" in stripped,
        )
    )


def convert_joplin_table(html_line: str) -> list[str]:
    soup = BeautifulSoup(html_line, "html.parser")
    table = soup.find("table")
    if table is None:
        return [html_line]

    rows = []
    for tr in table.find_all("tr"):
        cells = []
        for cell in tr.find_all(["th", "td"]):
            text = " ".join(cell.stripped_strings)
            cells.append(text)
        if cells:
            rows.append(cells)

    if not rows:
        return []

    max_cols = max(len(row) for row in rows)
    padded_rows = [row + [""] * (max_cols - len(row)) for row in rows]
    markdown = [
        "| " + " | ".join(padded_rows[0]) + " |",
        "| " + " | ".join(["---"] * max_cols) + " |",
    ]
    for row in padded_rows[1:]:
        markdown.append("| " + " | ".join(row) + " |")
    return markdown


def normalize_list_line(line: str) -> str:
    line = re.sub(r"^(\s*)- - - -\s+", r"\1- ", line)
    line = re.sub(r"^(\s*)- - -\s+", r"\1- ", line)
    line = re.sub(r"^(\s*)- - (\d+\.\s+)", r"\1\2", line)
    line = re.sub(r"^(\s*)- -\s+", r"\1- ", line)
    line = re.sub(r"^(\s*)- (\d+\.\s+)", r"\1\2", line)
    return line


def normalize_chapter_lines(lines: list[str]) -> list[str]:
    normalized: list[str] = []
    in_code = False
    pending_code: list[str] = []

    def flush_code() -> None:
        nonlocal pending_code
        if not pending_code:
            return
        normalized.append("```text")
        normalized.extend(pending_code)
        normalized.append("```")
        pending_code = []

    index = 0
    while index < len(lines):
        raw_line = lines[index]
        line = normalize_list_line(raw_line)
        next_line = normalize_list_line(lines[index + 1]) if index + 1 < len(lines) else ""

        if line.startswith("<div class=\"joplin-table-wrapper\">"):
            flush_code()
            normalized.extend(convert_joplin_table(line))
            index += 1
            continue

        if line.startswith("```"):
            flush_code()
            in_code = not in_code
            normalized.append(line)
            index += 1
            continue

        short_pipe_art = (
            not in_code
            and re.match(r"^\|.*\|$", line.strip())
            and len(re.findall(r"\|", line)) <= 2
            and len(line.strip()) < 48
            and not re.match(r"^\|\s*(---\s*\|)+\s*$", next_line.strip())
        )

        if not in_code and (is_ascii_art_line(line) or short_pipe_art):
            pending_code.append(line)
            index += 1
            continue

        if pending_code and not line.strip():
            pending_code.append("")
            index += 1
            continue

        flush_code()

        line = re.sub(r"(\*\*List of checks:\*\*)$", r"\n\n\1", line)
        normalized.append(line)
        index += 1

    flush_code()

    compacted: list[str] = []
    blank_count = 0
    for line in normalized:
        if line.strip():
            blank_count = 0
            compacted.append(line)
            continue
        blank_count += 1
        if blank_count <= 2:
            compacted.append("")
    return semantic_cleanup(compacted)


def semantic_cleanup(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    current_section = ""
    index = 0

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if stripped == "flag":
            index += 1
            continue

        embedded_heading = re.match(r"^(.*\S)\s+(\*\*[A-Z][^*]+:\*\*)\s*$", line)
        if embedded_heading and not stripped.startswith("**"):
            cleaned.append(embedded_heading.group(1))
            cleaned.append("")
            cleaned.append(embedded_heading.group(2))
            index += 1
            continue

        if re.match(r"^\\[-=]{10,}$", stripped):
            block = [line]
            index += 1
            while index < len(lines):
                probe = lines[index]
                probe_stripped = probe.strip()
                if not probe_stripped:
                    break
                if probe_stripped.startswith("#") or probe_stripped.startswith("**") and re.match(r"^\*\*\d+\.", probe_stripped):
                    break
                block.append(probe)
                index += 1
            cleaned.append("```text")
            cleaned.extend(block)
            cleaned.append("```")
            continue

        if stripped in {"Arguments:", "**Arguments:**"}:
            current_section = "arguments"
        elif stripped in {"Options:", "**Options:**"}:
            current_section = "options"
        elif stripped in {"Switches:", "**Switches:**"}:
            current_section = "switches"
        elif stripped in {"Examples:", "**Examples:**"}:
            current_section = "examples"
        elif stripped.startswith("#") or re.match(r"^\*\*\d+\.", stripped):
            current_section = ""

        if current_section in {"arguments", "options", "switches"} and stripped not in {
            "Arguments:",
            "**Arguments:**",
            "Options:",
            "**Options:**",
            "Switches:",
            "**Switches:**",
        }:
            if stripped and not stripped.startswith(("-", "#", "**", "```", "|")):
                if re.match(r"^(all|root|no argument|<[^>]+>|\\-?[A-Za-z0-9<].*?|[A-Za-z0-9_./()=-]+)\s*:", stripped):
                    line = f"- {stripped}"

        if current_section == "examples":
            if stripped and re.match(r"^\d+\.\s+\*\*[^*]+\*\*$", stripped):
                line = stripped

        cleaned.append(line)
        index += 1

    return cleaned


def main() -> None:
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Missing source file: {SOURCE_PATH}")

    raw_lines = SOURCE_PATH.read_text(encoding="utf-8").splitlines()
    lines = [clean_line(line) for line in raw_lines]
    lines = strip_contents_block(lines)
    preface, content_lines = split_preface(lines)

    DOCS_DIR.mkdir(parents=True, exist_ok=True)

    chapters: list[Chapter] = []
    if preface:
        overview = new_chapter("0 Overview", 0)
        overview.content.extend(preface)
        chapters.append(overview)

    current: Chapter | None = None
    chapter_index = 1
    section_counts: dict[str, int] = {}

    for line in content_lines:
        if re.match(r"^#\s+\d+\s+", line):
            current = new_chapter(line[2:].strip(), chapter_index)
            current.content.append(line)
            chapters.append(current)
            chapter_index += 1
            section_counts = {}
            continue

        if current is None:
            continue

        current.content.append(line)

        heading_match = re.match(r"^(#{2,3})\s+(.+)$", line)
        if heading_match:
            level = len(heading_match.group(1))
            title = heading_match.group(2).strip()
            anchor_base = slugify(title)
            count = section_counts.get(anchor_base, 0)
            section_counts[anchor_base] = count + 1
            anchor = anchor_base if count == 0 else f"{anchor_base}-{count + 1}"
            current.sections.append(
                Section(
                    level=level,
                    title=title,
                    anchor=anchor,
                )
            )

    for chapter in chapters:
        write_chapter(chapter)

    build_manifest(chapters)
    print(f"Wrote {len(chapters)} chapter files to {DOCS_DIR}")


if __name__ == "__main__":
    main()
