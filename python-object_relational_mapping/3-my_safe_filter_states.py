#!/usr/bin/python3
"""This module safely lists states matching a user-provided name."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Get the state name searched by the user
    state_name = sys.argv[4]

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

    # Build a safe SQL query using a parameter placeholder
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY %s "
        "ORDER BY states.id ASC"
    )

    # Execute the query with the user input passed separately
    cursor.execute(query, (state_name,))

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Display each row exactly as a tuple
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
