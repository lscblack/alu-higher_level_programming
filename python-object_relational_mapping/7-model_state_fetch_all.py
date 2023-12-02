#!/usr/bin/python3
"""lists all State objects from the database
hbtn_0e_6_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)

    records = session.query(State).all()

    for data in records:
        print("{}: {}".format(data.__dict__['id'], data.__dict__['name']))

    session.close()
