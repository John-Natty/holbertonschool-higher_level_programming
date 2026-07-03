#!/usr/bin/env python3
"""Flask app reading and displaying products from JSON, CSV, or SQLite."""

import csv
import json
import sqlite3
from pathlib import Path

from flask import Flask, render_template, request

# Get the directory where this file is located.
BASE_DIR = Path(__file__).resolve().parent

# Create the Flask application.
app = Flask(__name__)


def read_json_products(product_id=None):
    """Read products from the JSON file."""
    # Open and load the JSON file.
    with open(BASE_DIR / "products.json", encoding="utf-8") as file:
        products = json.load(file)

    # If an id is provided, keep only the matching product.
    if product_id:
        return [
            product for product in products
            if str(product.get("id")) == product_id
        ]

    # If no id is provided, return all products.
    return products


def read_csv_products(product_id=None):
    """Read products from the CSV file."""
    products = []

    # Open and read the CSV file as dictionaries.
    with open(BASE_DIR / "products.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        # Add each product, or only the matching one if id is provided.
        for row in reader:
            if not product_id or row.get("id") == product_id:
                products.append(row)

    return products


def read_sql_products(product_id=None):
    """Read products from the SQLite database."""
    query = "SELECT id, name, category, price FROM Products"
    params = ()

    # Add a WHERE clause if an id is provided.
    if product_id:
        query += " WHERE id = ?"
        params = (product_id,)

    # Connect to the SQLite database.
    with sqlite3.connect(BASE_DIR / "products.db") as connection:
        # This allows rows to behave like dictionaries.
        connection.row_factory = sqlite3.Row

        # Execute the SQL query.
        cursor = connection.execute(query, params)

        # Convert sqlite3.Row objects into normal dictionaries.
        return [dict(row) for row in cursor.fetchall()]


@app.route("/products")
def products():
    """Display products from JSON, CSV, or SQLite source."""
    # Get query parameters from the URL.
    source = request.args.get("source")
    product_id = request.args.get("id")

    try:
        # Select the correct data source.
        if source == "json":
            products_list = read_json_products(product_id)
        elif source == "csv":
            products_list = read_csv_products(product_id)
        elif source == "sql":
            products_list = read_sql_products(product_id)
        else:
            return render_template(
                "product_display.html",
                products=[],
                error="Wrong source"
            )

    except sqlite3.Error:
        # Handle SQLite-related errors.
        return render_template(
            "product_display.html",
            products=[],
            error="Database error"
        )

    # If an id was provided but no product matched, show an error.
    if product_id and not products_list:
        return render_template(
            "product_display.html",
            products=[],
            error="Product not found"
        )

    # Render the template with the products list.
    return render_template(
        "product_display.html",
        products=products_list,
        error=None
    )


if __name__ == "__main__":
    # Run the application on port 5000.
    app.run(debug=True, port=5000)
