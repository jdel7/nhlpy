import requests
import json

from constants import BASE_URL

class Player:

    def __init__(self, id):
        self.id = id

    """
    Gets details for player, id must be specified to return data
    """

    def info(self):
        response = requests.get('%s/people/%s' % (BASE_URL, str(self.id)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    Get single season stats for a player. Two valid consecutive years must
    be specified.
    """

    def season(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=statsSingleSeason&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def home_away(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=homeAndAway&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def win_loss(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=winLoss&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data







