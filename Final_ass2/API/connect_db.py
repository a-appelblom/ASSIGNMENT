# STEG 1
# SKAPA KONTAKT MED DATABSEN. 

# In this example, we are "connecting" to a SQLite database (opening a file with the SQLite database).


from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base

from schemas_db import Agents

engine = create_engine("sqlite:///Agents.db", connect_args={"check_same_thread": False}, echo=True # echo är gött att ha så man ser vad man gör.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base() # denna är importerad till model_db 








# conn = engine.connect()

# Result = conn.execute(query)


# output = conn.execute(Agents.select()).fetchall()
# print(output)



