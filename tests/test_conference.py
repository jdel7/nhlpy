import pytest
from nhlpy import conference

def first_key(dictionary):
    for key in dictionary:
        return key

def test_conference_all():
    conf = conference.Conference()
    response = conf.all()
    assert isinstance(response, dict)
    assert first_key(response) == 'conferences'
    
def test_conference_info():
    conf = conference.Conference()
    response = conf.info(5)
    assert isinstance(response, dict)
    assert first_key(response) == 'conferences'


