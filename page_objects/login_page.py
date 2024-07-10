import allure
from selenium.webdriver.common.by import By

from locators.locators import *
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_area_btn_in_header(self):
        self.click_element((By.XPATH, header_personal_area_btn))

    def click_password_recovery_link(self):
        self.scroll_page_center()
        self.click_element((By.XPATH, password_recovery))

    def recovery_password(self, email):
        with allure.step('ввод почты и клик по кнопке «Восстановить»'):
            self.input_text((By.XPATH, recovery_input_email), email)
            self.click_element((By.XPATH, recovery_btn))
        with allure.step('клик по кнопке показать/скрыть пароль'):
            self.click_element((By.XPATH, show_password_icon))
        with allure.step('результат проверки статуса поля ввода пароля - True, если поле активно'):
            return self.check_password_input_is_active((By.XPATH, recovery_input_password))

    def check_password_input_is_active(self, locator):
        element = self.wait_for_visibility(locator)
        with allure.step('проверка текущего статуса поля ввода пароля - активно'):
            return "input_status_active" in element.get_attribute("class")
