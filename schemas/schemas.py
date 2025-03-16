from pydantic import BaseModel
from datetime import date

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        from_attributes  = True

class TaskResponse(BaseModel):
    id: int
    taskName: str
    taskDescribe: str
    date: date
    user_id: int

    class Config:
        from_attributes = True