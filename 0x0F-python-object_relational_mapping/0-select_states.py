#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def main() -> None:
    """Entry point of the script"""

    # Store the arguments passed as arguments
    args = sys.argv[1:]

    # Connect to the database
    database = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Create the cursor object
    cur = database.cursor()

    # Querying the database
    query = "SELECT * FROM states"
    cur.execute(query)

    for rows in cur.fetchall():
        print(rows)


if __name__ == '__main__':
    main()
