# PDF Export Scripts

This directory only contains the PDF export helper used by `admissions-cv-writing`.

## Files

- `export-pdf/run.sh`: single entry point. Initializes the venv on first run, then delegates to `export_pdf.py`.
- `export-pdf/export_pdf.py`: reads Markdown, assembles CSS/HTML, and exports PDF.
- `export-pdf/css/offerclaw.css`: main CV stylesheet for typography, headings, body text, and bullet layout.
- `export-pdf/watermark_overlay.py`: optional footer watermark overlay.
- `export-pdf/setup.sh`: creates the venv and installs dependencies (called automatically by `run.sh`).
- `export-pdf/requirements.txt`: Python dependencies for export.

## Setup and Usage

- Python dependencies: `weasyprint`, `markdown`.
- From the `admissions-cv-writing/` skill directory:
  ```bash
  bash scripts/export-pdf/run.sh <input.md> <output.pdf>
  ```
  The venv is created automatically on first run. No manual setup needed.
- Font loading defaults to `--font-source auto`: use packaged fonts when available, otherwise fall back to similar local fonts.
- Optional font-source modes:
  - `--font-source auto`: prefer packaged fonts, then local fonts.
  - `--font-source local-only`: never read packaged font files; useful on platforms that forbid shipping fonts.
  - `--font-source bundled-only`: require packaged font files and fail fast if they are missing.

## Watermark Toggle

- Keep `export-pdf/watermark_overlay.py` to enable the footer watermark.
- Delete `export-pdf/watermark_overlay.py` to disable the watermark.

`export_pdf.py` checks for that file at runtime and skips the overlay automatically when it is absent.
