from player import Player
from team import Team
import random


class Match:
    """
    Клас для моделювання баскетбольного матчу між двома командами.

    Атрибути:
        teams (list): Список з двох об'єктів Team, які беруть участь у матчі.
    """
    
    # Константи класу для покращення читабельності та легкості налаштування
    FATIGUE_MODERATE_THRESHOLD = 0.5
    FATIGUE_HIGH_THRESHOLD = 0.8
    FATIGUE_MODERATE_MULTIPLIER = 0.8
    FATIGUE_HIGH_MULTIPLIER = 0.5
    SCORE_BASE_MULTIPLIER = 3
    SCORE_FATIGUE_MULTIPLIER = 4
    SCORE_NORMAL_MULTIPLIER = 5
    BONUS_MULTIPLIER = 4
    
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
        self.teams = [team_1, team_2]            # зберігаємо їх у об'єкт Match
        print(f"Match: {team_1.team_name} vs {team_2.team_name}")
    
    def _calculate_team_performance(self, team):
        """
        Приватний метод для обчислення продуктивності команди.
        Усуває дублювання коду між командами.

        Parameters:
            team (Team): Команда для аналізу.

        Returns:
            tuple: (strength, avg_fatigue, player_count)
        """
        strength = 0
        fatigue = 0
        player_count = len(team.playing_players)

        for player in team.playing_players:
            coef = player.player_coef
            
            # Застосовуємо множники втоми
            if player.fatigue >= self.FATIGUE_MODERATE_THRESHOLD and player.fatigue <= self.FATIGUE_HIGH_THRESHOLD:
                coef *= self.FATIGUE_MODERATE_MULTIPLIER
            elif player.fatigue > self.FATIGUE_HIGH_THRESHOLD:
                coef *= self.FATIGUE_HIGH_MULTIPLIER
            
            strength += coef
            fatigue += player.fatigue

        strength = int(strength)
        avg_fatigue = fatigue / player_count if player_count > 0 else 0
        
        return strength, avg_fatigue, player_count
    
    def play_match(self):
        """
        Моделює матч між двома командами.

        - Перша команда отримує очки на основі своєї сили (`team_strength()`).
        - Друга команда отримує випадкову кількість очок (0-100).

        Після чого визначається переможець та виводиться результат матчу.

        Returns:
            tuple: score_1, score_2 - рахунок 1 і 2 команди відповідно.
        """
        # Обчислюємо продуктивність обох команд
        team1_strength, team1_avg_fatigue, team1_count = self._calculate_team_performance(self.teams[0])
        team2_strength, team2_avg_fatigue, team2_count = self._calculate_team_performance(self.teams[1])

        # Визначаємо верхні межі для рахунку залежно від втоми
        team1_max = team1_strength * self.SCORE_FATIGUE_MULTIPLIER if team1_avg_fatigue > self.FATIGUE_MODERATE_THRESHOLD else team1_strength * self.SCORE_NORMAL_MULTIPLIER
        team2_max = team2_strength * self.SCORE_FATIGUE_MULTIPLIER if team2_avg_fatigue > self.FATIGUE_MODERATE_THRESHOLD else team2_strength * self.SCORE_NORMAL_MULTIPLIER

        # Генеруємо рахунок для обох команд
        score_1 = random.randint(team1_strength * self.SCORE_BASE_MULTIPLIER, team1_max)
        score_2 = random.randint(team2_strength * self.SCORE_BASE_MULTIPLIER, team2_max)
       
        # Додаємо бонус за різницю сил команд
        diff = abs(team1_strength - team2_strength)
        if diff > 0:
            bonus = random.randint(0, self.BONUS_MULTIPLIER * diff)
            if team1_strength > team2_strength:
                score_2 += bonus
            elif team2_strength > team1_strength:
                score_1 += bonus
        
        return score_1, score_2

            
