import requests
import json

from constants import BASE_URL

class Schedule:

    def today(self):
        response = requests.get('%s/schedule' % (BASE_URL))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def date(self, start_date=None, end_date=None):
        self.start_date = start_date
        self.end_date = end_date

        if self.start_date == None and self.end_date == None:
            return self.today()

        if self.start_date != None and self.end_date == None:
            response = requests.get('%s/schedule%s%s' % (BASE_URL, '?date=', str(self.start_date)))
            self.data = response.json()
            del self.data['copyright']
            return self.data

        if self.start_date == None and self.end_date == None:
            return self.today()



