from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from locators.locators import *
from page_objects.base_methods import BaseMethods


class Constructor(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor_btn_in_header(self):
        self.click_element((By.XPATH, header_constructor_btn))

    def check_presence_of_make_order_button(self):
        return self.wait_for_visibility((By.XPATH, make_order_btn))

    def click_main_ingredient(self, locator):
        self.click_element((By.XPATH, filling_btn))
        self.scroll_to_element((By.XPATH, locator))
        self.click_element((By.XPATH, locator))

    def click_sauce_ingredient(self, locator):
        self.click_element((By.XPATH, sauce_btn))
        self.scroll_to_element((By.XPATH, locator))
        self.click_element((By.XPATH, locator))

    def get_ingredient_details(self):
        self.wait_for_visibility((By.XPATH, opened_modal))
        title = self.get_text((By.XPATH, ingredient_details_title))
        name = self.get_text((By.XPATH, ingredient_details_name))
        return title, name

    def close_ingredient_details(self):
        self.click_element((By.XPATH, close_modal_button))

    def check_ingredient_details_closed(self):
        self.wait_for_invisibility((By.XPATH, opened_modal))
        try:
            self.wait_for_visibility((By.XPATH, closed_modal))
            return True
        except TimeoutException:
            return False

    def drag_and_drop_ingredient_to_burger(self, locator):
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
        try:
            counter_element = self.wait_for_visibility((By.XPATH, locator))
            return int(counter_element.text)
        except ValueError:
            return 0

    def click_make_order_btn(self):
        self.wait_for_clickable((By.XPATH, make_order_btn))
        self.click_element((By.XPATH, make_order_btn))
        self.wait_for_clickable((By.XPATH, close_modal_button))

    def check_order_id_title(self):
        self.wait_for_visibility((By.XPATH, order_id_title))
        self.wait_for_visibility((By.XPATH, animation_success_order))
        return self.get_text((By.XPATH, order_id_title))
