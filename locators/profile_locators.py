# Личный кабинет
header_personal_area_btn = './/p[text()="Личный Кабинет"]'

# Меню личного кабинета
profile_orders_history = './/a[text()="История заказов"]'
profile_logout_btn = './/button[text()="Выход"]'

# Авторизация - кнопка "Войти"
login_btn = './/button[text()="Войти"]'

# Инпуты "Имя", "Email", "Пароль"
input_name = './/label[text()="Имя"]/following-sibling::input'
input_email = './/label[text()="Email"]/following-sibling::input'
input_password = './/input[@type="password"]'

# Восстановление пароля
password_recovery = './/a[text()="Восстановить пароль"]'
recovery_input_email = './/input[@name="name"]'
recovery_btn = './/button[text()="Восстановить"]'
recovery_input_password = './/label[text()="Пароль"]/ancestor::div[contains(@class, "input_size_default")]'
show_password_icon = './/div[@class="input__icon input__icon-action"]'
