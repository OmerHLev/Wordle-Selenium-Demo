import pytest
import time
from utilities.BaseTestClass import BaseTestClass
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait
import logging

class TestFrontPage(BaseTestClass):

    def test_all_games_present_in_dashboard(self, setup):
        logger = self.getLogger()
        logger.debug("Does the logger work correctly?")
        games_list = self.driver.find_elements(By.CSS_SELECTOR, ".hub-game-card__cover")
        assert len(games_list) == 7, "There are 7 Games in the page"


    def test_all_buttons_present_in_menu(self, setup):
        self.driver.find_element(By.ID, "js-nav-burger").click()
        menu_button_list = self.driver.find_elements(By.CSS_SELECTOR, ".js-nav-tracker.pz-nav-drawer__link")
        assert len(menu_button_list) == 16, "There are 16 buttons in the menu dropdown"


    #Check presence of the nyt logo



    #Click menu multiple times and check it appears and dissapears as intended



    #Find the "NEW" tag if it exists, and Log what item it refers to



    #Compare names of the games in the menu tab to games in the dashboard



    #Check Each button, and make sure it takes you to the correct page NOTE: Maybe do this in a different class
