#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument from
hbtn_0e_6_usa
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

    # Get the state name to search
    state_name = sys.argv[4]

    # Query the State object with the given name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the result
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Close the session
    session.close()
