from player import Player
from team import Team
import random


class Match:
    
    def __init__(self, date, time, stadium, match):
        self.teams = []
        self.date = date
        self.time = time
        self.stadium = stadium
        self.match = match
    
    def append_team(self, team):
        self.teams.append(team)
        # teams = [Team("Lakers", 1000000), Team("Warriors", 950000), Team("Celtics", 900000)]
    
    def random_match(teams, team_1, team_2):
        import random
        team_1, team_2 = random.sample(teams, 2)
        print(f"Match: {team_1.team_name} vs {team_2.team_name}")

            
