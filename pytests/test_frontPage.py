from utilities.BaseTestClass import BaseTestClass
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage


class TestFrontPage(BaseTestClass):
    expected_num_of_games_in_dashboard = 7
    expected_num_of_navigation_menu_buttons = 16

    def test_all_games_present_in_dashboard(self):
        homepage = HomePage(self.driver)
        assert (len(homepage.get_page_objects_list(HomePage.dashboard_games_list)) ==
                self.expected_num_of_games_in_dashboard), (f"There should be "
                                                           f"{self.expected_num_of_games_in_dashboard}"
                                                           f" Games in the dashboard")

    def test_all_buttons_present_in_menu(self):
        homepage = HomePage(self.driver)
        homepage.get_page_object(HomePage.navigation_menu_button).click()
        assert (len(homepage.get_page_objects_list(HomePage.navigation_menu_buttons_list)) ==
                self.expected_num_of_navigation_menu_buttons), (f"There should be "
                                                                f"{self.expected_num_of_navigation_menu_buttons} "
                                                                f"buttons in the navigation menu")

    # Check clickability of the nyt logo
    def test_nyt_logo_present(self):
        homepage = HomePage(self.driver)

        try:
            homepage.get_page_object(HomePage.logo).click()
        except:
            self.logger.error("NYT logo couldn't be clicked")
        finally:
            # logger.info(self.driver.current_url)
            assert self.driver.current_url == "https://www.nytimes.com/crosswords", \
                "Clicking the NYT logo took us to a different page"

    # Click menu multiple times and check it appears and disappears as intended

    def test_navigation_menu_collapsibility(self):
        homepage = HomePage(self.driver)
        assert (homepage.get_page_object(HomePage.navigation_menu_drawer).get_attribute("aria-hidden")
                == "true"), "Navigation menu drawer should start off as hidden"
        for count in range(5):
            homepage.get_page_object(HomePage.navigation_menu_button).click()
            if count % 2 == 0:
                assert (homepage.get_page_object(HomePage.navigation_menu_drawer).get_attribute("aria-hidden")
                        == "false"), (f"Navigation menu drawer failed to appear after "
                                      f"pressing navigation menu button {count} times")
            elif count % 2 == 1:
                assert (homepage.get_page_object(HomePage.navigation_menu_drawer).get_attribute("aria-hidden")
                        == "true"), (f"Navigation menu drawer failed to hide after"
                                     f" pressing navigation menu button {count} times")

    # Find the "NEW" tag if it exists, and Log what item it refers to

    # Make sure the games in the dashboard tab also appear in the menu

    # Check Each button, and make sure it takes you to the correct page NOTE: Maybe do this in a different class

    # Check button changes when hovering
