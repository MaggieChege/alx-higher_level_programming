#!/usr/bin/python3
"""
Python script to display all values where name matches the argument. Should be safe from MySQL injections
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
    search_sttment = argv[4]
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s  ORDER BY id", (search_sttment,)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
