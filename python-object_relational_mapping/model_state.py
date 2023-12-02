#!/usr/bin/python3
""" class definition of a State and an instance"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Tables states"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
