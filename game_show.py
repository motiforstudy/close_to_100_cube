# from utils import user_decision
from main import play_game
from utils import roll_two_dices

choose_to_pass = 0

def show_messages():
    player_1_score = 0
    player_2_score = 0
    player_1_turn = "this is the turn of player 1"
    player_2_turn = "this is the turn of player 2"
    print(f"the score of player 1: {player_1_score}")
    print(f"the score of player 2: {player_2_score}")

    show_the_user = user_decision()
    return show_the_user

def user_decision():
    # show_messages()
    user_choice = input ("please choose: do you want to roll or pass. \n"
                         "to roll press r,   to pass press p?  ")
    if user_choice == "p":
        choose_to_pass += 1
        play_game()
    elif user_choice == "r":
        roll_two_dices()
        # show_messages()
    else:
        # user_decision()
        ""

    return user_choice