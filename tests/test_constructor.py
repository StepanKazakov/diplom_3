import allure
import pytest

from page_objects.constructor import Constructor
from page_objects.personal_area import PersonalArea
from locators.locators import (ingredient_main_locator,
                               ingredient_counter_locator,
                               ingredient_sauce_locator,
                               ingredient_bun_locator)


@allure.feature('Тесты основного функционала - Конструктор заказа')
@pytest.mark.usefixtures("setup")
class TestConstructor:
    @allure.title('Переход в Конструктор залогиненым пользователем из Личного кабинета')
    def test_edit_constructor_authorised_user(self, test_user):
        self.page = Constructor(self.driver)
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal.click_personal_area_btn_in_header()
            self.personal.do_login(user_data["email"], user_data["password"])
            self.personal.click_personal_area_btn_in_header()
        with allure.step('Переход из Личного кабинета в Конструктор по кнопке в хедере и проверка,'
                         'что пользователю доступна кнопка "Оформить заказ" в Конструкторе'):
            self.page.click_constructor_btn_in_header()
            checkout_btn = self.page.check_presence_of_make_order_button()
            assert checkout_btn is not None, "Кнопка 'Оформить заказ' не найдена на странице"

    @allure.title('Проверка появления всплывающего окна с деталями ингредиента')
    def test_ingredient_details_popup(self, random_ingredients):
        main_name = random_ingredients["main"]
        main_locator = ingredient_main_locator(main_name)
        self.page = Constructor(self.driver)
        with allure.step('Клик по ингредиенту'):
            self.page.click_main_ingredient(main_locator)
        with allure.step('Проверка, что появилось всплывающее окно с деталями ингредиента'):
            title, name = self.page.get_ingredient_details()
            assert title == "Детали ингредиента" and name == main_name

    @allure.title('Закрытие всплывающего окна с деталями ингредиента')
    def test_close_ingredient_details_popup(self, random_ingredients):
        sauce = random_ingredients["sauce"]
        sauce = ingredient_sauce_locator(sauce)
        self.page = Constructor(self.driver)
        with allure.step('Клик по ингредиенту'):
            self.page.click_sauce_ingredient(sauce)
        with allure.step('Закрытие всплывающего окна с деталями ингредиента'):
            self.page.close_ingredient_details()
        with allure.step('Проверка, что всплывающее окно закрылось'):
            modal_closed = self.page.check_ingredient_details_closed()
            assert modal_closed is True, "Всплывающее окно не закрыто"

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increase(self, random_ingredients):
        bun_locator = ingredient_bun_locator(random_ingredients["bun"])
        counter_locator = ingredient_counter_locator(random_ingredients["bun"])
        self.page = Constructor(self.driver)
        initial_counter = self.page.get_ingredient_counter(counter_locator)
        with allure.step('Добавление ингредиента в заказ'):
            self.page.drag_and_drop_ingredient_to_burger(bun_locator)
        with allure.step('Проверка увеличения счетчика ингредиента'):
            updated_counter = self.page.get_ingredient_counter(counter_locator)
            assert updated_counter == initial_counter + 2, "Счетчик не соответствует ожидаемому значению"

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, test_user, random_ingredients):
        self.page = Constructor(self.driver)
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        bun_locator = ingredient_bun_locator(random_ingredients["bun"])
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal.click_personal_area_btn_in_header()
            self.personal.do_login(user_data["email"], user_data["password"])
        with allure.step('Добавление ингредиента в заказ'):
            self.page.drag_and_drop_ingredient_to_burger(bun_locator)
        with allure.step('Оформление заказа'):
            self.page.click_make_order_btn()
        with allure.step('Проверка, что заказ оформлен'):
            order_id_title = self.page.check_order_id_title()
            assert order_id_title == "идентификатор заказа", "Не удалось найти идентификатор заказа"
