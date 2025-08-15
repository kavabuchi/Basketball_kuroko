from player import Player
from team import Team
from match import Match

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
    print("❌  Exit")
    print("═" * 60)

def print_goodbye():
    print("\n" + "═" * 60)
    print("🏁 GAME OVER – Thanks for playing! 🏀".center(60))
    print("═" * 60)

def print_separator():
    print("\n" + "─" * 60 + "\n")

# === Створення гравців для команд ===

def create_team_players():
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

# === Ініціалізація ===

my_team = None  # Ініціалізація my_team

warriors_players, celtics_players, bulls_players, lakers_players = create_team_players()

teams = [ 
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000),
    Team("Lakers", 98000)
]

for player in warriors_players:
    teams[0].add_player_free(player)

for player in celtics_players:
    teams[1].add_player_free(player)

for player in bulls_players:
    teams[2].add_player_free(player)

for player in lakers_players:
    teams[3].add_player_free(player)

# Список доступних гравців для покупки (без дублювання)
players = [
    Player("Kevin Durant", 35, "Small_Forward", 0.1, 0.94, 110000),
    Player("Kyrie Irving", 31, "Point_Guard", 0.12, 0.90, 100000),
    Player("James Harden", 34, "Shooting_Guard", 0.15, 0.88, 95000),
    Player("Giannis Antetokounmpo", 29, "Power_Forward", 0.08, 0.93, 120000),
    Player("Joel Embiid", 29, "Center", 0.2, 0.91, 105000)
]

# === Функції гри ===

def create_team():
    global my_team
    print_separator()
    team_name = input("Enter a name for your team: ").strip()
    if not team_name:
        print("⚠️ Team name cannot be empty!")
        return False
    try:
        team_budget = int(input("Enter your team budget (100000 to 1000000): "))
        if not (100000 <= team_budget <= 1000000):
            print("⚠️ Budget must be between 100000 and 1000000!")
            return False
    except ValueError:
        print("⚠️ Budget must be a valid number!")
        return False

    my_team = Team(team_name, team_budget)
    print(f"✅ Team '{team_name}' created with budget ${team_budget:,}!")
    print(my_team)
    return True

def buy_player(my_team, players):
    if my_team is None:
        print("⚠️ Create a team first!")
        return

    print_separator()
    print("Available Players:")
    for player in players:
        print(f"{player}")

    buy_player = input("\nEnter player name to buy: ").strip()
    for player in players:
        if buy_player == player.name:
            if my_team.budget >= player.price:
                if len(my_team.players) < 5:
                    my_team.add_player(player)
                    players.remove(player)
                    print(f"✅ You bought {player.name}. New budget: ${my_team.budget:,}")
                else:
                    print("⚠️ You already have 5 players.")
            else:
                print("⚠️ Not enough budget.")
            break
    else:
        print("⚠️ Player not found.")

def sell_player(my_team, players):
    if my_team is None:
        print("⚠️ Create a team first!")
        return

    print_separator()
    if not my_team.players:
        print("⚠️ You have no players to sell.")
        return

    print("Your Team Players:")
    for player in my_team.players:
        print(f"{player}")

    sell_name = input("\nEnter player name to sell: ").strip()
    for player_in_team in my_team.players:
        if sell_name == player_in_team.name:
            my_team.sell_player(player_in_team)
            players.append(player_in_team)
            print(f"✅ You sold {player_in_team.name}. New budget: ${my_team.budget:,}")
            break
    else:
        print("⚠️ Player not found.")

def opponent_team(my_team, teams):
    if my_team is None:
        print("⚠️ Create a team first!")
        return

    if not my_team.players:
        print("⚠️ Your team has no players! Buy at least one player to start a match.")
        return

    print_separator()
    print("═" * 60)
    print("🏀 START MATCH 🏀".center(60))
    print("═" * 60)
    print("Available Opponent Teams:")
    for team in teams:
        if team != my_team:
            print(f"- {team.team_name} (Players: {len(team.players)}, Strength: {team.team_strength()})")
    print("═" * 60)

    opponent_name = input("Enter name of the opponent team: ").strip()
    opponent = None
    for team in teams:
        if team.team_name == opponent_name and team != my_team:
            opponent = team
            break

    if opponent is None:
        print("⚠️ No valid opponent team found!")
        return

    if not opponent.players:
        print(f"⚠️ Opponent team {opponent.team_name} has no players!")
        return

    # Перевірка втоми гравців вашої команди
    active_players = [player for player in my_team.players if player.fatigue < 1.0]
    tired_players = [player for player in my_team.players if player.fatigue >= 1.0]

    if not active_players:
        print("⚠️ All your players are too tired to play! Please rest them.")
        return

    # Сила команди до матчу
    pre_match_strength = my_team.team_strength()

    print("\n👥 Your Team Status (Before Match):")
    print(f"Team: {my_team.team_name}, Strength: {pre_match_strength}")
    print("Active Players:")
    for player in active_players:
        print(f"  • {player.name} (Fatigue: {player.fatigue:.2f}, Coef: {player.player_coef:.1f})")
    if tired_players:
        print("Tired Players (Will Not Play):")
        for player in tired_players:
            print(f"  ⚠️ {player.name} is too tired to play! (Fatigue: {player.fatigue:.2f})")
    print(f"\nOpponent: {opponent.team_name}, Strength: {opponent.team_strength()}")

    # Тимчасово змінюємо гравців команди на активних для матчу
    original_players = my_team.players[:]
    my_team.players = active_players

    match = Match(my_team, opponent)
    my_score, opp_score = match.play_match()

    # Відновлюємо оригінальний склад
    my_team.players = original_players

    print("\n═" * 60)
    print(f"🏀 MATCH RESULT: {my_team.team_name} vs {opponent.team_name} 🏀".center(60))
    print("═" * 60)
    if my_score is None or opp_score is None:
        print("⚠️ Match could not be completed.")
        return

    if my_score > opp_score:
        my_team.budget += 100000
        print(f"✅ {my_team.team_name} won! {my_score} - {opp_score}")
        print(f"💰 New budget: ${my_team.budget:,}")
    elif my_score == opp_score:
        print(f"🤝 It's a draw! {my_score} - {opp_score}")
    else:
        my_team.budget -= 50000
        print(f"❌ {opponent.team_name} won! {opp_score} - {my_score}")
        print(f"💰 New budget: ${my_team.budget:,}")

    # Збільшення втоми для активних гравців
    for player in active_players:
        player.increase_fatigue()

    # Сила команди після матчу
    post_match_strength = my_team.team_strength()

    print("\n👥 Team Status After Match:")
    print(f"Team: {my_team.team_name}, Strength: {post_match_strength}")
    for player in my_team.players:
        status = "⚠️ Too tired!" if player.fatigue >= 1.0 else "Ready"
        print(f"  • {player.name} (Fatigue: {player.fatigue:.2f}, Coef: {player.player_coef:.1f}, Status: {status})")
    if pre_match_strength != post_match_strength:
        print(f"⚠️ Team strength changed from {pre_match_strength} to {post_match_strength} due to fatigue.")
    print("═" * 60)

def buy_players(my_team, players):
    if my_team is None:
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
    for idx, player in enumerate(players):
        print("║ {:<4} │ {:<25} │ {:<15} │ {:<5} │ {:<10.1f} │ {:<12,} ║".format(
            idx + 1, player.name, player.position, player.age, player.player_coef, player.price
        ))
    print("╩════╧═══════════════════════════╧═════════════════╧═══════╧════════════╧══════════════╩")

    print(f"\n👥 Your Team: {my_team.team_name}")
    print(f"💰 Budget: ${my_team.budget:,}")
    print(f"🏀 Players: {len(my_team.players)}/5")
    print(f"💪 Team Strength: {my_team.team_strength()}")
    print("─" * 60)
    buy_players = input("Do you want to auto-buy up to 5 players? (yes/no): ").lower()
    
    if buy_players == "yes":
        to_remove = []
        bought_players = []
        
        # Сортуємо гравців за коефіцієнтом (від найвищого до найнижчого)
        sorted_players = sorted(players, key=lambda x: x.player_coef, reverse=True)
        
        for player in sorted_players:
            if my_team.budget >= player.price and len(my_team.players) < 5:
                my_team.add_player(player)
                to_remove.append(player)
                bought_players.append(player)
                print(f"✅ Bought {player.name} ({player.position}) for ${player.price:,}. Budget left: ${my_team.budget:,}")
        
        for player in to_remove:
            players.remove(player)
        
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
            print(f"💰 New budget: ${my_team.budget:,}")
            print(f"💪 New team strength: {my_team.team_strength()}")
            print("═" * 60)
        else:
            print("⚠️ No players bought. Insufficient budget or no suitable players.")
    elif buy_players == "no":
        print("No players bought.")
    else:
        print("⚠️ Invalid input. Please enter 'yes' or 'no'.")

def select_existing_team(teams):
    print_separator()
    print("═" * 60)
    print("Existing Teams:".center(60))
    print("═" * 60)
    for idx, team in enumerate(teams):
        print(f"{idx+1}. {team.team_name} - Budget: ${team.budget:,}, Players: {len(team.players)}")
        for player in team.players:
            print(f"   • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
    print("═" * 60)

    while True:
        try:
            team_idx = int(input(f"\nChoose a team to play with (1-{len(teams)}): "))
            if 1 <= team_idx <= len(teams):
                selected_team = teams[team_idx - 1]  # Не видаляємо команду зі списку
                print(f"\n✅ You selected team {selected_team.team_name}!")
                print(f"💰 Budget: ${selected_team.budget:,}")
                print(f"👥 Players: {len(selected_team.players)}")
                print(f"💪 Team Strength: {selected_team.team_strength()}")
                print("🏃 Team roster:")
                for player in selected_team.players:
                    print(f"   • {player.name} ({player.position}) - Coef: {player.player_coef:.1f}")
                return selected_team
            else:
                print("❌ Invalid team number!")
        except ValueError:
            print("❌ Please enter a valid number!")

def show_stats(my_team):
    print_separator()
    print("═" * 60)
    print("Team Statistics:".center(60))
    print("═" * 60)
    print(f"💰 Budget: ${my_team.budget:,}")
    print(f"👥 Players: {len(my_team.players)}")
    print(f"💪 Team Strength: {my_team.team_strength()}")
    print("║ {:<25} │ {:<15} │ {:<10} │ {:<12} │ {:<10} ║".format(
        "Name", "Position", "Coef", "Fatigue", "Price"
    ))
    print("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╤════════════╣")
    for player in my_team.players:
        status = "⚠️ High" if player.fatigue >= 0.8 else "OK"
        print("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12.2f} │ {:<10,} ║".format(
            player.name, player.position, player.player_coef, player.fatigue, player.price
        ))
    print("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╧════════════╩")
    print("═" * 60)

def rest_team(my_team):
    """
    Дозволяє команді відпочити, зменшуючи втому всіх гравців і виводячи оновлений статус команди.

    Parameters:
        my_team (Team): Команда, гравці якої відпочинуть.

    Returns:
        None
    """

    # Сила команди до відпочинку
    pre_rest_strength = my_team.team_strength()

    # Зменшення втоми для всіх гравців
    for player in my_team.players:
        player.decrease_fatigue()

    # Сила команди після відпочинку
    post_rest_strength = my_team.team_strength()

    # Виведення статусу
    print("\n" + "═" * 60)
    print("🏀 TEAM REST 🏀".center(60))
    print("═" * 60)
    print(f"👥 Team: {my_team.team_name}")
    print(f"💪 Team Strength Before Rest: {pre_rest_strength}")
    print(f"💪 Team Strength After Rest: {post_rest_strength}")
    if pre_rest_strength != post_rest_strength:
        print(f"✅ Team strength increased from {pre_rest_strength} to {post_rest_strength} due to rest!")
    print("\nPlayers Status After Rest:")
    print("║ {:<25} │ {:<15} │ {:<10} │ {:<12} │ {:<10} ║".format(
        "Name", "Position", "Coef", "Fatigue", "Price"
    ))
    print("╠═══════════════════════════╤═════════════════╤════════════╤══════════════╤════════════╣")
    for player in my_team.players:
        status = "⚠️ High" if player.fatigue >= 0.8 else "OK"
        print("║ {:<25} │ {:<15} │ {:<10.1f} │ {:<12.2f} │ {:<10,} ║".format(
            player.name, player.position, player.player_coef, player.fatigue, player.price
        ))
    print("╩═══════════════════════════╧═════════════════╧════════════╧══════════════╧════════════╩")
    print(f"✅ {my_team.team_name} is ready to play!")
    print("═" * 60)

# === Головний цикл ===

start_main_menu()
while True:
    choice = input("\nChoose an option (1, 2, or Exit): ").lower()
    if choice == "exit":
        print_goodbye()
        break
    elif choice == "1":
        if create_team():
            break  # Перейти до основного меню після створення команди
    elif choice == "2":
        if not teams:
            print("⚠️ No existing teams available!")
        else:
            my_team = select_existing_team(teams)
            break
    else:
        print("⚠️ Invalid choice. Please enter 1, 2, or Exit.")

if my_team is not None:
    print_main_menu()
    while True:
        command = input("\nEnter command (1-5 or Exit): ").strip().lower()
        if command == "exit":
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
        elif command == "5":
            show_stats(my_team)
        elif command == "6":
            rest_team(my_team)
        else:
            print("⚠️ Invalid command. Please try again.")