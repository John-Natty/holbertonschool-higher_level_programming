#!/usr/bin/python3
"""This module defines a State model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """This class represents the states table."""

    __tablename__ = "states"

    # id column: integer, primary key, not nullable
    id = Column(Integer, primary_key=True, nullable=False)

    # name column: string with a maximum of 128 characters, not nullable
    name = Column(String(128), nullable=False)
