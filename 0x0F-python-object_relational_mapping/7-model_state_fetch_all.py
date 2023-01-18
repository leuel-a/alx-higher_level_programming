#!/usr/bin/python3
"""Lists all State objects from the database hbtn_0e_6_usa"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main method of the program"""
    # Create the engine
    url = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(url)

    # Create the session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database
    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f'{state.id}: {state.name}')

if __name__ == '__main__':
    main()
