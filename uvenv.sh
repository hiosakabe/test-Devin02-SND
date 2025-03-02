#!/bin/bash

# Install uv if not already installed
if ! command -v uv &> /dev/null; then
    echo "Installing uv..."
    pip install uv
fi

# Create virtual environment with uv
echo "Creating virtual environment with uv..."
uv venv .uvenv

# Activate virtual environment
echo "Activating virtual environment..."
source .uvenv/bin/activate

# Install dependencies with uv
echo "Installing dependencies with uv..."
uv pip install -e .

# Install dev dependencies
echo "Installing dev dependencies..."
uv pip install -e ".[dev]"

echo "Setup complete! Virtual environment is activated."
echo "To activate this environment in the future, run: source .uvenv/bin/activate"
