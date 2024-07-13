from selenium.webdriver.common.by import By


# Конструктор бургера
header_constructor_btn = (By.XPATH,'.//p[text()="Конструктор"]')
constructor_page_title = (By.XPATH,'.//h1[@class="text text_type_main-large mb-5 mt-10"]')

# твбы «Булки», «Соусы», «Начинки»
buns_btn = (By.XPATH,'.//span[text()="Булки"]')
sauce_btn = (By.XPATH,'.//span[text()="Соусы"]')
filling_btn = (By.XPATH,'.//span[text()="Начинки"]')

# Кнопка "Оформить заказ" - появляется на главной странице после авторизации
make_order_btn = (By.XPATH,'.//button[contains(@class, "button_button__33qZ0")]')
order_id_title = (By.XPATH,'.//h2[contains(@class, "Modal_modal__title")]')
order_id_text = (By.XPATH,'.//p[contains(@class, "text_type_main-medium")]')
animation_success_order = (By.XPATH,'.//img[@alt="tick animation"]')

# Всплывающее окно Деталей ингредиента
opened_modal = (By.XPATH,'.//section[contains(@class, "Modal_modal_opened")]')
closed_modal = (By.XPATH,'.//section[@class="Modal_modal__P3_V5"]')
ingredient_details_title = (By.XPATH,'.//h2[contains(@class, "Modal_modal__title")]')
ingredient_details_name = (By.XPATH,'.//p[@class="text text_type_main-medium mb-8"]')
close_modal_button = (By.XPATH,'.//button[contains(@class, "Modal_modal__close_modified")]')

# Бургер - шаблон
burger_target_locator = (By.XPATH,'.//ul[contains(@class, "BurgerConstructor_basket__list")]')


# Карточки ингредиентов (выбираются рандомно для каждого теста из api)
def ingredient_bun_locator(ingredient_name):
    return (By.XPATH, f'.//img[@alt="{ingredient_name}"]')


def ingredient_sauce_locator(ingredient_name):
    return (By.XPATH, f'.//img[@alt="{ingredient_name}"]')


def ingredient_main_locator(ingredient_name):
    return (By.XPATH, f'.//img[@alt="{ingredient_name}"]')


def ingredient_counter_locator(ingredient_name):
    return (By.XPATH, f'.//img[@alt="{ingredient_name}"]/'
                      f'preceding-sibling::div/p[contains(@class, "counter_counter__num")]')
