
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from selenium.webdriver.edge.service import Service as edgeService
from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.support.wait import WebDriverWait
from utilities.Logger import LoggerClass
from contextlib import contextmanager
from utilities import Constants
driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="chrome, firefox, edge or chrome_view"
    )



@contextmanager
def setup_base(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    driver = invoke_browser(browser_name)
    wait = invoke_waits(driver,Constants.IMPLICIT_WAIT_TIME,Constants.EXPLICIT_WAIT_TIME)
    driver.get("https://www.nytimes.com/crosswords")
    yield driver, wait
    driver.close()

@pytest.fixture(scope="function")
def setup_insulated(request):
    with setup_base(request) as result:
        yield result


@pytest.fixture(scope="session",autouse=True)
def logger_fixture():
    yield LoggerClass().logger_object


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
        case "chrome_view":
            service_obj = chromeService("/Users/omerh/Documents/chromedriver-win64/chromedriver.exe")
            options = webdriver.ChromeOptions()
            return webdriver.Chrome(service=service_obj, options=options)


def invoke_waits(driver,imp_wait,exp_wait):
    driver.implicitly_wait(imp_wait)
    return WebDriverWait(driver, exp_wait)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.fixture(scope="session")
def daily_answer():
    daily_answer = {'value':''}
    yield daily_answer