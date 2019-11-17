class Handshake:
    def __init__(self):
        self.round = 1
        self.cooperate = True

    def decide_first(self):
        return 'D'

    def decide(self, previous_opponent_move):
        if self.round == 1:
            if previous_opponent_move == 'C':
                self.cooperate = False
            self.round = 2
            return 'C'
        if self.round == 2:
            self.round = 3
            if previous_opponent_move == 'D':
                self.cooperate = False
        if self.cooperate:
            return 'C'
        else:
            return 'D'

        
        return previous_opponent_move
    
    def clean(self):
        self.round = 1
        self.cooperate = True

    def __str__(self):
        return "Handshake"