import requests
import json

class Team:

    def __init__(self, id):
        self.id = id

    def info(self, data=None):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright'] # Delete the copy right from the beginning of the dictionary
        return self.data

    def active_players(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        path = path + '?expand=team.roster'
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def name(self):
        for team in self.data['teams']:
            print(team['name'])



