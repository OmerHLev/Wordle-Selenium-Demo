import string

import Constants

class WordleLogic:
    def __init__(self):
        self.unknowns = ([*string.ascii_uppercase])
        self.cells = []
        for cell_position in range(Constants.WORD_LENGTH): self.cells.append(WordleCell(cell_position))
        self.absent = []
        self.present =[]
        self.known = []

    def new_word(self, word, clues):
        pass
            
    def new_clue(self,letter,position,clue):
        match clue:
            case "absent":
                if letter in self.unknowns:
                    self.unknowns.remove(letter)
                    self.absent.append(letter)
                self.cells[position].incorrect.append(letter)
            case "elsewhere":
                if letter in self.unknowns:
                    self.unknowns.remove(letter)
                    self.present.append(letter)
                self.cells[position].incorrect.append(letter)
            case "hit":
                if letter in self.unknowns:
                    self.unknowns.remove(letter)
                    self.present.append(letter)
                self.cells[position].correct = letter

class WordleCell:
    def __init__(self,position):
        self.position = position
        self.incorrect =[]
        self.correct = False