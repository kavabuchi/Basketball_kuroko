from player import Player

class Team:
    """
    Представляє баскетбольну команду з бюджетом, списком гравців та можливістю купувати/продавати гравців.

    Атрибути:
        team_name (str): Назва команди.
        budget (int): Доступний бюджет команди.
        players (list): Повний список гравців команди (ростер).
        selected_lineup (list): Список з 5 обраних гравців для матчу.
        team_rate (float): Загальний рейтинг команди (може бути використаний додатково).
    
    Статичні дані:
        team_stats (dict): Заздалегідь задані характеристики деяких команд.
    """

    def __init__(self, team_name, budget):
        """
        Ініціалізує команду з заданою назвою та початковим бюджетом.

        Parameters:
            team_name (str): Назва команди.
            budget (int): Початковий бюджет команди.
        """
        self.team_name = team_name
        self.players = []  # Повний ростер команди
        self.selected_lineup = []  # Обрані гравці для матчу (максимум 5)
        self.budget = budget
        self.team_rate = 0
    
    def team_strength(self):
        """
        Обчислює сумарну ефективність (strength) команди на основі коефіцієнтів обраних гравців для матчу.

        Returns:
            int: Загальна сила команди (на основі обраного складу).
        """
        return int(sum(player.player_coef for player in self.selected_lineup))
    
    def get_team_strength(self):
        """
        Псевдонім для team_strength() для сумісності з існуючим кодом.

        Returns:
            int: Загальна сила команди.
        """
        return self.team_strength()
    

    def add_player(self, player):
        """
        Додає гравця до ростеру команди (без обмеження кількості).

        Parameters:
            player (Player): Об'єкт гравця, якого потрібно додати.

        Returns:
            bool: True, якщо гравця успішно додано, False - якщо недостатньо коштів.
        """
        if self.budget >= player.price:
            self.budget -= player.price
            self.players.append(player)
            return True
        else:
            print("Недостатньо коштів для покупки цього гравця!")
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
            # Також видаляємо з обраного складу, якщо він там є
            if player in self.selected_lineup:
                self.selected_lineup.remove(player)
            return True
        else: 
            print("Цього гравця немає у вашій команді!")
            return False
    
    def select_player_for_lineup(self, player):
        """
        Додає гравця до обраного складу для матчу (максимум 5 гравців).

        Parameters:
            player (Player): Гравець для додавання до складу.

        Returns:
            bool: True, якщо гравця додано, False - якщо склад повний або гравця немає в ростері.
        """
        if player not in self.players:
            print("Цей гравець не належить до вашої команди!")
            return False
        
        if player in self.selected_lineup:
            print("Цей гравець вже в обраному складі!")
            return False
            
        if len(self.selected_lineup) >= 5:
            print("Обраний склад вже повний (5 гравців)!")
            return False
            
        self.selected_lineup.append(player)
        print(f"✅ {player.name} додано до складу для матчу!")
        return True
    
    def remove_player_from_lineup(self, player):
        """
        Видаляє гравця з обраного складу для матчу.

        Parameters:
            player (Player): Гравець для видалення зі складу.

        Returns:
            bool: True, якщо гравця видалено, False - якщо гравця немає в складі.
        """
        if player in self.selected_lineup:
            self.selected_lineup.remove(player)
            print(f"✅ {player.name} видалено зі складу для матчу!")
            return True
        else:
            print("Цього гравця немає в обраному складі!")
            return False
    
    def auto_select_lineup(self):
        """
        Автоматично обирає 5 найкращих гравців для матчу (за коефіцієнтом ефективності).
        
        Returns:
            bool: True, якщо склад сформовано, False - якщо недостатньо гравців.
        """
        if len(self.players) < 5:
            print("Недостатньо гравців для формування складу (потрібно мінімум 5)!")
            return False
        
        # Сортуємо гравців за коефіцієнтом ефективності (від найвищого)
        sorted_players = sorted(self.players, key=lambda x: x.player_coef, reverse=True)
        
        # Обираємо 5 найкращих
        self.selected_lineup = sorted_players[:5]
        
        print("✅ Автоматично обрано 5 найкращих гравців для матчу:")
        for i, player in enumerate(self.selected_lineup, 1):
            print(f"  {i}. {player.name} ({player.position}) - Коеф: {player.player_coef:.1f}")
        
        return True
    
    def clear_lineup(self):
        """
        Очищує обраний склад для матчу.
        """
        self.selected_lineup = []
        print("✅ Склад для матчу очищено!")
    
    def show_lineup_status(self):
        """
        Показує поточний статус обраного складу.
        """
        print(f"\n🏀 Обраний склад для матчу ({len(self.selected_lineup)}/5):")
        if not self.selected_lineup:
            print("  Склад порожній")
        else:
            for i, player in enumerate(self.selected_lineup, 1):
                print(f"  {i}. {player.name} ({player.position}) - Коеф: {player.player_coef:.1f}")
        print(f"💪 Сила обраного складу: {self.team_strength()}")
        

    def __str__(self):
        """
        Повертає строкове представлення команди з інформацією про склад та бюджет у красивому форматі.

        Returns:
            str: Інформація про команду у зручному форматі.
        """
        divider = "=" * 60
        header = f"🏀 Team: {self.team_name} 🏀"
        budget = f"💰 Budget: ${self.budget:,}"
        roster_info = f"👥 Full Roster: {len(self.players)} players"
        lineup_info = f"⭐ Selected Lineup: {len(self.selected_lineup)}/5 players"
        strength = f"💪 Team Strength (Selected): {self.get_team_strength()}"
        
        # Повний ростер
        roster_title = "🏀 Full Roster:"
        roster_list = "\n".join([f"  - {player}" for player in self.players]) if self.players else "  No players in the team."
        
        # Обраний склад
        lineup_title = "\n⭐ Selected Lineup for Match:"
        if self.selected_lineup:
            lineup_list = "\n".join([f"  {i+1}. {player}" for i, player in enumerate(self.selected_lineup)])
        else:
            lineup_list = "  No players selected for match. Use auto-select or manual selection."

        return f"\n{divider}\n{header}\n{divider}\n{budget}\n{roster_info}\n{lineup_info}\n{strength}\n\n{roster_title}\n{roster_list}\n{lineup_title}\n{lineup_list}\n{divider}\n"


if __name__ == "__main__":
    team_1 = Team("Lakers", 100)
    team_2 = Team("Bulls", 90)

    print(team_1)
    print(team_2)
