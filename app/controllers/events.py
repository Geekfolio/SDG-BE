import json

from db import execute_many, execute_query, fetch_all, fetch_one
from robyn import Request, Response
from utils import send_email, send_registration_email


async def create_event(request: Request):
    NEEDED_AUTHORITY = 2
    payload = json.loads(request.body)
    name, email, description, team_size, event_type, start, end, status = (
        payload["name"],
        payload["email"],
        payload["description"],
        payload["team_size"],
        payload["event_type"],
        payload["start"],
        payload["end"],
        payload["status"],
    )
    user_authority = await fetch_one("SELECT authority FROM users WHERE email = ?", [email])

    if user_authority and user_authority["authority"] >= NEEDED_AUTHORITY:
        authority = user_authority["authority"]
        last_id = await execute_query(
            "INSERT INTO events (name, description, team_size, event_type, start, end, email, authority, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            [name, description, team_size, event_type, start, end, email, authority, status],
            fetch_last_id=True
        )
        departments, years = payload["departments"], payload["years"]
        await execute_many("INSERT INTO event_departments (event_id, department) VALUES (?, ?)", [(last_id, dep) for dep in departments])
        await execute_many("INSERT INTO event_years (event_id, year) VALUES (?, ?)", [(last_id, year) for year in years])
        await send_email(name, start, description)
        return {"message": "Event created successfully"}
    else:
        return {"message": "Authority not enough"}



async def fetch_all_events(request: Request):
    all_events = await fetch_all("SELECT * FROM events")
    return all_events

async def register_event(request: Request):
    payload = json.loads(request.body)
    email = payload["email"]
    team_name = payload["team_name"]
    team_members = payload["team_members"]
    event_name = payload["event_name"]
    event_date = payload["event_date"]
    event_id = payload["event_id"]

    await execute_query("INSERT INTO events_registered(event_id, email_id) VALUES(?, ?)", (event_id, email))
    user = await fetch_one("SELECT * FROM users WHERE email = ?", [email])
    if user:
        send_registration_email(email, event_name, event_date, team_name, team_members)
        return {"message": "Registration successful"}
    else:
        return {"message": "User not found"}, {}, 404

async def create_feedback(request: Request):
	payload = json.loads(request.body)
	event_id, email_id, rating, review = (payload["event_id"], payload["email_id"], payload["rating"], payload["review"])

	await execute_query("INSERT INTO feedback(email_id, event_id, rating, review) VALUES(?, ?, ?, ?)", (email_id, event_id, rating, review))
	return {"message": "Feedback added"}

async def get_registered_events(request: Request):
    payload = request.query_params.to_dict()
    email = payload["email"][0]

    events = await fetch_all("SELECT er.event_id as id, e.name, e.email, e.description, e.event_type, e.team_size, e.start, e.end, e.participants, e.status, e.authority FROM events_registered AS er JOIN events AS e ON er.event_id = e.id WHERE er.email_id = ?", [email])
    return events
