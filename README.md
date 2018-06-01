# NHLPY: Simple NHL API Python Wrapper

![nhlpy logo](https://github.com/0xalexdelgado/nhlpy/blob/master/other/pictures/nhlpy.png)

`nhlpy` is an easy to use NHL API python wrapper. This wrapper was designed to be very "thin" and easy to use as it just provides helper functions that map directly to the NHL API, and it's purpose is to get you the data you need as quick as possible. All data is returned as a python object of type `dict`.

## Installing

To install nhlpy with pip:

```python
pip install nhlpy
```

To install nhlpy in a pipenv environment:

```python
pipenv install nhlpy
```

## Usage

One of the best things about the NHL API is that it does not require an API key or any sign up to make requests, so all you have to do is install this package and start using it!

## Example

A quick example showing regular season statistics of the Vegas Golden Knights:

```python
>>> from nhlpy import team
>>> golden_knights = team.id(54)
>>> golden_knights.stats()
{'teams': [{'id': 54, 'name': 'Vegas Golden Knights', 'link': '/api/v1/teams/54', 'venue': {'name': 'T-Mobile Arena', 'link': '/api/v1/venues/null', 'city': 'Las Vegas', 'timeZone': {'id': 'America/Los_Angeles', 'offset': -7, 'tz': 'PDT'}}, 'abbreviation': 'VGK', 'teamName': 'Golden Knights', 'locationName': 'Vegas', 'firstYearOfPlay': '2016', 'division': {'id': 15, 'name': 'Pacific', 'link': '/api/v1/divisions/15'}, 'conference': {'id': 5, 'name': 'Western', 'link': '/api/v1/conferences/5'}, 'franchise': {'franchiseId': 38, 'teamName': 'Golden Knights', 'link': '/api/v1/franchises/38'}, 'teamStats': [{'type': {'displayName': 'statsSingleSeason'}, 'splits': [{'stat': {'gamesPlayed': 82, 'wins': 51, 'losses': 24, 'ot': 7, 'pts': 109, 'ptPctg': '66.5', 'goalsPerGame': 3.268, 'goalsAgainstPerGame': 2.744, 'evGGARatio': 1.121, 'powerPlayPercentage': '21.4', 'powerPlayGoals': 53.0, 'powerPlayGoalsAgainst': 44.0, 'powerPlayOpportunities': 248.0, 'penaltyKillPercentage': '81.4', 'shotsPerGame': 32.7561, 'shotsAllowed': 30.7439, 'winScoreFirst': 0.829, 'winOppScoreFirst': 0.415, 'winLeadFirstPer': 0.75, 'winLeadSecondPer': 0.861, 'winOutshootOpp': 0.688, 'winOutshotByOpp': 0.517, 'faceOffsTaken': 4987.0, 'faceOffsWon': 2439.0, 'faceOffsLost': 2548.0, 'faceOffWinPercentage': '48.9', 'shootingPctg': 10.0, 'savePctg': 0.911}, 'team': {'id': 54, 'name': 'Vegas Golden Knights', 'link': '/api/v1/teams/54'}}, {'stat': {'wins': '4th', 'losses': '5th', 'ot': '24th', 'pts': '5th', 'ptPctg': '5th', 'goalsPerGame': '5th', 'goalsAgainstPerGame': '8th', 'evGGARatio': '9th', 'powerPlayPercentage': '11th', 'powerPlayGoals': '12th', 'powerPlayGoalsAgainst': '6th', 'powerPlayOpportunities': '15th', 'penaltyKillOpportunities': '13th', 'penaltyKillPercentage': '10th', 'shotsPerGame': '11th', 'shotsAllowed': '7th', 'winScoreFirst': '6th', 'winOppScoreFirst': '6th', 'winLeadFirstPer': '15th', 'winLeadSecondPer': '15th', 'winOutshootOpp': '1st', 'winOutshotByOpp': '1st', 'faceOffsTaken': '16th', 'faceOffsWon': '20th', 'faceOffsLost': '22nd', 'faceOffWinPercentage': '22nd', 'savePctRank': '12th', 'shootingPctRank': '8th'}, 'team': {'id': 54, 'name': 'Vegas Golden Knights', 'link': '/api/v1/teams/54'}}]}], 'shortName': 'Vegas', 'officialSiteUrl': 'http://www.vegasgoldenknights.com', 'franchiseId': 38, 'active': True}]}
```