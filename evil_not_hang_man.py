def random_word(word_list):
    random_digit = randint(0,len(word_list))
    return word_list[random_digit]

def azubu_frost():
    wordpool = []
    random_word_length = len(random_word(list_of_words))
    for word in list_of_words:
        if len(word) == random_word_length:
            wordpool.append(word.lower())
    return wordpool

    def conami_code(letter):
    random_words = azubu_frost()
    new_word_pool = []
    letter_position = []
    positions = []
    for word in random_words:
        if letter in word:
            new_word_pool.append(word)
    for word in new_word_pool:
        positions = find_occurences(word, letter)
        if positions not in letter_position:
            letter_position.append(positions)
    return letter_position

    
