import random

game = True
counter = 0
text_width = 50


def no_duplicates(random_number):
    if (random_number[0] != random_number[1] and
            random_number[0] != random_number[2] and
            random_number[0] != random_number[3] and
            random_number[1] != random_number[2] and
            random_number[1] != random_number[3] and
            random_number[2] != random_number[3]
        ):
        return True
    else:
        return False


def compare_numbers(random_number, user_guess):
    cow = 0
    bull = 0
    for i in range(len(random_number)):
        if user_guess[i] == random_number[i]:
            cow += 1
        elif user_guess[i] in random_number:
            bull += 1

    if cow <= 1 and bull <= 1:
        print(('{} cow, {} bull').format(cow, bull))
    elif cow <= 1 and bull > 1:
        print(('{} cow, {} bulls').format(cow, bull))
    elif cow > 1 and bull <= 1:
        print(('{} cows, {} bull').format(cow, bull))
    elif cow > 1 and bull > 1:
        print(('{} cows, {} bulls').format(cow, bull))
    return game_status(cow)


def game_status(cow):
    if cow == 4:
        print('-'*text_width)
        print(('Congratz!').format(counter).center(text_width))
        if counter == 1:
            print(('You\'ve picked the right number after first guess!').format(
                counter).center(text_width))
        else:
            print(('You\'ve picked the right number after {} guesses!').format(
                counter).center(text_width))
        print('-'*text_width)
        return False
    else:
        return True


def cows_and_bulls_game():

    global counter

    print('-'*text_width)
    print(('Welcome to the Cows and Bulls Game!').center(text_width))
    print(('Guess the number from 1000 to 9999!').center(text_width))
    print(('The number cannot have duplicate digits!').center(text_width))
    print('-'*text_width)
    print("""
Quick instruction:
If the correct number were 1234
And your guess would be 1983
You would get the following hint: 
1 cow, 1 bull
cow - describes the correct digit in the correct position (here digit '1')
bull - describes the correct digit in the wrong position (here digit '3')

Have fun!""")
    print('-'*text_width)

    while True:
        random_number = str(random.randint(1000, 9999))
        if no_duplicates(random_number) == True:
            break
        else:
            continue
    

    while True:

        # print(random_number)

        user_guess = input("""Your guess:
>>> """)
        counter += 1
        if user_guess == 'end' or user_guess == 'exit':
            print('Game left by the user!')
            break
        elif int(user_guess) > 9999:
            print(('Number too long! End of the game! The number was {}').format(
                random_number))
            break
        elif int(user_guess) < 1000:
            print(('Number too short! End of the game! The number was {}').format(
                random_number))
            break
        elif (user_guess[0] == user_guess[1] or
              user_guess[0] == user_guess[2] or
              user_guess[0] == user_guess[3] or
              user_guess[1] == user_guess[2] or
              user_guess[1] == user_guess[3] or
              user_guess[2] == user_guess[3]
              ):
            print('The number you\'ve chosen is has duplicates! Try again!')
            continue
        elif compare_numbers(random_number, user_guess) == False:
            break

