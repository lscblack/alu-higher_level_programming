#!/usr/bin/python3
""" takes in an argument and displays all
values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys


def my_safe_filter_states():
    """ takes in an argument and displays all
    values in the states table
    of hbtn_0e_0_usa where name matches the argument
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = db.cursor()

    cursor \
        .execute("SELECT * FROM states WHERE name= %s\
                ORDER BY id ASC", (sys.argv[4],))

    records = cursor.fetchall()
    for data in records:
        print(data)

    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
