#!/usr/bin/python3
"""Lists all states with a `name` starting with `N`(Upper N)
from Database --> hbtn_0e_0_usa"""
import sys
import MySQLdb


def list_states_begin_N() -> None:
    """Lists all states with a name starting with N (upper N) from
    the database hbtn_0e_0_usa"""
    args = sys.argv[1:]
    # Connecting to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )
    # Creating the cursor object
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name LIKE "N%"')
    for i in cur.fetchall():
        print(i)


if __name__ == '__main__':
    list_states_begin_N()
