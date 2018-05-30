![nhlpy logo](https://github.com/0xalexdelgado/nhlpy/blob/master/other/pictures/nhlpy.png)

#
`nhlpy` is an easy to use NHL API python wrapper. This wrapper was designed to be very "thin" and easy to use as it just provides helper functions that map directly to the NHL API, and it's purpose it to get you the data you need as quick as possible. 
All data is returned as a python object of type `dict`. 

## Installing

## Usage

The NHL API does not require an API key to make requests so all you have to do is install this package and you can start using it!

### Teams 
The NHL API gives each team in the league an ID number. When working with the Team class, each instance of Team
takes a team id as a parameter. For a list of known team id's please see the document [team-ids.md](https://google.com).

#### Get general team information
```python
golden_knights = Team(54)
print(golden_knights.info())
```

#### Get team statistics
```python
golden_knights = Team(54)
print(golden_knights.stats())
```

#### Get team statistics simplified
```python
golden_knights = Team(54)
print(golden_knights.stats())
```

#### Get team's next game
```python
golden_knights = Team(54)
print(golden_knights.next_game())
```

#### Get team's previous game
```python
nj_devils = Team(1)
print(nj_devils.last_game())
```

#### Get team's current active roster
```python
ny_rangers = Team(3)
print(ny_rangers.roster())
```

### Games

The game class takes a game ID as a parameter when creating an instance of the class. 
__Tip to find a game ID:__ If you want to find a game ID you can go to the NHL team website
of one of the teams that participated in that game, go their schedule, select the game your
looking for and then copy and paste the game ID from your browser's address bar. The game ID will be the number that begins with the year of when the game took place.  

#### Getting a game's stats 
__Note:__ This returns about 30,000 lines of statistics. This is best viewed with some kind 
of JSON viewer.
```python
knights_vs_jackets = Game(2017021023)
print(knights_vs_jackets.all_stats))
```

#### Getting a game's boxscore
```python
knights_vs_jackets = Game(2017021023)
print(knights_vs_jackets.boxscore))
```

#### Getting a game's media
Returns links to media such as pictures and videos of shots, goals, and saves.

```python
knights_vs_jackets = Game(2017021023)
print(knights_vs_jackets.media))
```

### Conferences

#### Return details for all current NHL conferences
```python
conf = Conference()
print(conf.all())
```

#### Return details for specific conference ID
```python
eastern_conference = Conference()
print(eastern_conference.info(1))
```

### Divisions

#### Return details for all current NHL divisions
```python
divisions = Division()
print(divisions.all())
```

#### Returns details for a specific division ID
```python
atlantic = Division()
print(atlantic.info(6))
```

### Player 

A player ID must be specified when creating an instance of the Player class.
You can find a player's ID by searching for the player on your favorite search engine and appending NHL to the search. Then take the 7 digit number from the link. 

For example if you're looking for Alex Ovechkin's player ID, google search
`alex ovechkin nhl` and the first NHL link will be `https://www.nhl.com/player/alex-ovechkin-8471214`. In this case, Ovechkin's player ID is `8471214` to the NHL API. 

#### Get General Details of a Player
```python
ovechkin = Player(8471214)
print(ovechkin.info())
```

#### Single Season Statistics
The `season` method takes two parameters which are valid single season years. 
Valid: (1992, 1993), (2001, 2002), (2017, 2018)
Invalid: (1992, 1998), (2001, 2009)

```python
ovechkin = Player(8471214)
print(ovechkin.season(2017,2018))
```

#### Split Statistics by Home and Away games
```python
ovechkin = Player(8471214)
print(ovechkin.home_away(2017,2018))
```

#### Split Statistics by Win/Loss/OT 
```python
ovechkin = Player(8471214)
print(ovechkin.win_loss(2017,2018))
```

#### Split Statistics by Month
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_month(2017,2018))
```

#### Split Statistics by Day of Week
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_day(2017,2018))
```

#### Split Statistics by Division
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_division(2017,2018))
```

#### Split Statistics by Conference
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_conference(2017,2018))
```

#### Split Statistics by Team
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_team(2017,2018))
```

#### Split Statistics by Game
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_game(2017,2018))
```

#### Regular Season Standing of Player
```python
ovechkin = Player(8471214)
print(ovechkin.standing(2017,2018))
```

#### Goals by Situation 
```python
ovechkin = Player(8471214)
print(ovechkin.goals_by_situation(2017,2018))
```

#### Projected Statistics based on Current Regular Season Pace
```python
ovechkin = Player(8471214)
print(ovechkin.split_by_team(2017,2018))
```






__Note__: Each one of the above methods makes a request to the NHL API








