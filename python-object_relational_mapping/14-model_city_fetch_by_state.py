#!/usr/bin/python3
"""This module lists all City objects with their State names."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


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

    # Query all cities with their related states, sorted by city id
    results = (
        session.query(City, State)
        .filter(City.state_id == State.id)
        .order_by(City.id)
        .all()
    )

    # Display each city with the required format:
    # <state name>: (<city id>) <city name>
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session properly
    session.close()
