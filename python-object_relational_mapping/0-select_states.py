#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select all states sorted by id ascending
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
