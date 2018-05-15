[nhlpy logo](nhlpy/other/pictures/nhlpy.png)

# nhlpy
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

__Note__: Each one of the above methods makes a request to the NHL API



### To Do
1. Add a license
2. Add tests
3. Add CI
4. Add code of conduct
5. Prettify the JSON or `dict` output 



