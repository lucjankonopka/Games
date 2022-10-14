from guess_the_number import guess_the_number_game
from rock_paper_scissors import rock_paper_scissors_game
from hangman import hangman_game
from cows_and_bulls import cows_and_bulls_game

text_width = 50

print("""

>>>Welcome to the Mini Game Library!<<<
    """)
user_nickname = input("Enter your nickname: ")
print('~'*text_width)
print(('Hello {}!').format(user_nickname).center(text_width))
print('~'*text_width)

while True:
    init_txt = ("""
Below you can find a list of the games for you.
Enjoy!

1. Guess The Number
2. Rock, Paper & Scissors
3. Hangman
4. Cows & Bulls

Press the number to select the game or 'q' to quit: """)

    user_choice = input(init_txt)

    if user_choice == '1':
      guess_the_number_game()
      continue
    elif user_choice == '2':
      rock_paper_scissors_game()
      continue
    elif user_choice == '3':
      game = hangman_game()
      continue
    elif user_choice == '4':
      cows_and_bulls_game()
      continue
    elif user_choice == 'q' or 'Q':
      break
