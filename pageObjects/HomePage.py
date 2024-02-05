from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    dashboard_games_list = (By.CSS_SELECTOR, ".hub-game-card__cover")
    featured_rotating_game = (By.CSS_SELECTOR, ".hub-welcome__section.alternate")
    featured_games_permanent_list = (By.CSS_SELECTOR, ".featured")
    wordplay_link = (By.CSS_SELECTOR, ".hub-wordplay-link")
    logo = (By.CSS_SELECTOR, ".pz-nav__logo")
    navigation_menu = (By.CSS_SELECTOR, ".pz-nav__hamburger-box")
    subscribe_buttons_list = (By.CSS_SELECTOR, ".pz-nav__button.default.js-nav-subscribe.pz-hide-sub")
                                                            #First one is in the dashboard,
                                                            # seconed in the navigation collapsable menu
    login_buttons_list = (By.CSS_SELECTOR, ".js-nav-login") #First one is in the dashboard,
                                                            # seconed in the navigation collapsable menu
    navigation_menu_buttons_list = (By.CSS_SELECTOR, ".js-nav-tracker.pz-nav-drawer__link")

    #Finish page objects

    def get_dashboard_games_list(self):
        return self.driver.find_elements(*HomePage.dashboard_games_list)


    #Finish all get functions


    #Create get page functions
