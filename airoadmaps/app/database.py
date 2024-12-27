

from sqlalchemy import create_engine, MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from app.settings import DATABASE_URL

# Use the appropriate URL for your database
DATABASE_URL = DATABASE_URL


# Create an engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our models
Base = declarative_base()

# Create metadata object
metadata = MetaData()
