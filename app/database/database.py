from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base  

db = create_engine('postgresql://postgres:masterkey@db:5432/flaskapi')
metadata = MetaData(bind=db)

base = declarative_base()

con = db.connect()
