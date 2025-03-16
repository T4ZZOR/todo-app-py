from fastapi import FastAPI
from database.init_db import init_db
from routes import user, task

app = FastAPI()

# initialize database
@app.on_event("startup")
async def startup_event():
    await init_db()

# add routes
app.include_router(user.router)
app.include_router(task.router)

# main program
@app.get("/")
async def home():
    return{"message": "Todo APP is working!"}