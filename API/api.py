from sqlalchemy import *     # engine, Integer, String, Column, Boolean, CHAR
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from fastapi import FastAPI
import sqlite3


## AI copy paste   Denna kan ha och göra med datbas bygget och borde vara i db.py men vi får se.. 
# Base = declarative_base()

# class Agent(Base):
#     __tablename__ = 'Agent'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)

# engine = create_engine('sqlite:///example.db')
# Base.metadata.create_all(engine)

# Session = sessionmaker(bind=engine)
# session = Session()

# session.commit()
# session.close()






# http://127.0.0.1:8000  (Press CTRL+C to quit)
app = FastAPI()

@app.get("/") # detta är fråm lektionen med API så fortsätt kolla på den! 
def root():
    return {"message: Hellw world!"} 




# this created a emtyp paper 
# sqlite3.connect("agent_db")


# Connection.close()