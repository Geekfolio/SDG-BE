import os
import smtplib
import sys

from db import fetch_all
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
if (not EMAIL or not PASSWORD):
	print("No email/password")
	sys.exit(1);

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo()
s.starttls()

s.login(EMAIL, PASSWORD)


async def send_email(event_name, event_date, event_description):
    subject = f"New Hackathon Event: {event_name}"
    body = (
        "Dear Participant,\n\n"
        "We are excited to announce our upcoming hackathon event!\n\n"
        f"Event: {event_name}\n"
        f"Date: {event_date}\n"
        f"Description: {event_description}\n\n"
        "Please register at your earliest convenience.\n\n"
        "Regards,\n"
        "Team X-Helios"
    )
    message = f"Subject: {subject}\n\n{body}"

    query = await fetch_all("SELECT email FROM users WHERE authority = 4")
    for i in query:
        s.sendmail(EMAIL, i["email"], message)

def send_registration_email(recipient_email, event_name, event_date, team_name, team_members):
    subject = f"Registration Confirmation for {event_name}"
    if isinstance(team_members, list):
        members_text = ", ".join(team_members)
    else:
        members_text = team_members

    body = (
        f"Dear Participant,\n\n"
        f"Thank you for registering for our upcoming hackathon event, {event_name}.\n\n"
        f"Event Date: {event_date}\n"
        f"Team Name: {team_name}\n"
        f"Team Members: {members_text}\n\n"
        "We look forward to your active participation.\n\n"
        "Regards,\n"
        "Hackathon Team"
    )
    message = f"Subject: {subject}\n\n{body}"
    s.sendmail(EMAIL, recipient_email, message)
