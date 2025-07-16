from player import Player
from team import Team
from match import Match
import random

team_1 = Team("Lakers", 1000000)
team_2 = Team("Celtics", 1000000)

teams = [
    Team("Lakers", 100000),
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000),
]


players = [
    Player("LeBron James", 39, "Small_Forward", 0.1, 0.95, 100000),
    Player("Anthony Davis", 31, "Power_Forward", 0.15, 0.92, 95000),
    Player("D'Angelo Russell", 28, "Point_Guard", 0.2, 0.85, 75000),
    Player("Austin Reaves", 26, "Shooting_Guard", 0.12, 0.83, 70000),
    Player("Rui Hachimura", 26, "Small_Forward", 0.18, 0.8, 68000),
    Player("Jarred Vanderbilt", 25, "Power_Forward", 0.2, 0.78, 65000),
    Player("Jaxson Hayes", 24, "Center", 0.22, 0.76, 60000)
]

print("Hi, welcome to the NBA simulation!")
print("You can choose to simulate a match between two teams or to create a new team.")
print("Command: ")
print("Enter 1: buy new player")
print("Enter 2: sell player")
print("Enter 3: start the match")
print("Enter Exit: Exit")

while True:

    """
    Купує гравця для команди, якщо достатньо бюджету.

    Parameters:
        team (Team): Команда, яка купує гравця.
        players (Player): Список доступних гравців.

    Returns:
        bool: True, якщо покупка успішна, False — якщо гравець не знайдений або недостатньо коштів.
    """
 
    command = input("Enter command: ")
    if command == "Exit":
        print("GAME OVER")
        break
    print("The game continues")
    
    if command == "1":
        for player in players:
            print(player, end= "\n")
    
        buy_player = input("Enter player name to buy: ") 
        for player in players:
            
            if buy_player == player.name:
                if team_1.budget >= player.price:
                    team_1.budget -= player.price 
                    team_1.add_player(player)
                    players.remove(player)
                    print(f"You bought a new {player}. The new budget is {team_1.budget}")
                    break

                elif team_1.budget < player.price:
                    print("You don't have enough money to buy this player.")

        else:
            print("Player not found")


    """
    Продає гравця з команди за пів ціни та додає його до загального списку.

    Parameters:
        team (Team): Команда, що продає гравця.
        players (Player): Список доступних гравців.

    Returns:
        bool: True, якщо гравець був проданий, False — якщо не знайдено.
    """

    if command == "2":
        for player_in_team in team_1.players:
            print(player_in_team, end= "\n")
    
        sell_player = input("Enter player name to sell: ")
        
        found = False
        for player_in_team in team_1.players:

            if sell_player == player_in_team.name:

                team_1.budget += player_in_team.price // 2
                team_1.players.remove(player_in_team)
                players.append(player_in_team)
                print(f"You sold a {player_in_team}. The new budget is {team_1.budget}")
                found = True
                break

        if not found:
            print("Player not found")
    
    if command == "3":
        for team in teams:
            print(team.name, end= "\n")
            
        game_in_team = input("Enter names of teams to play: ")
        found = False

        for team in teams:
            if game_in_team == team.name:
                match = Match(team_1, team_2)
                match.play()
                print(f"Team {team_1.name} vs Team {team_2.name}")
                found = True
                break
        
        if not found:
            print("Team not found")
        

        

# написати рядки документації для всіх функцій (назва параметра, тип параметра, що вона собою виконує функція, що повертає функція)
# виправити додавання покупки гравця (щоб писало якого конткретного гравця було куплено)
# виправити продажу гравця (щоб писало якого конкретного гравця було продано)

            
