#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def my_safe_filter_states():
    """ lists all cities from the database
    hbtn_0e_4_usa"""

    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3]
                         )
    cursor = db.cursor()

    cursor \
        .execute("SELECT cities.id, cities.name, \
        states.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id ASC")

    records = cursor.fetchall()
    for data in records:
        print(data)

    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
