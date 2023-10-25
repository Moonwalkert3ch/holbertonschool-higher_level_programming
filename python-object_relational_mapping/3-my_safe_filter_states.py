#!/usr/bin/python3
""" SQL injection to delete a tb """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3])

    c = db.cursor()
    input = sys.argv[4]
    c.execute("SELECT * FROM states WHERE name = %s", (input, ))

    states = c.fetchall()

    for state in states:
        print(state)

        c.close()
        db.close()
