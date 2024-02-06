from utilities.BaseTestClass import BaseTestClass
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage


class TestFrontPage(BaseTestClass):
    expected_num_of_games_in_dashboard = 7
    expected_num_of_navigation_menu_buttons = 16

    def test_all_games_present_in_dashboard(self):
        # logger = self.get_logger()
        # logger.debug("Does the logger work correctly?")
        homepage = HomePage(self.driver)
        assert (len(homepage.get_page_objects_list(HomePage.dashboard_games_list)) ==
                self.expected_num_of_games_in_dashboard), "There should be 7 Games in the dashboard"

    def test_all_buttons_present_in_menu(self):
        homepage = HomePage(self.driver)
        homepage.get_page_object(HomePage.navigation_menu).click()
        assert (len(homepage.get_page_objects_list(HomePage.navigation_menu_buttons_list)) ==
                self.expected_num_of_navigation_menu_buttons), "There should be 16 buttons in the navigation menu"

    # Check presence of the nyt logo
    def test_nyt_logo_present(self):
        homepage = HomePage(self.driver)
        logger = self.get_logger()
        try:
            homepage.get_page_object(HomePage.logo).click()
        except:
            logger.error("NYT logo couldn't be clicked")
        finally:
            #logger.info(self.driver.current_url)
            assert self.driver.current_url == "https://www.nytimes.com/crosswords",\
                                                "Clicking the NYT logo took us to a different page"

    # Click menu multiple times and check it appears and dissapears as intended

    # Find the "NEW" tag if it exists, and Log what item it refers to

    # Make sure the games in the dashboard tab also appear in the menu

    # Check Each button, and make sure it takes you to the correct page NOTE: Maybe do this in a different class

    # Check button changes when hovering
