from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    games_list = (By.CSS_SELECTOR, ".hub-game-card__cover")
    featured_rotating_game = (By.CSS_SELECTOR, ".hub-welcome__section.alternate")
    featured_games_permanent = (By.CSS_SELECTOR, ".featured")
    wordplay_link = (By.CSS_SELECTOR, ".hub-wordplay-link")
    logo = (By.CSS_SELECTOR, ".pz-nav__logo")
    navigation_menu = (By.CSS_SELECTOR, ".pz-nav__hamburger-box")
    

    def get_games_list(self):
        return self.driver.find_elements(*HomePage.games_list)