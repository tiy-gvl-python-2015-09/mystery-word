# This will be my version of Hang-Man
from random import randint

with open("/usr/share/dict/words") as infile:
    available_words = infile.read()


def find_occurances(a_string, char):
    return [i for i, letter in enumerate(a_string)if letter == char]


def make_computer_guess_word(infile):
    available_words_list= available_words.split()
    upper_index_limit = len(available_words_list)
    random_num = randint(0, upper_index_limit)
    guess_word = available_words_list[random_num]
    guess_word = guess_word.lower()
    return guess_word


def get_spaces_list(word):
    num_spaces = len(word)
    string_of_spaces = "_ " * num_spaces
    spaces_list = string_of_spaces.split()
    return spaces_list


def man_who_hangs_game(spaces, guess_word):
    print("You think you can beat me, stupid human?")
    print("The word is {} letters long\n".format(len(guess_word)))
    empty_spaces = len(spaces)
    previous_guesses = []
    round_counter = 9
    while empty_spaces != 0:
        print(" ".join(spaces))
        print("You have {} guesses left.".format(round_counter))
        user_character_guess = input("What letter is your guess?  \n").lower()
        if user_character_guess in previous_guesses:
            print("You already guessed that one!\n")
        elif user_character_guess in guess_word:
            previous_guesses.append(user_character_guess)
            occurance_index = find_occurances(guess_word, user_character_guess)
            empty_spaces = empty_spaces - len(occurance_index)
            for occurance in occurance_index:
                spaces[occurance] = user_character_guess
                new_empty_spaces_string = " ".join(spaces)
        elif user_character_guess == 'give up':
            print("The word I was using was {}".format(guess_word))
            print("YOU LOSE HUMAN!")
            break
        elif round_counter == 1:
            print("GAME OVER!")
            print("My word was {}!".format(guess_word))
            print("I'VE BEATEN YOU HUMAN!!")
            print("MUAHAHAHAHA! I WILL TAKE OVER THE WORLD!")
            break
        else:
            previous_guesses.append(user_character_guess)
            round_counter = round_counter - 1
            print("That letter isn't in my word! \n")
    if empty_spaces == 0:
        print(" ".join(spaces))
        print("YOU BEAT ME HUMAN!!")

guess_word = make_computer_guess_word(available_words)

empty_spaces_list = get_spaces_list(guess_word)




man_who_hangs_game(empty_spaces_list, guess_word)
