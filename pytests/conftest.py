
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Logger import LoggerClass

IMPLICIT_WAIT_TIME = 5
EXPLICIT_WAIT_TIME = 10

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="chrome firefox or edge"
    )


@pytest.fixture()
def setup(request):
    browser_name = request.config.getoption("browser_name")
    driver = invoke_browser(browser_name)
    wait = invoke_waits(driver,IMPLICIT_WAIT_TIME,EXPLICIT_WAIT_TIME)
    driver.get("https://www.nytimes.com/crosswords")
    request.cls.logger = LoggerClass().logger_object
    request.cls.driver = driver
    request.cls.wait = wait
    yield

    driver.close()

def invoke_browser(browser_name):
    match browser_name:
        case "chrome":
            service_obj = chromeService("/Users/omerh/Documents/chromedriver-win64/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            return webdriver.Chrome(service=service_obj, options=options)
        case "firefox":
            service_obj = firefoxService("/Users/omerh/Documents/geckodriver-v0.33.0-win64/geckodriver.exe")
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            return webdriver.Firefox(service=service_obj, options=options)
        case "edge":
            service_obj = edgeService("/Users/omerh/Documents/edgedriver_win64/msedgedriver.exe")
            options = webdriver.EdgeOptions()
            options.add_argument('--headless')
            return webdriver.Edge(service=service_obj, options=options)
        case _:
            print("Invalid browser name, defaulting to chrome")  # TODO: switch to logger
            service_obj = chromeService("/Users/omerh/Documents/chromedriver-win64/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            return webdriver.Chrome(service=service_obj, options=options)

def invoke_waits(driver,imp_wait,exp_wait):
    driver.implicitly_wait(imp_wait)
    return WebDriverWait(driver, exp_wait)