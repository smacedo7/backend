from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import sesionmaker

DATABSE_URL = 'postgresql://postgresql:postgresql@localhost/escola'

engine = create_engine(DATABSE_URL)
SessionLocal = sesionmaker(bind=engine)

Base = declarative_base()
