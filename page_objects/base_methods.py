from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseMethods:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def wait_for_visibility(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_data_refresh(self, locator, data):
        return self.wait.until(lambda driver: self.get_text(locator) if data not in self.get_text(locator) else None)

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        element = self.wait_for_clickable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator, text):
        element = self.wait_for_visibility(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait_for_visibility(locator)
        return element.text

    def scroll_to_element_by_locator(self, locator):
        element = self.wait_for_visibility(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_to_element_by_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @property
    def current_url(self):
        return self.driver.current_url
    