from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Store(Base):
    __tablename__ = "stores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String)
    street = Column(String)
    phone = Column(String)