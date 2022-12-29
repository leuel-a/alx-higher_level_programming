#!/usr/bin/python3
"""Lists all cities by state"""
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

    query = "SELECT cities.id, cities.name, states.name\n \
            FROM cities\n \
            INNER JOIN states\n \
                ON (cities.state_id = states.id\n) \
            ORDER BY cities.id"

    cur = db.cursor()
    cur.execute(query)

    for row in cur.fetchall():
        print(row)


if __name__ == '__main__':
    main()
