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
        my_team_score = self.teams[0].team_strength()
        strength_2 = self.teams[1].team_strength()

        if self.teams[0].team_strength() == 0:
            my_team_score = 0
        elif self.teams[0].team_strength() >= 0 and self.teams[0].team_strength() < 12:
            my_team_score = random.randint(0, 13)
        elif self.teams[0].team_strength() > 12 and self.teams[0].team_strength() < 16:
            my_team_score = random.randint(12, 17)
        elif self.teams[0].team_strength() > 16 and self.teams[0].team_strength() < 21:
            my_team_score = random.randint(16, 22)

        if strength_2 == 0:
            score_2 = 0
        elif 0 <= strength_2 < 12:
            score_2 = random.randint(0, 13)
        elif 12 <= strength_2 < 16:
            score_2 = random.randint(12, 17)
        elif 16 <= strength_2 <= 20:
            score_2 = random.randint(16, 22)
        else:
            score_2 = random.randint(10, 20)

        print(f"Match Result: {self.teams[0].team_name} ({my_team_score}) vs {self.teams[1].team_name} ({score_2})")


        return my_team_score, score_2

            
