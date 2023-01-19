#!/usr/bin/python3
"""Takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = 'SELECT name FROM cities WHERE cities.state_id = (SELECT id FROM states WHERE name LIKE BINARY %s)'
    cur.execute(query, (sys.argv[4], ))
    check = 0
    for city in cur.fetchall():
        if check != 0:
            print(', ', end='')
        print(city[0], end='')

        if check == 0:
            check = 1
    print()
