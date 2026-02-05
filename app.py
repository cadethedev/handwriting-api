"""
Handwriting Synthesis API
Render web service that converts text to handwritten SVG.
"""

from flask import Flask, request, jsonify, Response
import numpy as np
import os
import sys

# Add handwriting-synthesis to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'handwriting-synthesis'))

from handwriting_synthesis.hand import Hand

app = Flask(__name__)

# Initialize the handwriting model (loads on startup)
hand = None

def get_hand():
    global hand
    if hand is None:
        print("Loading handwriting model...")
        hand = Hand()
        print("Model loaded!")
    return hand

@app.route('/', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "service": "handwriting-synthesis"})

@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate handwritten SVG from text.

    Request JSON:
    {
        "text": "Hello world",
        "style": 0,           # Optional: style number 0-11
        "bias": 0.75,         # Optional: how uniform the handwriting is (0-1)
        "width": 1000         # Optional: SVG width
    }

    Returns: SVG string
    """
    try:
        data = request.get_json()

        if not data or 'text' not in data:
            return jsonify({"error": "Missing 'text' field"}), 400

        text = data['text']
        style = data.get('style', None)  # None = random style
        bias = data.get('bias', 0.75)
        width = data.get('width', 1000)

        # Split text into lines
        lines = text.split('\n')

        # Generate handwriting
        h = get_hand()

        if style is not None:
            # Use specific style
            biases = [bias] * len(lines)
            styles = [style] * len(lines)
            stroke = h.write(
                filename=None,
                lines=lines,
                biases=biases,
                styles=styles,
                stroke_widths=[1] * len(lines),
                return_svg=True,
                width=width
            )
        else:
            # Random style
            stroke = h.write(
                filename=None,
                lines=lines,
                biases=[bias] * len(lines),
                stroke_widths=[1] * len(lines),
                return_svg=True,
                width=width
            )

        return Response(stroke, mimetype='image/svg+xml')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/styles', methods=['GET'])
def styles():
    """List available handwriting styles."""
    return jsonify({
        "styles": list(range(12)),
        "description": "Styles 0-11 are available. Each produces different handwriting."
    })

if __name__ == '__main__':
    # Preload model
    get_hand()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
