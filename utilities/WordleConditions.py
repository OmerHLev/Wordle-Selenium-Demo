
class waitForAttribute:
    def __init__(self, locator, locator_index, attr, value):
        self._locator = locator
        self._attribute = attr
        self._attribute_value = value
        self._locator_index = locator_index

    def __call__(self, driver):
        element = driver.find_elements(*self._locator)[self._locator_index]
        if element.get_attribute(self._attribute) == self._attribute_value:
            return element
        else:
            return False

class waitWordInfoLoaded:
    def __init__(self, locator, locator_index):
        self._locator = locator
        self._locator_index = locator_index

    def __call__(self, driver):
        element = driver.find_elements(*self._locator)[self._locator_index]
        if element.get_attribute("data_state") == "empty" or element.get_attribute("data_state") == "tbd":
            return False
        else:
            return element
