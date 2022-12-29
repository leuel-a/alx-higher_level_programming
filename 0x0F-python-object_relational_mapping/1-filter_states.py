#!/usr/bin/python3
"""Lists all states starting with the letter N"""
import sys
import MySQLdb


def main() -> None:
    """Entry point of program"""

    # Get the arguments passed
    args = sys.argv[1:]

    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Create the cursor object
    cur = db.cursor()

    # Execute the query
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%'"
    cur.execute(query)

    for rows in cur.fetchall():
        print(rows)


if __name__ == '__main__':
    main()
