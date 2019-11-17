import random

class TitForTatWithForgiveness:
    def decide_first(self):
        return 'C'

    def decide(self, previous_opponent_move):
        if previous_opponent_move == 'D':
            r = random.randint(0,100)
            if r >= 90:
                return 'C'
            else:
                return 'D'
        return 'C'
    
    def clean(self):
        pass

    def __str__(self):
        return "TitForTatWithForgiveness"