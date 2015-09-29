import random
import string
import re

with open("/usr/share/dict/words") as infile:
    language = infile.readlines()

active_words = []

def generate_word():
    for xyz in language:
        if 4 < len(xyz) < 8:
            active_words.append(xyz)

generate_word()
chosen_word = (random.choice(active_words)).upper()

blank = ["_", "_", "_", "_", "_",
 "_", "_", "_", "_", "_",
  "_", "_", "_", "_", "_"]
blank_letters = blank[1:len(chosen_word)]

print(chosen_word)
print(str(blank_letters))

failed_attempts = 0
while failed_attempts < 8:

    guess = list(input("Please guess a letter: ").upper())
    for [xyz] in chosen_word:
        if chosen_word[xyz] == guess:
            blank_letters = guess
            print("Yes! There's your %s!")(guess)
            print(str(blank_letters))

    if guess not in chosen_word:
        failed_attempts +=1
        print("Sorry, that character is not in my word.")
        print(str("You have" + 8 - failed_attempts + "incorrect guesses left.")


if failed_attempts > 7:
    print("GAME OVER.")
