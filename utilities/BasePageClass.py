
class BasePageClass:
    def __init__(self, driver):
        self.driver = driver

    def get_page_object(self, page_object_pathway):
        return self.driver.find_elements(*page_object_pathway)