import random
import string
import re

with open("/usr/share/dict/words") as infile:
    language = infile.readlines()

active_words = []
random_number = random.randint(4,10)

def generate_word():
    for xyz in language:
        if len(xyz) == random_number:
            active_words.append(xyz)

generate_word()
chosen_word = (random.choice(active_words)).upper()


blank_letters = ["_ "]
i = 0
while i < len(chosen_word):
    blank_letters = blank_letters.insert(0, "_ ")
    i += 1
return blank_letters

print(chosen_word)
print(random_number)
print(str(blank_letters))

guess = input("Please guess a letter: ").upper()

if(guess not in chosen_word):
    print("Sorry, that character is not in my word.")
    print("You have {} incorrect guesses left.")
else:
    for jkl in chosen_word:
        if blank_letters[jkl] == guess:
            [jkl] = guess

print(blank_letters)
print(find_letter_in_word( guess, chosen_word))
