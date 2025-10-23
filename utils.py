import random

from game_show import show_messages


def roll_two_dices() -> tuple [int, int]:
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    tuple_of_numbers = (dice_1, dice_2)

    return tuple_of_numbers


def past_100 (sum_points):
    if sum_points > 100:
        return True
    else:
        return False

def exact_100 (sum_points):
    if sum_points == 100:
        return ("winner")

def who_closer_to_100(player_1_score : int, player_2_score : int):
    if player_1_score > player_2_score:
        return "player 1 is the winner"
    elif player_2_score > player_1_score:
        return "player 2 is the winner"
    elif player_1_score == player_2_score:
        return None

def tie_breaker(player_1, player_2):
    if player_1 == player_2:
        breaker_turn = roll_two_dices()

def user_decision():
    show_messages()
    user_choice = input ("please choose: do you want to roll or pass. \n"
                         "to roll press r,   to pass press p")
    if user_choice == "p":
        pass
    elif user_choice == "r":
        roll_two_dices()
        show_messages()
    else:
        user_decision()

    return user_choice





