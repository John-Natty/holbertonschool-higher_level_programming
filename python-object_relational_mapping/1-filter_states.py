#!/usr/bin/python3
"""This module lists states whose names start with N."""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
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

    # Execute the SQL query that filters states starting with uppercase N
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all matching rows
    rows = cursor.fetchall()

    # Display each row as expected
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()
