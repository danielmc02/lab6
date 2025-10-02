"""
LAB #6
    10/01/2025
    Student 1: Jimmy Le
    Student 2: Daniel McCray

    Yahtzee: Roll three dice and score points for pairs, straights, and three of a kind. Pairs = 1 point, straights = 2 points, three of a kind = 3 points. 
    After each roll, the user can choose to roll again or quit. The game keeps track of the player's total score.
"""

import check_input
from player import Player

def take_turn(p):
    """Roll dice, display win type, and show updated score."""
    p.roll_dice()
    print(p)

    # Order matters so we don't double dip points
    if p.has_three_of_a_kind():
        print("You got 3 of a kind!")
    elif p.has_series():
        print("You got a series of 3!")
    elif p.has_pair():
        print("You got a pair!")
    else:
        print("Aww. Too Bad.")

    print("Score =", p.points)

def main():
    """Starts game, constructs a Player and loop turns until user chooses to stop."""
    print("-Yahtzee-")
    player = Player()

    playing = True
    while playing:
        take_turn(player)
        playing = check_input.get_yes_no("Play again? (Y/N): ")
        if playing:
            print()

    print("\nGame Over.")
    print("Final Score =", player.points)

if __name__ == "__main__":
    main()