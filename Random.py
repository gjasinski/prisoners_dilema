import random

class Random:
    def decide_first(self):
        if random.randint(0,1) == 0:    
            return 'D'
        else:
            return 'C'

    def decide(self, previous_opponent_move):
        if random.randint(0,1) == 0:    
            return 'D'
        else:
            return 'C'
    
    def clean(self):
        pass

    def __str__(self):
        return "Random"