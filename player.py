class Player:
    def __init__(self, name, age, position, shooting, defense, bloking, price):
        self.name = name
        self.age = age
        self.position = position
        self.shooting = shooting
        self.defense = defense
        self.bloking = bloking
        self.player_coef = (shooting * 0.4 + defense * 0.5 + bloking * 0.3) * price
        self.price = price


    def __str__(self):
        return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Shooting: {self.shooting}, Defense: {self.defense}, Bloking: {self.bloking}, Price: {self.price}, Player Coefficient: {self.player_coef}"


if __name__ == "__main__":
    player1 = Player("Koby Bryant", 25, 1, 0.8, 0.7, 0.9, 100000)
    player2 = Player("Lebron James", 30, 2, 0.9, 0.8, 0.7, 90000)

    print(player1)
    print(player2)