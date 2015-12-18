import random
import string
import re



class MysteryWord:
    def __init__(self):
        with open("/usr/share/dict/words") as infile:
            language = infile.readlines()
        possible_words = []
        for word in language:
            if 4 < len(word) < 10:
                possible_words.append(word.upper())
        self.mystery_word = (random.choice(possible_words)).upper()
        self.letters_guessed = []
        #print(self.mystery_word)

    def new_game(self):
        self.blank_letters = str("_ " * (len(self.mystery_word) - 1))
        print("Welcome to Hangman!")
        print("")
        print("")
        print(self.blank_letters)

class PlayerTurn(MysteryWord):
    def get_guess(self):
        print("You have {} incorrect guesses left.".format(self.guesses_remaining))
        self.guess = input("Please guess a letter: _ ").upper()
        return self.guess

    def check_guess(self):
        if self.guess in self.mystery_word:
            counter = 0
            revealed = list(self.blank_letters)
            for letter in self.mystery_word:
                if letter == self.guess:
                    revealed[counter*2] = self.guess
                counter += 1
            self.blank_letters = ""
            for char in revealed:
                self.blank_letters += char
            print("")
            print("")
            print(self.blank_letters)
            x = re.sub(" ", "", self.blank_letters)
            if x == self.mystery_word:
                print("Yay! You won!")
        else:
            self.guesses_remaining -= 1
            self.letters_guessed.append(str(self.guess) + " ")
            print("")
            print("Sorry, that letter is not in my word. :-(")
            print("You have {} incorrect guesses left.".format(self.guesses_remaining))
            print("You have already guessed: {}".format(self.letters_guessed))
            print("")
            print("")
            print(self.blank_letters)

    def run_turn(self):
        print("")
        self.guesses_remaining = 7
        while self.guesses_remaining > 0:
            PlayerTurn.get_guess(self)
            PlayerTurn.check_guess(self)
            if "_" not in self.blank_letters:
                print("Congrats! You won!")
                break
        else:
            print("Sorry, Game Over")
            print("(This is the word you were looking for): \n {}".format(self.mystery_word))

graphic = """
_________|
   |     |
  ()     |
 /[]\    |
  []     |
  /\     |
 /  \    |
_________|

  """
print(graphic)

start = MysteryWord()
start.new_game()
PlayerTurn.run_turn(start)
while input("Play again? \n[Y]es [N]o ").upper() == "Y":
    start = MysteryWord()
    start.new_game()
    PlayerTurn.run_turn(start)
