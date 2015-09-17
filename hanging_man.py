#with open("/usr/share/dict/words") as infile:
#    available_words  = infile.read().split()

game_word = "sammy".upper()

word_length = len(game_word)

word_as_list = list(game_word)

guessed_word_as_list = ["_", "_", "_", "_", "_"]

def check_letter(passed_letter): #checks a letter with game word and returns game word with correct guesses revealed
    letter = passed_letter.upper()
    if letter in word_as_list:
        for i, l in enumerate(word_as_list):
            if l == letter:
                guessed_word_as_list[i] = l
        return guessed_word_as_list
