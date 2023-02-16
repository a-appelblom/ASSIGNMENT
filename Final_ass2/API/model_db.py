# STEG 2 
# SKAPA MODELLERNA SOM API SKA ANVÄNDA FÖR ATT PRATA/SKAPA DATBASEN. 

from sqlalchemy import *
from sqlalchemy.orm import relationship


# We will use this Base class we created before to create the SQLAlchemy models.
# Import Base from database (the file connect_db.py from above).
# Create classes that inherit from it.
# These classes are the SQLAlchemy models.

from connect_db import Base



class Agents(Base): # User
    __tablename__ = "agents"

    # id = Column(Integer, primary_key=True)
    agents_id =Column( VARCHAR(3), primary_key=True)
    active_service = Column( Boolean, default=False) # denna ska då fungera genom att ge "Active" eller "Offline" 
                                                     # denna ska också fungera som en switch och aktivera en timer. Vid avaktivering loggas tiden i columen time_served. 
                                                     # tiden ska plussas på den befintliga tid som finns i time_served.

  
    #items = relationship("Item", back_populates="owner")


class Agent_info(Base): # Item
    __tablename__ = "agent_info"

    id = Column(Integer, primary_key=True)
    first_name = Column(VARCHAR(100))
    last_name = Column(VARCHAR(100))
    agent_ID = Column(VARCHAR(3), ForeignKey("agents.agents_id")) # Key:n funkar inte. Denna kanske är onödig eftersom man kan få fram all info och ta reda på relationen med hjälp av ID.
    time_served = Column(Time) # denna ska vara kopplad till en funktion som visar tiden som "uppdraget" har tagit. 


    # Agent = relationship("Agent_info", back_populates="agents") # denna ska då vid kallning av Agnet ge info från agent_info och agents 
                                                                # eller data som valjs från Agent_info ger relationell info fron angets också 


# with engine.connect() as conn:
#     agent = Table(
#         "agents",
#         metadata,
#         Column("id", Integer, primary_key=True),
#         Column("agent_id", VARCHAR(3)),
#         Column("active_service", Boolean, default=False), # denna ska då fungera genom att ge "Active" eller "Offline" 
#         )

#     agent_info = Table(
#         "agent_info",
#         metadata,
#         Column("id", Integer, primary_key=True),
#         Column("first_name", VARCHAR(100)),
#         Column("last_name", VARCHAR(100)),
#         Column("agent_id", ForeignKey("agents.agent_id")),
#         Column("time_served", Time),

#         )
# print(engine)

# metadata.create_all(engine)