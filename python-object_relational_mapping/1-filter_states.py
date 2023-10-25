#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from db """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306, 
                        passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    c.execute("SELECT * FROM states ORDER BY id")
    states = c.fetchall()

    for state in states:
        if state[1][0] == "N":
            print(state)

    c.close()
    db.close()
