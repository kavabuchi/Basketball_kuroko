from player import Player

class Team:
    """
    Представляє баскетбольну команду з бюджетом, списком гравців та можливістю купувати/продавати гравців.

    Атрибути:
        team_name (str): Назва команди.
        budget (int): Доступний бюджет команди.
        all_players (list): Список усіх гравців команди.
        playing_players (list): Список гравців, які беруть участь у матчі.
        team_rate (float): Загальний рейтинг команди (може бути використаний додатково).
    
    Статичні дані:
        team_stats (dict): Заздалегідь задані характеристики деяких команд.
    """
    
    # Константи класу
    MAX_PLAYING_PLAYERS = 5
    SELL_PRICE_RATIO = 0.5  # Команда отримує половину вартості при продажу гравця
    
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
        self.all_players = []  # Усі гравці команди
        self.playing_players = []  # Гравці, які беруть участь у матчі
        self.budget = budget
        self.team_rate = 0
    
    def team_strength(self):
        """
        Обчислює сумарну ефективність (strength) команди на основі коефіцієнтів гравців.

        Returns:
            int: Загальна сила команди.
        """
        return int(sum(player.player_coef for player in self.playing_players))
    
    def add_player(self, player):
        """
        Додає гравця до складу команди.

        Parameters:
            player (Player): Об'єкт гравця, якого потрібно додати.

        Returns:
            bool: True, якщо гравця додано, False – якщо недостатньо бюджету.
        """
        if self.budget >= player.price:
            self.budget -= player.price
            self.all_players.append(player)
            # Автоматично додаємо до playing_players, якщо є місце
            if len(self.playing_players) < self.MAX_PLAYING_PLAYERS:
                self.playing_players.append(player)
            return True
        else:
            print("Your budget is insufficient for this player!")
            return False
    
    def add_player_free(self, player):
        """
        Додає гравця до складу команди без списання бюджету.

        Parameters:
            player (Player): Об'єкт гравця, якого потрібно додати.

        Returns:
            bool: True, якщо гравця додано.
        """
        self.all_players.append(player)
        # Автоматично додаємо до playing_players, якщо є місце
        if len(self.playing_players) < self.MAX_PLAYING_PLAYERS:
            self.playing_players.append(player)
        return True
    
    def sell_player(self, player):
        """
        Продає гравця з команди, повертаючи половину вартості в бюджет.

        Parameters:
            player (Player): Об'єкт гравця для продажу.

        Returns:
            bool: True, якщо гравця успішно продано, False – якщо гравця немає в команді.
        """
        if player in self.all_players:
            self.budget += int(player.price * self.SELL_PRICE_RATIO)
            self.all_players.remove(player)
            if player in self.playing_players:
                self.playing_players.remove(player)
            return True
        else:
            print("You have not this player in your team!")
            return False
    
    def select_player_for_playing(self, player):
        """
        Додає гравця до списку граючих гравців.

        Parameters:
            player (Player): Об'єкт гравця, якого потрібно додати до гри.

        Returns:
            bool: True, якщо гравця додано, False – якщо гравця немає в команді або ліміт досягнуто.
        """
        if player not in self.all_players:
            print("You have not this player in your team!")
            return False
        if len(self.playing_players) >= self.MAX_PLAYING_PLAYERS:
            print("You have already 5 players in your team!")
            return False
        if player in self.playing_players:
            print("This player is already in the team!")
            return False
        
        self.playing_players.append(player)
        print("Player selected for playing")
        return True
    
    def remove_player_from_playing(self, player):
        """
        Видаляє гравця зі списку граючих гравців.

        Parameters:
            player (Player): Об'єкт гравця, якого потрібно прибрати з гри.

        Returns:
            bool: True, якщо гравця видалено, False – якщо гравця немає в playing_players.
        """
        if player in self.playing_players:
            self.playing_players.remove(player)
            print(f"{player.name} is now resting.")
            return True
        else:
            print("You have not this player in your playing team!")
            return False
    
    def can_add_to_playing(self):
        """
        Перевіряє, чи можна додати гравця до граючого складу.
        
        Returns:
            bool: True, якщо є місце для гравця.
        """
        return len(self.playing_players) < self.MAX_PLAYING_PLAYERS
    
    def get_available_players_for_rest(self):
        """
        Повертає список гравців, які можуть відпочивати.
        
        Returns:
            list: Список гравців, які не грають зараз.
        """
        return [player for player in self.all_players if player not in self.playing_players]
    
    def __str__(self):
        """
        Повертає строкове представлення команди з інформацією про склад та бюджет у красивому форматі.

        Returns:
            str: Інформація про команду у зручному форматі.
        """
        divider = "═" * 60
        header = f"🏀 Team: {self.team_name} 🏀".center(60)
        budget = f"💰 Budget: ${self.budget:,}"
        strength = f"💪 Team Strength: {self.team_strength()}"
        players_title = "🏀 Players:"
        
        # Формуємо таблицю гравців
        players_output = ["║ {:<25} │ {:<15} │ {:<10} │ {:<12} │ {:<10} │ {:<10} ║".format(
            "Name", "Position", "Coef", "Fatigue", "Price", "Status"
        )]
        players_output.append("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╤════════════╤════════════╣")
        
        if not self.all_players:
            players_output.append("║ {:<68} │ {:<10} ║".format("No players in the team.", ""))
        else:
            for player in self.all_players:
                status = "Playing" if player in self.playing_players else "Resting"
                players_output.append("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12.2f} │ {:<10,} │ {:<10} ║".format(
                    player.name, player.position, player.player_coef, player.fatigue, player.price, status
                ))
        
        players_output.append("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╧════════════╧════════════╩")
        
        return f"\n{divider}\n{header}\n{divider}\n{budget}\n{strength}\n\n{players_title}\n" + "\n".join(players_output) + f"\n{divider}\n"

if __name__ == "__main__":
    team_1 = Team("Lakers", 100)
    team_2 = Team("Bulls", 90)
    print(team_1)
    print(team_2)