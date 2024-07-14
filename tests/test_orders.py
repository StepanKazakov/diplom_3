import pytest
import allure

from page_objects.personal_area import PersonalArea
from page_objects.order_feed import OrderFeed
from page_objects.constructor import Constructor
from url_data import *


@allure.feature('Проверка основного функционала ленты заказов')
@pytest.mark.usefixtures("setup")
class TestOrderFeed:
    @allure.title('Переход по клику на «Лента заказов»')
    def test_click_order_feed(self):
        self.order_feed = OrderFeed(self.driver)
        with allure.step('Клик на «Лента заказов» и проверка заголовка страницы'):
            self.order_feed.click_order_feed_link()
            current_url, page_title = self.order_feed.get_order_feed_page_info()
            assert current_url == order_feed and page_title == "Лента заказов"

    @allure.title('Проверка открытия всплывающего окна с деталями заказа')
    def test_order_details_popup(self):
        self.order_feed = OrderFeed(self.driver)
        with allure.step('Открываем Ленту Заказов'):
            self.order_feed.click_order_feed_link()
        with allure.step('Кликаем по случайной карточке заказа'):
            self.order_feed.click_random_order_card()
        with allure.step('Проверяем, что открылось окно с деталями заказа'):
            order_details = self.order_feed.get_order_details()
            assert order_details == "Cостав"

    @allure.title('Проверка отображения заказа в разделе "В работе" после оформления')
    def test_order_in_progress(self, test_user, random_ingredients):
        self.personal_area = PersonalArea(self.driver)
        self.order_feed = OrderFeed(self.driver)
        self.constructor = Constructor(self.driver)
        user_data = test_user
        bun_name = random_ingredients["bun"]
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal_area.click_personal_area_btn_in_header()
            self.personal_area.do_login(user_data["email"], user_data["password"])
        with allure.step('Создание нового заказа'):
            self.constructor.wait_load_constructor_page()
            self.constructor.drag_and_drop_ingredient_to_burger(bun_name)
            self.constructor.click_make_order_btn()
            order_id = self.constructor.get_order_id()
            self.constructor.close_popup()
        with allure.step('Проверка, что заказ появился в разделе "В работе"'):
            self.order_feed.click_order_feed_link()
            order_number = self.order_feed.get_order_number_from_progress()
            assert order_number == order_id

    @allure.title('Проверка отображения заказа в ленте заказов')
    def test_order_in_feed(self, test_user, random_ingredients):
        self.personal_area = PersonalArea(self.driver)
        self.order_feed = OrderFeed(self.driver)
        self.constructor = Constructor(self.driver)
        user_data = test_user
        bun_name = random_ingredients["bun"]
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal_area.click_personal_area_btn_in_header()
            self.personal_area.do_login(user_data["email"], user_data["password"])
        with allure.step('Создание заказа'):
            self.constructor.wait_load_constructor_page()
            self.constructor.drag_and_drop_ingredient_to_burger(bun_name)
            self.constructor.click_make_order_btn()
            self.constructor.close_popup()
        with allure.step('Получение номера заказа из Истории заказов'):
            self.personal_area.click_personal_area_btn_in_header()
            self.personal_area.click_orders_history_link()
            order_number = self.personal_area.get_order_number_from_history()
        with allure.step('Проверка номера заказа в Ленте заказов'):
            self.order_feed.click_order_feed_link()
            assert self.order_feed.is_order_in_feed(order_number)

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" после создания нового заказа')
    def test_done_all_time_counter_increase(self, test_user, random_ingredients):
        self.personal_area = PersonalArea(self.driver)
        self.order_feed = OrderFeed(self.driver)
        self.constructor = Constructor(self.driver)
        user_data = test_user
        bun_name = random_ingredients["bun"]
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal_area.click_personal_area_btn_in_header()
            self.personal_area.do_login(user_data["email"], user_data["password"])
        with allure.step('Запоминаем начальное значение счетчика "Выполнено за все время"'):
            self.constructor.wait_load_constructor_page()
            self.order_feed.click_order_feed_link()
            initial_counter_all = self.order_feed.get_done_total_counters()
        with allure.step('Создание нового заказа'):
            self.constructor.click_constructor_btn_in_header()
            self.constructor.drag_and_drop_ingredient_to_burger(bun_name)
            self.constructor.click_make_order_btn()
            self.constructor.close_popup()
        with allure.step('Проверка увеличения счетчика "Выполнено за все время"'):
            self.order_feed.click_order_feed_link()
            updated_counter_all = self.order_feed.get_done_total_counters()
            assert updated_counter_all > initial_counter_all

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" после создания нового заказа')
    def test_done_daily_counter_increase(self, test_user, random_ingredients):
        self.personal_area = PersonalArea(self.driver)
        self.order_feed = OrderFeed(self.driver)
        self.constructor = Constructor(self.driver)
        user_data = test_user
        bun_name = random_ingredients["bun"]
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal_area.click_personal_area_btn_in_header()
            self.personal_area.do_login(user_data["email"], user_data["password"])
        with allure.step('Запоминаем начальное значение счетчика "Выполнено за сегодня"'):
            self.constructor.wait_load_constructor_page()
            self.order_feed.click_order_feed_link()
            initial_counter_daily = self.order_feed.get_done_today_counter()
        with allure.step('Создание нового заказа'):
            self.constructor.click_constructor_btn_in_header()
            self.constructor.drag_and_drop_ingredient_to_burger(bun_name)
            self.constructor.click_make_order_btn()
            self.constructor.close_popup()
        with allure.step('Проверка увеличения счетчика "Выполнено за сегодня"'):
            self.order_feed.click_order_feed_link()
            updated_counter_daily = self.order_feed.get_done_today_counter()
            assert updated_counter_daily > initial_counter_daily
