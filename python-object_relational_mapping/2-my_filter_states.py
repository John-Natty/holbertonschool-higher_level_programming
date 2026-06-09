#!/usr/bin/python3
"""This module lists states matching a user-provided name."""


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

    # Build the SQL query using format as requested by the task
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY states.id ASC".format(state_name)
    )

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows returned by the query
    rows = cursor.fetchall()

    # Display each row exactly as a tuple
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
