import time

import pytest
from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class TestFrontPage(BaseTestClass):

    @pytest.mark.current
    def test_wordle_case_1(self):
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        grid = wordlepage.get_guess_grid_array()
        actions = ActionChains(self.driver)
        # actions.click()
        actions.send_keys("rates")
        actions.perform()
        # logger.debug(grid[0][3].get_attribute("aria-label"))
        assert grid[0][3].get_attribute("aria-label") == "4th letter, E"