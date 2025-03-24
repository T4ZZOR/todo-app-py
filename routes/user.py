from http.client import HTTPException

from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.database import SessionLocal
from schemas.schemas import UserResponse, UserCreate
from models.todoModel import User

router = APIRouter(prefix="/users")

# database session
async def get_db():
    async with SessionLocal() as db:
        yield db

@router.get("/", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))
    users = result.scalars().all()
    return users

@router.post("/add", response_model=UserResponse)
async def add_users(user: UserCreate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this email exist in database!")

    new_user = User(username=user.username, email=user.email, password=user.password)

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return new_user