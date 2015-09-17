with open('words.txt') as infile:
    list_of_words = infile.read().split()


from random import randint


def find_occurences(word, char):
    return [i for i, letter in enumerate(word) if letter == char]


def random_word(word_list):
    random_digit = randint(0,len(word_list))
    return word_list[random_digit]


def not_hang_man():
    word = (random_word(list_of_words)).lower()
    letter_list = list(word)
    words_guessed = []
    print ('your word is {} letters long'.format(len(word)))
    num_of_guesses = 0
    occurance = []
    blank = list('_' * len(word))

    while num_of_guesses < 8:
        guess = (input('\nguess a letter ').lower())
        if guess not in words_guessed:
            words_guessed.append(guess)
            if guess in letter_list:
                occurance = find_occurences(letter_list, guess)
                for position in occurance:
                    blank[position] = letter_list[position]
                print("".join(blank))
                if ''.join(blank) == word:
                    return "Good Jorb Homestar!!"

            else:
                print("".join(blank))
                num_of_guesses+=1

        else:
            print("You already guessed that.")
            print("".join(blank))
    return 'FAILURE! the word was {}'.format(word)

print(not_hang_man)
