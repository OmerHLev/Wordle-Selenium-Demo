import pytest
import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from selenium.webdriver.support.wait import WebDriverWait
import logging


@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("/Users/omerh/Documents/chromedriver-win64/chromedriver.exe")
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service_obj, options=options)

    driver.implicitly_wait(5)
    driver.get("https://www.nytimes.com/crosswords")
    wait = WebDriverWait(driver, 10)

    # IMPORTANT! Currently __name__ always refers to conftest, this needs to be fixed
    logger = logging.getLogger(__name__)
    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.DEBUG)


    request.cls.driver = driver
    request.cls.wait = wait
    request.cls.logger = logger
    yield

    driver.close()
