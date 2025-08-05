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

# === Ініціалізація ===

teams = [ 
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000)
]

my_team = Team("Lakers", 3000000)

players = [
    Player("LeBron James", 39, "Small_Forward", 0.1, 0.95, 100000),
    Player("Anthony Davis", 31, "Power_Forward", 0.15, 0.92, 95000),
    Player("D'Angelo Russell", 28, "Point_Guard", 0.2, 0.85, 75000),
    Player("Austin Reaves", 26, "Shooting_Guard", 0.12, 0.83, 70000),
    Player("Rui Hachimura", 26, "Small_Forward", 0.18, 0.8, 68000),
    Player("Jarred Vanderbilt", 25, "Power_Forward", 0.2, 0.78, 65000),
    Player("Jaxson Hayes", 24, "Center", 0.22, 0.76, 60000)
]

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
