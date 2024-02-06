import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="chrome firefox or edge"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    #Replace code duplication with getDriver function
    if browser_name == "chrome":
        service_obj = chromeService("/Users/omerh/Documents/chromedriver-win64/chromedriver.exe")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(service=service_obj, options=options)
    elif browser_name == "firefox":
        service_obj = firefoxService("/Users/omerh/Documents/geckodriver-v0.33.0-win64/geckodriver.exe")
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        driver = webdriver.Firefox(service=service_obj, options=options)
    elif browser_name == "edge":
        service_obj = edgeService("/Users/omerh/Documents/edgedriver_win64/msedgedriver.exe")
        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        driver = webdriver.Edge(service=service_obj, options=options)

    driver.implicitly_wait(5)
    driver.get("https://www.nytimes.com/crosswords")
    wait = WebDriverWait(driver, 10)

    request.cls.driver = driver
    request.cls.wait = wait
    yield

    driver.close()
