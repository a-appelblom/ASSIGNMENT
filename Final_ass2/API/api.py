
from fastapi import FastAPI, HTTPException
from sqlalchemy.orm import Session

import model_db, schemas_db
from connect_db import SessionLocal, engine



model_db.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    db.close()