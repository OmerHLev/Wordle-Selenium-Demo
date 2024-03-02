import inspect
import pytest
import logging

from selenium.webdriver import ActionChains


@pytest.mark.usefixtures("setup_insulated")
class BaseTestClass:
    def send_action(self, driver, action):
        actions = ActionChains(driver)
        actions.send_keys(action)
        actions.perform()
        return
