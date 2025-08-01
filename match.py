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
            tuple: score_1, score_2 - рахунок 1 і 2 команди відповідно.
        """
        
        team1_strength = self.teams[0].get_team_strength()
        team2_strength = self.teams[1].get_team_strength()

        score_1 = random.randint(team1_strength * 3, team1_strength * 5)  # випадковий рахунок для команди 1
        score_2 = random.randint(team2_strength * 3, team2_strength * 5)  # випадковий рахунок для команди 2

        diff = abs(team1_strength - team2_strength)
        if diff > 0:
            bonus = random.randint(0, 4 * diff)  # випадковий бонус за різницю сил команд
            if team1_strength > team2_strength:
                score_2 += bonus
            elif team2_strength > team1_strength:
                score_1 += bonus
        
        return score_1, score_2

            
