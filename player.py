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
        "Shooting_Guard": {"speed": 0.7, "dribble": 0.7, "pass": 0.5, "shot": 0.8},
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
        """
        Обчислює коефіцієнт ефективності гравця (`player_coef`), 
        базуючись на навичках гравця, його позиції та рівні втоми.
        Формула:
            player_coef = Σ(position_stat[key] × skill) × (1 − fatigue)
        """
        stats = self.position_stats[self.position]
        skill_sum = sum(stat_value * self.skill for stat_value in stats.values())
        self.player_coef = skill_sum * (1 - self.fatigue)

    def __str__(self):
        """
        Повертає строкове представлення гравця для зручного виводу.
        """
        return (
            f"🏀 {self.name} ({self.position}) | Age: {self.age} | "
            f"Fatigue: {self.fatigue:.2f} | Skill: {self.skill} | "
            f"Coef: {self.player_coef:.1f} | Price: ${self.price}"
        )


# 🔽 Тестовий запуск модуля
if __name__ == "__main__":
    player1 = Player("Kobe Bryant", 25, "Point_Guard", 0.3, 100, 10000)
    player2 = Player("LeBron James", 25, "Shooting_Guard", 0.4, 92, 15000)

    print("=" * 60)
    print("⭐ Sample Players:")
    print("=" * 60)
    print(player1)
    print(player2)
