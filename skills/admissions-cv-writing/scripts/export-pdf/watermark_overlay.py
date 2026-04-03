"""Optional footer watermark overlay for PDF export.

Keep this file to enable watermark; remove it to disable watermark.
"""


def build_overlay() -> tuple[str, str]:
    overlay_css = """
    .pdf-watermark-footer {
        position: fixed;
        left: 0;
        right: 0;
        bottom: 0;
        text-align: center;
        font-family: {{FONT_SANS_STACK}};
        font-size: 8pt;
        color: #b7b7b7;
        z-index: 10;
        pointer-events: none;
    }
    """

    overlay_html = '<div class="pdf-watermark-footer">Powered by OfferClaw</div>'
    return overlay_css, overlay_html
