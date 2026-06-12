#!/usr/bin/env bash
set -euo pipefail

echo "=== Brihaspati Setup ==="

# Check Python
PYTHON_VERSION=$(python3 --version 2>/dev/null || echo "none")
if [ "$PYTHON_VERSION" = "none" ]; then
    echo "ERROR: Python 3.10+ is required"
    exit 1
fi
echo "Python: $PYTHON_VERSION"

# Create virtual environment
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r backend/requirements.txt
pip install -r backend/requirements-dev.txt

# Setup directories
echo "Setting up directories..."
mkdir -p data/sessions data/profiles data/conversations logs

# Check Ollama
if command -v ollama &>/dev/null; then
    echo "Ollama found. Checking models..."
    ollama list 2>/dev/null || echo "No models pulled yet. Run: ollama pull llama3.1:8b"
else
    echo "WARNING: Ollama not found. Install from https://ollama.ai"
fi

# Setup pre-commit
if command -v pre-commit &>/dev/null; then
    pre-commit install 2>/dev/null || true
fi

echo ""
echo "=== Setup Complete ==="
echo "Run: python -m backend.main"
