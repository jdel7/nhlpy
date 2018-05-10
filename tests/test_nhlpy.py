# We expect that our nhlpy package will have a Team class
import vcr
import requests
from pytest import fixture
from nhlpy.team import Team

@fixture
def team_keys():
    # Responsible only for returning the test data
    return ['teams']

@vcr.use_cassette()
def test_team_info(team_keys):
    """ Tests an API call to get a Teams information """

    team_instance = Team(1)
    response = team_instance.info()

    assert isinstance(response, dict)
    assert response['teams']
    assert set(team_keys).issubset(response.keys())

