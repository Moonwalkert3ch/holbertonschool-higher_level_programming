#!/usr/bin/python3
""" takes in the name of a state as an argument and lists
all cities of that state"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                      passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("""SELECT cities.name FROM cities INNER JOIN
                   states ON cities.state_id=states.id WHERE state
                   s.name=%s""", (sys.argv[4],))

    cities = cursor.fetchall()

    city_list = list(city[0] for city in cities)
    print(*city_list, sep=", ")

    cursor.close()
    db.close()
