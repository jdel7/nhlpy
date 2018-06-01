import requests
import json

from .constants import BASE_URL

class Division:

    """
    Shows only active divisions
    """

    def all(self):
        response = requests.get('%s/divisions' % (BASE_URL))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    Can show inactive divisions if specified
    """

    def info(self, id):
        self.id = id
        response = requests.get('%s/divisions/%s' % (BASE_URL, self.id))
        self.data = response.json()
        del self.data['copyright']
        return self.data




