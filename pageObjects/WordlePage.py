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
    guess_grid_rows = (By.CSS_SELECTOR, ".Row-module_row__pwpBq")

    def get_guess_grid_array(self):
        grid = []
        for row_count in range(self.number_rows):
            row = []
            letters = self.driver.find_elements(By.CSS_SELECTOR, f"div[aria-label='Row {row_count+1}'] div div")
            for letter in range(self.number_letters):
                row.append(letters[letter])
            grid.append(row)

        return grid

