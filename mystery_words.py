
import random
import re
import string

print("Hello. Welcome to hangman.")

with open("/usr/share/dict/words") as infile:
    language = infile.readlines()

class GetWord:
    def __init__(self, language):
        self.language = language

    def generate_word(self, language):
        self.mystery_word = random.choice(self.language)
        print(self.mystery_word)
        return (self.mystery_word)

    def check_length(self):
        if 3 >= len(self.mystery_word):
            self.generate_word(self.language)
        elif 11 <=len(self.mystery_word):
            self.generate_word(self.language)
        else:
            return self.mystery_word







a = GetWord(language)
print(a.generate_word(language))
print(a.check_length())
