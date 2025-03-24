from database.database import engine, Base, SessionLocal
from models.todoModel import User, Task
from datetime import date

async def init_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    async with SessionLocal() as session:
        # add example users
        user1 = User(username="Jack", password="Jack0-Pumpkin", email="jack@example.com")
        user2 = User(username="V", password="Lov3Silverhand!", email="samurai@example.com")
        user3 = User(username="Geralt", password="L0veGwent!", email="wolf.g@gmail.com")

        session.add_all([user1, user2, user3])
        await session.commit()

        await session.refresh(user1)
        await session.refresh(user2)
        await session.refresh(user3)

        # add example task to users
        task1 = Task(taskName="do homework", taskDescribe="math, english", date=date.today(), user_id=user1.id)
        task2 = Task(taskName="meeting", taskDescribe="subjects: main plan, date, how dangerous, enemies", date=date.today(), user_id=user2.id)
        session.add_all([task1, task2])
        await session.commit()

        await session.close()