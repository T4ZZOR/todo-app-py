from sqlalchemy.orm import Session
from database.database import engine, Base, SessionLocal
from models.todoModel import User, Task
from datetime import date

def init_db():
    Base.metadata.create_all(bind=engine)
    session = Session(bind=engine)

    # add example users
    user1 = User(username="Jack", password="Jack0-Pumpkin", email="jack@example.com")
    user2 = User(username="V", password="Lov3Silverhand!", email="samurai@example.com")

    session.add(user1)
    session.add(user2)
    session.commit()

    # add example task to users
    task1 = Task(taskName="do homework", taskDescribe="math, english", date=date.today(), userId=user1.id)
    task2 = Task(taskName="meeting", taskDescribe="subjects: main plan, date, how dangerous, enemies", date=date.today(), userId=user2.id)
    session.add(task1)
    session.add(task2)
    session.commit()

    session.close()