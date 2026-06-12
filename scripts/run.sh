#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
cd "$PROJECT_DIR"

# Activate virtual environment if exists
if [ -d ".venv" ]; then
    source .venv/bin/activate
fi

# Set defaults
export HOST="${HOST:-0.0.0.0}"
export PORT="${PORT:-8000}"
export LOG_LEVEL="${LOG_LEVEL:-INFO}"

echo "Starting Brihaspati on $HOST:$PORT"
exec python -m backend.main
