#!/usr/bin/python3
"""Lists all states where the name matches the argument passed"""
import sys
import MySQLdb


def main() -> None:
    """Entry point of script"""
    args = sys.argv[1:]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    query = "SELECT * FROM states WHERE name LIKE BINARY '{}';".format(args[3])
    cur = db.cursor()
    cur.execute(query)

    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()
