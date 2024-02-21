import string

from utilities import Constants

class WordleLogic:
    def __init__(self):
        self.unknowns = ([*string.ascii_uppercase])
        self.cells = []
        for cell_position in range(Constants.WORD_LENGTH): self.cells.append(WordleCell(cell_position))
        self.present =[]
        self.known = []

    def new_word(self, word, clues):
        position = 0
        for letter in word:
            self.new_clue(letter, position, clues[position])
            position += 1

    def exclusive_append(self,curr_list, item):
        if item not in curr_list:
            curr_list.append(item)
        return curr_list

    def new_clue(self, letter,position,clue):
        if letter in self.unknowns:
            self.unknowns.remove(letter)
        match clue:
            case "absent":
                if letter in self.cells[position].correct:
                    raise Exception("Letter said to be absent but is registered as correct")
                self.cells[position].incorrect = self.exclusive_append(self.cells[position].incorrect, letter)

            case "elsewhere":
                if letter in self.cells[position].correct:
                    raise Exception("Letter said to be elsewhere but is registered as correct")
                self.present = self.exclusive_append(self.present, letter)
                self.cells[position].incorrect = self.exclusive_append(self.cells[position].incorrect, letter)
            case "hit":
                if letter in self.cells[position].incorrect:
                    raise Exception("Letter said to be correct but is registered as incorrect")
                self.known = self.exclusive_append(self.known, letter)
                self.present = self.exclusive_append(self.present, letter)
                self.cells[position].correct = self.exclusive_append(self.cells[position].correct, letter)
    def check_word_to_guess(self,word):
        position = 0
        guessable_flag = True
        for letter in word:
            if letter in self.unknowns or letter in self.present:
                if letter not in self.cells[position].incorrect:
                    pass
                else:
                    guessable_flag = False
            else:
                guessable_flag = False
            position += 1
        return guessable_flag


class WordleCell:
    def __init__(self,position):
        self.position = position
        self.incorrect =[]
        self.correct = []


def testing_temporary():
    wordle = WordleLogic()
    wordle.new_word("RATES",["absent", "absent", "absent", "absent", "absent"])
    wordle.new_word("POUND", ["absent", "absent", "elsewhere", "absent", "hit"])
    wordle.new_word("MILKY", ["absent", "elsewhere", "elsewhere", "absent", "absent"])
    wordle.new_word("MILKY", ["absent", "elsewhere", "elsewhere", "absent", "absent"])

    wordle.new_word("GUILD", ["absent", "hit", "hit", "hit", "hit"])
    print(wordle.check_word_to_guess("BUILD"))
    print(wordle.check_word_to_guess("FIGHT"))
    print(wordle.unknowns)
    print(wordle.known)
    print(wordle.present)
    print(wordle.cells[3].incorrect)
    print(wordle.cells[3].correct)
    print(wordle.cells[4].incorrect)
    print(wordle.cells[4].correct)
testing_temporary()