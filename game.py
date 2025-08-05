from player import Player
from team import Team
from match import Match

# === Інтерфейсні функції ===

def print_main_menu():
    print("=" * 50)
    print("🏀 WELCOME TO NBA SIMULATION GAME 🏀".center(50))
    print("=" * 50)
    print("What would you like to do?")
    print("-" * 50)
    print("1️⃣  Buy new player (up to 5 players)")
    print("2️⃣  Sell player")
    print("3️⃣  Start the match")
    print("4️⃣  Buy full team (auto-buy up to 5)")
    print("❌  Exit")
    print("-" * 50)

def print_goodbye():
    print("\n" + "=" * 50)
    print("🏁 GAME OVER – Thanks for playing! 🏀".center(50))
    print("=" * 50)

def print_separator():
    print("\n" + "-" * 50 + "\n")

# === Створення гравців для команд ===

def create_team_players():
    """Створює гравців для різних команд"""
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
    
    return warriors_players, celtics_players, bulls_players

# === Ініціалізація ===

# Створюємо команди з гравцями
warriors_players, celtics_players, bulls_players = create_team_players()

teams = [ 
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000)
]

# Додаємо гравців до команд
for player in warriors_players:
    teams[0].add_player_free(player)

for player in celtics_players:
    teams[1].add_player_free(player)

for player in bulls_players:
    teams[2].add_player_free(player)

# Список вільних гравців для покупки
players = [
    Player("LeBron James", 39, "Small_Forward", 0.1, 0.95, 100000),
    Player("Anthony Davis", 31, "Power_Forward", 0.15, 0.92, 95000),
    Player("D'Angelo Russell", 28, "Point_Guard", 0.2, 0.85, 75000),
    Player("Austin Reaves", 26, "Shooting_Guard", 0.12, 0.83, 70000),
    Player("Rui Hachimura", 26, "Small_Forward", 0.18, 0.8, 68000),
    Player("Jarred Vanderbilt", 25, "Power_Forward", 0.2, 0.78, 65000),
    Player("Jaxson Hayes", 24, "Center", 0.22, 0.76, 60000)
]

# === Вибір або створення команди ===
print("=" * 50)
print("🏀 NBA SIMULATION: Team Selection 🏀".center(50))
print("=" * 50)
print("1️⃣  Створити нову команду")
print("2️⃣  Викупити існуючу команду")
print("-" * 50)

while True:
    team_choice = input("Виберіть опцію (1 або 2): ").strip()
    if team_choice == "1":
        # Створення нової команди
        team_name = input("Введіть назву вашої нової команди: ").strip()
        while True:
            try:
                budget = int(input("Введіть стартовий бюджет (наприклад, 100000): ").strip())
                break
            except ValueError:
                print("Введіть ціле число для бюджету!")
        my_team = Team(team_name, budget)
        print(f"✅ Ви створили команду {team_name} з бюджетом {budget} і без гравців.")
        break
    elif team_choice == "2":
        # Викуп існуючої команди
        print("\n🏀 Доступні команди для викупу:")
        print("=" * 50)
        for idx, team in enumerate(teams):
            print(f"\n{idx+1}. {team.team_name}")
            print(f"   💰 Бюджет: {team.budget}")
            print(f"   👥 Гравців: {len(team.players)}")
            print("   🏃 Склад:")
            for player in team.players:
                print(f"      • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
            print("-" * 30)
        
        while True:
            try:
                select = int(input("\nВведіть номер команди для викупу: ").strip())
                if 1 <= select <= len(teams):
                    my_team = teams.pop(select-1)
                    print(f"\n✅ Ви викупили команду {my_team.team_name}!")
                    print(f"💰 Бюджет: {my_team.budget}")
                    print(f"👥 Гравців: {len(my_team.players)}")
                    print("🏃 Ваш склад:")
                    for player in my_team.players:
                        print(f"   • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
                    break
                else:
                    print("❌ Невірний номер команди!")
            except ValueError:
                print("❌ Введіть ціле число!")
        break
    else:
        print("❌ Введіть 1 або 2!")

# === Функції гри ===

def buy_player(my_team, players):
    print_separator()
    print("Available Players:")
    for player in players:
        print(f"{player}")

    buy_player = input("\nEnter player name to buy: ") 
    for player in players:
        if buy_player == player.name:
            if my_team.budget >= player.price:
                if len(my_team.players) < 5:
                    my_team.add_player(player)
                    players.remove(player)
                    print(f"You bought {player.name}. New budget: {my_team.budget}")
                else:
                    print("You already have 5 players.")
            else:
                print("Not enough budget.")
            break
    else:
        print("Player not found.")

def sell_player(my_team, players):
    print_separator()
    if not my_team.players:
        print("You have no players to sell.")
        return

    print("Your Team Players:")
    for player in my_team.players:
        print(f"{player}")

    sell_name = input("\nEnter player name to sell: ")
    for player_in_team in my_team.players:
        if sell_name == player_in_team.name:
            my_team.sell_player(player_in_team)
            players.append(player_in_team)
            print(f"You sold {player_in_team.name}. New budget: {my_team.budget}")
            break
    else:
        print("Player not found.")

def opponent_team(my_team, teams):
    print_separator()
    print("Available Opponent Teams:")
    for team in teams:
        if team != my_team:
            print(f"- {team.team_name}")
    
    opponent_name = input("Enter name of the opponent team: ")
    opponent = None
    for team in teams:
        if team.team_name == opponent_name and team != my_team:
            opponent = team
            break

    if opponent is None:
        print("⚠️ No valid opponent team found!")
        return

    match = Match(my_team, opponent)
    my_score, opp_score = match.play_match()

    if my_score > opp_score:
        my_team.budget += 100000
        print(f"{my_team.team_name} won! {my_score} - {opp_score}. New budget: {my_team.budget}")
    elif my_score == opp_score:
        print(f"🤝 It's a draw! {my_score} - {opp_score}.")
    else:
        my_team.budget -= 50000
        print(f"{opponent.team_name} won! {opp_score} - {my_score}. New budget: {my_team.budget}")

def buy_players(my_team, players):
    print_separator()
    print("Available Players:")
    for player in players:
        print(f"{player}")

    buy_players = input("\nDo you want to auto-buy up to 5 players? (yes/no): ").lower()
    if buy_players == "yes":
        to_remove = []
        for player in players:
            if my_team.budget >= player.price:
                if len(my_team.players) < 5:
                    my_team.add_player(player)
                    to_remove.append(player)
                    print(f"✅ You bought {player.name}. Budget left: {my_team.budget}")
        for player in to_remove:
            players.remove(player)

    elif buy_players == "no":
        print("No players bought.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

# === Головний цикл ===

print_main_menu()

while True:
    command = input("\nEnter command (1-4 or Exit): ").strip()

    if command.lower() == "exit":
        print_goodbye()
        break

    elif command == "1":
        buy_player(my_team, players)

    elif command == "2":
        sell_player(my_team, players)

    elif command == "3":
        opponent_team(my_team, teams)

    elif command == "4":
        buy_players(my_team, players)

    else:
        print("⚠️ Invalid command. Please try again.")
