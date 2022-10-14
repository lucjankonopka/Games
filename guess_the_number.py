import random

text_width = 50
number = random.randint(1,100)

def guess_the_number_game():
    print('-'*text_width)
    print(('Welcome to Guess The Number!').center(text_width))
    print(('Try to guess the number between 1 and 100.').center(text_width))
    print(('You have 10 guesses! Have fun :)').center(text_width))
    print('-'*text_width)
    attempts = 10
    while True:
        if attempts == 0:
            print('-'*text_width)
            print((f'The number was {number}!').center(text_width))
            print(('You lost! :(').center(text_width))
            print('-'*text_width)
            break

        user_guess = int(input("Enter the number: "))

        if user_guess == number:
            print('-'*text_width)
            print((f'The number was {number}!').center(text_width))
            print(('You won! Congratz!').center(text_width))
            print('-'*text_width)
            break
        elif user_guess > number:
            print(('{} is too high! Try a lower number.').format(user_guess))
            attempts -= 1
            continue
        elif user_guess < number:
            print(('{} is too low! Try a higher number.').format(user_guess))
            attempts -= 1
            continue
