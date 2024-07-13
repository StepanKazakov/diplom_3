# Конструктор бургера
header_constructor_btn = './/p[text()="Конструктор"]'
constructor_page_title = './/h1[@class="text text_type_main-large mb-5 mt-10"]'

# твбы «Булки», «Соусы», «Начинки»
buns_btn = './/span[text()="Булки"]'
sauce_btn = './/span[text()="Соусы"]'
filling_btn = './/span[text()="Начинки"]'

# Кнопка "Оформить заказ" - появляется на главной странице после авторизации
make_order_btn = './/button[contains(@class, "button_button__33qZ0")]'
order_id_title = './/h2[contains(@class, "Modal_modal__title")]'
order_id_text = './/p[contains(@class, "undefined text text_type_main-medium")]'
animation_success_order = './/img[@alt="tick animation"]'

# Всплывающее окно Деталей ингредиента
opened_modal = './/section[contains(@class, "Modal_modal_opened")]'
closed_modal = './/section[@class="Modal_modal__P3_V5"]'
ingredient_details_title = './/h2[contains(@class, "Modal_modal__title")]'
ingredient_details_name = './/p[@class="text text_type_main-medium mb-8"]'
close_modal_button = './/button[contains(@class, "Modal_modal__close_modified")]'

# Бургер - шаблон
burger_target_locator = './/ul[contains(@class, "BurgerConstructor_basket__list")]'


# Карточки ингредиентов (выбираются рандомно для каждого теста из api)
def ingredient_bun_locator(ingredient_name):
    return f'.//img[@alt="{ingredient_name}"]'


def ingredient_sauce_locator(ingredient_name):
    return f'.//img[@alt="{ingredient_name}"]'


def ingredient_main_locator(ingredient_name):
    return f'.//img[@alt="{ingredient_name}"]'


def ingredient_counter_locator(ingredient_name):
    return f'.//img[@alt="{ingredient_name}"]/preceding-sibling::div/p[contains(@class, "counter_counter__num")]'
