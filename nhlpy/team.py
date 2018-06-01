import requests
import json

from .constants import BASE_URL

class Team:

    def __init__(self, id):
        self.id = id

    def info(self):
        response = requests.get('%s/teams/%s' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def roster(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        path = path + '?expand=team.roster'
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def name(self):
        for team in self.data['teams']:
            print(team['name'])

    def next_game(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        path = path + '?expand=team.schedule.next'
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def last_game(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        path = path + '?expand=team.schedule.previous'
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    Returns single season stats, regular season stat rankings, and general information about team
    """
    def stats(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self.id)
        path = path + '?expand=team.stats'
        response = requests.get(path)
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    Only returns the single season stats and regular season stat ranknings
    """
    def stats_simple(self):
        response = requests.get('%s/teams/%s/stats' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data




