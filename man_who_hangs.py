# This will be my version of Hang-Man
from random import randint

with open("/usr/share/dict/words") as infile:
    available_words = infile.read()


def find_occurances(a_string, char):
    return [i for i, letter in enumerate(a_string)if letter == char]


word_list = available_words.split()

how_many_words = len(word_list)

guess_number = randint(0, how_many_words)

guess_word = word_list[guess_number]

guess_word = guess_word.lower()

empty_spaces = len(guess_word)

empty_spaces_string = empty_spaces * "_ "

empty_spaces_list = empty_spaces_string.split()

while empty_spaces != 0:
    previous_guesses = []
    print(empty_spaces_string))
    user_character_guess = input("What letter is your guess?  ").lower()
    previous_guesses.append(user_character_guess)
    if user_character_guess in previous_guesses:
        print("You already guessed that one!")
    if user_character_guess in guess_word:
        occurance_index = find_occurances(guess_word, user_character_guess)
        for occurance in occurance_index:
            empty_spaces_list[x] = user_character_guess
            new_empty_spaces_string = " ".join(empty_spaces_list)
