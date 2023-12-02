#!/usr/bin/python3
"""Script that takes in arguments."""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{}' ORDER BY \
            id ASC".format(argv[4]))
    mylist = cursor.fetchall()
    for i in mylist:
        if i[1] == argv[4]:
            print(i)
    cursor.close()
    db.close()
