#!/usr/bin/python3
"""This module updates the name of the State object with id 2."""

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

    # Search for the State object with id equal to 2
    state = session.query(State).filter(State.id == 2).first()

    # Change the name of this State object
    if state:
        state.name = "New Mexico"

    # Save the modification into the database
    session.commit()

    # Close the session properly
    session.close()
