from game_show import show_messages

def play_game():

    def player_turn():
        turn = "player_1"
        if turn == "player_1":
            print("this is the turn of player 1")
            start = show_messages()
            start()
            turn = "player_2"
        else:
            print("this is the turn of player 2")
            start = show_messages()
            start()
            turn = "player_1"

        return turn

    player_turn()

play_game()



