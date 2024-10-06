#!/bin/bash

# Define the project directory and virtual environment
PROJECT_DIR="$(pwd)"
VENV_DIR="$PROJECT_DIR/venv"

# Check if virtual environment exists, if not, create it
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate the virtual environment
source "$VENV_DIR/bin/activate"

# Install necessary dependencies
echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Run the FastAPI application
echo "Starting FastAPI server..."
uvicorn jarvis.api:app --reload
