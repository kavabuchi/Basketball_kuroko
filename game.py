from player import Player
from team import Team
from match import Match
import random

player1 = Player("Koby Bryant", 25, "Point_Guard", 0.3, 100, 10000)
player2 = Player("Lebron James", 25, "Shooting_Guard", 0.3, 100, 15000) 

team_1 = Team("Lakers", 20000)

team_1.add_player(player1)
team_1.add_player(player2)

print(team_1)

team_1.sell_player(player1)
team_1.add_player(player2)

print(team_1)