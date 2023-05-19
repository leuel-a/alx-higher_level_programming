#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb


def list_states(username: str, password: str, db_name: str) -> None:
    """Lists all states from the database hbtn_0e_0_usa"""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=f"{username}",
        passwd=f"{password}",
        db=f"{db_name}",
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
