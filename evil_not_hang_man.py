with open('/usr/share/dict/words') as infile:
    list_of_words = infile.read().split()


from string import ascii_lowercase
from random import randint


letter_value = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
                'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 9, 'r': 1,
                's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}


def find_occurences(word, char):
    return [i for i, letter in enumerate(word) if letter == char]


def play_again():
    response = input("Do you want to run this program again? Y/N ").lower()
    if response == 'y':
        print("\n Another word coming your way!")
        not_hang_man()
    elif response == 'n':
        return"Bye."
    else:
        print ("{} is not an option!".format(response))
        play_again()


def random_word(word_list):
    random_digit = randint(0,len(word_list))
    return word_list[random_digit]


def word_value(word):
    value = 0
    for letter in letter_value:
        if letter in word:
            value += letter_value[letter]
    return value


def value_dictionary(word_list):
    word_value_dict = {}
    for word in word_list:
        value = word_value(word)
        word_value_dict[word] = value
    return word_value_dict
dictionary_of_value = value_dictionary(list_of_words)


def highest_value(dictionary):
    largest_value = 0
    for word in dictionary:
        if dictionary_of_value[word] > largest_value:
            largest_value = dictionary_of_value[word]
    return largest_value


def difficulty_level():
    difficulty = input("easy, medium or hard game? ".lower())
    word_list = value_dictionary(list_of_words)
    numerator = highest_value(word_list)
    easy = []
    medium = []
    hard = []
    for word in word_list:
        if word_list[word] < (numerator * (1/3)):
            easy.append(word)
        if word_list[word] < (numerator * (2/3)) and word_list[word] >= (numerator * (1/3)):
            medium.append(word)
        if word_list[word] <= numerator and word_list[word] >= (numerator * (2/3)):
            hard.append(word)
    if difficulty == 'easy':
        return easy
    elif difficulty == 'medium':
        return medium
    elif difficulty == 'hard':
        return hard
    else:
        print ("{} is not an option!".format(difficulty))
        return difficulty_level()


def azubu_frost(word_list):
    wordpool = []
    random_word_length = len(random_word(word_list))
    for word in list_of_words:
        if len(word) == random_word_length:
            wordpool.append(word.lower())
    return wordpool


def conami_code(letter, word_list):
    random_words = word_list
    new_word_pool = []
    letter_position = {}
    positions = []
    most_occurances = []
    largest_number_of_occurances = 0
    word_pool_redux = []
    for word in random_words:
        if letter in word:
            new_word_pool.append(word)
    for word in new_word_pool:
        positions.append(tuple(find_occurences(word, letter)))
    for marker in positions:
        if marker not in letter_position:
            letter_position[marker] = 1
        else:
            letter_position[marker] += 1
    for position in letter_position:
        if letter_position[position] > largest_number_of_occurances:
            most_occurances = position
            largest_number_of_occurances = letter_position[position]
    for word in new_word_pool:
        for spot in most_occurances:
            if word[spot] is letter:
                word_pool_redux.append(word)
    return word_pool_redux, most_occurances


def not_hang_man():
    word = azubu_frost(difficulty_level())
    letters_guessed = []
    print ('your word is {} letters long'.format(len(word[0])))
    num_of_guesses = 0
    total_guesses = 8
    occurance = []
    blank = list('_' * len(word[0]))

    while num_of_guesses < total_guesses:
        remaining = total_guesses-num_of_guesses
        print('you can guess {} more times'.format(remaining))
        guess = (input('\nguess a letter ').lower())
        if len(guess) > 1:
            print ("That's too many letters long.")
            guess = (input('\nguess a letter ').lower())
        if guess not in ascii_lowercase:
            print ("That's not a letter.")
            guess = (input('\nguess a letter ').lower())
        if guess not in letters_guessed:
            letters_guessed.append(guess)
            for letter_list in word:
                if guess in letter_list:
                    word, occurance = conami_code(guess, word)
                    for position in occurance:
                        blank[position] = letter_list[position]
                    print("".join(blank))
            else:
                print("".join(blank))
                num_of_guesses+=1
        else:
            print("You already guessed that.")
            print("".join(blank))
    if num_of_guesses >= 8:
        print('FAILURE! the word was {}'.format(word))
    play_again()
    return "Bye!"

print(not_hang_man())
