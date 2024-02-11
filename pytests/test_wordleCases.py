import time

import pytest
from selenium.webdriver import Keys


from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from utilities.WordleConditions import waitForAttribute
from selenium.webdriver.support import expected_conditions as EC


class TestFrontPage(BaseTestClass):

    @pytest.mark.current
    def test_wordle_case_1(self):
        # SETUP
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)
        # NAVIGATION
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        # SEND KEYS
        self.wait.until(waitForAttribute(WordlePage.cells, 0,
                        "aria-label", wordlepage.aria_label_constructor(1, "empty")))
        actions = ActionChains(self.driver)
        actions.send_keys("rates")
        actions.perform()
        # WAIT FOR KEYS
        self.wait.until(waitForAttribute(WordlePage.cells, 4,
                        "aria-label", wordlepage.aria_label_constructor(5, "S")))
        # ASSERT KEYS
        assert (wordlepage.get_page_objects_list(WordlePage.cells)[3].get_attribute("aria-label") ==
                wordlepage.aria_label_constructor(4, "E"))
