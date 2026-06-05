from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: extract_docx_text.py INPUT.docx OUTPUT.txt")
        return 2

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2])

    try:
        from docx import Document
    except Exception as exc:
        print(f"python-docx is unavailable: {exc}")
        return 2

    document = Document(str(src))
    lines = []

    for paragraph in document.paragraphs:
        text = paragraph.text.strip()
        if text:
            lines.append(text)

    for table_index, table in enumerate(document.tables, 1):
        lines.append(f"\n[Table {table_index}]")
        for row in table.rows:
            cells = [cell.text.strip().replace("\n", " / ") for cell in row.cells]
            if any(cells):
                lines.append(" | ".join(cells))

    dst.write_text("\n".join(lines), encoding="utf-8")
    print(f"paragraphs={len(document.paragraphs)} tables={len(document.tables)} chars={dst.stat().st_size} out={dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
