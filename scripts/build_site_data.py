from __future__ import annotations

import json
from pathlib import Path

from bs4 import BeautifulSoup
import markdown


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
SITE_DIR = ROOT / "site"
MANIFEST_PATH = DOCS_DIR / "manifest.json"
OUTPUT_PATH = SITE_DIR / "guide-data.json"
TRANSLATIONS_PATH = ROOT / "translations" / "ru.json"


def normalize_source(source: str) -> str:
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
        "»>": "->",
    }
    for bad, good in replacements.items():
        source = source.replace(bad, good)

    # Preserve command placeholders like <motype-filter> as text, not HTML tags.
    source = source.replace("<ipaddress>", "&lt;ipaddress&gt;")
    source = source.replace("</ipaddress>", "&lt;/ipaddress&gt;")
    source = source.replace("<filename>", "&lt;filename&gt;")
    source = source.replace("</filename>", "&lt;/filename&gt;")
    source = source.replace("<value2-filter>", "&lt;value2-filter&gt;")
    source = source.replace("</value2-filter>", "&lt;/value2-filter&gt;")
    source = source.replace("<value3-filter>", "&lt;value3-filter&gt;")
    source = source.replace("</value3-filter>", "&lt;/value3-filter&gt;")
    source = source.replace("<Trace-", "&lt;Trace-")
    source = source.replace("<boardGroup(s)>", "&lt;boardGroup(s)&gt;")

    import re
    source = re.sub(r"<([A-Za-z0-9][A-Za-z0-9_./,:=|()\-*? ]{0,80})>", r"&lt;\1&gt;", source)
    return source


def render_markdown(source: str) -> str:
    return markdown.markdown(
        normalize_source(source),
        extensions=[
            "tables",
            "fenced_code",
            "sane_lists",
            "smarty",
            "nl2br",
        ],
        output_format="html5",
    )


def assign_heading_ids(html: str, sections: list[dict[str, str]]) -> str:
    soup = BeautifulSoup(html, "html.parser")
    headings = soup.find_all(["h2", "h3"])
    for heading, section in zip(headings, sections):
        heading["id"] = section["anchor"]
    return str(soup)


def enhance_html(html: str, page_title: str | None = None) -> str:
    soup = BeautifulSoup(html, "html.parser")

    for table in soup.find_all("table"):
        wrapper = soup.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrapper)

    for pre in soup.find_all("pre"):
        classes = pre.code.get("class", []) if pre.code else []
        if "language-text" in classes:
            code_text = pre.get_text("\n")
            line_lengths = [len(line) for line in code_text.splitlines() if line.strip()]
            class_names = [*pre.get("class", []), "is-console"]
            if line_lengths and max(line_lengths) > 120:
                class_names.append("is-wide")
            if any(marker in code_text for marker in ("====", "----", "++++", "|", "\\----", "\\====")):
                class_names.append("is-ascii")
            pre["class"] = class_names

    for p in soup.find_all("p"):
        text = p.get_text(" ", strip=True)
        strong = p.find("strong")
        if strong and text == strong.get_text(" ", strip=True):
            normalized = text.replace("\\", "")
            if normalized in {"Arguments:", "Options:", "Examples:", "Switches:"}:
                label = soup.new_tag("p", attrs={"class": "section-label"})
                label.string = normalized[:-1]
                p.replace_with(label)
                continue
            if normalized.endswith(":") and len(normalized) <= 48:
                label = soup.new_tag("p", attrs={"class": "section-label"})
                label.string = normalized[:-1]
                p.replace_with(label)
                continue
            if normalized.startswith(tuple(f"4.{n}." for n in range(1, 10))) or normalized.startswith(
                tuple(f"{n}.{m}." for n in range(1, 10) for m in range(1, 10))
            ):
                heading = soup.new_tag("h4")
                heading.string = normalized
                p.replace_with(heading)
                continue
            label = soup.new_tag("p", attrs={"class": "section-label"})
            label.string = normalized.rstrip(":")
            p.replace_with(label)
            continue

        if text.endswith(":") and len(text) <= 40:
            next_sibling = p.find_next_sibling()
            if next_sibling and next_sibling.name in {"ul", "ol", "pre", "table", "div"}:
                label = soup.new_tag("p", attrs={"class": "section-label"})
                label.string = text[:-1]
                p.replace_with(label)
                continue

    for strong in soup.find_all("strong"):
        if strong.get_text(strip=True) == "??":
            badge = soup.new_tag("span", attrs={"class": "broken-ref"})
            badge.string = "section reference missing"
            strong.replace_with(badge)

    first_h1 = soup.find("h1")
    if first_h1 is not None:
        first_h1["class"] = [*first_h1.get("class", []), "page-kicker"]
        if page_title:
            first_h1.string = page_title

    return str(soup)


def plain_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    return " ".join(soup.stripped_strings)


def build_payload() -> dict:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    translations = (
        json.loads(TRANSLATIONS_PATH.read_text(encoding="utf-8"))
        if TRANSLATIONS_PATH.exists()
        else {"ui": {}, "chapters": {}}
    )
    pages = []

    for chapter in manifest["chapters"]:
        markdown_path = DOCS_DIR / chapter["file"]
        source = markdown_path.read_text(encoding="utf-8")
        rendered = render_markdown(source)
        translated = translations.get("chapters", {}).get(chapter["slug"], {})
        page_title = translated.get("title", chapter["title"])
        rendered = assign_heading_ids(rendered, chapter["sections"])
        rendered = enhance_html(rendered, page_title=page_title)
        pages.append(
            {
                "slug": chapter["slug"],
                "title": page_title,
                "titleEn": chapter["title"],
                "sections": chapter["sections"],
                "content": rendered,
                "searchText": plain_text(rendered),
            }
        )

    return {
        "siteTitle": translations.get("ui", {}).get("site_title", "MoShell GUIDE RU"),
        "siteDescription": translations.get("ui", {}).get(
            "site_description",
            "GUIDE-сайт, собранный из нормализованного UserGuide.",
        ),
        "ui": translations.get("ui", {}),
        "pages": pages,
    }


def main() -> None:
    SITE_DIR.mkdir(parents=True, exist_ok=True)
    payload = build_payload()
    OUTPUT_PATH.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Wrote {len(payload['pages'])} pages to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
