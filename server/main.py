from fastapi import FastAPI
from database import initialize_database

app = FastAPI()


@app.on_event("startup")
def on_startup():
    initialize_database()


@app.get("/")
def root():
    return {"message": "Finance API is running!"}
