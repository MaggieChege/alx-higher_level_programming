#!/usr/bin/python3
"""
Python script that takes in the name of a state as argument and lists all cities of that state
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
        "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s ORDER BY cities.id",
        (search_sttment,),
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
