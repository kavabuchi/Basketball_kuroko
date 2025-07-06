class Team:

    teams_inf = {
        "team_name_1": "Lakers", "team_rate": 8, "team_skill": 7, "team_players": 12, "team_win_rate": 7,
        "team_name_2": "Bulls", "team_rate": 9, "team_skill": 8, "team_players": 12, "team_win_rate": 8,
        "team_name_3": "Celtics", "team_rate": 7, "team_skill": 6, "team_players": 12, "team_win_rate": 6,
        "team-name_4": "Warriors", "team_rate": 9, "team_skill": 8, "team_players": 12, "team_win_rate": 8
    }

    def __init__(self, teams, team_skill, price):
        self.teams = teams
        self.team_skill = team_skill
        self.price = price
        self.team_rate = 0
        self.team_coef()
    
    def team_coef(self):
        rating = self.teams_inf[self.team_skill]
        skill_sum = 0
        
        for key in rating:
            skill_sum += self.teams_inf[key] + self.team_skill