from player import Player
from team import Team
from match import Match
import random

# Привітання та інструкції
print("🏀 Вітаю в NBA симуляції!")
print("Ви можете симулювати матч між двома командами або створити нову команду.")
print("\nКоманди:")
print("1 - Купити нового гравця (максимум 5 гравців)")
print("2 - Продати гравця")
print("3 - Почати матч")
print("4 - Купити всю команду")
print("Exit - Вийти з гри")

# Створення команд
teams = [ 
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000)
]

my_team = Team("Lakers", 3000000)

# Створення доступних гравців
players = [
    Player("LeBron James", 39, "Small_Forward", 0.1, 0.95, 100000),
    Player("Anthony Davis", 31, "Power_Forward", 0.15, 0.92, 95000),
    Player("D'Angelo Russell", 28, "Point_Guard", 0.2, 0.85, 75000),
    Player("Austin Reaves", 26, "Shooting_Guard", 0.12, 0.83, 70000),
    Player("Rui Hachimura", 26, "Small_Forward", 0.18, 0.8, 68000),
    Player("Jarred Vanderbilt", 25, "Power_Forward", 0.2, 0.78, 65000),
    Player("Jaxson Hayes", 24, "Center", 0.22, 0.76, 60000)
]

def buy_player(team, players_list):
    """
    Купує гравця для команди, якщо достатньо бюджету.

    Parameters:
        team (Team): Команда, яка купує гравця.
        players_list (list): Список доступних гравців.

    Returns:
        bool: True, якщо покупка успішна, False — якщо гравець не знайдений або недостатньо коштів.
    """
    print("\n📋 Доступні гравці:")
    for player in players_list:
        print(f"  {player}")
    
    buy_player_name = input("\nВведіть ім'я гравця для покупки: ")
    found = False

    for player in players_list:
        if buy_player_name == player.name:
            found = True
            if team.budget >= player.price:
                if len(team.players) < 5:
                    if team.add_player(player):
                        players_list.remove(player)
                        print(f"💰 Новий бюджет: {team.budget}")
                else:
                    print("❌ У вас вже є 5 гравців. Продайте когось спочатку.")
            break
    
    if not found:
        print("❌ Гравець не знайдений")

def sell_player(team, players_list):
    """
    Продає гравця з команди за пів ціни та додає його до загального списку.

    Parameters:
        team (Team): Команда, що продає гравця.
        players_list (list): Список доступних гравців.

    Returns:
        bool: True, якщо гравець був проданий, False — якщо не знайдено.
    """
    if not team.players:
        print("❌ У вашій команді немає гравців для продажу")
        return False
    
    print("\n👥 Гравці в вашій команді:")
    for player_in_team in team.players:
        print(f"  {player_in_team}")
    
    sell_player_name = input("\nВведіть ім'я гравця для продажу: ")
    
    found = False
    for player_in_team in team.players:
        if sell_player_name == player_in_team.name:
            if team.sell_player(player_in_team):
                players_list.append(player_in_team)
                print(f"💰 Новий бюджет: {team.budget}")
            found = True
            break

    if not found:
        print("❌ Гравець не знайдений у вашій команді")
    
    return found

def buy_all_team(team, players_list):
    """
    Купує всіх доступних гравців (максимум 5).

    Parameters:
        team (Team): Команда, яка купує гравців.
        players_list (list): Список доступних гравців.
    """
    print("\n📋 Доступні гравці:")
    for player in players_list:
        print(f"  {player}")
    
    buy_players = input("\nКупити всіх гравців? (так/ні): ").lower()

    if buy_players == "так":
        to_remove = []
        for player in players_list:
            if team.budget >= player.price and len(team.players) < 5:
                if team.add_player(player):
                    to_remove.append(player)
                    print(f"💰 Новий бюджет: {team.budget}")

        for player in to_remove:
            players_list.remove(player)
    elif buy_players == "ні":
        print("❌ Ви не купили жодного гравця")
    else:
        print("❌ Невірний ввід. Будь ласка, введіть 'так' або 'ні'.")

def play_match_game(team, teams_list):
    """
    Запускає симуляцію матчу між командою гравця та обраною командою.

    Parameters:
        team (Team): Команда гравця.
        teams_list (list): Список доступних команд для гри.
    """
    print("\n🏀 Доступні команди для матчу:")
    for team_opponent in teams_list:
        print(f"  {team_opponent.team_name}")
        
    opponent_team_name = input("\nВведіть назву команди для гри: ")
    
    # Знаходимо команду суперника
    opponent_team = None
    for team_opponent in teams_list:
        if team_opponent.team_name == opponent_team_name:
            opponent_team = team_opponent
            break
    
    if opponent_team is None:
        print("❌ Такої команди немає")
        return
    
    if opponent_team.team_name == team.team_name:
        print("❌ Команда не може грати сама з собою")
        return
    
    # Створюємо та проводимо матч
    match = Match(team, opponent_team)
    my_team_score, opponent_team_score = match.play_match()
    
    print(f"\n🏀 Результат матчу: {team.team_name} {my_team_score} - {opponent_team_score} {opponent_team.team_name}")
    
    if my_team_score > opponent_team_score:
        team.budget += 100000
        print(f"🎉 {team.team_name} перемогли! Новий бюджет: {team.budget}")
    elif my_team_score == opponent_team_score:
        print(f"🤝 Нічия! {my_team_score} - {opponent_team_score}")
    else:
        team.budget -= 50000
        print(f"😔 {opponent_team.team_name} перемогли! Новий бюджет: {team.budget}")

# Основний цикл гри
while True:
    print(f"\n💰 Ваш бюджет: {my_team.budget}")
    print(f"👥 Гравців у команді: {len(my_team.players)}/5")
    
    command = input("\nВведіть команду: ")
    
    if command == "Exit":
        print("👋 ГРА ЗАКІНЧЕНА")
        break
    
    if command == "1":
        buy_player(my_team, players)
    elif command == "2":
        sell_player(my_team, players)
    elif command == "3":
        play_match_game(my_team, teams)
    elif command == "4":
        buy_all_team(my_team, players)
    else:
        print("❌ Невірна команда. Спробуйте ще раз.")