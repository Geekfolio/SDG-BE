import os
import smtplib

from db import fetch_all
from dotenv import load_dotenv

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

s = smtplib.SMTP("smtp.gmail.com", 587)
s.ehlo() 
s.starttls()

s.login(EMAIL, PASSWORD)


async def send_email():
    subject = "You have successfully registered for the event"
    body = "You have successfully registered for the event"
    message = f"Subject: {subject}\n\n{body}"

    query = await fetch_all("SELECT email FROM users WHERE authority = 4")
    for i in query:
        s.sendmail(EMAIL, i["email"], message)
