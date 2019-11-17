import random

class Pavlov:
    def __init__(self):
        self.round = 1
        self.cooperate_counter = 0

    def decide_first(self):
        return 'C'

    def decide(self, previous_opponent_move):
        if self.round < 6:
            self.round = self.round + 1
            if previous_opponent_move == 'C':
                self.cooperate_counter = self.cooperate_counter + 1
            return previous_opponent_move
        if self.round == 6:
            self.round = self.round + 1
            if previous_opponent_move == 'C':
                self.cooperate_counter = self.cooperate_counter + 1
            if self.cooperate_counter == 6 or self.cooperate_counter == 3:
                self.tactic = 'TitForTat'
            elif self.cooperate_counter < 3:
                self.tactic = 'AlwaysDefect'
            else:
                self.tactic = 'Random'

        if self.tactic == 'Random':
            if random.randint(0,1) == 0:    
                return 'D'
            else:
                return 'C'
        if self.tactic == 'TitForTat':
            return previous_opponent_move
        if self.tactic == 'AlwaysDefect':
            return 'D'
        raise
    
    def clean(self):
        self.round = 1
        self.cooperate_counter = 0

    def __str__(self):
        return "Pavlov"