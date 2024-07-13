from selenium.webdriver.common.by import By


# Личный кабинет
header_personal_area_btn = (By.XPATH, './/p[text()="Личный Кабинет"]')

# Меню личного кабинета
profile_orders_history = (By.XPATH, './/a[text()="История заказов"]')
profile_logout_btn = (By.XPATH, './/button[text()="Выход"]')

# История заказов пользователя
orders_history_card = (By.XPATH, './/li[contains(@class, "OrderHistory_listItem")]')
orders_history_order_number = (By.XPATH, './/p[@class="text text_type_digits-default"]')

# Авторизация - кнопка "Войти"
login_btn = (By.XPATH, './/button[text()="Войти"]')

# Инпуты "Имя", "Email", "Пароль"
input_name = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')
input_email = (By.XPATH, './/label[text()="Email"]/following-sibling::input')
input_password = (By.XPATH, './/input[@type="password"]')

# Восстановление пароля
password_recovery = (By.XPATH, './/a[text()="Восстановить пароль"]')
recovery_input_email = (By.XPATH, './/input[@name="name"]')
recovery_btn = (By.XPATH, './/button[text()="Восстановить"]')
recovery_input_password = (By.XPATH, './/label[text()="Пароль"]/ancestor::div[contains(@class, "input_size_default")]')
show_password_icon = (By.XPATH, './/div[@class="input__icon input__icon-action"]')
