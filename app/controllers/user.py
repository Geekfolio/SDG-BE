import json

from db import execute_query, fetch_all, fetch_one
from robyn import Request


async def create_user(request: Request):
    payload = json.loads(request.body)
    name, reg, email, department, batch, authority = payload["name"], payload["reg"], payload["email"], payload["department"], payload["batch"], payload["authority"]
    await execute_query("INSERT INTO users (name, reg, email, department, batch, authority) VALUES (?, ?, ?, ?, ?, ?)", (name, reg, email, department, batch, authority))
    return {"message": "User created", "data": "your mom"}

async def fetch_user(request: Request):
    payload = json.loads(request.body)
    email = payload["email"]
    user = await fetch_one("SELECT * FROM users WHERE email = ?", [email])
    return {"data": user }

async def fetch_all_users(_request: Request):
    users = await fetch_all("SELECT * FROM users")
    return {"data": users}

async def login(request: Request):
    payload = request.json()
    email, password = payload["email"], payload["password"]
    user = await fetch_one("SELECT * FROM users WHERE email = ? AND reg = ?", (email, password))
    return {"message":"login successful", "data": user}
