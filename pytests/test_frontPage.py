import pytest
import time
from utilities.BaseTestClass import BaseTestClass
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait


class TestFrontPage(BaseTestClass):

    def test_all_games_present(self, setup):
        games_list = self.driver.find_elements(By.CSS_SELECTOR, ".hub-game-card__cover")
        assert len(games_list) == 7
