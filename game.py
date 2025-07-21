from player import Player
from team import Team
from match import Match
import random

teams = [ 
    Team("Lakers", 1000000),
    Team("Warriors", 95000),
    Team("Celtics", 90000),
    Team("Bulls", 92000)
]

my_team = None

for team in teams:
    if team.team_name == "Lakers":
        my_team = team
        break


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
print("Enter 4: buy all team")
print("Enter Exit: Exit")

"""
    Купує гравця для команди, якщо достатньо бюджету.

    Parameters:
        team (Team): Команда, яка купує гравця.
        players (Player): Список доступних гравців.

    Returns:
        bool: True, якщо покупка успішна, False — якщо гравець не знайдений або недостатньо коштів.
"""

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
                if my_team.budget >= player.price:
                    my_team.add_player(player)
                    players.remove(player)
                    print(f"You bought a new {player}. The new budget is {my_team.budget}")
                    break
        else:
            print("Player not found")
    
    if command == "4":
        for player in players:
            print(player, end= "\n")
        
        buy_players = input("Do you want to buy all players?: yes/no ")
        if buy_players == "yes":
            for player in players:
                if my_team.budget >= player.price:
                    my_team.add_player(player)
                    print(f"You bought a {player.name}. The new budget is {my_team.budget}")
                    
        elif buy_players == "no":
            print("You didn't buy any players")
        else:
            print("Players not found")


    """
    Продає гравця з команди за пів ціни та додає його до загального списку.

    Parameters:
        team (Team): Команда, що продає гравця.
        players (Player): Список доступних гравців.

    Returns:
        bool: True, якщо гравець був проданий, False — якщо не знайдено.
    """


    if command == "2":
        for player_in_team in my_team.players:
            print(player_in_team, end= "\n")
    
        sell_player = input("Enter player name to sell: ")
        
        found = False
        for player_in_team in my_team.players:

            if sell_player == player_in_team.name:
                my_team.sell_player(player_in_team)
                players.append(player_in_team)
                print(f"You sold a {player_in_team}. The new budget is {my_team.budget}")
                found = True
                break

        if not found:
            print("Player not found")

    
    if command == "3":
        for team in teams:
            print(team.team_name, end= "\n")
            
        game_in_team = input("Enter names of teams to play: ")
        team_names = game_in_team.split("-")
        if len(team_names) != 2:
            print("Please enter two team names separated by '-' (e.g. Lakers - Celtics)")
        elif team_names[0].strip() == team_names[1].strip():
            print("You can't play against yourself")
        else:

            team1_name = team_names[0].strip()
            team2_name = team_names[1].strip()
    
            for team in teams:
                if team.team_name == team1_name:
                    team1 = team
                elif team.team_name == team2_name:
                    team2 = team
    
            if team1 and team2:
                match = Match(team1, team2)
                match.play_match()
            else:
                print("One or both teams not found. Please try again.")
        

        
# 1)
# написати рядки документації для всіх функцій (назва параметра, тип параметра, що вона собою виконує функція, що повертає функція)
# виправити додавання покупки гравця (щоб писало якого конткретного гравця було куплено)
# виправити продажу гравця (щоб писало якого конкретного гравця було продано)


# 2)
# зробити документаці. до функцій і до класів
# змерджити гілку в мейн і створити нову для нових завданнь --
# вибрати в якості команди  свою команду
# пофіксити щоб команда не грала із собою
# бонус. рахунок команди не рандомився, а рахувався від сили своєї команди а у противника рандомилась, додавався бюджет до команди якщо вона виграла, віднімався якщо програла


# 3) 
# зробити документаці. до функцій і до класів
# зробити можливість вибрати свою команду за замовчуванням а команда суперника буде випадковим вибором із всіх команд
# зробити так зоб за перемогу мені закидували бабіноси
# зробити так щоб у моєї команди округлівалась сила до меншого числа
# зробити граф команд від слабких до сильних

            
