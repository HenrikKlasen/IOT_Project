# main code from https://developers.google.com/calendar/api/quickstart/python?hl=fr
# https://expertbeacon.com/mastering-google-calendar-api-integration-in-python-a-comprehensive-guide/#:~:text=Mastering%20Google%20Calendar%20API%20Integration%20in%20Python%3A%20A,Best%20Practices%20and%20Considerations%20...%206%20Conclusion%20 

from datetime import datetime
from datetime import timezone
import os.path
import os
from dotenv import load_dotenv
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def setupCalendar():
  """Shows basic usage of the Google Calendar API.
  Prints the start and name of the next 10 events on the user's calendar.
  """
  load_dotenv()
  
  apiKey = os.getenv("GOOGLE_CALENDAR_API_KEY")
  creds = {
    'apiKey' : apiKey
  }
  credsJSON = json.dumps(creds)
  
  SCOPES = ["https://www.googleapis.com/auth/calendar"]
  
  #credentials = Credentials.from_authorized_user_file(credsJSON, SCOPES)
  
  flow = InstalledAppFlow.from_client_secrets_file("././client_secret.json", SCOPES)
  credentials = flow.run_local_server(port=0)
  
  try:
    
    # aythenticated service object
    calendarService = build("calendar", "v3", credentials=credentials)

    # Call the Calendar API
    # use of Central Europe Time to get time of Luxembourg
    now = datetime.now(timezone.timezone.cet).isoformat() + "CET"
    
    #retrieve list of calendars that the auth user has access to (maybe not useful)
    calendar_list = calendarService.calendarList().list().execute()
    for calendar in calendar_list["items"]:
      print(f"Calendar ID: {calendar["id"]}")
      print(f"Calendar Name: {calendar["summary"]}")
    
    calendarId = "primary"
    
    print(f"Getting the upcoming 10 events from the {calendarId} calendar")
    events_result = (
        calendarService.events()
        .list(
            calendarId=calendarId,
            timeMin=now,
            maxResults=10,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

    # Prints the start and name of the next 10 events
    for event in events:
      print(f"Event Name: {event["summary"]}")
      print(f"Event Start: {event["start"].get("dateTime", event["start"].get("date"))}")
      print(f"Event End: {event["end"].get("dateTime", event["end"].get("date"))}")

  except HttpError as error:
    print(f"An error occurred: {error}")


if __name__ == "__main__":
  setupCalendar()