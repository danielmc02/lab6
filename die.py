import random

class Die:
    """Represents a single n-sided die."""

    def __init__(self, sides=6):
        """Create a die with the given number of sides"""
        self._sides = sides
        self._value = 0  # per spec: can start at 0 or the result of roll()

    def roll(self):
        """Roll the die and return the new value."""
        self._value = random.randint(1, self._sides)
        return self._value

    def __str__(self):
        """Return the die's current value as a string."""
        return str(self._value)

    def __lt__(self, other):
        """True if this die's value is less than the other's."""
        return self._value < other._value

    def __eq__(self, other):
        """True if the two dices values are equal."""
        return self._value == other._value

    def __sub__(self, other):
        """Return the difference between the two dices."""
        return self._value - other._value