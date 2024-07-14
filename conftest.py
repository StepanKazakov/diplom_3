import pytest
from utils.webdriver_factory import WebDriverFactory
from url_data import base_url
from utils.api_helper import create_user, unique_user_data, set_random_ingredients


@pytest.fixture(scope='function')
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


@pytest.fixture(scope='function')
def test_user():
    user_data = unique_user_data()
    create_user(user_data)
    yield user_data


@pytest.fixture(scope='function')
def random_ingredients():
    ingredients = set_random_ingredients()
    return ingredients
