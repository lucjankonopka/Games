import random

text_width = 50

def computer_selection():
    computer_selection_list = ['rock', 'paper', 'scissors']
    computer_random_selection = random.choice(computer_selection_list)
    return computer_random_selection


def user_selection():
    user_ipnut = (input('Rock "r", Paper "p" or Scissors "s"?: ')).lower()
    if user_ipnut == 'r' or user_ipnut == 'rock':
        return 'rock'
    elif user_ipnut == 'p' or user_ipnut == 'paper':
        return 'paper'
    elif user_ipnut == 's' or user_ipnut == 'scissors':
        return 'scissors'
    else:
        print('Wrong input! Try again!')


def win_check(user_choice, computer_choice):
    if user_choice == 'rock' and computer_choice == 'rock' or user_choice == 'paper' and computer_choice == 'paper' or user_choice == 'scissors' and computer_choice == 'scissors':
        print(('It\'s a tie!').center(text_width))
    elif user_choice == 'rock' and computer_choice == 'scissors' or user_choice == 'paper' and computer_choice == 'rock' or user_choice == 'scissors' and computer_choice == 'paper':
        print(('You won!').center(text_width))
    else:
        print(('You lost!').center(text_width))


def rock_paper_scissors_game():
    print('-'*text_width)
    print(('Welcome to Rock, Paper, Scissors!').center(text_width))
    print('Have fun :)'.center(text_width))
    print('-'*text_width)
    user_choice = user_selection()
    computer_choice = computer_selection()
    print('')
    print('-'*text_width)
    print((f'You\'ve chosen {user_choice}, computer has chosen {computer_choice}.').center(50))
    win_check(user_choice, computer_choice)
    print('-'*text_width)
