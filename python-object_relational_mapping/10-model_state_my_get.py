#!/usr/bin/python3
"""This module prints the id of a State object by name."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Get the state name searched by the user
    state_name = sys.argv[4]

    # Create the SQLAlchemy engine to connect Python to the MySQL database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )

    # Create all tables linked to Base if they do not already exist
    Base.metadata.create_all(engine)

    # Create a session class linked to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object to communicate with the database
    session = Session()

    # Search for the first State object whose name matches the user input
    state = session.query(State).filter(State.name == state_name).first()

    # If no state was found, display "Not found"
    if state is None:
        print("Not found")
    else:
        # If the state exists, display only its id as required
        print(state.id)

    # Close the session properly
    session.close()
