from player import Player
from check_input import get_yes_no
def take_turn(player:Player):
    player.roll_dice()
    print(player.__str__())

    #if player.
    print(f"Score: {player.points()}")

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