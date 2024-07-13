import allure
from selenium.webdriver.common.by import By

from locators.profile_locators import *
from locators.constructor_locators import constructor_page_title
from locators.order_feed_locators import order_feed_card, feed_order_number
from page_objects.base_methods import BaseMethods


class PersonalArea(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_area_btn_in_header(self):
        self.click_element((By.XPATH, header_personal_area_btn))

    def click_password_recovery_link(self):
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

    def check_link_is_active(self):
        element = self.wait_for_visibility((By.XPATH, profile_orders_history))
        with allure.step('проверка стиля меню "История заказов" - активно'):
            return "Account_link_active__2opc9" in element.get_attribute("class")

    def do_login(self, email, password):
        self.input_text((By.XPATH, input_email), email)
        self.input_text((By.XPATH, input_password), password)
        self.click_element((By.XPATH, login_btn))
        self.wait_for_visibility((By.XPATH, constructor_page_title))

    def check_presence_login_button(self):
        return self.wait_for_visibility((By.XPATH, login_btn))

    def check_profile_name(self):
        with allure.step('проверка текущего имени в Профиле'):
            current_name = self.wait_for_visibility((By.XPATH, input_name))
            return current_name.get_attribute('value')

    def click_orders_history_link(self):
        self.click_element((By.XPATH, profile_orders_history))
        return self.current_url

    def click_logout(self):
        self.click_element((By.XPATH, profile_logout_btn))
        self.wait_for_clickable((By.XPATH, login_btn))
        return self.current_url

    def get_order_number_from_history(self):
        self.wait_for_visibility((By.XPATH, order_feed_card))
        order_number_element = self.get_text((By.XPATH, feed_order_number))
        return order_number_element
