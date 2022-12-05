#!/usr/bin/python3
"""Takes in the name of a state as an argument and
lists all cities of that state, using the database
hbtn_0e_4_usa"""
import sys
import MySQLdb


def filter_cities() -> None:
    """Lists all cities of a state supplied as an argument"""
    args = sys.argv[1:]
    # Connecting to the Database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Creating the cursor
    cur = db.cursor()

    # Querying the DB
    query = "SELECT name FROM cities WHERE state_id LIKE \n" \
            "(SELECT id FROM states WHERE name LIKE BINARY %s) ORDER BY id;"
    cur.execute(query, (args[3], ))
    first = True
    for row in cur.fetchall():
        if first is True:
            print("{}".format(row[0]), end='')
            first = False
        else:
            print(", {}".format(row[0]), end='')
    print()


if __name__ == '__main__':
    filter_cities()
