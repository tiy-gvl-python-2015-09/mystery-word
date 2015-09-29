import random
import re
import string

with open("/usr/share/dict/words") as infile:
    language = infile.readlines()

random_word_list = list(random_word_string)

eligible_words = []
def generate_word(x):
    for word in x:
        if 4 < len(word) < 10:
            eligible_words.append(word)
    random_word_string = random.choice(eligible_words)
    return random_word_string
    print(random_word_string)
    pass


def listify_random_word(random_word_string):
    random_word_list = list(random_word_string)
    return random_word_list
    pass

def start_up():
    failed_attempts = 0
    blank_word_string = "_"*len(random_word_string)
    for x in blank_word_string:
        print(x, end=" ")
    blank_word_list = list(blank_word_string)

    print("Failed attempts: " + str(failed_attempts))
    return blank_word_list


def get_player_guess():
    guess = input("Please guess a letter: ")
    if not guess.isalpha():
        print("Sorry, that is not a letter")
    if len(guess) != 1:
        print("Only one letter, wise guy")
    return guess
#Why is guess not defined in the next function?


def test_guess_vs_word(a):
    a = get_player_guess()
    for xyz in random_word_list:
        if xyz == a:
            blank_word_list[random_word_list.index(a)] = a
    print(str(blank_word_list))
    return blank_word_list

    if a not in random_word_list:
        failed_attempts += 1
        print("Sorry, that letter is not in my word")
        print(str(blank_word_list))
        print("Incorrect guesses left: " + str(8 - failed_attempts))
    return failed_attempts

#To run the program:
generate_word(language)
listify_random_word(random_word_string)
start_up()
blank_word_list = start_up()
failed_attempts = 0
while failed_attempts < 7:
    test_guess_vs_word(get_player_guess)
