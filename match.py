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
        self.teams = [team1, team2]
    
    def random_match(self, teams):
        """
        Випадково вибирає дві команди з наданого списку для проведення матчу.

        Parameters:
            teams (list): Список об'єктів Team, з яких обираються учасники матчу.

        Returns:
            None
        """
        team_1, team_2 = random.sample(teams, 2)  # випадковий вибір 2 команд
        self.teams = [team_1, team_2]            # зберігаємо їх у об'єкт Match
        
        print(f"🏀 Матч: {team_1.team_name} vs {team_2.team_name}")
    
    def play_match(self):
        """
        Моделює матч між двома командами.

        - Перша команда отримує очки на основі своєї сили (`team_strength()`).
        - Друга команда отримує випадкову кількість очок (0-100).

        Після чого визначається переможець та виводиться результат матчу.

        Returns:
            tuple: (score_1, score_2) - рахунок першої та другої команди.
        """
        
        team1_strength = self.teams[0].get_team_strength()
        team2_strength = self.teams[1].get_team_strength()

        # Обчислюємо рахунок на основі сили команд
        score_1 = random.randint(team1_strength * 3, team1_strength * 5)
        score_2 = random.randint(team2_strength * 3, team2_strength * 5)

        # Додаємо бонус до слабшої команди для балансування матчу
        diff = abs(team1_strength - team2_strength)
        if diff > 0:
            bonus = random.randint(0,3 * diff)
            if team1_strength > team2_strength:
                score_2 += bonus  # Бонус додається до слабшої команди
            elif team2_strength > team1_strength:
                score_1 += bonus  # Бонус додається до слабшої команди
        
        return score_1, score_2

            
