#!/usr/bin/python3
"""
Python script to diplay all states in asc order
"""
from email import charset
import MySQLdb
from sys import argv
if __name__=="__main__":
    db = MySQLdb.connect(host="localhost", port="3306", user=argv[1],
                         password=argv[2], database=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
