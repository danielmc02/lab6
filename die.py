import random

class Die:
    _sides = 0
    _value = 0
    def __init__(self,sides = 6):
        self._sides = 6
    
    def roll(self):
        '''Generate a random number between 1 and the sides of the dice (usually 6)'''
        random_number = random.randrange(1, self._sides+1) # Inclusive to 6
        self._value = random_number
        
        
    def __str__(self):
        return f"Dice Value: {self._value}"
    
    def __lt__(self, other):
        return self._value < other._value
    def __eq__(self, other):
        return self._value == other._value
    def __sub__(self, other):
        return self._value - other._value