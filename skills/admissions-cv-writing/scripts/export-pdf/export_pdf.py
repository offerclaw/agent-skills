#!/usr/bin/env python3
"""Export a Markdown CV to PDF using WeasyPrint."""

import argparse
import importlib.util
import re
import sys
from pathlib import Path

import markdown
from weasyprint import CSS, HTML
from weasyprint.text.fonts import FontConfiguration


SCRIPT_DIR = Path(__file__).resolve().parent
FONTS_DIR = (SCRIPT_DIR / "../../assets/fonts").resolve()
CSS_FILE = SCRIPT_DIR / "css/offerclaw.css"
WATERMARK_OVERLAY_FILE = SCRIPT_DIR / "watermark_overlay.py"

FONT_SOURCE_CHOICES = ("auto", "local-only", "bundled-only")

FONT_FACE_SOURCES = {
    "FONT_SANS_REGULAR_SRC": {
        "file": "SourceHanSansCN-Regular.ttf",
        "local_names": [
            "Source Han Sans SC",
            "Source Han Sans CN",
            "SourceHanSansCN-Regular",
            "Noto Sans CJK SC",
            "Noto Sans SC",
            "PingFang SC",
            "Microsoft YaHei",
            "WenQuanYi Micro Hei",
        ],
    },
    "FONT_SANS_BOLD_SRC": {
        "file": "SourceHanSansCN-Bold.ttf",
        "local_names": [
            "Source Han Sans SC Bold",
            "Source Han Sans CN Bold",
            "SourceHanSansCN-Bold",
            "Noto Sans CJK SC Bold",
            "Noto Sans SC Bold",
            "PingFang SC Semibold",
            "Microsoft YaHei Bold",
            "WenQuanYi Micro Hei",
        ],
    },
    "FONT_SANS_ITALIC_SRC": {
        "file": "SourceHanSansCN-Regular.ttf",
        "local_names": [
            "Source Han Sans SC",
            "Source Han Sans CN",
            "SourceHanSansCN-Regular",
            "Noto Sans CJK SC",
            "Noto Sans SC",
            "PingFang SC",
            "Microsoft YaHei",
            "WenQuanYi Micro Hei",
        ],
    },
    "FONT_SERIF_BOLD_SRC": {
        "file": "SourceHanSerifCN-Bold.ttf",
        "local_names": [
            "Source Han Serif SC Bold",
            "Source Han Serif CN Bold",
            "SourceHanSerifCN-Bold",
            "Noto Serif CJK SC Bold",
            "Noto Serif SC Bold",
            "Songti SC",
            "STSong",
            "SimSun",
        ],
    },
    "FONT_MONO_REGULAR_SRC": {
        "file": "JetBrainsMono-Regular.ttf",
        "local_names": [
            "JetBrains Mono",
            "JetBrainsMono-Regular",
            "DejaVu Sans Mono",
            "Liberation Mono",
            "SFMono-Regular",
            "Menlo",
            "Consolas",
        ],
    },
}

FONT_STACKS = {
    "FONT_SANS_STACK": (
        '"OfferClaw Sans", "Noto Sans CJK SC", "Noto Sans SC", '
        '"Source Han Sans SC", "Source Han Sans CN", "PingFang SC", '
        '"Hiragino Sans GB", "Microsoft YaHei", "WenQuanYi Micro Hei", sans-serif'
    ),
    "FONT_SERIF_STACK": (
        '"OfferClaw Serif", "Noto Serif CJK SC", "Noto Serif SC", '
        '"Source Han Serif SC", "Source Han Serif CN", "Songti SC", '
        '"STSong", "SimSun", serif'
    ),
    "FONT_MONO_STACK": (
        '"OfferClaw Mono", "JetBrains Mono", "DejaVu Sans Mono", '
        '"Liberation Mono", "SFMono-Regular", "Menlo", "Consolas", monospace'
    ),
}

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


def render_template(text: str, template_values: dict[str, str]) -> str:
    rendered = text
    for key, value in template_values.items():
        rendered = rendered.replace(f"{{{{{key}}}}}", value)
    return rendered


def build_font_source(
    local_names: list[str], font_file: Path | None, font_source_mode: str
) -> str:
    local_sources = [f'local("{name}")' for name in local_names]

    if font_source_mode == "local-only":
        sources = local_sources
    elif font_source_mode == "bundled-only":
        sources = [f"url('{font_file.as_uri()}') format('truetype')"]
    elif font_file is not None:
        sources = [f"url('{font_file.as_uri()}') format('truetype')", *local_sources]
    else:
        sources = local_sources

    return ",\n        ".join(sources)


def build_font_template_values(font_source_mode: str) -> dict[str, str]:
    template_values = dict(FONT_STACKS)
    missing_files: list[str] = []

    for key, spec in FONT_FACE_SOURCES.items():
        font_path = FONTS_DIR / spec["file"]
        font_file: Path | None = None

        if font_source_mode == "bundled-only":
            if not font_path.exists():
                missing_files.append(spec["file"])
            else:
                font_file = font_path
        elif font_source_mode == "auto":
            if font_path.exists():
                font_file = font_path
            else:
                missing_files.append(spec["file"])

        template_values[key] = build_font_source(
            spec["local_names"], font_file, font_source_mode
        )

    if font_source_mode == "bundled-only" and missing_files:
        missing_list = ", ".join(sorted(set(missing_files)))
        raise RuntimeError(
            f"Bundled font mode requested, but these files are missing: {missing_list}"
        )

    if font_source_mode == "auto" and missing_files:
        missing_list = ", ".join(sorted(set(missing_files)))
        print(
            "Bundled font files missing; falling back to local fonts for: "
            f"{missing_list}",
            file=sys.stderr,
        )
    elif font_source_mode == "local-only":
        print("Using local font fallbacks only.", file=sys.stderr)

    return template_values


def build_css(template_values: dict[str, str]) -> str:
    css_text = CSS_FILE.read_text(encoding="utf-8")
    return render_template(css_text, template_values)


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


def build_overlay(template_values: dict[str, str]) -> tuple[str, str]:
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
    return render_template(overlay_css, template_values), overlay_html


def export(input_md: Path, output_pdf: Path, font_source_mode: str) -> None:
    body_html = md_to_html(input_md)
    template_values = build_font_template_values(font_source_mode)
    cv_css = build_css(template_values)
    overlay_css, overlay_html = build_overlay(template_values)
    full_html = HTML_TEMPLATE.format(
        page_css=PAGE_CSS,
        cv_css=cv_css,
        overlay_css=overlay_css,
        overlay_html=overlay_html,
        body=body_html,
    )

    font_config = FontConfiguration()
    css = CSS(string=f"{PAGE_CSS}\n{cv_css}\n{overlay_css}", font_config=font_config)
    html = HTML(string=full_html, base_url=str(input_md.parent))
    html.write_pdf(str(output_pdf), stylesheets=[css], font_config=font_config)
    print(f"PDF written to {output_pdf}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Markdown CV to PDF")
    parser.add_argument("input_md", type=Path, help="Input Markdown file")
    parser.add_argument("output_pdf", type=Path, help="Output PDF file")
    parser.add_argument("--style", default="serif", help="Style variant (default: serif)")
    parser.add_argument(
        "--font-source",
        choices=FONT_SOURCE_CHOICES,
        default="auto",
        help=(
            "Font loading strategy: auto prefers bundled fonts and falls back to local fonts, "
            "local-only never uses bundled font files, bundled-only requires bundled font files."
        ),
    )
    args = parser.parse_args()

    if not args.input_md.exists():
        print(f"Error: {args.input_md} not found", file=sys.stderr)
        sys.exit(1)

    export(args.input_md, args.output_pdf, args.font_source)


if __name__ == "__main__":
    main()
