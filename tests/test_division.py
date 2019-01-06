from nhlpy import division
import pytest


def test_division_id_equals_zero():
    with pytest.raises(Exception) as excinfo:
        div = division.Division()
        div.info(0)
    assert "The division ID cannot be 0" in str(excinfo.value)


def test_division_id_is_greater_than_eighteen():
    with pytest.raises(Exception) as excinfo:
        div = division.Division()
        div.info(19)
    assert "The division ID cannot be an int greater than 18" in str(excinfo.value)


def test_division_id_is_negative():
    with pytest.raises(Exception) as excinfo:
        div = division.Division()
        div.info(-1)
    assert "The division ID cannot be a negative int" in str(excinfo.value)
