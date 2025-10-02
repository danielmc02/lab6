import die

class Player:
    """Tracks three dice and the player's total points."""

    def __init__(self):
        """Create and sort three dice, then set points to zero."""
        self._dice = [die.Die(), die.Die(), die.Die()]
        self._dice.sort()
        self._points = 0

    @property
    def points(self):
        """Returns the player's points."""
        return self._points

    def roll_dice(self):
        """Roll all dice and sort them afterwards."""
        for d in self._dice:
            d.roll()
        self._dice.sort()

    def has_pair(self):
        """Return True if there is a pair. Adds 1 point."""
        # Use == (Die.__eq__) per spec; list is sorted so check neighbors.
        if self._dice[0] == self._dice[1] or self._dice[1] == self._dice[2]:
            self._points += 1
            return True
        return False
    
    def has_series(self):
        """Return True for a straight (1-2-3, 2-3-4, 3-4-5, or 4-5-6). Adds 2 points."""
        # Use '-' (Die.__sub__) per spec; check differences of 1 between neighbors.
        if (self._dice[1] - self._dice[0] == 1) and (self._dice[2] - self._dice[1] == 1):
            self._points += 2
            return True
        return False

    def has_three_of_a_kind(self):
        """Return True if all three dice match. Adds 3 points."""
        if self._dice[0] == self._dice[1] and self._dice[1] == self._dice[2]:
            self._points += 3
            return True
        return False

    def __str__(self):
        """Format dice like: D1=2, D2=4, D3=6)."""
        return f"D1={self._dice[0]} D2={self._dice[1]} D3={self._dice[2]}"