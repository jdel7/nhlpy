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
        self.example_data = {
            {
                'conference': {
                    'link': '/api/v1/conferences/5',
                    'id': 5,
                    'name': 'Western'
                },
                'locationName': 'Vegas',
                'name': 'Vegas Golden Knights',
                'division': {
                    'link': '/api/v1/divisions/15',
                    'id': 15,
                    'name': 'Pacific'
                },
                'firstYearOfPlay': '2016',
                'teamStats': [
                    {
                        'type': {
                            'displayName': 'statsSingleSeason'
                        },
                        'splits': [
                            {
                                'stat': {
                                    'faceOffsWon': 2439.0,
                                    'goalsAgainstPerGame': 2.744,
                                    'winScoreFirst': 0.829,
                                    'winLeadFirstPer': 0.75,
                                    'goalsPerGame': 3.268,
                                    'evGGARatio': 1.121,
                                    'powerPlayGoalsAgainst': 44.0,
                                    'pts': 109,
                                    'powerPlayGoals': 53.0,
                                    'shootingPctg': 10.0,
                                    'shotsPerGame': 32.7561,
                                    'savePctg': 0.911,
                                    'faceOffsLost': 2548.0,
                                    'powerPlayPercentage': '21.4',
                                    'ptPctg': '66.5',
                                    'winOutshootOpp': 0.688,
                                    'powerPlayOpportunities': 248.0,
                                    'shotsAllowed': 30.7439,
                                    'winLeadSecondPer': 0.861,
                                    'faceOffsTaken': 4987.0,
                                    'winOppScoreFirst': 0.415,
                                    'gamesPlayed': 82,
                                    'faceOffWinPercentage': '48.9',
                                    'wins': 51,
                                    'losses': 24,
                                    'winOutshotByOpp': 0.517,
                                    'penaltyKillPercentage': '81.4',
                                    'ot': 7
                                },
                                'team': {
                                    'link': '/api/v1/teams/54',
                                    'id': 54,
                                    'name': 'Vegas Golden Knights'
                                }
                            },
                            {
                                'stat': {
                                    'faceOffsWon': '20th',
                                    'losses': '5th',
                                    'winScoreFirst': '6th',
                                    'winLeadFirstPer': '15th',
                                    'penaltyKillOpportunities': '13th',
                                    'goalsPerGame': '5th',
                                    'evGGARatio': '9th',
                                    'powerPlayGoalsAgainst': '6th',
                                    'pts': '5th',
                                    'powerPlayGoals': '12th',
                                    'shotsPerGame': '11th',
                                    'faceOffsLost': '22nd',
                                    'powerPlayPercentage': '11th',
                                    'ptPctg': '5th',
                                    'savePctRank': '12th',
                                    'winOutshootOpp': '1st',
                                    'powerPlayOpportunities': '15th',
                                    'shootingPctRank': '8th',
                                    'shotsAllowed': '7th',
                                    'winLeadSecondPer': '15th',
                                    'faceOffsTaken': '16th',
                                    'winOppScoreFirst': '6th',
                                    'faceOffWinPercentage': '22nd',
                                    'wins': '4th',
                                    'goalsAgainstPerGame': '8th',
                                    'winOutshotByOpp': '1st',
                                    'penaltyKillPercentage': '10th',
                                    'ot': '24th'
                                },
                                'team': {
                                    'link': '/api/v1/teams/54',
                                    'id': 54,
                                    'name': 'Vegas Golden Knights'
                                }
                            }
                        ]
                    }
                ],
                'venue': {
                    'city': 'Las Vegas',
                    'link': '/api/v1/venues/null',
                    'name': 'T-Mobile Arena',
                    'timeZone': {
                        'tz': 'PDT',
                        'id': 'America/Los_Angeles',
                        'offset': -7
                    }
                },
                'teamName': 'Golden Knights',
                'abbreviation': 'VGK',
                'active': True,
                'franchiseId': 38,
                'link': '/api/v1/teams/54',
                'officialSiteUrl':             'http://www.vegasgoldenknights.com',
                'franchise': {
                    'franchiseId': 38,
                    'link': '/api/v1/franchises/38',
                    'teamName': 'Golden Knights'
                },
                'shortName': 'Vegas',
                'id': 54
            }
        }
