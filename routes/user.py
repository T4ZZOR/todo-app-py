from fastapi import APIRouter, Depends, HTTPException
from typing import List

from sqlalchemy.ext.asyncio import async_session, AsyncSession
from sqlalchemy.orm import Session, sessionmaker
from database.database import SessionLocal, engine
from schemas.schemas import UserResponse
from models.todoModel import User

router = APIRouter()

# database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/users", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    allUsers = db.query(User).all()
    return allUsers
