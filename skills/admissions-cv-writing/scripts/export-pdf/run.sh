#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [ ! -f "$SCRIPT_DIR/venv/bin/python" ]; then
  echo "Initializing export environment..." >&2
  bash "$SCRIPT_DIR/setup.sh"
fi

exec "$SCRIPT_DIR/venv/bin/python" "$SCRIPT_DIR/export_pdf.py" "$@"
