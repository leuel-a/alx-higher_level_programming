#!/usr/bin/python3
"""List all State objects from database hbtn_0e_6_usa"""
import sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main method / Driver method"""
    connection_url = sqlalchemy.engine.URL.create(
        drivername='mysql+mysqldb',
        username=sys.argv[1],
        password=sys.argv[2],
        host='localhost',
        port=3306,
        database=sys.argv[3]
    )
    engine = create_engine(connection_url)
    session = sessionmaker(bind=engine)
    session_obj = session()

    for instance in session_obj.query(State).order_by(State.id):
        print(f'{instance.id}: {instance.name}')


if __name__ == '__main__':
    main()
