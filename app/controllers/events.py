import json

from db import execute_many, execute_query, fetch_all, fetch_one
from robyn import Request, Response
from utils import send_email


async def create_event(request: Request):
    NEEDED_AUTHORITY = 2
    payload = json.loads(request.body)
    name, email, description, team_size, event_type, start, end, status = payload["name"], payload["email"], payload["description"], payload["team_size"], payload["event_type"], payload["start"], payload["end"], payload["status"]
    user_authority = await fetch_one("SELECT authority FROM users WHERE email = ?", [email])

    if user_authority and user_authority["authority"] >= NEEDED_AUTHORITY:
        authority = user_authority["authority"]
        last_id = await execute_query("INSERT INTO events (name, description, team_size, event_type, start, end, email, authority, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", [name, description, team_size, event_type, start, end, email, authority, status], fetch_last_id=True)
        departments, years = payload["departments"], payload["years"]
        await execute_many("INSERT INTO event_departments (event_id, department) VALUES (?, ?)", [(last_id, dep) for dep in departments])
        await execute_many("INSERT INTO event_years (event_id, year) VALUES (?, ?)", [(last_id, year) for year in years])
        await send_email()
        return "potachu db la"
    else:
        return "authority not enough"



async def fetch_all_events(request: Request):
    all_events = await fetch_all("SELECT * FROM events")
    return all_events

async def register_event(request: Request):
    payload = json.loads(request.body)
    email, team_name, team_members = payload["email"], payload["team_name"], payload["team_members"]

    query = await fetch_one("SELECT * FROM users WHERE email = ?", [email])
    return query
