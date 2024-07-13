import allure

from locators.profile_locators import *
from locators.constructor_locators import constructor_page_title
from locators.order_feed_locators import order_feed_card, feed_order_number
from page_objects.base_methods import BaseMethods


class PersonalArea(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_personal_area_btn_in_header(self):
        with allure.step('клик на Личный кабинет в хэдере'):
            self.wait_for_clickable(header_personal_area_btn)
            self.click_element(header_personal_area_btn)

    def click_password_recovery_link(self):
        with allure.step('клик на надпись Восстановить пароль'):
            self.click_element(password_recovery)

    def recovery_password(self, email):
        with allure.step('ввод почты и клик по кнопке «Восстановить»'):
            self.input_text(recovery_input_email, email)
            self.click_element(recovery_btn)
        with allure.step('клик по кнопке показать/скрыть пароль'):
            self.click_element(show_password_icon)
        with allure.step('результат проверки статуса поля ввода пароля - True, если поле активно'):
            return self.check_password_input_is_active(recovery_input_password)

    def check_password_input_is_active(self, locator):
        with allure.step('проверка текущего статуса поля ввода пароля - активно'):
            element = self.wait_for_visibility(locator)
            return "input_status_active" in element.get_attribute("class")

    def check_link_is_active(self):
        with allure.step('проверка стиля меню "История заказов" - активно'):
            element = self.wait_for_visibility(profile_orders_history)
            return "Account_link_active__2opc9" in element.get_attribute("class")

    def do_login(self, email, password):
        with allure.step('авторизация: вводим email, пароль и нажимаем кнопку "Войти", '
                         'ожидаем при успешной авторизации редиректа на страницу конструктора'):
            self.input_text(input_email, email)
            self.input_text(input_password, password)
            self.click_element(login_btn)
            self.wait_for_visibility(constructor_page_title)

    def check_presence_login_button(self):
        with allure.step('проверка наличия в зоне видимости кнопки "Войти"'):
            return self.wait_for_visibility(login_btn)

    def check_profile_name(self):
        with allure.step('проверка текущего имени в Профиле'):
            current_name = self.wait_for_visibility(input_name)
            return current_name.get_attribute('value')

    def click_orders_history_link(self):
        with allure.step('кликаем на меню История заказов в Профиле и возвращаем url'):
            self.click_element(profile_orders_history)
            return self.current_url

    def click_logout(self):
        with allure.step('кликаем на меню Выход в Профиле и возвращаем url'):
            self.click_element(profile_logout_btn)
            self.wait_for_clickable(login_btn)
            return self.current_url

    def get_order_number_from_history(self):
        with allure.step('получаем номер заказа в ленте Истории заказов'):
            self.wait_for_visibility(order_feed_card)
            order_number_element = self.get_text(feed_order_number)
            return order_number_element
