import allure
import pytest

from page_objects.constructor import Constructor
from page_objects.personal_area import PersonalArea


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
            assert self.page.check_presence_of_make_order_button()

    @allure.title('Проверка появления всплывающего окна с деталями ингредиента')
    def test_ingredient_details_popup(self, random_ingredients):
        main_name = random_ingredients["main"]
        self.page = Constructor(self.driver)
        with allure.step('Клик по ингредиенту'):
            self.page.click_main_ingredient(main_name)
        with allure.step('Проверка, что появилось всплывающее окно с деталями ингредиента'):
            title, name = self.page.get_ingredient_details()
            assert title == "Детали ингредиента" and name == main_name

    @allure.title('Закрытие всплывающего окна с деталями ингредиента')
    def test_close_ingredient_details_popup(self, random_ingredients):
        sauce = random_ingredients["sauce"]
        self.page = Constructor(self.driver)
        with allure.step('Клик по ингредиенту'):
            self.page.click_sauce_ingredient(sauce)
        with allure.step('Закрытие всплывающего окна с деталями ингредиента'):
            self.page.close_popup()
        with allure.step('Проверка, что всплывающее окно закрылось'):
            assert self.page.check_ingredient_details_closed()

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении в заказ')
    def test_ingredient_counter_increase(self, random_ingredients):
        bun_name = random_ingredients["bun"]
        self.page = Constructor(self.driver)
        initial_counter = self.page.get_ingredient_counter(bun_name)
        with allure.step('Добавление ингредиента в заказ'):
            self.page.drag_and_drop_ingredient_to_burger(bun_name)
        with allure.step('Проверка увеличения счетчика ингредиента'):
            updated_counter = self.page.get_ingredient_counter(bun_name)
            assert updated_counter == initial_counter + 2

    @allure.title('Залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_place_order(self, test_user, random_ingredients):
        bun_name = random_ingredients["bun"]
        self.page = Constructor(self.driver)
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Авторизация и вход в Личный кабинет'):
            self.personal.click_personal_area_btn_in_header()
            self.personal.do_login(user_data["email"], user_data["password"])
        with allure.step('Добавление ингредиента в заказ'):
            self.page.drag_and_drop_ingredient_to_burger(bun_name)
        with allure.step('Оформление заказа'):
            self.page.click_make_order_btn()
        with allure.step('Проверка, что заказ оформлен'):
            order_id = self.page.get_order_id_text()
            assert order_id == "идентификатор заказа"
