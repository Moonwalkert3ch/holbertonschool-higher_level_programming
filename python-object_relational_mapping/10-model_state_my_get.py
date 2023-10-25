#!/usr/bin/python3
"""prints the State object with the name passed as argument
from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    search = False

    for state in session.query(State):
        if state.name == sys.argv[4]:
            print('{}'.format(state.id))
            match = True
            break
        if match is False:
            print("Not found")
