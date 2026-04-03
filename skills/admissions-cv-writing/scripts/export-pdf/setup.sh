#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

python3 -m venv --without-pip venv
source venv/bin/activate
curl -sS https://bootstrap.pypa.io/get-pip.py | python3
pip install -r requirements.txt
