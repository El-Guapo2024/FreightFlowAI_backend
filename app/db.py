from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import settings

# Create the SQLAlchemy engine
#echo=True logs all SQL queries to the console 

if "sqlite" in settings.DATABASE_URL:
    connect_args = {"check_same_thread": False}
else:
    connect_args = {}

engine = create_engine(settings.DATABASE_URL, echo=True, connect_args=connect_args)

# Create a SessionLocal class
# Each request will crate a new session instance from this class

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our models
# All our database models will inherit from this

Base = declarative_base()

# Dependendcy for FastApi routes

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()