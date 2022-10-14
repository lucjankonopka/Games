import random
import string

with open('sowpods.txt', 'r') as output:
    words = output.readlines()

chosen_word = ''
display = []
guesses = 6
user_guesses = set()
letter_list = list(string.ascii_lowercase[0:26])
text_width = 50


def display_the_word(user_guess, chosen_word):
    print('The word to guess:')
    if len(user_guesses) > 0:
        adding_correct_letters(user_guess, chosen_word)
    return ' '.join(display)


def input_check(user_guess):
    if len(user_guess) > 1:
        print('Wrong input! Please choose just one letter!')
        print('-'*text_width)
        return False
    if user_guess.lower() not in letter_list:
        print('Wrong input! Only letters will be accepted!')
        print('-'*text_width)
        return False
    else:
        return True


def adding_correct_letters(user_guess, chosen_word):
    i = 0
    while i < len(chosen_word):
        if chosen_word[i] == user_guess:
            display[i] = user_guess
        i += 1


def win_check(chosen_word):
    chosen_word_set = {el for el in chosen_word}
    user_guesses_correct = {el for el in user_guesses if el in chosen_word}
    if sorted(chosen_word_set) == sorted(user_guesses_correct):
        print('-'*text_width)
        print(('You won!').center(text_width))
        print((('The word was "{}"').format(chosen_word)).center(text_width))
        print('-'*text_width)
        return False
    else:
        True
    print('-'*text_width)


def game_status(chosen_word):
    if guesses == 0:
        print('-'*text_width)
        print(('You lost!').center(text_width))
        print((('The word was "{}"').format(chosen_word)).center(text_width))
    elif guesses == 1:
        print('You have 1 guess left!')
    else:
        print(('You have {} guesses left!').format(guesses))
    print('-'*text_width)


hangman_graph = [' ', '_', '_', '_', '_', ' \n',
                 ' ', '|', '/', ' ', '|', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 ' ', '|', ' ', ' ', ' ', ' \n',
                 '/', ' ', '\\', ' ', ' ', ' \n']


def draw_hangman():
    print(''.join(hangman_graph))


def change_hangman_graph():
    if guesses == 5:
        hangman_graph[16] = 'O'
    if guesses == 4:
        hangman_graph[22] = '|'
    if guesses == 3:
        hangman_graph[21] = '/'
    if guesses == 2:
        hangman_graph[23] = '\\\n'
    if guesses == 1:
        hangman_graph[27] = '/'
    if guesses == 0:
        hangman_graph[29] = '\\\n'
    draw_hangman()


def hangman_game():

    global guesses, display, chosen_word, user_guesses

    while True:
        chosen_word = words[random.randint(0, len(words))].strip()
        for el in chosen_word:
            display.append('_')
        break

    # print(chosen_word)

    print('-'*text_width)
    print(('Welcome to Hangman!').center(text_width))
    print(('Have fun :)').center(text_width))
    print('-'*text_width)

    user_guess = ''
    while True:
        if guesses == 0:
            break
        print(display_the_word(user_guess, chosen_word))
        print()
        user_guess = (input("""Guess your letter:
>>>: """)).lower()
        if input_check(user_guess) == False:
            continue
        if user_guess in chosen_word:
            if user_guess in user_guesses:
                print('You\'ve already chosen this letter!')
            else:
                user_guesses.add(user_guess)
                if win_check(chosen_word) == False:
                    break
                print('Correct! The words contains your letter!')
        else:
            if user_guess in user_guesses:
                print('You\'ve already chosen this letter!')
            else:
                print('Incorrect!')
                user_guesses.add(user_guess)
                guesses -= 1
                change_hangman_graph()
        game_status(chosen_word)

    chosen_word = ''
    display = []
    guesses = 6
    user_guesses = set()
