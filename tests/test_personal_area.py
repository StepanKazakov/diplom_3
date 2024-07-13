import allure
import pytest

from page_objects.personal_area import PersonalArea


@allure.feature('Тесты по функционалу Личного кабинета')
@pytest.mark.usefixtures("setup")
class TestPersonalArea:
    @allure.title('Тест функционала восстановления пароля')
    def test_password_recovery(self, test_user):
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Открытие Личного кабинета по ссылке в хедере главной страницы'):
            self.personal.click_personal_area_btn_in_header()
        with allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»'):
            self.personal.click_password_recovery_link()
        with allure.step('Ввод email и проверка статуса поля ввода нового пароля '
                         'после нажатия на иконку показа пароля'):
            is_active = self.personal.recovery_password(user_data["email"])
            assert is_active, "Поле должно быть активным после нажатия на иконку показа пароля"

    @allure.title('Вход в Профиль по клику на «Личный кабинет»')
    def test_edit_personal_area(self, test_user):
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Авторизация по ссылке в хедере главной страницы'):
            self.personal.click_personal_area_btn_in_header()
        with allure.step('Заполнение логина, пароля и нажатие кнопки "Войти"'):
            self.personal.do_login(user_data["email"], user_data["password"])
        with allure.step('Открытие Профиля по ссылке "Личный кабинет"'):
            self.personal.click_personal_area_btn_in_header()
            current_name = self.personal.check_profile_name()
            assert current_name == user_data["name"]

    @allure.title('Переход в раздел «История заказов» по клику на «Личный кабинет»')
    def test_edit_orders_history(self, test_user):
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Авторизация по ссылке в хедере главной страницы'):
            self.personal.click_personal_area_btn_in_header()
        with allure.step('Заполнение логина, пароля и нажатие кнопки "Войти"'):
            self.personal.do_login(user_data["email"], user_data["password"])
        with allure.step('Открытие Профиля и переход в раздел «История заказов»'):
            self.personal.click_personal_area_btn_in_header()
            orders_history = self.personal.click_orders_history_link()
        with allure.step('Проверка редиректа на страницу истории заказов'):
            assert self.personal.check_link_is_active()
            assert orders_history == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.title('Выход из аккаунта в «Личном кабинете»')
    def test_logout(self, test_user):
        self.personal = PersonalArea(self.driver)
        user_data = test_user
        with allure.step('Авторизация по ссылке в хедере главной страницы'):
            self.personal.click_personal_area_btn_in_header()
        with allure.step('Заполнение логина, пароля и нажатие кнопки "Войти"'):
            self.personal.do_login(user_data["email"], user_data["password"])
        with allure.step('Открытие Профиля и клик по кнопке "Выход"'):
            self.personal.click_personal_area_btn_in_header()
            logout = self.personal.click_logout()
        with allure.step('Проверка редиректа на страницу авторизации'):
            assert self.personal.check_presence_login_button()
            assert logout == "https://stellarburgers.nomoreparties.site/login"
