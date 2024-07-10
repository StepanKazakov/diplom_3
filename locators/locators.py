# Хедер - кнопка "Конструктор", логотип "Stellar Burgers", кнопка "Личный кабинет"
header_constructor_btn = './/p[text()="Конструктор"]'
header_logo_btn = './/div[@class="AppHeader_header__logo__2D0X2"]'
header_personal_area_btn = './/p[text()="Личный Кабинет"]'

# Вход в личный кабинет - ссылки "Зарегистрироваться" и "Восстановить пароль"
do_register = './/a[text()="Зарегистрироваться"]'
password_recovery = './/a[text()="Восстановить пароль"]'

# Инпуты "Имя", "Email", "Пароль"
input_name = './/label[text()="Имя"]/following-sibling::input'
input_email = './/label[text()="Email"]/following-sibling::input'
input_password = './/input[@type="password"]'

# Регистрация - кнопка "Зарегистрироваться"
register_btn = './/button[text()="Зарегистрироваться"]'

# Текст ошибки при регистрации с некорректным паролем
incorrect_password = './/p[@class="input__error text_type_main-default"]'

# Регистрация/восстановление пароля - ссылка "Войти"
login_link = './/a[@class="Auth_link__1fOlj"]'

# Авторизация - кнопка "Войти"
login_btn = './/button[text()="Войти"]'

# Кнопка "Войти в аккаунт" / "Оформить заказ" - появляется на главной странице после авторизации
login_or_make_order_btn = \
    './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg"]'

# Личный кабинет - кнопка "Выход"
profile_logout_btn = './/button[text()="Выход"]'

# Конструктор - кнопки «Булки», «Соусы», «Начинки»
cons_bread_btn = './/span[text()="Булки"]'
cons_sauce_btn = './/span[text()="Соусы"]'
cons_filling_btn = './/span[text()="Начинки"]'
