from enum import Enum
from sqlalchemy import Boolean, Column, Integer, String, Date, ForeignKey
from database.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), unique=True)
    password = Column(String)
    email = Column(String(100), unique=True)

    tasks = relationship("Task", back_populates="owner")

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    taskName = Column(String(20))
    taskDescribe = Column(String(200))
    date = Column(Date)
    user_id = Column(Integer, ForeignKey=('users.id'))

    owner = relationship("User", back_populates="tasks")




