from pathlib import Path
import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: extract_pdf_text.py INPUT.pdf OUTPUT.txt")
        return 2

    pdf = Path(sys.argv[1])
    out = Path(sys.argv[2])

    try:
        import pypdf
    except Exception:
        try:
            import PyPDF2 as pypdf
        except Exception as exc:
            print(f"no PDF extraction library available: {exc}")
            return 2

    reader = pypdf.PdfReader(str(pdf))
    parts = []
    for index, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        parts.append(f"\n\n--- PAGE {index} ---\n{text}")

    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"pages={len(reader.pages)} chars={out.stat().st_size} out={out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
