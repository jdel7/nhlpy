import requests
import json

from .constants import BASE_URL

class Schedule:

    def today(self, id=None):
        self.id = id
        if self.id == None:
            response = requests.get('%s/schedule' % (BASE_URL))
            self.data = response.json()
            del self.data['copyright']
            return self.data
        else:
            response = requests.get('%s/schedule?teamId=%s' % (BASE_URL, str(self.id)))
            self.data = response.json()
            del self.data['copyright']
            return self.data


    def date(self, start_date=None, end_date=None):
        self.start_date = start_date
        self.end_date = end_date

        if self.start_date == None and self.end_date == None:
            return self.today()
        elif self.start_date != None and self.end_date == None:
            response = requests.get('%s/schedule%s%s' % (BASE_URL, '?date=', str(self.start_date)))
            self.data = response.json()
            del self.data['copyright']
            return self.data
        else:
            return self.today()

    """
    Returns line score for today's completed games. Can't add date parameters to this.
    """
    def linescore(self):
        response = requests.get('%s/schedule?expand=schedule.linescore' % (BASE_URL))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def tickets(self):
        response = requests.get('%s/schedule?expand=schedule.ticket' % (BASE_URL))
        self.data = response.json()
        del self.data['copyright']
        return self.data





