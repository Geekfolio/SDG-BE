from db import execute_query, fetch_one, fetch_all
from robyn import Request


async def create_user(request: Request):
    payload = request.json()
    name, reg, email, department, batch, role = payload["name"], payload["reg"], payload["email"], payload["department"], payload["batch"], payload["role"]
    await execute_query("INSERT INTO users (name, reg, email, department, batch, role) VALUES (?, ?, ?, ?, ?, ?)", (name, reg, email, department, batch, role))
    return {"message": "User created", "data": "your mom"}

async def fetch_user(request: Request):
    user = await fetch_one("SELECT * FROM users")
    return {"data": user }

async def fetch_all_users(request: Request):
    users = await fetch_all("SELECT * FROM users")
    return {"data": users}

async def login(request: Request):
    payload = request.json()
    email, password = payload["email"], payload["password"]
    user = await fetch_one("SELECT * FROM users WHERE email = ? AND reg = ?", (email, password))
    return {"message":"login successful", "data": user}