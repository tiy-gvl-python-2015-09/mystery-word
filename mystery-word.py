
from random import choice
import string

with open ("/usr/share/dict/words") as infile:
    text = infile.read()
    text = str(text).lower().split()

def generate_random_word(data):
    random_word = choice(data)
    return random_word

def tell_word_length(word):
    return "Welcome! The word has {} letters. You have eight guesses.".format(len(word))

word = generate_random_word(text)



print(tell_word_length(word))

userguess = str(input("Pick a letter, any letter: ").lower())

correct_guess = 0
guesses_left = 8

# Choose whether to show word
#print(word)

word = list(word)
blank_word = []
counter = 0
guesses = 0
guess_list = []

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)


while counter < len(word):
    for x in word:
        if x != userguess:
            blank_word.append("_")
            counter += 1
        if x == userguess:
            blank_word.append(userguess)
            counter += 1
    if userguess not in word:
        guesses += 1
        guesses_left = 8 - guesses
        print("Sorry, {} is not in the word. You have {} guesses left.\r".format(userguess.upper(), guesses_left))
        print(blank_word)

    if  userguess in word:
        print(blank_word)

while guesses < 8:
    userguess = input("Pick a letter, any letter: ")
    #if userguess in guess_list:
       # print("You already selected {}, please guess again.".format(userguess.upper())
    if userguess not in word:
        guesses += 1
        guesses = int(guesses)
        guesses_left = 8 - guesses
        print("Sorry, {} is not in the word. You have {} guesses left.\r".format(userguess.upper(), guesses_left))
        print(blank_word)
        continue
        #if userguess in word:
            #if userguess in blank_word:
                #print("You already guessed {}.".format(userguess))
    else:
        for x in word:
            if x == userguess:
                word = ("").join(word)
                location_list = list(find_all(word, userguess))
                for x in location_list:
                    blank_word.insert(x, userguess)
                    del blank_word[x + 1]
                word = list(word)
        print(blank_word)
        if "_" not in blank_word:
            word = ("").join(word)
            guesses_left = 8 - guesses
            print("Congratulations! You guessed the word {} with {} guesses left.\r".format(word, guesses_left))
            break
if guesses == 8:
    word = ''.join(word)
    print("Sorry, better luck next time. The word was {}.".format(word))



    
