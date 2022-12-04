#!/usr/bin/python3
"""Script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.

But this time, write one that is safe from MySQL injections!"""
import sys
import MySQLdb


def my_safe_filter_states() -> None:
    """Lists all states matched by the argument supplied to this script"""
    args = sys.argv[1:]
    # Connecting to the DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Create the cursor
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"
    cur = db.cursor()
    cur.execute(query, (args[3], ))
    for state in cur.fetchall():
        print(state)


if __name__ == '__main__':
    my_safe_filter_states()