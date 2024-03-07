import time
import pytest
from selenium.webdriver import Keys
from pageObjects.WordlePage import WordlePage
from utilities.BaseTestClass import BaseTestClass
from pageObjects.HomePage import HomePage
from utilities.WordleConditions import waitForAttribute, waitWordInfoLoaded
from projectData.wordleData import wordleData
from utilities.Constants import WORD_LENGTH
from utilities.WordleLogic import WordleLogic



@pytest.mark.current
class TestWordleCase1(BaseTestClass):
    driver = None
    wait = None
    wordlepage = None
    homepage = None
    log = None
    WordleLogic = None
    wordle_answer = None

    @pytest.mark.parametrize('words', wordleData().getSets(2))
    def test_wordle_case_1(self, words, logger_fixture, setup_insulated):
        # SETUP
        self.driver, self.wait, self.wordle_answer = setup_insulated
        self.wordlepage = WordlePage(self.driver)
        self.homepage = HomePage(self.driver)
        self.log = logger_fixture
        self.word_count = 0

        self.WordleLogic = WordleLogic(self.wordle_answer)

        # NAVIGATION
        self.log.info("Going to Wordle page")
        self.homepage.get_page_objects_list(HomePage.dashboard_games_list)[1].click()
        self.wordlepage.get_page_object(WordlePage.play_button).click()
        self.wordlepage.get_page_object(WordlePage.close_button).click()
        # SEND KEYS
        self.log.info("Waiting for the cells to load")
        time.sleep(1)  # TODO FIX THIS SHIT FOR FIREFOX
        self.wait.until(waitForAttribute(WordlePage.cells, 0,
                                         "aria-label",
                                         self.wordlepage.aria_label_constructor(0, "empty")))
        for word_num in range(len(words)):
            self.insert_word(words[word_num], word_num)
            assert (self.WordleLogic.is_new_word_clues_valid(words[word_num], self.get_clues(word_num))), (
                f"The clues given by wordle for the word {words[word_num]} were inconsistent"
                f" with the word of the day: {self.wordle_answer}")
        self.log.info("---------------------")

    def insert_word(self, word, row):
        self.log.info(f"Typing '{word}' into wordle")
        self.send_action(self.driver, word)
        self.log.info("Waiting for the last cell to load in the appropriate character")
        self.wait.until(waitForAttribute(WordlePage.cells, 4 + row * len(word),
                                         "aria-label",
                                         self.wordlepage.aria_label_constructor(4, word[4])))
        self.log.info("Verifying that the 4th cell received the correct character")
        assert (self.wordlepage.get_page_objects_list(WordlePage.cells)[4 + row * len(word)].get_attribute(
            "aria-label") ==
                self.wordlepage.aria_label_constructor(4, word[4]))
        self.send_action(self.driver, Keys.ENTER)
        time.sleep(3)  # Since there is a real time delay of the animation, I've allowed myself to use this here

    def get_clues(self, row):
        clues = []
        for cell in range(WORD_LENGTH):
            clues.append(
                self.wordlepage.get_page_objects_list(self.wordlepage.cells)[cell+row*WORD_LENGTH].get_attribute("data-state"))
        return clues
