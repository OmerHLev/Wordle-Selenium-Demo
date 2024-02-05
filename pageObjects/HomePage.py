from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    # HEAD
    logo = (By.CSS_SELECTOR, ".pz-nav__logo")
    navigation_menu = (By.CSS_SELECTOR, ".pz-nav__hamburger-box")
    subscribe_buttons_list = (By.CSS_SELECTOR, ".pz-nav__button.default.js-nav-subscribe.pz-hide-sub")
                            # First one is in the dashboard, seconed in the navigation collapsable menu
    login_buttons_list = (By.CSS_SELECTOR, ".js-nav-login")  # First one is in the dashboard,
                                                             # seconed in the navigation collapsable menu
    # NAVIGATION MENU
    navigation_menu_buttons_list = (By.CSS_SELECTOR, ".js-nav-tracker.pz-nav-drawer__link")

    # FEATURED
    featured_rotating_game = (By.CSS_SELECTOR, ".hub-welcome__section.alternate")
    featured_games_permanent_list = (By.CSS_SELECTOR, ".featured")
    wordplay_link = (By.CSS_SELECTOR, ".hub-wordplay-link")

    # DASHBOARD
    dashboard_games_list = (By.CSS_SELECTOR, ".hub-game-card__cover")
    dashboard_header = (By.CSS_SELECTOR, ".section__header")

    # FEATURED ARTICLE
    featured_article_header = (By.CSS_SELECTOR, "h3[class='hub-section-header']")
    feature_article = (By.CSS_SELECTOR, ".hub-guide-promo-card.js-hub-tracker")

    # ARCHIVE
    archive_header = (By.CSS_SELECTOR, "h2[class='hub-section-header']")
    archive_puzzles_list = (By.CSS_SELECTOR, ".island.action-play.standard.puzzleInfo.js-hub-tracker")
    # Should be 4
    more_button = (By.LINK_TEXT, "MORE")

    # BOTTOM
    # I think these are unnecessary to add, but if in the future I want those tested too here would
    # be the place to add them


    def get_page_object(self, page_object_pathway):
        return self.driver.find_elements(*page_object_pathway)

    # Create get page functions
