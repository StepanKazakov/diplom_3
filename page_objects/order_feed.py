import random
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.order_feed_locators import *
from page_objects.base_methods import BaseMethods


class OrderFeed(BaseMethods):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_feed_link(self):
        self.wait_for_clickable((By.XPATH, header_order_feed_btn))
        self.click_element((By.XPATH, header_order_feed_btn))

    def get_order_feed_page_info(self):
        self.wait_for_visibility((By.XPATH, order_feed_page_title))
        current_url = self.driver.current_url
        page_title = self.get_text((By.XPATH, order_feed_page_title))
        return current_url, page_title

    def click_random_order_card(self):
        self.wait_for_visibility((By.XPATH, done_today_counter))
        cards = self.driver.find_elements(By.XPATH, order_feed_card)
        random_card = random.choice(cards)
        self.scroll_to_element_by_element(random_card)
        random_card.click()

    def get_order_details(self):
        self.wait_for_visibility((By.XPATH, modal_order_details_content))
        return self.get_text((By.XPATH, modal_order_details_content))

    def get_done_total_counters(self):
        total_counter = self.wait_for_visibility((By.XPATH, done_all_time_counter))
        return int(total_counter.text)

    def get_done_today_counter(self):
        daily_counter = self.wait_for_visibility((By.XPATH, done_today_counter))
        return int(daily_counter.text)

    def is_order_in_feed(self, order_number):
        self.wait_for_visibility((By.XPATH, feed_order_number))
        order_numbers = self.driver.find_elements(By.XPATH, feed_order_number)
        for number in order_numbers:
            if number.text == order_number:
                return True
        return False

    def get_order_number_from_progress(self):
        try:
            self.wait_for_visibility((By.XPATH, orders_in_progress))
            order_number = self.wait_until_data_refresh((By.XPATH, orders_in_progress), 'готовы!')
            return order_number.lstrip('0')
        except TimeoutException:
            return None
