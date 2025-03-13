from fastapi import FastAPI
from database.init_db import init_db
from routes import user

app = FastAPI()

# initialize database
init_db()

# add routes
app.include_router(user.router)

# main program
@app.get("/")
async def home():
    return{"message": "Todo APP is working!"}