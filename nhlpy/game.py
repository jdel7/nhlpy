import requests
import json

from .constants import BASE_URL


class Game:
    def __init__(self, id):
        self.id = id

        if self.id < 1917020001:
            raise Exception("The game ID cannot be an int less than 1917020001")

    def all_stats(self):
        response = requests.get("{0}/game/{1}/feed/live".format(BASE_URL, self.id))
        self.data = response.json()

        if self.data.get('message') == "Game data couldn't be found":
            raise Exception("Game ID {} stats not found".format(self.id))

        del self.data["copyright"]
        return self.data

    def boxscore(self):
        response = requests.get("{0}/game/{1}/boxscore".format(BASE_URL, self.id))
        self.data = response.json()

        if self.data.get('message') == "Game data couldn't be found":
            raise Exception("Game ID {} boxscore not found".format(self.id))

        del self.data["copyright"]
        return self.data

    def media(self):
        response = requests.get("{0}/game/{1}/content".format(BASE_URL, self.id))
        self.data = response.json()

        if self.data.get('message') == "Object not found":
            raise Exception("Game ID {} media not found".format(self.id))

        del self.data["copyright"]
        return self.data
