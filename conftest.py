import pytest
from selenium import webdriver
from urls_data import base_url


@pytest.fixture(scope='function')
def driver_chrome():
    driver = webdriver.Chrome()
    driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def driver_ff():
    driver = webdriver.Firefox()
    driver.get(base_url)
    yield driver
    driver.quit()
