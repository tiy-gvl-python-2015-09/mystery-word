#To play, enter play_hangman(text)

from random import choice
import string

with open ("/usr/share/dict/words") as infile:
    text = infile.read()
    text = str(text).lower().split()

def play_hangman(list_words):
    word = choice(list_words)
    
    #print(word)

    print("Welcome! The word has {} letters. You have eight guesses.".format(len(word)))

    userguess = str(input("Pick a letter, any letter: ").lower())

    word = list(word)
    counter = 0
    guesses = 0
    correct_guess = 0
    guesses_left = 8
    guess_list = []
    blank_word = []

    def find_all(a_str, sub):
        start = 0
        while True:
            start = a_str.find(sub, start)
            if start == -1: return
            yield start
            start += len(sub)

#first guess and creating blank spaces
    while counter < len(word):
        guess_list.append(userguess)
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

        if userguess in word:
            print(blank_word)
            
#all other guesses
    while guesses < 8:
        userguess = input("Pick a letter, any letter: ")
        if userguess in guess_list:
            print("You already guessed {}, please guess again.".format(userguess.upper()))
            continue
        guess_list.append(userguess)
        if userguess not in word:
            guesses += 1
            guesses = int(guesses)
            guesses_left = 8 - guesses
            print("Sorry, {} is not in the word. You have {} guesses left.\r".format(userguess.upper(), guesses_left))
            print(blank_word)
            
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