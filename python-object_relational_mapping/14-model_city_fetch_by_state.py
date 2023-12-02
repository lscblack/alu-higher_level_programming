#!/usr/bin/python3
"""prints all City objects from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    records = session.query(State, City) \
        .filter(State.id == City.state_id).order_by(City.id).all()

    for data in records:
        print("{}: ({}) {}".format(
            data[0].__dict__['name'],
            data[1].__dict__['id'],
            data[1].__dict__['name']))

    session.close()
