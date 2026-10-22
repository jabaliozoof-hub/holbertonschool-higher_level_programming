#!/usr/bin/python3
"""
A script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections.
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

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query securely using parameters tuple to prevent SQL injection
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
        (sys.argv[4],)
    )

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
