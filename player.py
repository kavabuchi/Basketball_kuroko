class Player:
    """
    Представляє гравця баскетбольної команди з характеристиками, що впливають на його ефективність.

    Атрибути:
        name (str): Ім'я гравця.
        age (int): Вік гравця.
        position (str): Позиція на полі (наприклад: "Point_Guard").
        fatigue (float): Рівень втоми (від 0.0 до 1.0).
        skill (float): Загальний рівень навичок (від 0.0 до 1.0 або від 0 до 100).
        price (int): Вартість гравця.
        player_coef (float): Обчислений коефіцієнт ефективності гравця.
    """

    # Константи класу для покращення читабельності та легкості зміни
    FATIGUE_REDUCTION_YOUNG = 0.1
    FATIGUE_REDUCTION_OLD = 0.05
    YOUNG_AGE_THRESHOLD = 30
    MAX_FATIGUE = 1.0
    MIN_FATIGUE = 0.0
    MIN_AGE = 18
    MAX_AGE = 50
    MIN_SKILL = 0.0
    MAX_SKILL = 1.0
    MIN_PRICE = 0

    position_stats = {
        "Point_Guard": {"speed": 0.8, "dribble": 0.7, "pass": 0.6, "shot": 0.9},
        "Shooting_Guard": {"speed": 0.7, "dribble": 0.7, "pass": 0.5, "shot": 0.8},
        "Small_Forward": {"speed": 0.6, "dribble": 0.6, "pass": 0.6, "shot": 0.7},
        "Power_Forward": {"speed": 0.5, "dribble": 0.5, "pass": 0.5, "shot": 0.6},
        "Center": {"speed": 0.4, "dribble": 0.5, "pass": 0.4, "shot": 0.5}
    }

    def __init__(self, name, age, position, fatigue, skill, price):
        """
        Ініціалізує гравця з валідацією вхідних параметрів.
        
        Parameters:
            name (str): Ім'я гравця
            age (int): Вік гравця
            position (str): Позиція гравця
            fatigue (float): Рівень втоми
            skill (float): Рівень навичок
            price (int): Вартість гравця
            
        Raises:
            ValueError: Якщо параметри не відповідають вимогам
        """
        self._validate_inputs(name, age, position, fatigue, skill, price)
        
        self.name = name
        self.age = age
        self.position = position
        self.fatigue = fatigue
        self.skill = skill
        self.price = price
        self.player_coef = 0
        self.count_coef()

    def _validate_inputs(self, name, age, position, fatigue, skill, price):
        """Валідує вхідні параметри для створення гравця."""
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        
        if not isinstance(age, int) or not (self.MIN_AGE <= age <= self.MAX_AGE):
            raise ValueError(f"Age must be an integer between {self.MIN_AGE} and {self.MAX_AGE}")
        
        if position not in self.position_stats:
            raise ValueError(f"Position must be one of: {', '.join(self.position_stats.keys())}")
        
        if not isinstance(fatigue, (int, float)) or not (self.MIN_FATIGUE <= fatigue <= self.MAX_FATIGUE):
            raise ValueError(f"Fatigue must be a number between {self.MIN_FATIGUE} and {self.MAX_FATIGUE}")
        
        if not isinstance(skill, (int, float)) or not (self.MIN_SKILL <= skill <= self.MAX_SKILL):
            raise ValueError(f"Skill must be a number between {self.MIN_SKILL} and {self.MAX_SKILL}")
        
        if not isinstance(price, int) or price < self.MIN_PRICE:
            raise ValueError(f"Price must be a non-negative integer")

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

    def increase_fatigue(self):
        """
        Збільшує рівень втоми гравця на 0.1.
        """
        self.fatigue = min(self.fatigue + 0.1, self.MAX_FATIGUE)
        self.count_coef()  # Оновлюємо коефіцієнт після зміни втоми

    def decrease_fatigue(self):
        """
        Зменшує рівень втоми гравця залежно від віку.
        - Молодші гравці (< 30 років): зменшення на 0.1.
        - Старші гравці (≥ 30 років): зменшення на 0.05.
        - Втома не може бути нижче 0.0.
        """
        reduction = self.FATIGUE_REDUCTION_YOUNG if self.age < self.YOUNG_AGE_THRESHOLD else self.FATIGUE_REDUCTION_OLD
        self.fatigue = max(self.fatigue - reduction, self.MIN_FATIGUE)
        self.count_coef()
       
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
    try:
        player1 = Player("Kobe Bryant", 25, "Point_Guard", 0.3, 1.0, 10000)
        player2 = Player("LeBron James", 25, "Shooting_Guard", 0.4, 0.92, 15000)

        print("=" * 60)
        print("⭐ Sample Players:")
        print("=" * 60)
        print(player1)
        print(player2)
        
        # Тест валідації
        print("\n" + "=" * 60)
        print("🧪 Testing Validation:")
        print("=" * 60)
        
        try:
            invalid_player = Player("", 15, "Invalid_Position", 1.5, 2.0, -100)
        except ValueError as e:
            print(f"✅ Validation caught error: {e}")
            
    except Exception as e:
        print(f"❌ Error during testing: {e}")
