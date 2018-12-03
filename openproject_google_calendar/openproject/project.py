import requests
import json
from requests.auth import HTTPBasicAuth

from openproject_google_calendar.openproject.work_package import WorkPackage


class Project:

    def __init__(self, url, apikey):
        self._url = url + "/api/v3/"
        self._apikey = apikey
        self.id = 3

    @property
    def projects(self):
        return json.loads(requests.get(self._url+'/projects', auth=HTTPBasicAuth('apikey', self._apikey))
                          .content.decode('utf-8'))

    @property
    def work_packages(self):
        payload = json.loads(requests.get(self._url+f'projects/{self.id}/work_packages',
                                       auth=HTTPBasicAuth('apikey', self._apikey)).content.decode('utf-8'))

        return [WorkPackage(data) for data in payload['_embedded']['elements']]


if __name__ == '__main__':
    p = Project(url="-",
                apikey='-')

    print(json.loads(p.projects.content.decode('utf-8')))
    print(p.work_packages[0])
