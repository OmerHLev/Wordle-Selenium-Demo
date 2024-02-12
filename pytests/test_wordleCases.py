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
    def test_wordle_case_1(self,load_data):
        # SETUP
        logger = self.get_logger()
        homepage = HomePage(self.driver)
        wordlepage = WordlePage(self.driver)
        # NAVIGATION
        logger.info("Going to Wordle page")
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        # SEND KEYS
        logger.info("Waiting for the cells to load")
        self.wait.until(waitForAttribute(WordlePage.cells, 0,
                        "aria-label", wordlepage.aria_label_constructor(1, "empty")))
        logger.info(f"Typing '{load_data[0]}' into wordle")
        # TODO: move to function
        actions = ActionChains(self.driver)
        actions.send_keys(load_data[0])
        actions.perform()
        # WAIT FOR KEYS
        logger.info("Waiting for the last cell to load in the appropriate character")
        self.wait.until(waitForAttribute(WordlePage.cells, 4,
                        "aria-label", wordlepage.aria_label_constructor(5, load_data[0][4])))
        # ASSERT KEYS
        logger.info("Verifying that the 4th cell received the correct character")
        assert (wordlepage.get_page_objects_list(WordlePage.cells)[3].get_attribute("aria-label") ==
                wordlepage.aria_label_constructor(4, load_data[0][3]))
        logger.info("---------------------")
    @pytest.fixture(params=[("RATES","CAKED"),("SCARE","FAKES")])
    def load_data(self, request):
        return request.param