#!/usr/bin/python3
"""List a safe method for the 2-filter_my_states.py"""
import sys
import MySQLdb


def main() -> None:
    """Entry point of the script"""
    args = sys.argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cur = db.cursor()
    cur.execute(query, (args[3], ))

    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()
