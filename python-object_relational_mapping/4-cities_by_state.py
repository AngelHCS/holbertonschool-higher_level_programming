#!/usr/bin/python3
"""
placeholder
newline
newline
newline
"""

import MySQLdb
import sys


def main():
    # Retrieve the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to retrieve cities along with their state names
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows from the executed query
    cities = cursor.fetchall()

    # Print the rows
    for city in cities:
        print(city)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
