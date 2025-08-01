class Player:

    """
    Представляє гравця баскетбольної команди з характеристиками, що впливають на його ефективність.

    Атрибути:
        name (str): Ім’я гравця.
        age (int): Вік гравця.
        position (str): Позиція на полі (наприклад: "Point_Guard").
        fatigue (float): Рівень втоми (від 0.0 до 1.0).
        skill (float): Загальний рівень навичок (від 0.0 до 1.0 або від 0 до 100).
        price (int): Вартість гравця.
        player_coef (float): Обчислений коефіцієнт ефективності гравця.
    """
    
    position_stats = {
        "Point_Guard": {"speed": 0.8, "dribble": 0.7, "pass": 0.6, "shot": 0.9},
        "Shooting_Guard": {"speed": 0.7, "dribble": 0.7 , "pass": 0.5, "shot": 0.8},
        "Small_Forward": {"speed": 0.6, "dribble": 0.6, "pass": 0.6, "shot": 0.7}, 
        "Power_Forward": {"speed": 0.5, "dribble": 0.5, "pass": 0.5, "shot": 0.6},
        "Center": {"speed": 0.4, "dribble": 0.5, "pass": 0.4, "shot": 0.5}
    }
    
    
    def __init__(self, name, age, position, fatigue, skill, price):

        """
        Ініціалізує нового гравця з заданими характеристиками.

        Parameters:
            name (str): Ім’я гравця.
            age (int): Вік гравця.
            position (str): Позиція на полі.
            fatigue (float): Рівень втоми (0.0 – 1.0).
            skill (float): Рівень навичок (0.0 – 1.0 або 0 – 100).
            price (int): Вартість гравця.
        """

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

        """
        Обчислює коефіцієнт ефективності гравця (`player_coef`), 
        базуючись на навичках гравця, його позиції та рівні втоми.

        Формула:
            player_coef = Σ(position_stat[key] × skill) × (1 − fatigue)
        """

        #stats = {"speed": 0.8, "dribble": 0.7, "pass": 0.6, "shot": 0.9}
        #self.skill = 100
        
        for stat_value in stats.values():
            skill_sum += stat_value * self.skill

            #skill_sum += 0.8(speed) * 100 | 80
            #skill_sum += 0.7(dribble) * 100 | 80 + 70 = 150

        #skill_sum = 300
        #self.palyer_coef = 300 * (1 - 0.3) | 210

        self.player_coef = skill_sum * (1 - self.fatigue)
        
    def __str__(self):
        """
        Повертає строкове представлення гравця для зручного виводу.

        Returns:
            str: Інформація про гравця у читабельному форматі.
        """
        return f"Player: {self.name}, Age: {self.age}, Position: {self.position}, Fatigue: {self.fatigue}, Skill: {self.skill}, Price: {self.price}, Coef: {self.player_coef:.1f}"
 

if __name__ == "__main__":
    player1 = Player("Koby Bryant", 25, "Point_Guard", 0.3, 100, 10000)
    player2 = Player("Lebron James", 25, "Shooting_Guard", 0.4, 92, 15000)
    
    print(player1)
    print(player2)