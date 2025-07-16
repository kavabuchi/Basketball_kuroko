from player import Player
from team import Team
import random


class Match:
    
    def __init__(self, date, time, stadium):
        self.teams = []          # список із 2 команд
        self.date = date
        self.time = time
        self.stadium = stadium
    
    def random_match(self, teams):
        team_1, team_2 = random.sample(teams, 2)  # випадковий вибір 2 команд
        self.teams = [team_1, team_2]             # зберігаємо їх у об’єкт Match
        print(f"Match: {team_1.team_name} vs {team_2.team_name}")


            
