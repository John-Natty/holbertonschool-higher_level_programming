#!/usr/bin/python3
"""This module lists all states from a MySQL database."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server running on localhost
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Select all rows from the states table, ordered by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Display each row exactly as a tuple
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
