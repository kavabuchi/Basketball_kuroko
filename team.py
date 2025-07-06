class Team:

    teams_stats = {
        "Lakers": {"rate": 0.8, "skill": 0.7, "win": 0.7},
        "Bulls": {"rate": 0.9, "skill": 0.8,"win": 0.8},
        "Celtics": {"rate": 0.7, "skill": 0.6, "win": 0.6},
        "Warriors": {"rate": 0.9, "skill": 0.8, "win": 0.8}
    }

    def __init__(self, team_name, team_rate, team_skill, price):
        self.team_name = team_name
        self.team_skill = team_skill
        self.team_rate = team_rate
        self.price = price
        self.team_rate = 0
        self.team_coef()
    
    def team_coef(self):
        rating = self.teams_stats[self.team_skill]
        skill_sum = 0
        
        # rating = {"team_name_1": "Lakers", "team_rate": 8, "team_skill": 7,}
        # self.team_skill = 100
 
        for key in rating:
            skill_sum += self.teams_stats[key] + self.team_skill

            # skill_sum += 8(rate) * 100 | 80
            # skill_sum += 7(skill) * 100 | 70 + 80 = 150
    
    def __str__(self):
        return f"Team: {self.team_name}, Team Rate: {self.team_rate}, Team skill: {self.team_skill}, Price: {self.price},"
    
    if __name__ == "__main__":
        team_1 = Team("Lakers", 100, 80, 100)
        print(team_1)
        
