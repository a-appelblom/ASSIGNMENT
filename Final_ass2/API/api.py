# Steg 5
# Här bygger vi routes.

import sqlite3
from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

import model_db, schemas_db, crud
from connect_db import SessionLocal, engine


app = FastAPI()


model_db.Base.metadata.create_all(bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_antons_agent")
def create_antons_agent(agent: schemas_db.Agent, db: Session = Depends(get_db)):
    data = crud.create_agent(db, agent)
    return data


#______________DETTA ÄR FRÅN ANTONS API FILER___________________-

@app.get("/", response_class=HTMLResponse)
def root():
    with open("index.html") as f:
        return f.read()





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

# @app.get("/agents")
# def get_agents():
#     agents_query = """
#     SELECT * FROM agents
#     """
#     agents = call_db(agents_query)

#     return agents

#succsess! 
#--------------------------------------




# #_________Denna funkar utmärkt. 
def populate_database2():
    connection = sqlite3.connect("Agents.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO agent_info (first_name, last_name, agent_ID) VALUES ( 'James', 'Bond', '007')")
    cur.close()
    connection.commit()
    connection.close()


@app.post("/populate2") # Frågan är om jag lägger till post istället? eftersom jag för in data... ? 
def root():
    populate_database2()
    return "Populated the agnet_info table"







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

@app.post("/populate")
def root():
    populate_database()
    return "Populated"
#_________________________________________________________











 #------------------CONSTRUCTION---ZONE---------------------------------------------

 
# Förhoppningsvis ska denna ge all info som finns declarerat i klassen Agent_infoBase
@app.get("/all_agents_id") 
def read_agents(db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
    agents = crud.get_agents(db) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
    return agents





# @app.get("/all_agents_id") 
# def read_agents(db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
#     agents = db(agents) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
#     return agents



# @app.get("/all_agents_id", response_model=list[schemas_db.Agents]) 
# def read_agents(db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
#     agents = db.get(agents) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
#     return agents


# @app.get("/agents")
# def get_agents():
#     data = call_db()
#     return data



# # test funktion för att korrigera felet missing one positional argument. * detta kan vara för det inte finns någon data registread i agent_info än. 
# @app.get("/agents_info/", response_model=list[schemas_db.Agenet_infoBase]) 
# def read_agents(db: Session = Depends(get_db)): 
#     agents_info = crud.get_agent(db, read_agents) 
#     return agents_info

###### DETTA ÄR EN ANNAN ROUTE SOM ANTON HAR GJORT OCH SOM JAG SKA FÖRSÖKA FIXA SÅ DEN FUNKAR MED MITT API. 
# @app.put("/update_person")
# def update_person(person: Person):
#     update_person_query = """
#     UPDATE person SET name = ? WHERE id = ?
#     """
#     call_db(update_person_query, person.name, person.id)
#     pass




#---------------------------CONSTRUCTIONS--ZONE----------------------------------




# Här är felet 405 method not allowd.  * se screenshot i mappen. 
@app.post("/agent_create", response_model=schemas_db.Agent_infoCreate)
def create_agent(agent: schemas_db.Agent_infoCreate, db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
    new_agent = crud.create_agent(db)
    if new_agent:
        raise HTTPException(status_code=400, detail="Agent already registered")
    return crud.create_agent(db=db, agent=agent)









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