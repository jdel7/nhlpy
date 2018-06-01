import requests
import json

from .constants import BASE_URL

class Conference:

    """
    Shows only active conferences
    """

    def all(self):
        response = requests.get('%s/conferences' % (BASE_URL))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    Shows specific conference and can show World Cup of Hockey
    """

    def info(self, id):
        self.id = id
        response = requests.get('%s/conferences/%s' % (BASE_URL, self.id))
        self.data = response.json()
        del self.data['copyright']
        return self.data

