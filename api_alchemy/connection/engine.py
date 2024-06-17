# This file will create an engine to connect to the database, and a provide a sessionmaker() factory for creating sessions to connect to the database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model.alchemy import Base

# create an engine for connecting to the database
engine = create_engine("sqlite:///../stock.db", echo=True)

# create the tables in the database
Base.metadata.create_all(bind=engine)

# create Session factory for use elsewhere
Session = sessionmaker(bind=engine)