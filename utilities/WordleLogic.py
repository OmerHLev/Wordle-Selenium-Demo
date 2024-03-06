import string

from utilities import Constants

class WordleLogic:
    def __init__(self,true_answer):
        self.answer = true_answer
        self.unique_letters_answer = list(set(self.answer))

    def is_new_word_clues_valid(self,word,clues):
        unique_letters = list(set(word))
        for letter_unique in unique_letters:
            if letter_unique not in self.unique_letters_answer:
                pos = 0
                for letter in word:
                    if letter == letter_unique and clues[pos] != "absent":
                        return False
                    pos += 1
            elif self.answer.count(letter_unique) >= word.count(letter_unique):
                pos = 0
                for letter in word:
                    if letter == letter_unique:
                        if self.answer[pos] != letter_unique:
                            if clues[pos] != "present":
                                return False
                        elif clues[pos] != "correct":
                            return False
                    pos += 1
            elif self.answer.count(letter_unique) < word.count(letter_unique):
                pos = 0
                positive_clue_count = 0
                for letter in word:
                    if letter == letter_unique:
                        if clues[pos] == "correct" or clues[pos] == "present":
                            positive_clue_count += 1
                    pos += 1
                if positive_clue_count != self.answer.count(letter_unique):
                    return False
                else:
                    pos = 0
                    for letter in word:
                        if letter == letter_unique:
                            if self.answer[pos] == letter_unique and clues[pos] != "correct":
                                return False
                        pos += 1
        return True


"""logic = WordleLogic("TEARY")
print(logic.is_new_word_clues_valid("ABOUT", ["present", "absent", "absent", "absent", "present"]))
"""

"""print(logic.is_new_word_clues_valid("AATEA", ["present", "absent", "present", "present", "absent"]))
print(logic.is_new_word_clues_valid("TAHEA", ["correct", "absent", "absent", "present", "present"]))
print(logic.is_new_word_clues_valid("AAHEA", ["present", "correct", "absent", "present", "absent"]))
print(logic.is_new_word_clues_valid("GEEKY", ["absent", "correct", "absent", "absent", "correct"]))
print(logic.is_new_word_clues_valid("AAAAA", ["absent", "absent", "correct", "absent", "absent"]))"""




