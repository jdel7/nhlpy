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

    def split_by_month(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=byMonth&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def split_by_day(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=byDayOfWeek&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def split_by_division(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=vsDivision&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def split_by_conference(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=vsConference&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def split_by_team(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=vsTeam&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def split_by_game(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=gameLog&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def standing(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=regularSeasonStatRankings&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    def goals_by_situation(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=goalsByGameSituation&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data

    """
    This only works with the current in-progress season during the regular season
    """
    def on_pace_stats(self, year_start, year_end):
        self.year_start = year_start
        self.year_end = year_end
        response = requests.get('%s/people/%s/%s%s%s' % (BASE_URL, str(self.id),
            'stats?stats=onPaceRegularSeason&season=', str(self.year_start), str(self.year_end)))
        self.data = response.json()
        del self.data['copyright']
        return self.data













