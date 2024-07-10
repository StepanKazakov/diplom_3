import pytest
from utils.webdriver_factory import WebDriverFactory
from url_data import base_url


@pytest.fixture(scope='class')
def setup(request):
    browser = request.config.getoption("--browser")
    web_driver_factory = WebDriverFactory(browser=browser)
    driver = web_driver_factory.get_driver()
    driver.get(base_url)
    request.cls.driver = driver
    yield
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
