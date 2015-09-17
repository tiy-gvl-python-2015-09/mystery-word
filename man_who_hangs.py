# This will be my version of Hang-Man
from random import randint

with open("/usr/share/dict/words") as infile:
    available_words = infile.read()

word_list = available_words.split('\n')

how_many_words = len(word_list)

guess_number = randint(0, how_many_words)
guess_word = word_list[guess_number]

empty_spaces = len(guess_word)
