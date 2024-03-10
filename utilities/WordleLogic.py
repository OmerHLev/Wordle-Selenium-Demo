import string

from utilities import Constants
from utilities.Logger import LoggerClass


class WordleLogic:
    def __init__(self,true_answer):
        self.answer = true_answer
        self.unique_letters_answer = list(set(self.answer))
        self.words_guessed = []
        self.clues_guessed = []
        self.log = LoggerClass()


#TODO: Separate into functions for readability
    def is_new_word_clues_valid(self,word,clues):
        self.words_guessed.append(word)
        self.clues_guessed.append(clues)
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

    def verify_keyboard_clues(self, keyboard_clues):
        for letter in string.ascii_lowercase:
            letter = letter.upper()
            if keyboard_clues[letter.lower()] == "add":
                for guess in self.words_guessed:
                    if letter in guess:
                        return False
            elif keyboard_clues[letter.lower()] == "absent":
                if letter in self.unique_letters_answer:
                    return False

                # TODO break loop when finding letter
                else:
                    flag_letter_found = False
                    for guess in self.words_guessed:
                        if letter in guess:
                            flag_letter_found = True
                    if not flag_letter_found:
                        return flag_letter_found

            elif keyboard_clues[letter.lower()] == "correct":
                if letter not in self.unique_letters_answer:
                    return False
                # TODO break loop when finding correct clue
                else:
                    flag_letter_correct_found = False
                    guess_pos = 0
                    for guess in self.words_guessed:
                        pos = 0
                        for character in guess:
                            if character == letter:
                                if self.clues_guessed[guess_pos][pos] == "correct":
                                    flag_letter_correct_found = True
                            pos += 1
                        guess_pos += 1
                    if not flag_letter_correct_found:
                        return flag_letter_correct_found
            elif keyboard_clues[letter.lower()] == "present":
                if letter not in self.unique_letters_answer:
                    return False
                else:
                    flag_letter_guessed = False
                    guess_pos = 0
                    for guess in self.words_guessed:
                        pos = 0
                        for character in guess:
                            if character == letter:
                                flag_letter_guessed = True
                                if self.clues_guessed[guess_pos][pos] == "correct":
                                    return False
                            pos += 1
                        guess_pos += 1
                    if not flag_letter_guessed:
                        return flag_letter_guessed


        return True

