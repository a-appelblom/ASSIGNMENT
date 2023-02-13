# STEG 2
# SKAPA KONTAKT MED DATABSEN. 


from sqlalchemy import *
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///Agents.db", connect_args={"check_same_thread": False}, echo=True # echo är gött att ha så man ser vad man gör.
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base() # denna är importerad till model_db 






