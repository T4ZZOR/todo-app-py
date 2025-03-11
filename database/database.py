from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = 'postgresql://postgres:admin@localhost:5432/todo-python-app'

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocomit=False, autoflush=False, bind=engine)

Base = declarative_base()