from player import Player
from team import Team
from match import Match
import random

team_1 = Team("Lakers", 1000000)

players = [
    Player("John Smith", 25, "Point_Guard", 0.1, 0.85, 50000),
    Player("Mike Johnson", 28, "Shooting_Guard", 0.2, 0.8, 47000),
    Player("Alex Brown", 24, "Small_Forward", 0.15, 0.83, 52000),
    Player("Chris Davis", 30, "Power_Forward", 0.3, 0.75, 45000),
    Player("Tom Wilson", 27, "Center", 0.25, 0.78, 49000),
    Player("James White", 26, "Point_Guard", 0.12, 0.82, 51000),
    Player("Robert Green", 29, "Shooting_Guard", 0.18, 0.79, 48000) 
]

print("Hi, welcome to the NBA simulation!")
print("You can choose to simulate a match between two teams or to create a new team.")
print("Command: ")
print("Enter 1: buy new player")
print("Enter 2: sell player")
print("Enter Exit: Exit")

while True:

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

# написати рядки документації для всіх функцій (назва параметра, тип параметра, що вона собою виконує функція, що повертає функція)
# виправити додавання покупки гравця (щоб писало якого конткретного гравця було куплено)
# виправити продажу гравця (щоб писало якого конкретного гравця було продано)

            
