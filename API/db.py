
# import os
# from sqlalchemy import (
#     create_engine,
#     engine,
#     Time,
#     Boolean, 
#     Table,
#     Column,
#     String,
#     Integer,
#     MetaData,
#     ForeignKey,
#     VARCHAR,
#     insert,
# )
from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker


#############################################
######## HÄR SKAPAR VI DATABASEN! ###########
                                          
engine = create_engine("sqlite:///Agents.db", echo=True) # echo är gött att ha så man ser vad man gör.
meta_data = MetaData()
    # nu skapar vi tables och vad de ska inehålla. 

agent = Table(
    "agents",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("agent_id", VARCHAR(3)),
    Column("active_service", Boolean, default=False), # denna ska då fungera genom att ge "Active" eller "Offline" 
    )

agent_info = Table(
    "agent_info",
    meta_data,
    Column("id", Integer, primary_key=True),
    Column("first_name", VARCHAR(100)),
    Column("last_name", VARCHAR(100)),
    Column("agent_id", ForeignKey("agents.id")),
    Column("active_service", Time),

    )
print(engine)
meta_data.create_all(engine)



















# class DB: 
#     engine = create_engine("sqlite:///Agents.db", echo=True) # echo är gött att ha så man ser vad man gör.
#     meta_data = MetaData()
#         # nu skapar vi tables och vad de ska inehålla. 

#     agent = Table(
#         "agents",
#         meta_data,
#         Column("id", Integer, primary_key=True),
#         Column("agent_id", VARCHAR(3)),
#         Column("active_service", Boolean, default=False), # denna ska då fungera genom att ge "Active" eller "Offline" 
#         )

#     agent_info = Table(
#         "agent_info",
#         meta_data,
#         Column("id", Integer, primary_key=True),
#         Column("first_name", VARCHAR(100)),
#         Column("last_name", VARCHAR(100)),
#         Column("agent_id", ForeignKey("agents.id")),
#         Column("active_service", Time),

#         )
#     print(engine)
#     meta_data.create_all(engine)
