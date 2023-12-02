#!/usr/bin/python3
"""Lists all states from the db starting with N."""


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    mylist = cursor.fetchall()
    for i in mylist:
        if i[1][0] == 'N':
            print(i)
    cursor.close()
    db.close()
