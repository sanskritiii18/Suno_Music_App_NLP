from sqlalchemy import create_engine ,String,Integer,Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from streamlit import exception
import os

#MongoDB → Store playlists, user preferences, song metadata (JSON-based).
#PostgreSQL → Store users, subscriptions, payments, transactions (relational data).
Base = declarative_base()
database_url = os.getenv("database_url")

engine = create_engine(database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    print("connection succesful")
except exception as e:
    print(e)

