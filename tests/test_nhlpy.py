# We expect that our nhlpy package will have a Team class
from nhlpy import team

def test_team_info():

    test_team = team.Team(54)
    response = test_team.info()

    assert isinstance(response, dict)
    assert response['teams'] == [
  {
    'id': 54,
    'name': 'Vegas Golden Knights',
    'link': '/api/v1/teams/54',
    'venue': {
      'name': 'T-Mobile Arena',
      'link': '/api/v1/venues/null',
      'city': 'Las Vegas',
      'timeZone': {
        'id': 'America/Los_Angeles',
        'offset': -7,
        'tz': 'PDT'
      }
    },
    'abbreviation': 'VGK',
    'teamName': 'Golden Knights',
    'locationName': 'Vegas',
    'firstYearOfPlay': '2016',
    'division': {
      'id': 15,
      'name': 'Pacific',
      'link': '/api/v1/divisions/15'
    },
    'conference': {
      'id': 5,
      'name': 'Western',
      'link': '/api/v1/conferences/5'
    },
    'franchise': {
      'franchiseId': 38,
      'teamName': 'Golden Knights',
      'link': '/api/v1/franchises/38'
    },
    'shortName': 'Vegas',
    'officialSiteUrl': 'http://www.vegasgoldenknights.com',
    'franchiseId': 38,
    'active': True
  }
]

