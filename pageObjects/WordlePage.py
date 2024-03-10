from selenium.webdriver.common.by import By
from utilities.BasePageClass import BasePageClass


class WordlePage(BasePageClass):

    # CONSTANTS
    number_rows = 6
    number_letters = 5

    # WELCOME SCREEN
    play_button = (By.CSS_SELECTOR, "button[class='Welcome-module_button__ZG0Zh']")

    # LOGIN POPUP
    close_button = (By.CSS_SELECTOR, "button[aria-label='Close']")

    # WORDLE
    wordle_main = (By.ID, "wordle-app-game")
    wordle_board = (By.CSS_SELECTOR, ".Board-module_boardContainer__TBHNL")
    # wordle_board = (By.CSS_SELECTOR, ".Board-module_board__jeoPS")
    keyboard = (By.CSS_SELECTOR, "div[aria-label='Keyboard']")
    cells = (By.CSS_SELECTOR, "div[aria-roledescription = 'tile']")

    # ANSWER POP-UP
    answer_pop = (By.CSS_SELECTOR, ".Toast-module_toast__iiVsN")

    def aria_label_constructor(self,slot,letter):
        slot +=1
        label = f"{slot}"
        # TODO: MATCH CASE INSTEAD OF ELSE IF
        if slot == 1:
            label += "st"
        elif slot == 2:
            label += "nd"
        elif slot == 3:
            label += "rd"
        else:
            label += "th"
        label += f" letter, {letter}"
        return label




