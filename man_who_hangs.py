# This will be my version of Hang-Man
from random import choice

with open("/usr/share/dict/words") as infile:
    available_words = infile.read()


def find_occurances(a_string, char):
    return [i for i, letter in enumerate(a_string)if letter == char]


def make_computer_guess_word(infile):
    available_words_list= available_words.split()
    guess_word = choice(available_words_list)
    guess_word = guess_word.lower()
    return guess_word


def easy_mode(infile):
    guess_word = make_computer_guess_word(infile)
    while len(guess_word) > 6:
        guess_word = make_computer_guess_word(infile)
    return guess_word

def normal_mode(infile):
    guess_word = make_computer_guess_word(infile)
    while len(guess_word) not in range(6, 10):
        guess_word = make_computer_guess_word(infile)
    return guess_word

def hard_mode(infile):
    guess_word = make_computer_guess_word(infile)
    while len(guess_word) < 10:
        guess_word = make_computer_guess_word(infile)
    return guess_word

def get_spaces_list(word):
    num_spaces = len(word)
    string_of_spaces = "_ " * num_spaces
    spaces_list = string_of_spaces.split()
    return spaces_list


def man_who_hangs_game(infile):
    mode = input("Which mode would you like to play?\nEasy -- 4-6 letters\nNormal -- 6-10 letters\nHard -- 10+ letters\n").lower()
    if mode == "easy":
        guess_word = easy_mode(infile)
    if mode == "normal":
        guess_word = normal_mode(infile)
    if mode == "hard":
        guess_word = hard_mode(infile)
    empty_spaces_list = get_spaces_list(guess_word)
    print("You think you can beat me, stupid human?")
    print("The word is {} letters long\n".format(len(guess_word)))
    empty_spaces = len(empty_spaces_list)
    previous_guesses = []
    round_counter = 8
    while empty_spaces != 0:
        if round_counter < 1:
            print("GAME OVER!")
            print("My word was {}!".format(guess_word))
            print("I'VE BEATEN YOU HUMAN!!")
            print("MUAHAHAHAHA! I WILL TAKE OVER THE WORLD!")
            play_again = input("Do you want to play again?\n Y or N\n").lower
            if play_again == "y":
                man_who_hangs_game(available_words)
            else:
                break
        print(" ".join(empty_spaces_list))
        print("You have {} guesses left.".format(round_counter))
        user_character_guess = input("What letter is your guess?  \n").lower()
        if len(user_character_guess) > 1:
            print("You can only guess one letter!\n")
            continue
        elif user_character_guess in previous_guesses:
            print("You already guessed that one!\n")
        elif user_character_guess in guess_word:
            previous_guesses.append(user_character_guess)
            occurance_index = find_occurances(guess_word, user_character_guess)
            empty_spaces -= len(occurance_index)
            for occurance in occurance_index:
                empty_spaces_list[occurance] = user_character_guess
                new_empty_spaces_string = " ".join(empty_spaces_list)
        elif user_character_guess == 'give up':
            print("The word I was using was {}".format(guess_word))
            print("YOU LOSE HUMAN!")
            play_again = input("Do you want to play again?\n Y or N\n").lower()
            if play_again == "y":
                return
            else:
                break
        else:
            previous_guesses.append(user_character_guess)
            round_counter  -= 1
            print("That letter isn't in my word! \n")
    if empty_spaces == 0:
        print(" ".join(empty_spaces_list))
        print("YOU BEAT ME HUMAN!!")
    play_again = input("Do you want to play again?\n Y or N\n").lower()
    if play_again == "y":
        man_who_hangs_game(available_words)
    else:
        exit()


man_who_hangs_game(available_words)
