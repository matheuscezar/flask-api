from sqlalchemy import create_engine, Table, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker
from app.database import database


class User(database.base):  
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    mail = Column(String, unique=True)
    password = Column(String)

def __init__(self, name, mail, password):
    self.name = name
    self.mail = mail
    self.password = password

# Session = sessionmaker(database.db)  
# session = Session()

database.base.metadata.create_all(database.db)

users = Table('users', database.metadata, autoload=True)
