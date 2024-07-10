import allure
import pytest

from page_objects.login_page import LoginPage
from user_data import *


@allure.feature('Тесты Личного кабинета')
@pytest.mark.usefixtures("setup")
class TestPA:
    def setup_method(self):
        self.login_page = LoginPage(self.driver)
        
    @allure.title('Тест функционала восстановления пароля')
    def test_password_recovery(self):
        with allure.step('Открытие Личного кабинета по ссылке в хедере главной страницы'):
            self.login_page.click_personal_area_btn_in_header()
        with allure.step('Переход на страницу восстановления пароля по кнопке «Восстановить пароль»'):
            self.login_page.click_password_recovery_link()
        with allure.step('Восстановление пароля и проверка статуса поля ввода пароля '
                         'после нажатия на иконку показа пароля'):
            is_active = self.login_page.recovery_password(user_email)
            assert is_active, "Поле должно быть активным после нажатия на иконку показа пароля"

    # def test_login_invalid(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.load()  # Optionally reload the page if needed
    #     login_page.login("invalid_user", "invalid_password")
    #     assert not login_page.is_logged_in()