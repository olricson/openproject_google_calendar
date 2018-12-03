import json


class WorkPackage:

    def __init__(self, data):
        # print(json.dumps(data, indent=4))
        self.subject = data['subject']
        self.data = data
        self.id = data['id']
        self.content = data['description']['html']

    @property
    def start_date(self):
        return self.data['startDate']

    @property
    def end_date(self):
        return self.data.get('endDate', None)

    def __str__(self):
        return f'Work package: {self.subject} \nID: {self.id}\nContent: {self.content}'
