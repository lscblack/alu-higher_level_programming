#!/usr/bin/python3
"""List all states from the databse."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    mylist = cursor.fetchall()
    for i in mylist:
        print(i)
    cursor.close()
    db.close()
