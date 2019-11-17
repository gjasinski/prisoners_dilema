class TitForTat:
    def decide_first(self):
        return 'C'

    def decide(self, previous_opponent_move):
        return previous_opponent_move
    
    def clean(self):
        pass
    
    def __str__(self):
        return "TitForTat"