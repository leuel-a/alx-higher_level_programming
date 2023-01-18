#!/usr/bin/python3
"""List all State objects from database hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main method / Driver method"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    ))
    session = sessionmaker(bind=engine)
    session_obj = session()

    for instance in session_obj.query(State).order_by(State.id).all():
        print(f'{instance.id}: {instance.name}')

    session_obj.close()


if __name__ == '__main__':
    main()
