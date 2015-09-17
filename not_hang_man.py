def find_occurences(word, char):
    return [i for i, letter in enumerate(word) if letter == char]

def not_hang_man():
    word = 'stranger'
    letter_list = list(word)
    words_guessed = []
    print ('your word is {} letters long'.format(len(word)))
    num_of_guesses = 0
    occurance = []
    blank = list('_' * len(word))

    while num_of_guesses < 8:
        guess = (input('guess a letter ').lower())
        print("You're guess is {}".format(guess))
        if guess not in words_guessed:
            words_guessed.append(guess)
            if guess in letter_list:
                occurance = find_occurences(letter_list, guess)
                for position in occurance:
                    blank[position] = letter_list[position]
                    print("".join(blank))
                    if blank == word):
                        return "Good Jorb!!"

            else:
                print("".join(blank))
                num_of_guesses+=1

        else:
            print("".join(blank))
            print("You already guessed that.")
            print("".join(blank))
    return 'FAILURE!'
