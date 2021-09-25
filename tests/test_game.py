from nhlpy import game
import pytest


def test_game_id_is_less_than_earliest():
    with pytest.raises(Exception) as excinfo:
        gm = game.Game(1916020001)
        gm.all_stats()
    assert "The game ID cannot be an int less than 1917020001" in str(excinfo.value)

def test_game_id_9999999999_all_stats():
    with pytest.raises(Exception) as excinfo:
        gm = game.Game(9999999999)
        gm.all_stats()
    assert "Game ID 9999999999 stats not found" in str(excinfo.value)

def test_game_id_9999999999_boxscore():
    with pytest.raises(Exception) as excinfo:
        gm = game.Game(9999999999)
        gm.boxscore()
    assert "Game ID 9999999999 boxscore not found" in str(excinfo.value)

def test_game_id_9999999999_media():
    with pytest.raises(Exception) as excinfo:
        gm = game.Game(9999999999)
        gm.media()
    assert "Game ID 9999999999 media not found" in str(excinfo.value)
