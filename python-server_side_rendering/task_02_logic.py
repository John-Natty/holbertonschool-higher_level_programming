#!/usr/bin/env python3
"""Flask app displaying dynamic content from a JSON file."""

import json
from flask import Flask, render_template

# Create the Flask application.
app = Flask(__name__)


@app.route("/items")
def items():
    """Render the items page with data from a JSON file."""
    # Open and read the JSON file.
    with open("items.json", encoding="utf-8") as file:
        data = json.load(file)

    # Get the list of items from the JSON data.
    items_list = data.get("items", [])

    # Send the list to the Jinja template.
    return render_template("items.html", items=items_list)


if __name__ == "__main__":
    # Run the application on port 5000.
    app.run(debug=True, port=5000)
