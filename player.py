class Player:

    position_stats = {
        "Point_Guard": {"speed": 0.8, "dribble": 0.7, "pass": 0.6, "shot": 0.9},
        "Shooting_Guard": {"speed": 0.7, "dribble": 0.7 , "pass": 0.5, "shot": 0.8},
        "Small_Forward": {"speed": 0.6, "dribble": 0.6, "pass": 0.6, "shot": 0.7}, 
        "Power_Forward": {"speed": 0.5, "dribble": 0.5, "pass": 0.5, "shot": 0.6},
        "Center": {"speed": 0.4, "dribble": 0.5, "pass": 0.4, "shot": 0.5}
    }
    
    def __init__(self, name, age, position, fatigue, skill, price):
        self.name = name
        self.age = age
        self.position = position
        self.fatigue = fatigue
        self.skill = skill
        self.price = price
        self.player_coef = 0
        self.count_coef()
    
    def count_coef(self):
        stats = self.position_stats[self.position]
        skill_sum = 0

        #stats = {"speed": 0.8, "dribble": 0.7, "pass": 0.6, "shot": 0.9}
        #self.skill = 100
        
        for key in stats:
            skill_sum += stats[key] * self.skill

            #skill_sum += 0.8(speed) * 100 | 80
            #skill_sum += 0.7(dribble) * 100 | 80 + 70 = 150

        #skill_sum = 300
        #self.palyer_coef = 300 * (1 - 0.3) | 210

        self.player_coef = skill_sum * (1 - self.fatigue)
        
    def __str__(self):
        return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Fatigue: {self.fatigue}, Skill: {self.skill}, Price: {self.price}, Coef: {self.palyer_coef}"


if __name__ == "__main__":
    player1 = Player("Koby Bryant", 25, "Point_Guard", 0.3, 100, 10000)
    player2 = Player("Lebron James", 25, "Shooting_Guard", 0.4, 92, 15000)
    
    print(player1)
    print(player2)