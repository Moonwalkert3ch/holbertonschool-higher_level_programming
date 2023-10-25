#!/usr/bin/python3
""" displays all values in the table where name matches the argument """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = '{}' "
                   "ORDER BY states.id ASC".format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
