from player import Player

class Team:

    team_stats = {
        "Lakers": {"rate": 0.8, "skill": 0.7, "win": 0.7},
        "Bulls": {"rate": 0.9, "skill": 0.8,"win": 0.8},
        "Celtics": {"rate": 0.7, "skill": 0.6, "win": 0.6},
        "Warriors": {"rate": 0.9, "skill": 0.8, "win": 0.8}
    }


    def __init__(self, team_name, budget):
        self.team_name = team_name
        self.players = []
        self.budget = budget
        self.team_rate = 0
    

    def team_strength(self):
        return sum(player.player_coef for player in self.players)
        

    def add_player(self, player):
        if self.budget >= player.price:
            self.budget -= player.price
            self.players.append(player)
            return True
        else:
            print("Your fucking ass have no money for that player")
            return False
    

    def sell_player(self, player):
        if player in self.players:
            self.budget += player.price // 2
            self.players.remove(player)
            return True
        else: 
            print("You have not this player in your team, stupid bastard")
            return False
        

    def __str__(self):
        players_str = ", ".join(str(player) for player in self.players)
        return f"Team: {self.team_name}, Team Rate: {self.team_rate}, Team Budget: {self.budget}, Players: [{players_str}]"


if __name__ == "__main__":
    team_1 = Team("Lakers", 100, 80)
    team_2 = Team("Bulls", 90, 70)

    print(team_1)
    print(team_2)
