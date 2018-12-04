import requests
import json
from requests.auth import HTTPBasicAuth
from typing import Dict

from openproject_google_calendar.openproject.work_package import WorkPackage


class OpenProject:

    def __init__(self, url: str, apikey: str):
        self.url = url + "/api/v3/"
        self._apikey = apikey
        self.session = requests.sessions.Session()
        self.session.auth = HTTPBasicAuth('apikey', self._apikey)

    @property
    def projects(self):
        payload = json.loads(self.session.get(self.url + '/projects').content.decode('utf-8'))
        return {data['name']: Project(self, data) for data in payload['_embedded']['elements']}


class Project:

    def __init__(self, server, data):
        self.server = server
        self.id = data['id']
        self.name = data['name']

    @property
    def work_packages(self) -> Dict[int, WorkPackage]:
        payload = json.loads(self.server.session.get(self.server.url+f'projects/{self.id}/work_packages').content.decode('utf-8'))
        return {data['id']: WorkPackage(data) for data in payload['_embedded']['elements']}

    def __str__(self):
        return f"Project: [{self.name}] - id: [{self.id}]"

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    p = OpenProject(url="-",
                apikey='-')

    print(p.projects)
    print(p.projects['Maison'].work_packages[0])
    print(p.projects['Maison'].work_packages[0].start_date)
