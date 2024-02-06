from utilities.BaseTestClass import BaseTestClass
from selenium.webdriver.common.by import By
from pageObjects.HomePage import HomePage
class TestFrontPage(BaseTestClass):

    def test_all_games_present_in_dashboard(self, setup):
        #logger = self.getLogger()
        #logger.debug("Does the logger work correctly?")
        homepage = HomePage(self.driver)
        assert len(homepage.get_page_object(HomePage.dashboard_games_list)) == 7, "There are 7 Games in the dashboard"


    def test_all_buttons_present_in_menu(self, setup):
        self.driver.find_element(By.ID, "js-nav-burger").click()
        menu_button_list = self.driver.find_elements(By.CSS_SELECTOR, ".js-nav-tracker.pz-nav-drawer__link")
        assert len(menu_button_list) == 16, "There are 16 buttons in the menu dropdown"


    #Check presence of the nyt logo



    #Click menu multiple times and check it appears and dissapears as intended



    #Find the "NEW" tag if it exists, and Log what item it refers to



    #Make sure the games in the dashboard tab also appear in the menu



    #Check Each button, and make sure it takes you to the correct page NOTE: Maybe do this in a different class


    #Check button changes when hovering
