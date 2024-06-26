#!/usr/bin/python3
"""
Script that lists all State objects from hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query all State objects ordered by id
    states = session.query(State).order_by(State.id).all()

    # Print results in the desired format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close():
