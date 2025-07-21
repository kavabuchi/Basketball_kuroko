from player import Player
from team import Team
import random


class Match:
    
    def __init__(self, team1, team2):
        self.teams = [team1, team2]      # список із 2 команд
        # self.date = date
        # self.time = time
        # self.stadium = stadium
    
    def random_match(self, teams):
        team_1, team_2 = random.sample(teams, 2)  # випадковий вибір 2 команд
        self.teams = [team_1, team_2]            # зберігаємо їх у об’єкт Match
        
        print(f"Match: {team_1.team_name} vs {team_2.team_name}")
    
    def play_match(self):
        my_team_score = self.teams[0].team_strength()
        team2_score = random.randint(0, 100)
        if my_team_score  > team2_score:
            print(f"{self.teams[0].team_name} wins with {my_team_score} - {team2_score}")
        elif team2_score > my_team_score:
            print(f"{self.teams[1].team_name} wins with {team2_score} - {my_team_score}")


            
