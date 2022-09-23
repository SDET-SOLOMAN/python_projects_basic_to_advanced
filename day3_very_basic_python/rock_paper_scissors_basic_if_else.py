from random import randint

player_win = 0
comp_win = 0

while player_win < 2 or comp_win < 2:

    print("Rock ... ")
    print("Paper ... ")
    print("Scissors ... ")

    computer = ['rock', 'paper', 'scissors']
    computer = computer[randint(0, 2)]

    user_choice = input('Make your choose, rock, paper, or scissors? ')

    while user_choice.lower() != 'rock' and user_choice.lower() != 'paper' and user_choice.lower() != 'scissors':
        user_choice = input('Make your choose, rock, paper, or scissors? ')

    user_wins = f'User win, user picked {user_choice} and comp picked {computer}'
    comp_wins = f'COMP win, user picked {user_choice} and comp picked {computer}'

    if user_choice == computer:
        print(f"It's A Draw, user {user_choice} and comp {computer}")
    elif user_choice == 'rock' and computer == 'scissors':
        player_win += 1
        print(user_wins)
    elif user_choice == 'paper' and computer == 'rock':
        player_win += 1
        print(user_wins)
    elif user_choice == 'scissors' and computer == 'paper':
        player_win += 1
        print(user_wins)
    else:
        comp_win += 1
        print(comp_wins)
