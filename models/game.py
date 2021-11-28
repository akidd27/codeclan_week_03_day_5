class Game:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

    def result(self):
        #compares choices of 2 players and returns winner
        if self.player_1.choice == self.player_2.choice:
            #returns None for draw
            return None
        if self.player_1.choice == "Rock":
            if self.player_2.choice == "Paper":
                return self.player_2
            elif self.player_2.choice == "Scissors":
                return self.player_1
        elif self.player_1.choice == "Paper":
            if self.player_2.choice == "Scissors":
                return self.player_2
            elif self.player_2.choice == "Rock":
                return self.player_1
        elif self.player_1.choice == "Scissors":
            if self.player_2.choice == "Rock":
                return self.player_2
            elif self.player_2.choice == "Paper":
                return self.player_1