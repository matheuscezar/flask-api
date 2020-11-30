from sqlalchemy import create_engine, Table, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from app.database import database


class Phone(database.base):  
    __tablename__ = 'phones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    value = Column(String)
    monthyPrice = Column(Float)
    setupPrice = Column(String)
    currency = Column(String)

#Session = sessionmaker(database.db)  
#session = Session()

database.base.metadata.create_all(database.db)
phones = Table('phones', database.metadata, autoload=True)