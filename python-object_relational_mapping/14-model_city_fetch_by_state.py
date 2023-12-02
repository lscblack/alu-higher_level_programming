#!/usr/bin/python3
"""
Prints all City objects from a database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    rows = session.query(City, State).filter(City.state_id == State.id)\
                                     .order_by(City.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
