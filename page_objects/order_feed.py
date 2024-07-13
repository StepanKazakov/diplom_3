import random
import allure
from selenium.common import TimeoutException

from locators.order_feed_locators import *
from page_objects.base_methods import BaseMethods


class OrderFeed(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_feed_link(self):
        with allure.step('клик на Ленту заказов в хэдере'):
            self.wait_for_clickable(header_order_feed_btn)
            self.click_element(header_order_feed_btn)

    def get_order_feed_page_info(self):
        with allure.step('получаем урл и заголовок страницы Лента заказов'):
            self.wait_for_visibility(order_feed_page_title)
            current_url = self.current_url
            page_title = self.get_text(order_feed_page_title)
            return current_url, page_title

    def click_random_order_card(self):
        with allure.step('кликаем на случайно выбранную карточку в Ленте заказов'):
            self.wait_for_visibility(done_today_counter)
            cards = self.find_elements(order_feed_card)
            random_card = random.choice(cards)
            self.scroll_to_element_by_element(random_card)
            random_card.click()

    def get_order_details(self):
        with allure.step('получаем текст на карточке любого заказа - "Состав"'):
            self.wait_for_visibility(modal_order_details_content)
            return self.get_text(modal_order_details_content)

    def get_done_total_counters(self):
        with allure.step('получаем значение счетчика заказов за все время'):
            total_counter = self.wait_for_visibility(done_all_time_counter)
            return int(total_counter.text)

    def get_done_today_counter(self):
        with allure.step('получаем значение счетчика заказов за текущий день'):
            daily_counter = self.wait_for_visibility(done_today_counter)
            return int(daily_counter.text)

    def is_order_in_feed(self, order_number):
        with allure.step('проверяем наличие конкретного заказа в ленте заказов по номеру'):
            self.wait_for_visibility(feed_order_number)
            order_numbers = self.find_elements(feed_order_number)
            for number in order_numbers:
                if number.text == order_number:
                    return True
            return False

    def get_order_number_from_progress(self):
        with allure.step('проверяем наличие конкретного номера заказа в работе'):
            try:
                self.wait_for_visibility(orders_in_progress)
                order_number = self.wait_until_data_refresh(orders_in_progress, 'готовы!')
                return order_number.lstrip('0')
            except TimeoutException:
                return None
