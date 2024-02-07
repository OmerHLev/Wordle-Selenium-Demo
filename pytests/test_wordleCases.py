from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage


class TestFrontPage(BaseTestClass):

    def test_wordle_case_1(self):
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)

        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        grid = wordlepage.get_guess_grid_array()
        assert len(grid) == 6
        assert len(grid[0]) == 5