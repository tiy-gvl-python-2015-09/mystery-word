# This will be my version of Hang-Man
from random import choice

# This allows easy access to the MacBook spell check dictionary
with open("/usr/share/dict/words") as infile:
    available_words = infile.read()



# This is a helper function that will allow us to see if the player's guess letter
# later on in the game.
def find_occurances(a_string, char):
    return [i for i, letter in enumerate(a_string)if letter == char]


# This is a basic function that has the computer choose a random word from our
# list of available words.
def make_computer_guess_word(infile):
    available_words_list= available_words.split()
    guess_word = choice(available_words_list)
    guess_word = guess_word.lower()
    return guess_word


# The following 3 functions allow the player to choose their difficulty level,
# which determines how long the word is.  Difficulty is based solely on length.
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


# This function gives us a list of underscores with the same length as the guess word.
# Very helpful for giving the user a visual of the word in the command line.
def get_spaces_list(word):
    num_spaces = len(word)
    string_of_spaces = "_ " * num_spaces
    spaces_list = string_of_spaces.split()
    return spaces_list


def man_who_hangs_game(infile):
    # Simple prompt asking the user for the desired difficulty level.
    mode = input("Which mode would you like to play?\nEasy -- 4-6 letters\nNormal -- 6-10 letters\nHard -- 10+ letters\n").lower()
    if mode == "easy":
        guess_word = easy_mode(infile)
    if mode == "normal":
        guess_word = normal_mode(infile)
    if mode == "hard":
        guess_word = hard_mode(infile)

    # Below, we set up our game environment.  Our list of underscores is preparred,
    # then the user sees how long the word is.  Finally, we set our two main variables,
    # empty_spaces and round_counter, which determine when the game ends.  8 rounds
    # for 8 guesses, or if there are 0 empty spaces left, the game ends.  Whichever is first.
    empty_spaces_list = get_spaces_list(guess_word)
    print("You think you can beat me, stupid human?")
    print("The word is {} letters long\n".format(len(guess_word)))
    empty_spaces = len(empty_spaces_list)
    previous_guesses = []
    round_counter = 8

    # Below here is the actual game play.
    while empty_spaces != 0:
        # Once the user has made 8 incorrect guesses, the game automatically ends.
        if round_counter < 1:
            print("GAME OVER!")
            print("My word was {}!".format(guess_word))
            print("I'VE BEATEN YOU HUMAN!!")
            print("MUAHAHAHAHA! I WILL TAKE OVER THE WORLD!")
            break
        # We print our list of underscores, then tell the user how many guesses
        # they have left, and finally we ask the user for their input.
        print(" ".join(empty_spaces_list))
        print("You have {} guesses left.".format(round_counter))
        user_character_guess = input("What letter is your guess?  \n").lower()
        # Now we determine what happens with the user's guessed letter.
        # If they try more than one letter, we start the round over again. The same
        # happens if they try to guess the same letter for a second time.  If
        # the user's guess is in the word the computer picked, we use our helper function
        # from earlier to find the number and index of the occurances.  Those occurances
        # replace the underscores from our underscore list, in the correct position, our
        # empty spaces variable is updated, and the user's guess is logged to prevent losing
        # a round for a duplicate guess.  Finally, if the user's guess was not in the computer's
        # guess word, the user loses a round and the guess is logged.  The round now ends with any
        # of these scenarios, but the user only loses a round if they guess incorrectly.
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
        else:
            previous_guesses.append(user_character_guess)
            round_counter  -= 1
            print("That letter isn't in my word! \n")
    # The final step in the round is to check to see if the user has guessed the word
    # correctly.  if there are no more empty spaces, the user must have filled them
    # with correct guesses.  The game is now over.
    if empty_spaces == 0:
        print(" ".join(empty_spaces_list))
        print("YOU BEAT ME HUMAN!!")


# We are now actually calling the game to play.  The start variable is so that the user
# can play multiple games in a row.  We call the game initially, the game is played, then
# the user is asked if they want to play again.  If they do want to play more, start remains
# the same, continuing the loop.  If they do not want to play, the start variable is adjusted
# and the loop ends, closing the program.
start = 1
while start == 1:
    man_who_hangs_game(available_words)
    play_again = input("Do you want to play again?\n Y or N\n").lower()
    if play_again == "y":
        start = 1
    else:
        start = 2
