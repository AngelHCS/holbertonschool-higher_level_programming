#!/usr/bin/python3

"""
    Connects to a MySQL database and retrieves the list of states from a table called 'states'.

    Command-line arguments:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: MySQL database name

    The script connects to the local MySQL server using the provided credentials,
    executes a query to fetch all states and prints each state's ID and name.

    Dependencies:
    - MySQLdb: Python interface to MySQL
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

    # Execute the SQL query to retrieve all states
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

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
