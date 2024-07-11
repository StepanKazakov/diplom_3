from selenium import webdriver


class WebDriverFactory:
    def __init__(self, browser):
        self.browser = browser

    def get_driver(self):
        if self.browser == 'chrome':
            driver = webdriver.Chrome()
        elif self.browser == 'firefox':
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Browser '{self.browser}' is not supported")
        driver.maximize_window()
        return driver
