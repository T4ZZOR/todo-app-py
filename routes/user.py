from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import SessionLocal
from schemas.schemas import UserResponse
from models.todoModel import User

router = APIRouter()

# database session
async def get_db():
    async with SessionLocal() as db:
        yield db

@router.get("/users", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users
