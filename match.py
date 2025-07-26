from player import Player
from team import Team
import random


class Match:
    """
    Клас для моделювання баскетбольного матчу між двома командами.

    Атрибути:
        teams (list): Список з двох об'єктів Team, які беруть участь у матчі.
    """
    
    def __init__(self, team1, team2):
        """
        Ініціалізує матч між двома командами.

        Parameters:
            team1 (Team): Перша команда.
            team2 (Team): Друга команда.
        """
        self.teams = [team1, team2]      # список із 2 команд
        # self.date = date
        # self.time = time
        # self.stadium = stadium
    
    def random_match(self, teams):
        """
        Випадково вибирає дві команди з наданого списку для проведення матчу.

        Parameters:
            teams (list): Список об'єктів Team, з яких обираються учасники матчу.

        Returns:
            None
        """
        team_1, team_2 = random.sample(teams, 2)  # випадковий вибір 2 команд
        self.teams = [team_1, team_2]            # зберігаємо їх у об’єкт Match
        
        print(f"Match: {team_1.team_name} vs {team_2.team_name}")
    
    def play_match(self):
        """
        Моделює матч між двома командами.

        - Перша команда отримує очки на основі своєї сили (`team_strength()`).
        - Друга команда отримує випадкову кількість очок (0-100).

        Після чого визначається переможець та виводиться результат матчу.

        Returns:
            None
        """

        opponent_team_strength = random.randint(0, 20)

        if opponent_team_strength >= 0 and opponent_team_strength < 10:
            opponent_team_score = random.randint(0, 13)
        elif opponent_team_strength >= 10 and opponent_team_strength < 15:
            opponent_team_score = random.randint(12, 17)
        elif opponent_team_strength >= 15 and opponent_team_strength <= 20:
            opponent_team_score = random.randint(15, 20)

        if self.teams[0].team_strength() == 0:
            my_team_score = 0
        elif self.teams[0].team_strength() >= 0 and self.teams[0].team_strength() < 12:
            my_team_score = random.randint(0, 13)
        elif self.teams[0].team_strength() > 12 and self.teams[0].team_strength() < 16:
            my_team_score = random.randint(12, 17)
        elif self.teams[0].team_strength() > 16 and self.teams[0].team_strength() < 21:
            my_team_score = random.randint(16, 22)


        if my_team_score > opponent_team_score:
            print(f"{self.teams[0].team_name} wins with {my_team_score} - {opponent_team_score}")
        elif opponent_team_score > my_team_score:
            print(f"{self.teams[1].team_name} wins with {opponent_team_score} - {my_team_score}")
  

        return my_team_score, opponent_team_score
            
