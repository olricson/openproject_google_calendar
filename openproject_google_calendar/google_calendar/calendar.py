import sys
import httplib2
from googleapiclient.discovery import build, Resource
from googleapiclient.errors import HttpError
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
from httplib2 import Http
from oauth2client import file, client, tools

CLIENT_SECRET_FILE = 'calender_key.json'
SCOPES = 'https://www.googleapis.com/auth/calendar'
scopes = [SCOPES]
APPLICATION_NAME = 'OpenProject To Google Calendar'


class Calendar:

    def __init__(self, credentials_file):
        self._credentials_file = credentials_file
        self._service = None  # type: Resource
        self._build_service()
        print(type(self._service))

    def _build_service(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets(self._credentials_file, SCOPES)
            creds = tools.run_flow(flow, store)

        self._service = build('calendar', 'v3', http=creds.authorize(Http()), cache_discovery=False)

    def create_event(self, calendar_id, start, end, name, desc=''):
        end_date = end if end is not None else start

        event = self._service.events().insert(calendarId=calendar_id, body={
            'description': desc,
            'summary': name,
            'start': {'date': start},
            'end': {'date': end_date},
        }).execute()
        return event['id']

    def update_event(self, calendar_id, event_id, start, end, desc):
        try:
            event = self._service.events().get(calendarId=calendar_id, eventId=event_id).execute()
        except HttpError as e:
            if e.resp.status == 404:
                return self.create_event(calendar_id, start, end, desc)
        event["start"] = {'dateTime': start}
        event["end"] = {'dateTime': end}
        event["summary"] = desc
        event["description"] = desc
        updated_event = self._service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
        return updated_event["id"]


if __name__ == '__main__':
    c = Calendar('credentials.json')
    c.create_event(calendar_id='-',start='2018-12-5', end='2018-12-6', name='toto')
