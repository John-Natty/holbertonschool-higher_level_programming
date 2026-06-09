#!/usr/bin/python3
"""This module lists all cities with their states."""

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

    # Execute one SQL query joining cities and states
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Display each city with its state
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
