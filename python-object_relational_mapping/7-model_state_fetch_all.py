#!/usr/bin/python3
"""This module lists all State objects using SQLAlchemy."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            username,
            password,
            database
        ),
        pool_pre_ping=True
    )

    # Create all tables linked to Base if they do not exist
    Base.metadata.create_all(engine)

    # Create a session to query the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects sorted by id
    states = session.query(State).order_by(State.id).all()

    # Display each State object
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
