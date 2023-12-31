from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

app = APIRouter()

@app.get("/")
async def get_data():
    return conn.execute(users.select()).fetchall()

@app.get("/{id}")
async def get_data(id: int):
    query = users.select().where(users.c.id == id)
    result = conn.execute(query)
    return result.fetchall()
    
@app.post("/")
async def write_data(user: User):
     conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password,
    ))
     return conn.execute(users.select()).fetchall()
    

@app.put("/{id}")
async def update_data(id: int, user: User):
    conn.execute(users.update().where(users.c.id == id).values(
        name=user.name,
        email=user.email,
        password=user.password,
    ))
    return conn.execute(users.select()).fetchall()

@app.delete("/{id}")
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
