from selenium.webdriver.common.by import By

from utilities.BaseTestClass import BaseTestClass

# DOESN'T WORK. ABANDONED
class letterEntered:
    def __init__(self, letter, path):
        self.path = path
        self.letter = letter

    def __call__(self, driver):
        aria_label = driver.find_element(By.CSS_SELECTOR, self.path).get_attribute("aria-label")
        if "empty" in aria_label:
            return False
        elif self.letter == aria_label[-1].upper:
            return driver
        else:
            return False
class waitForAttribute:
    def __init__(self, locator, attr, value):
        self._locator = locator
        self._attribute = attr
        self._attribute_value = value

    def __call__(self, driver):
        element = driver.find_element(By.CSS_SELECTOR, self._locator)
        if element.get_attribute(self._attribute) == self._attribute_value:
            return element
        else:
            return False
