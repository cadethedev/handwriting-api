#!/usr/bin/env bash
set -e

echo "Installing requirements..."
pip install -r requirements.txt

echo "Cloning handwriting-synthesis..."
git clone https://github.com/otuva/handwriting-synthesis.git

echo "Installing handwriting-synthesis..."
cd handwriting-synthesis
pip install -e .
cd ..

echo "Build complete!"
