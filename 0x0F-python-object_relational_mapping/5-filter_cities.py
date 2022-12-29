#!/usr/bin/python3
"""Lists all cities by state name provided"""
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

    query = "SELECT cities.name\n \
            FROM cities\n \
                INNER JOIN states\n \
                    ON (cities.state_id = states.id)\n \
                    WHERE states.name LIKE BINARY %s\n \
            ORDER BY cities.id"
    cur = db.cursor()
    cur.execute(query, (args[3], ))

    first = 0
    for row in cur.fetchall():
        if first == 0:
            print(row[0], end="")
            first = 1
        else:
            print(f", {row[0]}", end="")
    print()


if __name__ == '__main__':
    main()
