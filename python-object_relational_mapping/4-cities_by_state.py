#!/usr/bin/python3
""" lists all cities from the db """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                         passwd=sys.argv[2], db=sys.argv[3],)
    cursor = db.cursor()

    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                   cities JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id""")

    cities = cursor.fetchall()

    for city in cities:

        print(city)

    cursor.close()
    db.close()
