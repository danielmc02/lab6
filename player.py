from die import Die

class Player:
    
    _die: list[Die]
    _points: int
    def __init__(self):
        self._die = [Die(sides=6), Die(sides=6), Die(sides=6)]
        self._points = 0
    def points(self):
        return self._points
    
    def roll_dice(self):
        for die in self._die:
            die.roll()

        if self.has_pair():
            self._points += 1
            print("You got a pair!")

        if self.has_series():
            print("You got a series of 3!")
            self._points += 2
        if self.has_three_of_a_kind():
            self._points += 3
            print("You got 3 of a kind!")        
        
            
        # Call sort on the list
        self._die.sort(key=lambda x: x._value)
        
    def has_pair(self):
        """Apparently set is a unique list, so if we turn the die list into this type and the length isn't 3 that means that there is a duplicate"""
        if(self._die[0].__eq__(self._die[1]) or self._die[0].__eq__(self._die[2])):
            return True
        elif(self._die[1].__eq__(self._die[0]) or self._die[0].__eq__(self._die[2])):
            return True
        elif(self._die[2].__eq__(self._die[1]) or self._die[0].__eq__(self._die[0])):
            return True
        else:
            return False
        
    def has_three_of_a_kind(self):
        index = 1
        match = 0
        for die in self._die:
            if index == 1:
                if die.__eq__(self._die[1]) or die.__eq__(self._die[2]):
                    match += 1
            elif index == 2:
                if die.__eq__(self._die[0]) or die.__eq__(self._die[1]):
                    match += 1
            elif index == 3:
                if die.__eq__(self._die[0]) or die.__eq__(self._die[1]):
                    match += 1
            index +=1
            
        if match == 3:
            self._points+= 3
            return True
        else:
            return False
        
    def has_series(self):
        """Manually check"""
        if (self._die[1]._value == (self._die[0]._value + 1)):
            """Check the last value"""
            if (self._die[2]._value == (self._die[1]._value + 1)):
                self._points += 2
                return True
            
        else:
            return False
    def __str__(self):
        return f"D1={self._die[0]._value}, D2={self._die[1]._value}, D3={self._die[2]._value}"