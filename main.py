from player import Player
from check_input import get_yes_no
def take_turn(player:Player):
    player.roll_dice()
    print(player.__str__())
    if player.has_pair():
        print("You got a pair!")
        
    if player.has_series():
        print("You got a series of 3!")
    if player.has_three_of_a_kind():
        print("You got 3 of a kind!")
    #if player.
    print(f"Score: {player.points}")

def main():
    print("1")
    while True:
        player = Player()
        take_turn(player=player)
        if get_yes_no("Play again: ") == False:
            print("Goodbye")
            break
    
    

if __name__ == "__main__":
    main()