#!/usr/bin/python3
"""
Creates the State California with the City San Francisco from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cali = State(name="California")
    cali.cities = [City(name="San Francisco")]
    session.add(cali)
    session.commit()
    session.close()
