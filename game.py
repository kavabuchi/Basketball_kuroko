from player import Player
from team import Team
from match import Match

class GameManager:
    """
    Клас для управління станом гри та основними операціями.
    Замінює глобальні змінні та покращує структуру коду.
    """
    
    def __init__(self):
        self.my_team = None
        self.teams = []
        self.available_players = []
        self._initialize_game_data()
    
    def _initialize_game_data(self):
        """Ініціалізує початкові дані гри: команди та доступних гравців."""
        # Створення гравців для команд
        warriors_players, celtics_players, bulls_players, lakers_players = self._create_team_players()
        
        # Створення команд
        self.teams = [
            Team("Warriors", 95000),
            Team("Celtics", 90000),
            Team("Bulls", 92000),
            Team("Lakers", 98000)
        ]
        
        # Додавання гравців до команд
        self._add_players_to_teams(warriors_players, celtics_players, bulls_players, lakers_players)
        
        # Список доступних гравців для покупки
        self.available_players = [
            Player("Kevin Durant", 35, "Small_Forward", 0.1, 0.94, 110000),
            Player("Kyrie Irving", 31, "Point_Guard", 0.12, 0.90, 100000),
            Player("James Harden", 34, "Shooting_Guard", 0.15, 0.88, 95000),
            Player("Giannis Antetokounmpo", 29, "Power_Forward", 0.08, 0.93, 120000),
            Player("Joel Embiid", 29, "Center", 0.2, 0.91, 105000)
        ]
    
    def _create_team_players(self):
        """Створює гравців для всіх команд."""
        warriors_players = [
            Player("Stephen Curry", 35, "Point_Guard", 0.1, 0.95, 120000),
            Player("Klay Thompson", 33, "Shooting_Guard", 0.15, 0.88, 95000),
            Player("Draymond Green", 33, "Power_Forward", 0.2, 0.85, 85000),
            Player("Andrew Wiggins", 28, "Small_Forward", 0.12, 0.82, 80000),
            Player("Kevon Looney", 27, "Center", 0.18, 0.78, 70000)
        ]
        celtics_players = [
            Player("Jayson Tatum", 25, "Small_Forward", 0.08, 0.92, 110000),
            Player("Jaylen Brown", 27, "Shooting_Guard", 0.12, 0.89, 105000),
            Player("Marcus Smart", 29, "Point_Guard", 0.15, 0.84, 85000),
            Player("Al Horford", 37, "Power_Forward", 0.25, 0.80, 75000),
            Player("Robert Williams", 25, "Center", 0.22, 0.82, 78000)
        ]
        bulls_players = [
            Player("Zach LaVine", 28, "Shooting_Guard", 0.1, 0.87, 95000),
            Player("DeMar DeRozan", 34, "Small_Forward", 0.18, 0.85, 90000),
            Player("Lonzo Ball", 25, "Point_Guard", 0.3, 0.79, 75000),
            Player("Patrick Williams", 22, "Power_Forward", 0.15, 0.76, 65000),
            Player("Nikola Vucevic", 32, "Center", 0.2, 0.83, 85000)
        ]
        lakers_players = [
            Player("LeBron James", 39, "Small_Forward", 0.1, 0.95, 100000),
            Player("Anthony Davis", 31, "Power_Forward", 0.15, 0.92, 95000),
            Player("D'Angelo Russell", 28, "Point_Guard", 0.2, 0.85, 75000),
            Player("Austin Reaves", 26, "Shooting_Guard", 0.12, 0.83, 70000),
            Player("Rui Hachimura", 26, "Small_Forward", 0.18, 0.8, 68000)
        ]
        return warriors_players, celtics_players, bulls_players, lakers_players
    
    def _add_players_to_teams(self, warriors_players, celtics_players, bulls_players, lakers_players):
        """Додає гравців до відповідних команд."""
        team_players = [warriors_players, celtics_players, bulls_players, lakers_players]
        for team, players in zip(self.teams, team_players):
            for player in players:
                team.add_player_free(player)

# === Інтерфейсні функції ===

def start_main_menu():
    print("═" * 60)
    print("🏀 WELCOME TO NBA SIMULATION GAME 🏀".center(60))
    print("═" * 60)
    print("What would you like to do?".center(60))
    print("1️⃣  Create a new team")
    print("2️⃣  Select an existing team")
    print("❌  Exit")
    print("═" * 60)

def print_main_menu():
    print("═" * 60)
    print("What would you like to do?".center(60))
    print("1️⃣  Buy new player (up to 5 players)")
    print("2️⃣  Sell player")
    print("3️⃣  Start the match")
    print("4️⃣  Auto-buy full team (up to 5)")
    print("5️⃣  Show stats")
    print("6️⃣  Rest team")
    print("7️⃣  Manage playing players")
    print("❌  Exit")
    print("═" * 60)

def print_goodbye():
    print("\n" + "═" * 60)
    print("🏁 GAME OVER – Thanks for playing! 🏀".center(60))
    print("═" * 60)

def print_separator():
    print("\n" + "─" * 60 + "\n")

# === Функції валідації ===

def validate_player_input(player_name, available_players):
    """
    Валідує введення користувача для пошуку гравця.
    
    Parameters:
        player_name (str): Ім'я гравця, введене користувачем
        available_players (list): Список доступних гравців
        
    Returns:
        tuple: (is_valid, player, error_message)
    """
    if not player_name.strip():
        return False, None, "⚠️ Player name cannot be empty!"
    
    # Пошук гравця за точним співпадінням
    for player in available_players:
        if player_name.lower() == player.name.lower():
            return True, player, ""
    
    # Пошук за частковим співпадінням
    matching_players = [p for p in available_players if player_name.lower() in p.name.lower()]
    if len(matching_players) == 1:
        return True, matching_players[0], ""
    elif len(matching_players) > 1:
        return False, None, f"⚠️ Multiple players found: {', '.join(p.name for p in matching_players)}"
    
    return False, None, "⚠️ Player not found!"

def validate_team_name(team_name):
    """
    Валідує назву команди.
    
    Parameters:
        team_name (str): Назва команди для валідації
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not team_name.strip():
        return False, "⚠️ Team name cannot be empty!"
    
    if len(team_name.strip()) < 2:
        return False, "⚠️ Team name must be at least 2 characters long!"
    
    if len(team_name.strip()) > 30:
        return False, "⚠️ Team name is too long (max 30 characters)!"
    
    return True, ""

def validate_budget(budget_str):
    """
    Валідує бюджет команди.
    
    Parameters:
        budget_str (str): Рядок з бюджетом для валідації
        
    Returns:
        tuple: (is_valid, budget, error_message)
    """
    try:
        budget = int(budget_str)
        if not (100000 <= budget <= 1000000):
            return False, 0, "⚠️ Budget must be between 100000 and 1000000!"
        return True, budget, ""
    except ValueError:
        return False, 0, "⚠️ Budget must be a valid number!"

# === Функції гри ===

def create_team(game_manager):
    print_separator()
    team_name = input("Enter a name for your team: ").strip()
    
    # Валідація назви команди
    is_valid_name, error_message = validate_team_name(team_name)
    if not is_valid_name:
        print(error_message)
        return False
    
    budget_str = input("Enter your team budget (100000 to 1000000): ")
    
    # Валідація бюджету
    is_valid_budget, team_budget, error_message = validate_budget(budget_str)
    if not is_valid_budget:
        print(error_message)
        return False

    game_manager.my_team = Team(team_name, team_budget)
    print(f"✅ Team '{team_name}' created with budget ${team_budget:,}!")
    print(game_manager.my_team)
    return True


def buy_player(game_manager):
    if game_manager.my_team is None:
        print("⚠️ Create a team first!")
        return

    print_separator()
    print("Available Players:")
    for player in game_manager.available_players:
        print(f"{player}")

    buy_player_name = input("\nEnter player name to buy: ").strip()
    
    # Використання функції валідації
    is_valid, player, error_message = validate_player_input(buy_player_name, game_manager.available_players)
    
    if not is_valid:
        print(error_message)
        return
    
    if game_manager.my_team.budget >= player.price:
        if game_manager.my_team.can_add_to_playing():
            game_manager.my_team.add_player(player)
            game_manager.available_players.remove(player)
            print(f"✅ You bought {player.name}. New budget: ${game_manager.my_team.budget:,}")
        else:
            print("⚠️ You already have 5 players.")
    else:
        print("⚠️ Not enough budget.")


def sell_player(game_manager):
    if game_manager.my_team is None:
        print("⚠️ Create a team first!")
        return

    print_separator()
    if not game_manager.my_team.playing_players:
        print("⚠️ You have no players to sell.")
        return

    print("Your Team Players:")
    for player in game_manager.my_team.playing_players:
        print(f"{player}")

    sell_name = input("\nEnter player name to sell: ").strip()
    
    # Використання функції валідації
    is_valid, player, error_message = validate_player_input(sell_name, game_manager.my_team.playing_players)
    
    if not is_valid:
        print(error_message)
        return
    
    if game_manager.my_team.sell_player(player):
        game_manager.available_players.append(player)
        print(f"✅ You sold {player.name}. New budget: ${game_manager.my_team.budget:,}")


def select_opponent(game_manager):
    """Вибір команди-суперника для матчу."""
    print_separator()
    print("═" * 60)
    print("🏀 START MATCH 🏀".center(60))
    print("═" * 60)
    print("Available Opponent Teams:")
    for team in game_manager.teams:
        if team != game_manager.my_team:
            print(f"- {team.team_name} (Players: {len(team.playing_players)}, Strength: {team.team_strength()})")
    print("═" * 60)

    opponent_name = input("Enter name of the opponent team: ").strip()
    opponent = None
    for team in game_manager.teams:
        if team.team_name == opponent_name and team != game_manager.my_team:
            opponent = team
            break

    if opponent is None:
        print("⚠️ No valid opponent team found!")
        return None

    if not opponent.playing_players:
        print(f"⚠️ Opponent team {opponent.team_name} has no players!")
        return None
    
    return opponent


def check_team_status(game_manager):
    """Перевіряє статус команди гравця перед матчем."""
    active_players = [player for player in game_manager.my_team.playing_players if player.fatigue < 1.0]
    tired_players = [player for player in game_manager.my_team.playing_players if player.fatigue >= 1.0]

    if not active_players:
        print("⚠️ All your players are too tired to play! Please rest them.")
        return None, None

    pre_match_strength = game_manager.my_team.team_strength()
    
    print("\n👥 Your Team Status (Before Match):")
    print(f"Team: {game_manager.my_team.team_name}, Strength: {pre_match_strength}")
    print("Active Players:")
    for player in active_players:
        print(f"  • {player.name} (Fatigue: {player.fatigue:.2f}, Coef: {player.player_coef:.1f})")
    if tired_players:
        print("Tired Players (Will Not Play):")
        for player in tired_players:
            print(f"  ⚠️ {player.name} is too tired to play! (Fatigue: {player.fatigue:.2f})")
    
    return active_players, pre_match_strength


def play_match_logic(game_manager, opponent, active_players, pre_match_strength):
    """Логіка проведення матчу."""
    print(f"\nOpponent: {opponent.team_name}, Strength: {opponent.team_strength()}")

    # Тимчасово змінюємо гравців команди на активних для матчу
    original_players = game_manager.my_team.playing_players[:]
    game_manager.my_team.all_players = active_players

    match = Match(game_manager.my_team, opponent)
    my_score, opp_score = match.play_match()

    # Відновлюємо оригінальний склад
    game_manager.my_team.all_players = original_players

    print("\n═" * 60)
    print(f"🏀 MATCH RESULT: {game_manager.my_team.team_name} vs {opponent.team_name} 🏀".center(60))
    print("═" * 60)
    if my_score is None or opp_score is None:
        print("⚠️ Match could not be completed.")
        return

    if my_score > opp_score:
        game_manager.my_team.budget += 100000
        print(f"✅ {game_manager.my_team.team_name} won! {my_score} - {opp_score}")
        print(f"💰 New budget: ${game_manager.my_team.budget:,}")
    elif my_score == opp_score:
        print(f"🤝 It's a draw! {my_score} - {opp_score}")
    else:
        game_manager.my_team.budget -= 50000
        print(f"❌ {opponent.team_name} won! {opp_score} - {my_score}")
        print(f"💰 New budget: ${game_manager.my_team.budget:,}")

    # Збільшення втоми для активних гравців
    for player in active_players:
        player.increase_fatigue()

    # Сила команди після матчу
    post_match_strength = game_manager.my_team.team_strength()

    print("\n👥 Team Status After Match:")
    print(f"Team: {game_manager.my_team.team_name}, Strength: {post_match_strength}")
    for player in game_manager.my_team.playing_players:
        status = "⚠️ Too tired!" if player.fatigue >= 1.0 else "Ready"
        print(f"  • {player.name} (Fatigue: {player.fatigue:.2f}, Coef: {player.player_coef:.1f}, Status: {status})")
    if pre_match_strength != post_match_strength:
        print(f"⚠️ Team strength changed from {pre_match_strength} to {post_match_strength} due to fatigue.")
    print("═" * 60)


def opponent_team(game_manager):
    """Основна функція для проведення матчу (рефакторена)."""
    if game_manager.my_team is None:
        print("⚠️ Create a team first!")
        return

    if not game_manager.my_team.playing_players:
        print("⚠️ Your team has no players! Buy at least one player to start a match.")
        return

    # Вибір суперника
    opponent = select_opponent(game_manager)
    if opponent is None:
        return

    # Перевірка статусу команди
    active_players, pre_match_strength = check_team_status(game_manager)
    if active_players is None:
        return

    # Проведення матчу
    play_match_logic(game_manager, opponent, active_players, pre_match_strength)


def buy_players(game_manager):
    if game_manager.my_team is None:
        print("⚠️ Create a team first!")
        return

    print_separator()
    print("═" * 60)
    print("🏀 AUTO-BUY PLAYERS 🏀".center(60))
    print("═" * 60)
    print("║ {:<4} │ {:<25} │ {:<15} │ {:<5} │ {:<10} │ {:<12} ║".format(
        "#", "Name", "Position", "Age", "Skill Coef", "Price"
    ))
    print("╠════╤═══════════════════════════╤═════════════════╤═══════╤════════════╤══════════════╣")
    for idx, player in enumerate(game_manager.available_players):
        print("║ {:<4} │ {:<25} │ {:<15} │ {:<5} │ {:<10.1f} │ {:<12,} ║".format(
            idx + 1, player.name, player.position, player.age, player.player_coef, player.price
        ))
    print("╩════╧═══════════════════════════╧═════════════════╧═══════╧════════════╧══════════════╩")

    print(f"\n👥 Your Team: {game_manager.my_team.team_name}")
    print(f"💰 Budget: ${game_manager.my_team.budget:,}")
    print(f"🏀 Players: {len(game_manager.my_team.all_players)}/5")
    print(f"💪 Team Strength: {game_manager.my_team.team_strength()}")
    print("─" * 60)
    buy_players_choice = input("Do you want to auto-buy up to all players? (yes/no): ").lower()
    
    if buy_players_choice == "yes":
        to_remove = []
        bought_players = []
        
        # Сортуємо гравців за коефіцієнтом (від найвищого до найнижчого)
        sorted_players = sorted(game_manager.available_players, key=lambda x: x.player_coef, reverse=True)
        
        for player in sorted_players:
            if game_manager.my_team.budget >= player.price and len(game_manager.my_team.all_players) < 5:
                game_manager.my_team.add_player(player)
                to_remove.append(player)
                bought_players.append(player)
                print(f"✅ Bought {player.name} ({player.position}) for ${player.price:,}. Budget left: ${game_manager.my_team.budget:,}")
        
        for player in to_remove:
            game_manager.available_players.remove(player)
        
        if bought_players:
            print("\n═" * 60)
            print("🏀 PURCHASE SUMMARY 🏀".center(60))
            print("═" * 60)
            print("║ {:<25} │ {:<15} │ {:<10} │ {:<12} ║".format(
                "Name", "Position", "Skill Coef", "Price"
            ))
            print("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╣")
            for player in bought_players:
                print("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12,} ║".format(
                    player.name, player.position, player.player_coef, player.price
                ))
            print("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╩")
            print(f"✅ Total players bought: {len(bought_players)}")
            print(f"💰 New budget: ${game_manager.my_team.budget:,}")
            print(f"💪 New team strength: {game_manager.my_team.team_strength()}")
            print("═" * 60)
        else:
            print("⚠️ No players bought. Insufficient budget or no suitable players.")
    elif buy_players_choice == "no":
        print("No players bought.")
    else:
        print("⚠️ Invalid input. Please enter 'yes' or 'no'.")


def select_existing_team(game_manager):
    print_separator()
    print("═" * 60)
    print("Existing Teams:".center(60))
    print("═" * 60)
    for idx, team in enumerate(game_manager.teams):
        print(f"{idx+1}. {team.team_name} - Budget: ${team.budget:,}, Players: {len(team.playing_players)}")
        for player in team.playing_players:
            print(f"   • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
    print("═" * 60)

    while True:
        try:
            team_idx = int(input(f"\nChoose a team to play with (1-{len(game_manager.teams)}): "))
            if 1 <= team_idx <= len(game_manager.teams):
                selected_team = game_manager.teams[team_idx - 1]  # Не видаляємо команду зі списку
                print(f"\n✅ You selected team {selected_team.team_name}!")
                print(f"💰 Budget: ${selected_team.budget:,}")
                print(f"👥 Players: {len(selected_team.playing_players)}")
                print(f"💪 Team Strength: {selected_team.team_strength()}")
                print("🏃 Team roster:")
                for player in selected_team.playing_players:
                    print(f"   • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
                return selected_team
            else:
                print("❌ Invalid team number!")
        except ValueError:
            print("❌ Please enter a valid number!")


def show_stats(game_manager):
    print_separator()
    print("═" * 60)
    print("Team Statistics:".center(60))
    print("═" * 60)
    print(f"💰 Budget: ${game_manager.my_team.budget:,}")
    print(f"👥 Players: {len(game_manager.my_team.all_players)}")
    print(f"💪 Team Strength: {game_manager.my_team.team_strength()}")
    print("║ {:<25} │ {:<15} │ {:<10} │ {:<12} │ {:<10} ║".format(
        "Name", "Position", "Coef", "Fatigue", "Price"
    ))
    print("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╤════════════╣")
    for player in game_manager.my_team.all_players:
        status = "⚠️ High" if player.fatigue >= 0.8 else "OK"
        print("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12.2f} │ {:<10,} ║".format(
            player.name, player.position, player.player_coef, player.fatigue, player.price
        ))
    print("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╧════════════╩")
    print("═" * 60)


def rest_team(game_manager):
    """
    Дозволяє команді відпочити, зменшуючи втому всіх гравців і виводячи оновлений статус команди.

    Parameters:
        game_manager (GameManager): Менеджер гри з командою гравця.

    Returns:
        None
    """

    # Сила команди до відпочинку
    pre_rest_strength = game_manager.my_team.team_strength()

    # Зменшення втоми для всіх гравців
    for player in game_manager.my_team.all_players:
        player.decrease_fatigue()

    # Сила команди після відпочинку
    post_rest_strength = game_manager.my_team.team_strength()

    # Виведення статусу
    print("\n" + "═" * 60)
    print("🏀 TEAM REST 🏀".center(60))
    print("═" * 60)
    print(f"👥 Team: {game_manager.my_team.team_name}")
    print(f"💪 Team Strength Before Rest: {pre_rest_strength}")
    print(f"💪 Team Strength After Rest: {post_rest_strength}")
    if pre_rest_strength != post_rest_strength:
        print(f"✅ Team strength increased from {pre_rest_strength} to {post_rest_strength} due to rest!")
    print("\nPlayers Status After Rest:")
    print("║ {:<25} │ {:<15} │ {:<10} │ {:<12} │ {:<10} ║".format(
        "Name", "Position", "Coef", "Fatigue", "Price"
    ))
    print("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╤════════════╣")
    for player in game_manager.my_team.all_players:
        status = "⚠️ High" if player.fatigue >= 0.8 else "OK"
        print("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12.2f} │ {:<10,} ║".format(
            player.name, player.position, player.player_coef, player.fatigue, player.price
        ))
    print("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╧════════════╩")
    print(f"✅ {game_manager.my_team.team_name} is ready to play!")
    print("═" * 60)


def managing_playing_players():
    print("1️⃣  Choose the player for match")
    print("2️⃣  Choose the player for rest")
    while True:
        choice = input("Enter your choice: 1 or 2: ")
        if choice == "1":
            # Вибір гравця для гри
            pass
        if choice == "2":
            # Вибір гравця для відпочинку
            pass

# === Головний цикл ===

def main():
    """Головна функція гри."""
    game_manager = GameManager()
    
    start_main_menu()
    while True:
        choice = input("\nChoose an option (1, 2, or Exit): ").lower()
        if choice == "exit":
            print_goodbye()
            break
        elif choice == "1":
            if create_team(game_manager):
                break  # Перейти до основного меню після створення команди
        elif choice == "2":
            if not game_manager.teams:
                print("⚠️ No existing teams available!")
            else:
                game_manager.my_team = select_existing_team(game_manager)
                break
        else:
            print("⚠️ Invalid choice. Please enter 1, 2, or Exit.")

    if game_manager.my_team is not None:
        print_main_menu()
        while True:
            command = input("\nEnter command (1-7 or Exit): ").strip().lower()
            if command == "exit":
                print_goodbye()
                break
            elif command == "1":
                buy_player(game_manager)
            elif command == "2":
                sell_player(game_manager)
            elif command == "3":
                opponent_team(game_manager)
            elif command == "4":
                buy_players(game_manager)
            elif command == "5":
                show_stats(game_manager)
            elif command == "6":
                rest_team(game_manager)
            elif command == "7":
                managing_playing_players()
            else:
                print("⚠️ Invalid command. Please try again.")

if __name__ == "__main__":
    main()