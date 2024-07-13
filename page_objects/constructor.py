import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.constructor_locators import *
from page_objects.base_methods import BaseMethods


class Constructor(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor_btn_in_header(self):
        with allure.step('клик на Конструктор в хэдере'):
            self.click_element((By.XPATH, header_constructor_btn))

    def check_presence_of_make_order_button(self):
        with allure.step('проверка наличия в зоне видимости кнопки "Оформить заказ"'):
            return self.wait_for_visibility((By.XPATH, make_order_btn))

    def click_main_ingredient(self, locator):
        with allure.step('клик на таб "Начинки"'):
            self.click_element((By.XPATH, filling_btn))
            self.scroll_to_element_by_locator((By.XPATH, locator))
            self.click_element((By.XPATH, locator))

    def click_sauce_ingredient(self, locator):
        with allure.step('клик на таб "Соусы"'):
            self.click_element((By.XPATH, sauce_btn))
            self.scroll_to_element_by_locator((By.XPATH, locator))
            self.click_element((By.XPATH, locator))

    def get_ingredient_details(self):
        with allure.step('получаем название ингредиента во всплывающем окне "Детали ингредиента"'):
            self.wait_for_visibility((By.XPATH, opened_modal))
            title = self.get_text((By.XPATH, ingredient_details_title))
            name = self.get_text((By.XPATH, ingredient_details_name))
            return title, name

    def close_popup(self):
        with allure.step('закрываем всплывающее окно'):
            self.wait_for_clickable((By.XPATH, close_modal_button))
            self.click_element((By.XPATH, close_modal_button))

    def check_ingredient_details_closed(self):
        with allure.step('проверяем, что всплывающее окно закрыто'):
            self.wait_for_invisibility((By.XPATH, opened_modal))
            try:
                self.wait_for_visibility((By.XPATH, closed_modal))
                return True
            except TimeoutException:
                return False

    def drag_and_drop_ingredient_to_burger(self, locator):
        with allure.step('перетаскивание ингредиента из ленты на шаблон заказа бургера'):
            source_element = self.wait_for_clickable((By.XPATH, locator))
            target_element = self.wait_for_visibility((By.XPATH, burger_target_locator))
            self.driver.execute_script("""
                        const source = arguments[0];
                        const target = arguments[1];
    
                        const dataTransfer = new DataTransfer();
                        const dragStartEvent = new DragEvent('dragstart', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer,
                        });
    
                        source.dispatchEvent(dragStartEvent);
    
                        const dropEvent = new DragEvent('drop', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer,
                        });
    
                        target.dispatchEvent(dropEvent);
    
                        const dragEndEvent = new DragEvent('dragend', {
                            bubbles: true,
                            cancelable: true,
                            dataTransfer: dataTransfer,
                        });
    
                        source.dispatchEvent(dragEndEvent);
                    """, source_element, target_element)

    def get_ingredient_counter(self, locator):
        with allure.step('получаем выбранное количество ингредиента в карточке'):
            try:
                counter_element = self.wait_for_visibility((By.XPATH, locator))
                return int(counter_element.text)
            except ValueError:
                return 0

    def click_make_order_btn(self):
        with allure.step('кликаем на кнопку "Оформить заказ"'):
            self.wait_for_clickable((By.XPATH, make_order_btn))
            self.click_element((By.XPATH, make_order_btn))

    def get_order_id_text(self):
        with allure.step('считываем текст в модальном окне подтверждения заказа'):
            self.wait_for_visibility((By.XPATH, order_id_text))
            self.wait_for_visibility((By.XPATH, animation_success_order))
            return self.get_text((By.XPATH, order_id_text))

    def get_order_id(self):
        with allure.step('получаем номер заказа в модальном окне подтверждения заказа'):
            try:
                self.wait_for_visibility((By.XPATH, order_id_title))
                order_number = self.wait_until_data_refresh((By.XPATH, order_id_title), '9999')
                return order_number
            except TimeoutException:
                return None
