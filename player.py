class Player:
    def __init__(self, name, age, position, fatigue, price):
        self.name = name
        self.age = age
        self.position = position
        self.fatigue = fatigue
        self.player_coef = (1 * age + position * 1.5) / fatigue
        self.price = price
    
lebron_James = Player("Lebron_James", 38, 1, 0.8, 10000000)
koby_bryant = Player("Koby_Bryant", 40, 1, 0.7, 8000000)

print(lebron_James.player_coef)
print(koby_bryant.player_coef)
