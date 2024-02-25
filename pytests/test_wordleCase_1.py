import logging
import time

import pytest
from selenium.webdriver import Keys

from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.action_chains import ActionChains
from utilities.WordleConditions import waitForAttribute
from selenium.webdriver.support import expected_conditions as EC
from utilities.Logger import LoggerClass
from _pytest.fixtures import FixtureRequest


@pytest.mark.parametrize('words', [("RATES", "CAKED"), ("SCARE", "FAKES")])
@pytest.mark.current
class TestWordleCase1(BaseTestClass):
    def test_wordle_case_1(self, words, logger_fixture, setup_insulated):
        driver, wait = setup_insulated
        wordlepage = WordlePage(driver)
        homepage = HomePage(driver)
        log = logger_fixture
        log.info("Waiting for the cells to load")
        log.info("Going to Wordle page")
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        # SEND KEYS
        wait.until(waitForAttribute(WordlePage.cells, 0,
                                         "aria-label", wordlepage.aria_label_constructor(0, "empty")))
        log.info(f"Typing '{words[0]}' into wordle")
        # TODO: move to function
        actions = ActionChains(driver)
        actions.send_keys(words[0])
        actions.perform()
        # WAIT FOR KEYS
        log.info("Waiting for the last cell to load in the appropriate character")
        wait.until(waitForAttribute(WordlePage.cells, 4,
                                         "aria-label", wordlepage.aria_label_constructor(4, words[0][4])))
        # ASSERT KEYS
        log.info("Verifying that the 4th cell received the correct character")
        assert (wordlepage.get_page_objects_list(WordlePage.cells)[3].get_attribute("aria-label") ==
                wordlepage.aria_label_constructor(3, words[0][3]))
        actions = ActionChains(driver)
        actions.send_keys(Keys.ENTER)
        actions.perform()
        log.info("---------------------")

    @pytest.fixture()
    def navigate(self, logger_fixture, setup_insulated):
        # SETUP
        driver, wait = setup_insulated
        log = logger_fixture
        homepage = HomePage(driver)
        wordlepage = WordlePage(driver)
        # NAVIGATION
        log.info("Going to Wordle page")
        homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        wordlepage.get_page_object(WordlePage.play_button).click()
        wordlepage.get_page_object(WordlePage.close_button).click()
        yield
        driver.get("https://www.nytimes.com/crosswords")
