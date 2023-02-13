from fastapi import FastAPI
from pydantic import BaseModel
import os
import sqlite3

from db_connect import DB

# Här ska vi bygga routs. # det är även här uvicorn aktiveras!! 
app = FastAPI()
# http://127.0.0.1:8000 

def call_db(query: str, *args):
    connection = sqlite3.connect("Agents.db")
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

def populate_databse():
    connection = sqlite3.connect("Agents.db")
    cur = connection.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS agents(id INTEGER PRIMARY KEY, agent_id varchar(3))" 
    )
    cur.execute("INSERT INTO agents (agent_id) VALUES ('007' )")
    cur.close()
    connection.commit()
    connection.close()


statement = insert(user_table).values(first_name="Anton", last_name="Appelblom")

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()

with engine.connect() as conn:
    conn.execute(
        insert(user_table),
        [
            {"first_name": "Erik", "last_name": "Eriksson"},
            {"first_name": "Karl", "last_name": "Karlsson"},
        ]
)
    conn.commit()

    

# @app.get("/populate")  
# def root(): 
#     populate_databse()
#     return "Populated"

# vad jag lämmnar detta med är att jag tror jag gjort mitt databas bygge till en class i db.py och nu importerat klassen här. 



# def populate_databse():
#     connection = sqlite3.connect("api.db")
#     cur = connection.cursor()
#     cur.execute(
#         "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY, name varchar(255) NOT NULL)" 
#     )
#     cur.execute("INSERT INTO person (name) VALUES ('Anton' )")
#     cur.execute("INSERT INTO person (name) VALUES ('Erik' )")
#     cur.execute("INSERT INTO person (name) VALUES ('Karl' )")
#     cur.close()
#     connection.commit()
#     connection.close()
    

# @app.get("/populate")  
# def root(): 
#     populate_databse()
#     return "Populated"






# #########################################################################################
# def __call_db(query: str, *args):                                                         # Detta
#     connection = sqlite3.connect("Agents.db")                                              # är 
#     cursor = connection.cursor()  ###############                                       # själva kopplingen till 
#     res = cursor.execute(query, args)           # Denna funktion hämtar data            # databasen 
#     data = res.fetchall()                       # från databas med cursorn.             # som 
#     cursor.close ################################                                       # skapats 
#     connection.commit()                                                                 #        
#     connection.close()                                                                  #
#     return data                                                                         #
# ######################

# jag ändrarde den något.

# #########################################################################################
# def __call_db(self, query):                                                         # Detta
#     connection = sqlite3.connect(self.db_url)                                              # är 
#     cursor = connection.cursor()  ###############                                       # själva kopplingen till 
#     res = cursor.execute(query)           # Denna funktion hämtar data            # databasen 
#     data = res.fetchall()                       # från databas med cursorn.             # som 
#     cursor.close ################################                                       # skapats 
#     connection.commit()                                                                 #        
#     connection.close()                                                                  #
#     return data                                                                         #
# ######################




























# url = 'http://127.0.0.1:8000/Agents'

# data = {"agent_id": 007,  }









############ AVANCERAD VÄG #########################################
########################### VÅR API ##############################
# # http://127.0.0.1:8000  (Press CTRL+C to quit) This is the old one... 
# app = FastAPI()
# db = DB
# print(db)


# # define the database model 
# class Agent(BaseModel):
#     agent_id: int

# engine = sa.create_engine("sqlite:///Agents.db")
# SessionLocal = sessionmaker(bind=engine)

# # Define a dependency to get the database session
# def get_db(request):
#     return request.state.db





@app.get("/") # detta är fråm lektionen med API så fortsätt kolla på den! 
def root():
    return "Hello user!"

@app.get("/test") 
def root():
    return "Hello user! This is a test. "










# this created a emtyp paper 
# sqlite3.connect("agent_db")


# Connection.close()