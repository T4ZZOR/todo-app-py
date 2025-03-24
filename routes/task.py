from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import SessionLocal
from schemas.schemas import TaskResponse
from models.todoModel import Task

router = APIRouter()

# database session
async def get_db():
    async with SessionLocal() as db:
        yield db

@router.get("/tasks", response_model=List[TaskResponse])
async def get_tasks(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Task))
    tasks = result.scalars().all()
    return tasks