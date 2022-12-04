#!/usr/bin/python3
"""Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument."""
import sys
import MySQLdb


def my_filter_states() -> None:
    """Filters states supplied as arguments"""
    args = sys.argv[1:]
    # Connecting to the DB
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Creating the cursor
    cur = db.cursor()
    cur.execute("SELECT *\n"
                "FROM states\n"
                "WHERE name='{}'\n"
                "ORDER BY id".format(args[3]))
    for state in cur.fetchall():
        print(state)


if __name__ == '__main__':
    my_filter_states()
