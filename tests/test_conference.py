from nhlpy import conference
import pytest


def test_id_equals_zero():
    with pytest.raises(Exception) as excinfo:
        conf = conference.Conference()
        conf.info(0)
    assert 'The conference ID cannot be 0' in str(excinfo.value)


def test_id_is_greater_than_seven():
    with pytest.raises(Exception) as excinfo:
        conf = conference.Conference()
        conf.info(9)
    assert 'The conference ID cannot be an int greater than 7' in str(excinfo.value)


def test_id_is_not_negative():
    with pytest.raises(Exception) as excinfo:
        conf = conference.Conference()
        conf.info(-1)
    assert 'The conference ID cannot be a negative int' in str(excinfo.value)



