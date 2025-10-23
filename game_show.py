from utils import user_decision

player_1_score = 0
player_2_score = 0
player_1_turn = "this is the turn of player 1"
player_2_turn = "this is the turn of player 2"

def show_messages():
    print(f"the score of player 1 {player_1_score}")
    print(f"the score of player 2 {player_2_score}")
    print(player_1_turn)
    print(player_2_turn)
    show_the_user = user_decision()
    return show_the_user