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


    def get_guess_grid_array(self):
        grid = []
        for row_count in range(self.number_rows):
            row = []
            letters = self.driver.find_elements(By.CSS_SELECTOR, f"div[aria-label='Row {row_count+1}'] div div")
            for letter in range(self.number_letters):
                row.append(letters[letter])
            grid.append(row)

        return grid

