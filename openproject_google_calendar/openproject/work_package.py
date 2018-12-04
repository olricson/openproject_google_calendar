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
        return self.data.get('startDate', self.data.get('date', None))

    @property
    def end_date(self):
        return self.data.get('dueDate', None)

    @property
    def planned(self):
        return self.start_date is not None

    def __str__(self):
        return f'Work package: {self.subject}\nID: {self.id}\n' \
            f'Start: {self.start_date} - End {self.end_date}\n' \
            f'Content: {self.content}'

    def __repr__(self):
        return self.__str__()