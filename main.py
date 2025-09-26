from fastapi import FastAPI
from sqlmodel import Field, SQLModel

app = FastAPI()

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    password: str

hero_1 = User(username="Ariel", password="1234")

@app.get("/")
async def read_root():
    return {"Login": "Welcome to the Login API"}


@app.post("/login")
async def login(username: str, password: str):
    if username == hero_1.username and password == hero_1.password:
        return {"message": "Login successful"}
    return {"message": "Invalid credentials"}