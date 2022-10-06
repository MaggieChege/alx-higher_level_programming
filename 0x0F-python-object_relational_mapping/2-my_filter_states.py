#!/usr/bin/python3
"""
Python script to display all where state starts with N sort states in asc order
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3],
        charset="utf8",
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}%'  ORDER BY id".format(argv[4])
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
