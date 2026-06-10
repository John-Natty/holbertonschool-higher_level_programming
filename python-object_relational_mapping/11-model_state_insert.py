#!/usr/bin/python3
"""This module adds the State object Louisiana to the database."""

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

    # Create a new State object with the name Louisiana
    new_state = State(name="Louisiana")

    # Add the new object to the current session
    session.add(new_state)

    # Save the new object into the database
    session.commit()

    # Print the new state's id after creation
    print(new_state.id)

    # Close the session properly
    session.close()
