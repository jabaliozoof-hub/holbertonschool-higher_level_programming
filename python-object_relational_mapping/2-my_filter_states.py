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

    # Escape single quotes to prevent SQL syntax errors on special inputs
    safe_name = sys.argv[4].replace("'", "''")

    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY states.id ASC".format(safe_name)
    )
    cursor.execute(query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
