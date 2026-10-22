#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()

    # Escape user input to safely handle special characters and quotes
    searched_name = db.escape_string(sys.argv[4])
    if isinstance(searched_name, bytes):
        searched_name = searched_name.decode('utf-8')

    # Execute SQL query using format() with the escaped input
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY states.id ASC".format(searched_name)
    )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
