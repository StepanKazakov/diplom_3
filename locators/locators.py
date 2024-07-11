# Хедер - кнопки "Конструктор", "Лента заказов", "Личный кабинет"
header_constructor_btn = './/p[text()="Конструктор"]'
header_orders_btn = './/p[text()="Лента Заказов"]'
header_personal_area_btn = './/p[text()="Личный Кабинет"]'

# Восстановление пароля
password_recovery = './/a[text()="Восстановить пароль"]'
recovery_input_email = './/input[@name="name"]'
recovery_btn = './/button[text()="Восстановить"]'
recovery_input_password = './/label[text()="Пароль"]/ancestor::div[contains(@class, "input_size_default")]'
show_password_icon = './/div[@class="input__icon input__icon-action"]'

# Инпуты "Имя", "Email", "Пароль"
input_name = './/label[text()="Имя"]/following-sibling::input'
input_email = './/label[text()="Email"]/following-sibling::input'
input_password = './/input[@type="password"]'

# Авторизация - кнопка "Войти"
login_btn = './/button[text()="Войти"]'

# Кнопка "Оформить заказ" - появляется на главной странице после авторизации
make_order_btn = './/button[text()="Оформить заказ"]'

# Личный кабинет - кнопка "Выход"
profile_orders_history = './/a[text()="История заказов"]'
profile_logout_btn = './/button[text()="Выход"]'

# Конструктор бургера
ingredient_bun_1 = './/img[@alt="Флюоресцентная булка R2-D3"]'
ingredient_counter_locator = ('.//img[@alt="Флюоресцентная булка R2-D3"]/preceding-sibling::'
                              'div/p[contains(@class, "counter_counter__num")]')
opened_modal = './/section[contains(@class, "Modal_modal_opened")]'
closed_modal = './/section[@class="Modal_modal__P3_V5"]'
ingredient_details_title = './/h2[text()="Детали ингредиента"]'
ingredient_details_name = './/p[@class="text text_type_main-medium mb-8"]'
close_modal_button = './/button[contains(@class, "Modal_modal__close_modified")]'
burger_target_locator = './/ul[contains(@class, "BurgerConstructor_basket__list")]'
order_id_title = './/p[@class="undefined text text_type_main-medium mb-15"]'
animation_success_order = './/img[@alt="tick animation"]'


# # Конструктор - кнопки «Булки», «Соусы», «Начинки»
# cons_bread_btn = './/span[text()="Булки"]'
# cons_sauce_btn = './/span[text()="Соусы"]'
# cons_filling_btn = './/span[text()="Начинки"]'
