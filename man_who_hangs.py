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

previous_guesses = []

round_counter = 7
print("You think you can beat me, stupid human?")
print("The word is {} letters long\n".format(len(guess_word)))
while empty_spaces != 0:
    print(" ".join(empty_spaces_list))
    user_character_guess = input("What letter is your guess?  \n").lower()
    if user_character_guess in previous_guesses:
        print("You already guessed that one!\n")
    elif user_character_guess in guess_word:
        previous_guesses.append(user_character_guess)
        occurance_index = find_occurances(guess_word, user_character_guess)
        empty_spaces = empty_spaces - len(occurance_index)
        for occurance in occurance_index:
            empty_spaces_list[occurance] = user_character_guess
            new_empty_spaces_string = " ".join(empty_spaces_list)
    elif user_character_guess == 'give up':
        print("The word I was using was {}".format(guess_word))
        print("YOU LOSE HUMAN!")
        break
    else:
        previous_guesses.append(user_character_guess)
        print("That letter isn't in my word! \n")

if empty_spaces == 0:
    print(" ".join(empty_spaces_list))
    print("YOU BEAT ME HUMAN!!")
