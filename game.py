from player import Player
from team import Team
from match import Match
import random

print("Hi, welcome to the NBA simulation!")
print("You can choose to simulate a match between two teams or to create a new team.")
print("Command: ")
print("Enter 1: buy new player, but you can buy only 5 players")
print("Enter 2: sell player")
print("Enter 3: start the match")
print("Enter 4: buy all team")
print("Enter Exit: Exit")


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
        found = False


        for player in players:
            if buy_player == player.name:
                found = True
                if my_team.budget >= player.price:
                    if len(my_team.players) < 5:
                        my_team.add_player(player)
                        players.remove(player)
                        print(f"You bought a new {player}. The new budget is {my_team.budget}")
                    else:
                        print("You already have 5 players.")
            else:
                print("Player is not found")
            break
    
    if command == "4":
        for player in players:
            print(player, end= "\n")
        
        buy_players = input("You can buy only 5 players: ").lower()

        if buy_players == "yes":
            to_remove = []
            for player in players:
                if my_team.budget >= player.price:
                    if len(my_team.players) < 5:
                        my_team.add_player(player)
                        to_remove.append(player)
                        print(f"You bought a {player.name}. The new budget is {my_team.budget}")

            for player in to_remove:
                players.remove(player)


        elif buy_players == "no":
            print("You didn't buy any players")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


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

    try: 
        if command == "3":
            """
            Запускає симуляцію матчу між двома обраними командами користувачем.
    
            Вхід:
                - Користувач вводить два імені команд у форматі: "Team1 - Team2".
    
            Перевірки:
                - Обидві команди мають бути різними.
                - Має бути саме два імені, розділені символом '-'.
    
            Поведінка:
                - Створюється об'єкт Match з цими двома командами.
                - Відбувається матч: перша команда грає проти другої.
                - Якщо перша команда виграє, її бюджет збільшується на 10 000.
                - Інакше виводиться повідомлення про поразку або помилку.
    
            Повертає:
                None
            """
    
            for team in teams:
                print(team.team_name, end= "\n")
                
            opponent_team = input("Enter name for team to play: ")
        
            for team in teams:
                if team.team_name == opponent_team:
                    opponent_team = team
            match = Match(my_team, opponent_team)
            my_team_score, opponent_team_score = match.play_match()
                
            if my_team_score > opponent_team_score:
                my_team.budget += 100000
                print(f"{my_team.team_name} won! {my_team_score} - {opponent_team_score} . Your new budget is {my_team.budget}")
            elif my_team_score == opponent_team_score:
                print("🤝 It's a draw! {my_team_score} - {opponent_team_score}.")
            else:
                my_team.budget -= 50000
                print(f"{opponent_team.team_name} won! {opponent_team_score} - {my_team_score} . Your new budget is {my_team.budget}")
    except:
        print("You write the wrong team name")    

        
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
# зробити документаці. до функцій і до класів -- 
# зробити можливість вибрати свою команду за замовчуванням а команда суперника буде випадковим вибором із всіх команд -- 
# зробити так зоб за перемогу мені закидували бабіноси -- 
# зробити так щоб у моєї команди округлівалась сила до меншого числа --
# зробити граф команд від слабких до сильних

# 4) 
# зробити перевірки коректності вводу команди опонента, щоб писало якщо не правильна команда , наприклад "Такої команди немає" -- підсказка 144 -- 
# треба щоб сила суперників (match.py) 55 рядок не рандомиоась а бралась з teams_stats (team.py)

# 5)
# злити гілку в мейн і створити нову для нових завдань 
# зробити обмеженя на кількість гравців у команді, наприклад 5 гравців які можуть грати, якщо хочешь інщого продай попереднього