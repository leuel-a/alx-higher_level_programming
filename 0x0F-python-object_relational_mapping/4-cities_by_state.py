#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


def cities_by_states() -> None:
    """Lists all cities from DB hbtn_0e_4_usa"""
    args = sys.argv[1:]
    # Connecting to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=args[0],
        passwd=args[1],
        db=args[2]
    )

    # Creating the cursor
    cur = db.cursor()

    # Query from DB
    query = "SELECT cities.id, cities.name, states.name\n" \
            "FROM cities\n" \
            "\tINNER JOIN states" \
            "\tON (cities.state_id = states.id)" \
            "ORDER BY cities.id"
    cur.execute(query)
    for city in cur.fetchall():
        print(city)


if __name__ == '__main__':
    cities_by_states()
