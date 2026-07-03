#!/usr/bin/env python3
"""Flask app reading and displaying products from JSON or CSV files."""

import csv
import json
from flask import Flask, render_template, request

# Create the Flask application.
app = Flask(__name__)


def read_json_products():
    """Read products from the JSON file."""
    with open("products.json", encoding="utf-8") as file:
        return json.load(file)


def read_csv_products():
    """Read products from the CSV file."""
    products = []

    with open("products.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            products.append(row)

    return products


@app.route("/products")
def products():
    """Display products from JSON or CSV source."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source == "json":
        products_list = read_json_products()
    elif source == "csv":
        products_list = read_csv_products()
    else:
        return render_template(
            "product_display.html",
            products=[],
            error="Wrong source"
        )

    if product_id:
        products_list = [
            product for product in products_list
            if str(product.get("id")) == product_id
        ]

        if not products_list:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=products_list,
        error=None
    )


if __name__ == "__main__":
    # Run the application on port 5000.
    app.run(debug=True, port=5000)
