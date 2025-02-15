from db import execute_query, fetch_all, fetch_one
from robyn import Request


async def create_user(request: Request):
    payload = request.json()
    name, reg, email, department, batch, role = payload["name"], payload["reg"], payload["email"], payload["department"], payload["batch"], payload["role"]
    await execute_query("INSERT INTO users (name, reg, email, department, batch, role) VALUES (?, ?, ?, ?, ?, ?)", (name, reg, email, department, batch, role))
    return {"message": "User created", "data": "your mom"}

async def fetch_user(request: Request):
    user = await fetch_one("SELECT * FROM users")
    return {"data": user }
