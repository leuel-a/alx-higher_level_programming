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
    query = "SELECT *\n" \
            "FROM states\n" \
            "WHERE name='{}' ORDER BY id".format(args[3])
    cur = db.cursor()
    cur.execute(query)
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()


if __name__ == '__main__':
    my_filter_states()
