#!/usr/bin/python3
"""This module lists all cities of a given state safely."""

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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    # Execute the query with the user input passed separately
    cursor.execute(query, (state_name,))

    # Fetch all matching cities
    rows = cursor.fetchall()

    # Convert the result tuples into a list of city names
    cities = [row[0] for row in rows]

    # Display city names separated by comma and space
    print(", ".join(cities))

    # Close the cursor and the database connection
    cursor.close()
    db.close()
