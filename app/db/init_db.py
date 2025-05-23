# app/db/init_db.py

from app.db.database import Base, engine
from app import models

def init():
    print("Creating tables if they do not exist...")
    Base.metadata.create_all(bind=engine)
    print("Done.")

if __name__ == "__main__":
    init()
