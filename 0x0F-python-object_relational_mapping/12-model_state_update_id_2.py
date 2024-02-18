#!/usr/bin/python3
"""This script adds the State object “Louisiana” to
the database hbtn_0e_6_usa
"""
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # for inst in query_result:
    #     if inst.id == 2:
    #         inst.name = 'New Mexico'
    new_state = session.query(State).filter_by(id=2).first()
    new_state.name = 'New Mexico'

    session.commit()