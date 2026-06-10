#!/usr/bin/python3
"""This module deletes all State objects containing the letter a."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Get MySQL connection information from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the SQLAlchemy engine to connect Python to MySQL
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

    # Search for all State objects whose name contains the letter "a"
    states = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each matching State object from the session
    for state in states:
        session.delete(state)

    # Save the deletions into the database
    session.commit()

    # Close the session properly
    session.close()
