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
        .execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = %s\
                    ORDER BY cities.id ASC", (sys.argv[4],))

    records = cursor.fetchall()
    cites = []
    for data in records:
        cites.append(data[0])

    print(", ".join(cites))
    cursor.close()
    db.close()


if __name__ == "__main__":
    my_safe_filter_states()
