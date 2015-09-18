from random import choice
import string

with open ("/usr/share/dict/words") as infile:
    text = infile.read()
    text = str(text).lower().split()

def generate_random_word(data):
    random_word = choice(data)
    return random_word

game_word = generate_random_word(text)
print(game_word)

def tell_word_length(word):
    return "Welcome! The word has {} letters. You have eight guesses.".format(len(word))

print(tell_word_length(game_word))

guess_count = 0
correct_guess = 0

for guess_count in range(0,100):
    user_guess = str(input("Pick a letter, any letter: ").lower())
    if user_guess.isalpha() == False:
        print("Please choose a letter.")
        continue
    if user_guess in game_word:
        correct_guess += 1
        print("The word contains {}!".format(user_guess))
        print("You have {} guesses remaining.".format(guesses_left))
        if correct_guess == len(game_word):
            print("Congratulations, you win! The word was {}.".format(game_word))
            break
        continue
    else:
        guess_count += 1
        guesses_left = 8 - int(guess_count)
        print("The word does not contain {}. Muahaha.".format(user_guess))
        if guess_count < 8:
            print("You have {} guesses remaining.".format(guesses_left))
            continue
        if guess_count ==8:
            print("Sorry, out of guesses :(. Better luck next time.")
            break
        
