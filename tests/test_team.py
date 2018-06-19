# We expect that our nhlpy package will have a Team class
from nhlpy import team

def test_team_info():

  team_info_keys = [
    'id', 'name', 'link', 'venue', 'abbreviation', 'teamName', 'locationName', 'firstYearOfPlay',
   'division', 'conference', 'franchise', 'shortName', 'officialSiteUrl', 'franchiseId', 'active'
   ]

  golden_knights = team.Team(54)
  response = golden_knights.info()
  keys = response['teams']
  keys = keys[0]
  keys = [*keys]

  assert isinstance(response, dict)
  assert team_info_keys == keys

def test_team_roster():

  team_roster_keys = [
      'id', 'name', 'link', 'venue', 'abbreviation', 'teamName', 'locationName', 'firstYearOfPlay', 
    'division', 'conference', 'franchise', 'roster', 'shortName', 'officialSiteUrl', 'franchiseId', 'active'
  ]

  golden_knights = team.Team(54)
  response = golden_knights.roster()
  keys = response['teams']
  keys = keys[0]
  keys = [*keys]

  assert isinstance(response, dict)
  assert team_roster_keys == keys

def test_team_stats():

  team_stats_keys = [
    'id', 'name', 'link', 'venue', 'abbreviation', 'teamName', 'locationName', 'firstYearOfPlay',
   'division', 'conference', 'franchise', 'teamStats', 'shortName', 'officialSiteUrl', 'franchiseId', 'active'
   ]

  golden_knights = team.Team(54)
  response = golden_knights.stats()
  keys = response['teams']
  keys = keys[0]
  keys = [*keys]

  assert isinstance(response, dict)
  assert team_stats_keys == keys