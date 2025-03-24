from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

URL_DATABASE = 'postgresql+asyncpg://postgres:admin@localhost:5432/todo-python-app'

engine = create_async_engine(URL_DATABASE, echo=True)

SessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
