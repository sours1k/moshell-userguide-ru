from __future__ import annotations

import json
import re
import shutil
from dataclasses import dataclass, field
from html import escape
from pathlib import Path
from typing import Iterator

from deep_translator import GoogleTranslator
from docx import Document
from docx.document import Document as DocxDocument
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph


ROOT = Path(__file__).resolve().parent.parent
DOCX_PATH = ROOT / "UserGuide.docx"
SITE_DIR = ROOT / "site"
ASSETS_DIR = SITE_DIR / "assets"
CACHE_PATH = ROOT / ".cache" / "translate-cache.json"

CODE_PATTERNS = (
    r"<[^>]+>",
    r"\[[^\]]+\]",
    r"[a-z]+/[a-z]",
    r"\b[a-z]{1,8}\[[^\]]+\]",
    r"\b[a-z]{1,12}\s+[<\[]",
    r"^\s*[-+#|].*",
    r"==",
    r"\t",
)


@dataclass
class Block:
    type: str
    text: str | None = None
    level: int | None = None
    rows: list[list[str]] | None = None
    html: str | None = None


@dataclass
class Page:
    slug: str
    title_en: str
    title: str
    blocks: list[Block] = field(default_factory=list)
    sections: list[dict[str, str]] = field(default_factory=list)


def slugify(value: str) -> str:
    value = re.sub(r"^\d+(\.\d+)*\s*", "", value).strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return value or "section"


def is_toc_line(text: str) -> bool:
    return bool(re.search(r"\.{3,}\s*\d+$", text)) or bool(re.match(r"^[A-Za-z].*\d+$", text) and "." in text)


def is_code_like(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if len(stripped) < 3:
        return False
    if any(re.search(pattern, stripped) for pattern in CODE_PATTERNS):
        return True
    letters = sum(ch.isalpha() for ch in stripped)
    specials = sum((not ch.isalnum()) and (not ch.isspace()) for ch in stripped)
    digits = sum(ch.isdigit() for ch in stripped)
    if specials >= max(6, len(stripped) // 8):
        return True
    if digits and specials and letters < len(stripped) * 0.45:
        return True
    if stripped.isupper() and len(stripped.split()) <= 5:
        return True
    return False


class Translator:
    def __init__(self, cache_path: Path) -> None:
        self.cache_path = cache_path
        self.cache_path.parent.mkdir(parents=True, exist_ok=True)
        if cache_path.exists():
            self.cache = json.loads(cache_path.read_text(encoding="utf-8"))
        else:
            self.cache = {}
        self.translator = GoogleTranslator(source="en", target="ru")

    def save(self) -> None:
        self.cache_path.write_text(
            json.dumps(self.cache, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def translate(self, text: str) -> str:
        clean = text.strip()
        if not clean:
            return text
        if clean in self.cache:
            return self.cache[clean]
        result = self.translator.translate(clean)
        self.cache[clean] = result
        return result

    def translate_many(self, texts: list[str]) -> list[str]:
        pending = []
        order = []
        for text in texts:
            clean = text.strip()
            if not clean:
                order.append(text)
                continue
            if clean in self.cache:
                order.append(self.cache[clean])
                continue
            pending.append(clean)
            order.append(None)

        if pending:
            for start in range(0, len(pending), 40):
                batch = pending[start : start + 40]
                translated = self.translator.translate_batch(batch)
                for source, target in zip(batch, translated):
                    self.cache[source] = target

        result = []
        for item in order:
            if item is None:
                raise RuntimeError("Translation order was not resolved")
            result.append(item)
        return [self.cache.get(text.strip(), text) if text.strip() else text for text in texts]


def iter_blocks(parent: DocxDocument) -> Iterator[Paragraph | Table]:
    parent_elm = parent.element.body
    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


def paragraph_text(paragraph: Paragraph) -> str:
    return "".join(run.text for run in paragraph.runs).strip()


def table_to_rows(table: Table) -> list[list[str]]:
    rows: list[list[str]] = []
    for row in table.rows:
        cells = [" ".join(cell.text.split()) for cell in row.cells]
        if any(cells):
            rows.append(cells)
    return rows


def translate_table(rows: list[list[str]], translator: Translator) -> list[list[str]]:
    translated = []
    for row in rows:
        translated_row = []
        for cell in row:
            translated_row.append(cell if is_code_like(cell) else translator.translate(cell))
        translated.append(translated_row)
    return translated


def render_inline_code(text: str) -> str:
    safe = escape(text)
    safe = re.sub(r"(`[^`]+`)", r"<code>\1</code>", safe)
    return safe.replace("&lt;code&gt;`", "<code>").replace("`&lt;/code&gt;", "</code>")


def render_block(block: Block) -> str:
    if block.type == "heading":
        tag = "h2" if block.level == 2 else "h3"
        anchor = slugify(block.text or "")
        return f'<{tag} id="{anchor}">{escape(block.text or "")}</{tag}>'
    if block.type == "code":
        return f"<pre><code>{escape(block.text or '')}</code></pre>"
    if block.type == "table":
        rows = block.rows or []
        if not rows:
            return ""
        head = rows[0]
        body = rows[1:] or []
        thead = "".join(f"<th>{escape(cell)}</th>" for cell in head)
        tbody = ""
        for row in body:
            tbody += "<tr>" + "".join(f"<td>{escape(cell)}</td>" for cell in row) + "</tr>"
        return f"<div class=\"table-wrap\"><table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table></div>"
    return f"<p>{render_inline_code(block.text or '')}</p>"


def build_pages(doc: Document) -> list[Page]:
    pages: list[Page] = []
    current_page: Page | None = None
    in_contents = False

    for item in iter_blocks(doc):
        if isinstance(item, Paragraph):
            text = paragraph_text(item)
            if not text:
                continue
            style = item.style.name
            if style == "Heading 1":
                if text == "Contents":
                    in_contents = True
                    continue
                in_contents = False
                current_page = Page(
                    slug=slugify(text),
                    title_en=text,
                    title=text,
                )
                pages.append(current_page)
                continue
            if in_contents or is_toc_line(text) or current_page is None:
                continue
            if style in {"Heading 2", "Heading 3"}:
                level = 2 if style == "Heading 2" else 3
                current_page.blocks.append(Block(type="heading", text=text, level=level))
                current_page.sections.append(
                    {
                        "id": slugify(text),
                        "title": text,
                        "level": str(level),
                    }
                )
                continue
            if is_code_like(text):
                current_page.blocks.append(Block(type="code", text=text))
            else:
                current_page.blocks.append(Block(type="paragraph", text=text))
        else:
            if current_page is None:
                continue
            rows = table_to_rows(item)
            if not rows:
                continue
            current_page.blocks.append(Block(type="table", rows=rows))

    return pages


def translate_pages(pages: list[Page], translator: Translator) -> None:
    texts: list[str] = []
    keys: list[tuple[str, int | tuple[int, int] | None]] = []

    for page_index, page in enumerate(pages):
        texts.append(page.title_en)
        keys.append((f"page:{page_index}", None))
        for block_index, block in enumerate(page.blocks):
            if block.type in {"paragraph", "heading"} and block.text and not is_code_like(block.text):
                texts.append(block.text)
                keys.append((f"block:{page_index}", block_index))
            if block.type == "table" and block.rows:
                for row_index, row in enumerate(block.rows):
                    for cell_index, cell in enumerate(row):
                        if cell and not is_code_like(cell):
                            texts.append(cell)
                            keys.append((f"cell:{page_index}", (block_index, row_index * 1000 + cell_index)))

    translated = translator.translate_many(texts)

    for (kind, position), value in zip(keys, translated):
        _, page_idx = kind.split(":")
        page = pages[int(page_idx)]
        if position is None:
            page.title = value
            continue
        if kind.startswith("block"):
            block = page.blocks[position]
            block.text = value
            if block.type == "heading":
                for section in page.sections:
                    if slugify(section["title"]) == slugify(page.blocks[position].text or ""):
                        section["title"] = value
                        section["id"] = slugify(value)
            continue
        if kind.startswith("cell"):
            block_index, packed = position
            row_index = packed // 1000
            cell_index = packed % 1000
            page.blocks[block_index].rows[row_index][cell_index] = value

    for page in pages:
        for block, section in zip(
            [b for b in page.blocks if b.type == "heading"],
            page.sections,
        ):
            section["title"] = block.text or section["title"]
            section["id"] = slugify(section["title"])


def extract_images() -> list[str]:
    media_dir = ROOT / "media"
    media_dir.mkdir(exist_ok=True)
    document = Document(DOCX_PATH)
    seen = []
    rels = document.part.rels
    for rel in rels.values():
        target = getattr(rel, "target_ref", "")
        if "image" not in target:
            continue
        image_part = rel.target_part
        filename = Path(target).name
        out_path = media_dir / filename
        if not out_path.exists():
            out_path.write_bytes(image_part.blob)
        seen.append(filename)
    return seen


def write_data(pages: list[Page], images: list[str]) -> None:
    payload = {
        "siteTitle": "MoShell GUIDE RU",
        "siteDescription": "Русскоязычный GUIDE-сайт, собранный из UserGuide.docx.",
        "pages": [
            {
                "slug": page.slug,
                "title": page.title,
                "titleEn": page.title_en,
                "sections": page.sections,
                "content": "\n".join(
                    rendered for rendered in (render_block(block) for block in page.blocks) if rendered
                ),
            }
            for page in pages
        ],
        "images": [f"media/{name}" for name in images],
    }
    (SITE_DIR / "guide-data.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def copy_media(images: list[str]) -> None:
    target = SITE_DIR / "media"
    target.mkdir(parents=True, exist_ok=True)
    for name in images:
        shutil.copy2(ROOT / "media" / name, target / name)


def main() -> None:
    SITE_DIR.mkdir(exist_ok=True)
    ASSETS_DIR.mkdir(exist_ok=True)
    translator = Translator(CACHE_PATH)
    doc = Document(DOCX_PATH)
    pages = build_pages(doc)
    translate_pages(pages, translator)
    images = extract_images()
    write_data(pages, images)
    copy_media(images)
    translator.save()
    print(f"Built {len(pages)} pages into {SITE_DIR}")


if __name__ == "__main__":
    main()
