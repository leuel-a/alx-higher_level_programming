#!/usr/bin/python3
"""Lists all states from the database `hbtn_0e_0_usa`"""
import MySQLdb
import sys


def list_states() -> None:
    """Function that list all states in `hbtn_0e_0_usa`"""
    args = sys.argv[1:]
    # Connecting to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )
    # Creating the cursor
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id')
    for i in cur.fetchall():
        print(i)


if __name__ == '__main__':
    list_states()
