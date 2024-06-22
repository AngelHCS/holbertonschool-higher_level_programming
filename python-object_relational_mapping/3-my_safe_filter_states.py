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
    state_name = sys.argv[4]

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

    # Execute the SQL query to retrieve states matching the given name safely
    query = ("SELECT id, name FROM states WHERE BINARY name = %s"
             "ORDER BY id ASC")
    cursor.execute(query, (state_name,))

    # Fetch all the rows from the executed query
    states = cursor.fetchall()

    # Print the rows
    for state in states:
        print(state)

    # Close the cursor and the connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
