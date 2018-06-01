import requests
import json

from .constants import BASE_URL

class Game:

    def __init__(self, id):
        self.id = id

    """
    Returns over 30k lines of detailed game information
    """

    def all_stats(self):
        response = requests.get('%s/game/%s/feed/live' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def boxscore(self):
        response = requests.get('%s/game/%s/boxscore' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def media(self):
        response = requests.get('%s/game/%s/content' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data




