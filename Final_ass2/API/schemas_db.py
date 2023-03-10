
# STEG 3 

# To avoid confusion between the SQLAlchemy models and the Pydantic models, 
# we will have the file models.py with the SQLAlchemy models, and the file schemas.py with the Pydantic models.
# These Pydantic models define more or less a "schema" (a valid data shape).
# So this will help us avoiding confusion while using both.


# WHAT WE ARE DOING 
######
# Create an ItemBase and UserBase Pydantic models (or let's say "schemas") to have common attributes while creating or reading data.
######
# Create Pydantic models / schemas for reading / returning
# Now create Pydantic models (schemas) that will be used when reading data, when returning it from the API.
################


# ALLT NEDAN FÖRKLARAS I DENNA: https://fastapi.tiangolo.com/tutorial/sql-databases/#__tabbed_1_3

## NOTES 

# Time funktionen funkar inte. 
# Jag vill bygga en funktion som går att atkivera och logga tid efter "avslutat uppdrag"




import time ##
from pydantic import BaseModel
class Agent(BaseModel):
    id: int = None
    first_name: str
    last_name: str
    agent_ID: int
    time_served: int
    pass



#__AGENTS_INFO____MODELLER____________________________________________________________

# en info modell / read
class Agent_infoBase(BaseModel): # Item
    id: int
    first_name: str         # orginalet från models_db.py =  first_name = Column("first_name", VARCHAR(100)),
    last_name: str # Union[str, None] = None
    agent_ID: str    
    #time_served: time ###################### needs an import  


# en skapa modell 
class Agent_infoCreate(Agent_infoBase): # Item
    first_name: str         # orginalet från models_db.py =  first_name = Column("first_name", VARCHAR(100)),
    last_name: str # Union[str, None] = None
    agent_ID: str 


#-------------------------------------------------
class Agent_info(Agent_infoBase): # Item
    id: int
    first_name: str
    time_served: int # needs an import                                  # denna kanske inte behövs. 
                                                                         # Jag tror att mallen som FastAPI har i sin tutorial är annpasad effter vad den vill få ut av sin "user/item" grej 

    class Config:                   
        orm_mode = True # jag vet inte vad denna gör??  
#-------------------------------------------------
#______________________________________________________________________________________






#______AGENTS_____MODELLER_____________________________________________________________


# en info modell /read
class AgentsBase(BaseModel): # User 
    agents_id: str
    active_service: bool
    
    class Config: 
        orm_mode = True 

# en skapa modell
class AgentsCreate(AgentsBase): # User 
    agents_id: str
    active_service: bool

#-------------------------------------------------
class Agents(AgentsBase): # User 
    agents_id: str
    active_service: bool                            
    
    class Config: 
        orm_mode = True # jag vet inte vad denna gör?? 
#-------------------------------------------------





