# steg 4


from sqlalchemy.orm import Session
import model_db, schemas_db


#-------------------------------------------------ERROR---------------------------------------------------------
# vad vill du att denna ska göra?
# den ska hämta och visa alla agenter i agnets table. 


def get_agents(db: Session): # denna kanske är onöding
    return db.query(schemas_db.Agents)
    


# # denna är från min api.py fil och ska hämta från filen åvan här. 
# # @app.get("/all_agents_id") 
# # def read_agents(db: Session = Depends(get_db)): # det stod Depends före paranteserna här förut 
# #     agents = crud.get_agents(db) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
# #     return agents



# #------------------DETTA ÄR FRÅN FAST APIS TUTORIAL ----------------------------------------
# # DENNA ÄR FRÅN CRUDE SAMMA I MIN och tar from filen models. 
# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()

# # DENNA ÄR FRÅN MAIN ALLTSÅ API I MIN 
# @app.get("/users/", response_model=list[schemas.User]) 
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users
# #-----------------------------------------------------------------





# def get_agents(db: Session): # denna kanske är onöding
#     return db(model_db.Agents)
# print(model_db) #.all() #.filter(model_db.Agent_info.id)




# THE ERROR :
# INFO:     127.0.0.1:60950 - "GET /agents_info/ HTTP/1.1" 500 Internal Server Error
# ERROR:    Exception in ASGI application
# Traceback (most recent call last): [...]


#[...] File "C:\Users\Bananberg\.virtualenvs\api-ldk3itRZ\Lib\site-packages\anyio\_backends\_asyncio.py", line 867, in run
#     result = context.run(func, *args)
#              ^^^^^^^^^^^^^^^^^^^^^^^^
#   File "C:\Users\Bananberg\Desktop\Python_ass\Final_ass2\API\api.py", line 87, in read_agents
#     agents_info = crud.get_agent(db) # DETTA BLEV ETT FEL VID ANVÄNDING I BROWSER. missing one positional argument.
#                   ^^^^^^^^^^^^^^^^^^
# TypeError: get_agent() missing 1 required positional argument: 'agent_id'
#---------------------------------------------------------------------------------------------------------






def create_agent(db: Session, agent_create: schemas_db.Agent_infoCreate): 
    #fake_hashed_password = user.password + "notreallyhashed"
    agent_create = model_db.Agent_info(first_name=agent_create.first_name, last_name=agent_create.last_name) # Det kan saknas ett argumet här som finns i modellen men inte här. 
    db.add(agent_create)
    db.commit()
    db.refresh(agent_create)
    return agent_create

