#!/usr/bin/python3
"""
Script that takes in an argument and displays all values
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
        db=sys.argv[3]
    )
    cursor = db.cursor()
    
    # تنفيذ الاستعلام باستخدام LIKE BINARY لضمان تطابق الأحرف (Case-sensitive)
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC".format(sys.argv[4])
    
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()
