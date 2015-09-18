import random

with open("/usr/share/dict/words") as infile:
   available_words = infile.read().split()


def create_guessed_word(random_word): #creates guessed word same length as random word
    guessed_word_as_list = []
    count = 0
    while count < len(random_word):
        guessed_word_as_list.append("_")
        count += 1
    return guessed_word_as_list


def player_turn(word_as_list, guessed_word_show): #loops through the player turn with appropriate response
        count = 0
        guessed_letters = []
        while count < 8 and word_as_list != guessed_word_show:
            player_letter = input("Please guess a letter: ").upper()
            if len(player_letter) > 1:
                print("That's more than one letter. No cheating!")
            elif player_letter in guessed_letters:
                print("You've already guessed that letter.")
            else:
                guessed_letters.append(player_letter)
                if player_letter in word_as_list:
                        print("Congrats! You guessed a correct letter!")
                        for i, l in enumerate(word_as_list):
                            if l == player_letter:
                                guessed_word_show[i] = l
                        if guessed_word_show == word_as_list:
                            print("You win! Your word was {}.".format("".join(word_as_list)))
                        else:
                            print(" ".join(guessed_word_show))
                            print("You still have {} guesses left.".format(8 - count))
                else:
                    print("Sorry! That's a wrong guess.")
                    count += 1
                    print("You have {} guess(es) left.".format(8 - count))
        if count >= 8:
            print("Welp, it looks like the man got hanged!")
            print("Your word was {}.".format("".join(word_as_list)))


def hanging_man():
    #generate random word using random.choice, see above, call it game_word

    game_word = random.choice(available_words)
    list_of_gw = list(game_word.upper())
    show_word = create_guessed_word(game_word)

    print("Welcome to the Hanging Man game!")
    print("Your word to guess is {} letters long.".format(len(game_word)))
    print("You will have 8 guesses to get the word.")
    player_turn(list_of_gw, show_word)


hanging_man()
