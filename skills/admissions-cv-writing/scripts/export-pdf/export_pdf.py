#!/usr/bin/env python3
"""Export a Markdown CV to PDF using WeasyPrint."""

import argparse
import importlib.util
import re
import sys
from pathlib import Path

import markdown
from weasyprint import HTML


SCRIPT_DIR = Path(__file__).resolve().parent
FONTS_DIR = (SCRIPT_DIR / "../../assets/fonts").resolve()
CSS_FILE = SCRIPT_DIR / "css/offerclaw.css"
WATERMARK_OVERLAY_FILE = SCRIPT_DIR / "watermark_overlay.py"

PAGE_CSS = """
@page {
    size: A4;
    margin: 1.2cm 1.1cm 1.2cm 1.1cm;
}
"""

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
{page_css}
{cv_css}
{overlay_css}
</style>
</head>
<body>
{overlay_html}
{body}
</body>
</html>
"""


def build_css() -> str:
    css_text = CSS_FILE.read_text(encoding="utf-8")
    fonts_url = FONTS_DIR.as_uri()
    css_text = css_text.replace("{{FONTS_DIR}}", fonts_url)
    return css_text


def replace_ul_with_divs(html: str) -> str:
    html = re.sub(r"<ul[^>]*>", "", html)
    html = html.replace("</ul>", "")
    html = re.sub(r"<li[^>]*>", '<div class="bullet-item">', html)
    html = html.replace("</li>", "</div>")
    return html


def md_to_html(md_path: Path) -> str:
    md_text = md_path.read_text(encoding="utf-8")
    html = markdown.markdown(md_text, extensions=["extra"])
    return replace_ul_with_divs(html)


def build_overlay() -> tuple[str, str]:
    if not WATERMARK_OVERLAY_FILE.exists():
        return "", ""

    spec = importlib.util.spec_from_file_location("watermark_overlay", WATERMARK_OVERLAY_FILE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load overlay module: {WATERMARK_OVERLAY_FILE}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    build_fn = getattr(module, "build_overlay", None)
    if not callable(build_fn):
        raise RuntimeError(
            f"Overlay module must define callable build_overlay(): {WATERMARK_OVERLAY_FILE}"
        )

    overlay_css, overlay_html = build_fn()
    if not isinstance(overlay_css, str) or not isinstance(overlay_html, str):
        raise RuntimeError(
            f"build_overlay() must return tuple[str, str]: {WATERMARK_OVERLAY_FILE}"
        )
    return overlay_css, overlay_html


def export(input_md: Path, output_pdf: Path) -> None:
    body_html = md_to_html(input_md)
    cv_css = build_css()
    overlay_css, overlay_html = build_overlay()
    full_html = HTML_TEMPLATE.format(
        page_css=PAGE_CSS,
        cv_css=cv_css,
        overlay_css=overlay_css,
        overlay_html=overlay_html,
        body=body_html,
    )
    html = HTML(string=full_html, base_url=str(input_md.parent))
    html.write_pdf(str(output_pdf))
    print(f"PDF written to {output_pdf}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Markdown CV to PDF")
    parser.add_argument("input_md", type=Path, help="Input Markdown file")
    parser.add_argument("output_pdf", type=Path, help="Output PDF file")
    parser.add_argument("--style", default="serif", help="Style variant (default: serif)")
    args = parser.parse_args()

    if not args.input_md.exists():
        print(f"Error: {args.input_md} not found", file=sys.stderr)
        sys.exit(1)

    export(args.input_md, args.output_pdf)


if __name__ == "__main__":
    main()
