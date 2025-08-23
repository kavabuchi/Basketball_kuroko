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
        team1_strength = 0
        team1_fatigue = 0
        team1_count = len(self.teams[0].playing_players)

        for player in self.teams[0].playing_players:
            coef = player.player_coef
            if player.fatigue >= 0.5 and player.fatigue <= 0.8:
                coef *= 0.8  # Зменшуємо внесок для втоми 0.5–0.8

            elif player.fatigue > 0.8:
                coef *= 0.5  # Зменшуємо внесок для втоми > 0.8
            team1_strength += coef
            team1_fatigue += player.fatigue

        team1_strength = int(team1_strength)
        team1_avg_fatigue = team1_fatigue / team1_count if team1_count > 0 else 0

        team2_strength = 0
        team2_fatigue = 0
        team2_count = len(self.teams[1].playing_players)

        for player in self.teams[1].playing_players:
            coef = player.player_coef
            if player.fatigue >= 0.5 and player.fatigue <= 0.8:
                coef *= 0.8

            elif player.fatigue > 0.8:
                coef *= 0.5

            team2_strength += coef
            team2_fatigue += player.fatigue

        team2_strength = int(team2_strength)
        team2_avg_fatigue = team2_fatigue / team2_count if team2_count > 0 else 0

        # Зменшуємо верхню межу для втомлених команд
        team1_max = team1_strength * 4 if team1_avg_fatigue > 0.5 else team1_strength * 5
        team2_max = team2_strength * 4 if team2_avg_fatigue > 0.5 else team2_strength * 5

        score_1 = random.randint(team1_strength * 3, team1_max)  # Рахунок для команди 1
        score_2 = random.randint(team2_strength * 3, team2_max)  # Рахунок для команди 2
       
        diff = abs(team1_strength - team2_strength)
        if diff > 0:
            bonus = random.randint(0, 4 * diff)  # випадковий бонус за різницю сил команд
            if team1_strength > team2_strength:
                score_2 += bonus
            elif team2_strength > team1_strength:
                score_1 += bonus
        
        return score_1, score_2

            
