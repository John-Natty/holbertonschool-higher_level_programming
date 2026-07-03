#!/usr/bin/env python3
"""Create and populate the SQLite products database."""

import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "products.db"


def create_database():
    """Create products.db and insert sample products."""
    # Remove the old database file if it already exists.
    # This avoids the error: "file is not a database".
    if DB_PATH.exists():
        DB_PATH.unlink()

    # Connect to the SQLite database.
    connection = sqlite3.connect(DB_PATH)

    # Create a cursor to execute SQL commands.
    cursor = connection.cursor()

    # Create the Products table.
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    # Insert sample products.
    cursor.execute("""
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    """)

    # Save changes.
    connection.commit()

    # Close the database connection.
    connection.close()


if __name__ == "__main__":
    create_database()