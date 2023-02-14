# steg 4


from sqlalchemy.orm import Session
import model_db, schemas_db



def get_agent(db: Session, agent_id: str ): # denna kanske är onöding
    return db.query(model_db.Agent_info) #.filter(model_db.Agent_info.id)

def create_agent(db: Session, agent_info: schemas_db.Agent_infoCreate): 
    #fake_hashed_password = user.password + "notreallyhashed"
    agent_info = model_db.Agent_info(first_name=agent_info.first_name, last_name=agent_info.last_name)
    db.add(agent_info)
    db.commit()
    db.refresh(agent_info)
    return agent_info

