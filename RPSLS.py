import random
from enum import IntEnum

class Choice(IntEnum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2
    LIZARD = 3
    SPOCK = 4

wins={
    Choice.ROCK:[Choice.SCISSOR,Choice.LIZARD],
    Choice.PAPER:[Choice.ROCK,Choice.SPOCK],
    Choice.SCISSOR:[Choice.PAPER,Choice.LIZARD],
    Choice.LIZARD:[Choice.SPOCK,Choice.PAPER],
    Choice.SPOCK:[Choice.ROCK,Choice.SCISSOR]}


def get_user_choice():
    choices=[f'{choice.name}[{choice.value}]' for choice in Choice]
    choices_str = ", ".join(choices)
    user_selection = int(input(f"Enter a choice ({choices_str}): "))
    choice = Choice(user_selection)
    return choice

def get_comp_choice():
    comp_selection=random.randint(0,len(Choice)-1)
    choice= Choice(comp_selection)
    return choice

def get_winner(user_choice,comp_choice):
    loses=wins[user_choice]
    if user_choice == comp_choice:
        print(f' You both think alike. It is {user_choice.name}')
    elif comp_choice in loses:
        print(f' {user_choice.name} beats {comp_choice.name}. You win!!!')
    else:
        print(f' {comp_choice.name} beats {user_choice.name}. You lose!!!')

while True:
    try:
        user_choice=get_user_choice()
    except ValueError as e:
        range_str = f"[0, {len(Choice)-1}]"
        print(f'Invalid selection. Enter value in the range {range_str}')
        continue

    comp_choice=get_comp_choice()
    get_winner(user_choice,comp_choice)
    
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
