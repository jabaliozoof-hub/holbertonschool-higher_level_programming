#!/usr/bin/python3
"""
A script that lists all states with a name starting with N
from the database hbtn_0e_0_usa.
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

    # Execute SQL query with a filter for names starting with 'N'
    # Using BINARY to ensure case sensitivity (matching uppercase 'N')
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY states.id ASC"
    )

    # Fetch all the matching rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
