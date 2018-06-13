import logging
import requests

from .constants import BASE_URL

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger_console_handler = logging.StreamHandler()
logger_console_handler.setLevel(logging.INFO)
logger_formatter = logging.Formatter('%(asctime)s - %(name)s:%(lineno)s - %(levelname)s - %(message)s')
logger_console_handler.setFormatter(logger_formatter)
logger.addHandler(logger_console_handler)


class Team:
    def __init__(self, team_id, populate=False):
        self._id = team_id
        self.Info = None
        self.LastGame = None
        self.NextGame = None
        self.Roster = None
        self.SimpleStats = None
        self.Stats = None

        if populate:
            self.populate_all_data()

    def info(self):
        response = requests.get('%s/teams/%s' % (BASE_URL, str(self._id)))
        data = self.pre_process_data(response.json())
        self.Info = data
        logger.debug(data)

    def last_game(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self._id)
        path = path + '?expand=team.schedule.previous'
        response = requests.get(path)
        data = self.pre_process_data(response.json())
        self.LastGame = data
        logger.debug(data)

    def next_game(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self._id)
        path = path + '?expand=team.schedule.next'
        response = requests.get(path)
        data = self.pre_process_data(response.json())
        self.NextGame = data
        logger.debug(data)

    def roster(self):
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self._id)
        path = path + '?expand=team.roster'
        response = requests.get(path)
        data = self.pre_process_data(response.json())
        self.Roster = data
        logger.debug(data)

    def simple_stats(self):
        """
        Only returns the single season stats and regular season stat rankings
        """
        response = requests.get('%s/teams/%s/stats' % (BASE_URL, str(self._id)))
        data = self.pre_process_data(response.json())
        self.SimpleStats = data
        logger.debug(data)

    def stats(self):
        """
        Returns single season stats, regular season stat rankings, and general information about team
        """
        path = 'https://statsapi.web.nhl.com/api/v1/teams/{}'.format(self._id)
        path = path + '?expand=team.stats'
        response = requests.get(path)
        data = self.pre_process_data(response.json())
        self.Stats = data
        logger.debug(data)

    @staticmethod
    def pre_process_data(data):
        try:
            data = data['teams'][0]
        except KeyError:
            logger.warning('Copyright data not found in response object when attempting to remove it from payload')

        return data

    def populate_all_data(self):
        self.info()
        self.last_game()
        self.next_game()
        self.roster()
        self.simple_stats()
        self.stats()


class SimpleStats(object):
    def __init__(self):
        pass
