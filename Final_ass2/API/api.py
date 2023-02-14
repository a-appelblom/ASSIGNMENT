# Steg 5
# Här bygger vi routes.

import sqlite3
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import model_db, schemas_db, crud
from connect_db import SessionLocal, engine


app = FastAPI()


model_db.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    db.close()


#______________DETTA ÄR FRÅN ANTONS API FILER___________________-
# de vill inte köras utan ignoreras av någon annledning.. 
# det måste saknas en liten del bara... 

#-------------------UNESSESARY AT THE MOMENT------- Här försöker göra en rout som visar hela databasen. 
def call_db(query: str, *args):
    connection = sqlite3.connect("Agents.db")
    cursor = connection.cursor()
    res = cursor.execute(query, args)
    data = res.fetchall()
    cursor.close()
    connection.commit()
    connection.close()
    return data

# @app.get("/call_db") 
# def root(): FEL HÄR 
#     call_db()
#     return "Showing database"
#--------------------------------------


# denna funkar utmärkt att köra i browser eller thunder. 
def populate_database():
    connection = sqlite3.connect("Agents.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO agents (agents_id) VALUES ( '007' )")
    cur.execute("INSERT INTO agents (agents_id) VALUES ( '001' )")
    cur.execute("INSERT INTO agents (agents_id) VALUES ( '002' )")
    cur.close()
    connection.commit()
    connection.close()

@app.get("/populate")
def root():
    populate_database()
    return "Populated"
#_________________________________________________________

# Här är felet 405 method not allowd.  * se screenshot i mappen. 
@app.post("/agent_create/", response_model=schemas_db.Agent_infoCreate)
def create_agent(agent: schemas_db.Agent_infoCreate, db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
    new_agent = crud.create_agent(db)
    if new_agent:
        raise HTTPException(status_code=400, detail="Agent already registered")
    return crud.create_agent(db=db, agent=agent)






# Förhoppningsvis ska denna ge all info som finns declarerat i klassen Agent_infoBase
@app.get("/agents_info/", response_model=list[schemas_db.Agenet_infoBase]) 
def read_agents(db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
    agents_info = crud.get_agent(db) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
    return agents_info


# # test funktion för att korrigera felet missing one positional argument. * detta kan vara för det inte finns någon data registread i agent_info än. 
# @app.get("/agents_info/", response_model=list[schemas_db.Agenet_infoBase]) 
# def read_agents(db: Session = Depends(get_db)): 
#     agents_info = crud.get_agent(db, read_agents) 
#     return agents_info






#_________________________________________________________
#____JUST_____PUTTING____IN____SAMPEL____DATA_____________





    # def populate_database():
    # connection = sqlite3.connect("api.db")
    # cur = connection.cursor()
    # cur.execute(
    #     "CREATE TABLE IF NOT EXISTS person(id INTEGER PRIMARY KEY,  name varchar(255) NOT NULL)"
    # )
    # cur.execute("INSERT INTO person (name) VALUES ( 'Anton' )")
    # cur.execute("INSERT INTO person (name) VALUES ( 'Erik' )")
    # cur.execute("INSERT INTO person (name) VALUES ( 'Karl' )")
    # cur.close()
    # connection.commit()
    # connection.close()