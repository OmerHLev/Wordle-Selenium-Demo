import time

import pytest
from selenium.webdriver import Keys

from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from utilities.WordleConditions import waittest


class TestFrontPage(BaseTestClass):

    # DISASTER TEST: ABANDONED FOR NOW
    def test_wordle_case_1(self):
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        grid = wordlepage.get_guess_grid_array()
        assert grid[0][3].get_attribute("aria-label") == "4th letter, empty"
        actions = ActionChains(self.driver)
        actions.send_keys("rates")
        actions.perform()
        logger.debug("About to execute wait")
        self.wait.until(waittest("div[aria-label='Row 0'] div:nth-child(4)",
                                 "aria-label", "4th letter, E"))
        assert grid[0][3].get_attribute("aria-label") == "4th letter, E"
        actions.send_keys(Keys.ENTER)
        actions.perform()
        time.sleep(2)
        for cell in grid[0]:
            logger.debug(cell.get_attribute("data-state"))

    @pytest.mark.current
    def test_wordle_case_2(self):
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        # GET GRID CELLS PATHS
        # SEND KEYS
        # WAIT FOR KEYS
        # ASSERT KEYS
        