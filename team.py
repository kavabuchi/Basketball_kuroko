from player import Player

class Team:
    """
    Представляє баскетбольну команду з бюджетом, списком гравців та можливістю купувати/продавати гравців.

    Атрибути:
        team_name (str): Назва команди.
        budget (int): Доступний бюджет команди.
        players (list): Список гравців команди.
        team_rate (float): Загальний рейтинг команди (може бути використаний додатково).
    
    Статичні дані:
        team_stats (dict): Заздалегідь задані характеристики деяких команд.
    """
    
    team_stats = {
        "Bulls": 20,
        "Celtics": 15,
        "Warriors": 12
    }

    def __init__(self, team_name, budget):
        """
        Ініціалізує команду з заданою назвою та початковим бюджетом.

        Parameters:
            team_name (str): Назва команди.
            budget (int): Початковий бюджет команди.
        """
        self.team_name = team_name
        self.players = []
        self.budget = budget
        self.team_rate = 0
    
    def team_strength(self):
        """
        Обчислює сумарну ефективність (strength) команди на основі коефіцієнтів гравців.

        Returns:
            float: Загальна сила команди.
        """
        return int(sum(player.player_coef for player in self.players))
    
    def add_player(self, player):
        """
        Додає гравця до складу команди.

        Parameters:
            player (Player): Об’єкт гравця, якого потрібно додати.

        Returns:
            None
        """
        if self.budget >= player.price:
            self.budget -= player.price
            self.players.append(player)
            return True
        else:
            print("Your fucking ass have no money for that player")
            return False
    def add_player_free(self, player):
        """
        Додає гравця до складу команди без списання бюджету.

        Parameters:
            player (Player): Об’єкт гравця, якого потрібно додати.

        Returns:
            bool: True, якщо гравця додано.
        """
        self.players.append(player)
        return True
    
    
    def sell_player(self, player):
        """
        Продає гравця з команди, повертаючи половину вартості в бюджет.

        Parameters:
            player (Player): Об'єкт гравця для продажу.

        Returns:
            bool: True, якщо гравця успішно продано, False – якщо гравця немає в команді.
        """
        if player in self.players:
            self.budget += player.price // 2
            self.players.remove(player)
            return True
        else: 
            print("You have not this player in your team, stupid bastard")
            return False
        
    def get_team_strength(self):
        """
        Повертає загальну силу команди з урахуванням статистики.
        
        Returns:
            int: Загальна сила команди.
        """
        return self.team_stats.get(self.team_name, self.team_strength())

    def __str__(self):
        """
        Повертає строкове представлення команди з інформацією про склад та бюджет у красивому форматі.

        Returns:
            str: Інформація про команду у зручному форматі.
        """
        divider = "=" * 50
        header = f"🏀 Team: {self.team_name} 🏀"
        budget = f"💰 Budget: ${self.budget:,}"
        strength = f"💪 Team Strength: {self.get_team_strength()}"
        players_title = "🏀 Players:"
        players_list = "\n".join([f"  - {player}" for player in self.players]) if self.players else "  No players in the team."

        return f"\n{divider}\n{header}\n{divider}\n{budget}\n{strength}\n\n{players_title}\n{players_list}\n{divider}\n"


if __name__ == "__main__":
    team_1 = Team("Lakers", 100)
    team_2 = Team("Bulls", 90)

    print(team_1)
    print(team_2)
