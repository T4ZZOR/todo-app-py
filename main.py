from fastapi import FastAPI
from database.init_db import init_db

app = FastAPI()

# initialize database
@app.on_event("startup")
def startup_event():
    init_db()

# main program
@app.get("/")
def home():
    return{"message": "Todo APP is working!"}